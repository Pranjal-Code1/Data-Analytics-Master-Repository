import streamlit as st
import json
import random
import string
from pathlib import Path
from datetime import datetime

# --- Library Class Backend Architecture ---
class Library:
    BASE_DIR = Path(__file__).resolve().parent
    database = BASE_DIR / "library.json"
    
    data = {"books": [], "members": []}

    if database.exists():
        with open(database, "r") as f:
            content = f.read().strip()
            if content:
                data = json.loads(content)
    else:
        with open(database, 'w') as f:
            json.dump(data, f, indent=4)

    def gen_id(self, Prefix="B"):
        random_id = "".join(random.choices(string.ascii_uppercase + string.digits, k=5))
        return Prefix + "-" + random_id
    
    @classmethod
    def save_data(cls):
        with open(cls.database, 'w') as f:
            json.dump(cls.data, f, indent=4, default=str)

    @classmethod
    def clear_database(cls):
        cls.data = {"books": [], "members": []}
        cls.save_data()

# Initialize library system instance
library_system = Library()

# --- Streamlit Page Configuration ---
st.set_page_config(
    page_title="Library Management System",
    page_icon="📚",
    layout="centered"
)

# App Header
st.title("📚 Library Management System")
st.markdown("A full-stack Python application powered by **Object-Oriented Programming**, **JSON persistence**, and an interactive web interface.")
st.markdown("---")

# Sidebar Navigation Menu
menu = [
    "📖 View Books", 
    "➕ Add Book", 
    "👥 View Members", 
    "👤 Add Member", 
    "🔄 Borrow Book", 
    "↩️ Return Book", 
    "🗑️ Clear Database"
]
choice = st.sidebar.selectbox("Navigation Menu", menu)

# --- 1. View Books ---
if choice == "📖 View Books":
    st.subheader("📚 Book Inventory Catalog")
    books = Library.data["books"]
    
    if not books:
        st.info("No books found in the library database. Add some books to get started!")
    else:
        for b in books:
            with st.container():
                col1, col2, col3 = st.columns([2, 2, 1])
                with col1:
                    st.markdown(f"**{b['title']}**")
                    st.caption(f"Author: {b['author']}")
                with col2:
                    st.text(f"ID: {b['id']}")
                    st.text(f"Added: {b['added_on']}")
                with col3:
                    st.metric("Available", f"{b['available_copies']}/{b['total_copies']}")
                st.divider()

# --- 2. Add Book ---
elif choice == "➕ Add Book":
    st.subheader("➕ Register a New Book")
    
    with st.form("add_book_form"):
        title = st.text_input("Book Title")
        author = st.text_input("Author Name")
        copies = st.number_input("Total Copies", min_value=1, value=1, step=1)
        submitted = st.form_submit_button("Add to Inventory")
        
        if submitted:
            if title.strip() and author.strip():
                book = {
                    "id": library_system.gen_id("B"),
                    "title": title.strip(),
                    "author": author.strip(),
                    "total_copies": int(copies),
                    "available_copies": int(copies),
                    "added_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                Library.data['books'].append(book)
                Library.save_data()
                st.success(f"Successfully added '{title.strip()}' to the library database!")
            else:
                st.error("Please fill out both the title and author fields.")

# --- 3. View Members ---
elif choice == "👥 View Members":
    st.subheader("👥 Registered Members Directory")
    members = Library.data["members"]
    
    if not members:
        st.info("No members registered in the system yet.")
    else:
        for m in members:
            with st.container():
                st.markdown(f"### {m['name']}")
                st.text(f"Member ID: {m['id']} | Email: {m['email']}")
                
                if m['borowed']:
                    st.markdown("**Active Borrowed Books:**")
                    for item in m['borowed']:
                        st.markdown(f"- *{item['title']}* (ID: `{item['book_id']}`) — *Checked out on: {item['borrow_on']}*")
                else:
                    st.caption("No active borrowed books.")
                st.divider()

# --- 4. Add Member ---
elif choice == "👤 Add Member":
    st.subheader("👤 Register a New Member")
    
    with st.form("add_member_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        submitted = st.form_submit_button("Register Member")
        
        if submitted:
            if name.strip() and email.strip():
                member = {
                    "id": library_system.gen_id("M"),
                    "name": name.strip(),
                    "email": email.strip(),
                    "borowed": []
                }
                Library.data['members'].append(member)
                Library.save_data()
                st.success(f"Successfully registered member: {name.strip()}!")
            else:
                st.error("Please provide both name and email address.")

# --- 5. Borrow Book ---
elif choice == "🔄 Borrow Book":
    st.subheader("🔄 Process Book Checkout")
    members = Library.data["members"]
    books = Library.data["books"]
    
    if not members or not books:
        st.warning("Ensure you have both registered members and available books in the system before checking out.")
    else:
        member_options = {f"{m['name']} ({m['id']})": m['id'] for m in members}
        book_options = {f"{b['title']} (Available: {b['available_copies']}/{b['total_copies']})": b['id'] for b in books if b['available_copies'] > 0}
        
        selected_member_label = st.selectbox("Select Member", list(member_options.keys()))
        
        if not book_options:
            st.error("No book copies are currently available for borrowing.")
        else:
            selected_book_label = st.selectbox("Select Book", list(book_options.keys()))
            
            if st.button("Confirm Checkout"):
                m_id = member_options[selected_member_label]
                b_id = book_options[selected_book_label]
                
                member = next(m for m in members if m['id'] == m_id)
                book = next(b for b in books if b['id'] == b_id)
                
                borrow_entry = {
                    "book_id": book['id'],
                    "title": book['title'],
                    "borrow_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                
                member['borowed'].append(borrow_entry)
                book['available_copies'] -= 1
                Library.save_data()
                st.success(f"Successfully checked out '{book['title']}' to {member['name']}!")
                st.rerun()

# --- 6. Return Book ---
elif choice == "↩️ Return Book":
    st.subheader("↩️ Process Book Return")
    members_with_books = [m for m in Library.data["members"] if m['borowed']]
    
    if not members_with_books:
        st.info("No members currently have active checked-out books.")
    else:
        member_options = {f"{m['name']} ({m['id']})": m['id'] for m in members_with_books}
        selected_member_label = st.selectbox("Select Member", list(member_options.keys()))
        m_id = member_options[selected_member_label]
        member = next(m for m in Library.data["members"] if m['id'] == m_id)
        
        borrowed_options = {f"{b['title']} (ID: {b['book_id']})": i for i, b in enumerate(member['borowed'])}
        selected_borrowed_label = st.selectbox("Select Book to Return", list(borrowed_options.keys()))
        
        if st.button("Confirm Return"):
            idx = borrowed_options[selected_borrowed_label]
            selected = member['borowed'].pop(idx)
            
            book = next(bk for bk in Library.data['books'] if bk['id'] == selected['book_id'])
            book['available_copies'] += 1
            
            Library.save_data()
            st.success(f"Successfully processed return for '{selected['title']}'!")
            st.rerun()

# --- 7. Clear Database ---
elif choice == "🗑️ Clear Database":
    st.subheader("⚠️ System Reset Zone")
    st.warning("This action will permanently wipe all books, member profiles, and active transactions from the JSON database.")
    
    confirm = st.checkbox("I understand that this action is irreversible.")
    if st.button("Clear All Data", type="primary"):
        if confirm:
            Library.clear_database()
            st.success("Database has been completely cleared and reset.")
            st.rerun()
        else:
            st.error("Please check the confirmation box to proceed.")