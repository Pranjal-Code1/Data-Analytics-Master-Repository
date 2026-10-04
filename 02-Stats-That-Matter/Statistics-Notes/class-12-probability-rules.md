# Class - 12: Probability Rules

## 1. Why Probability Rules Are Important
- In probability problems, the biggest challenge is choosing the correct rule rather than performing calculations.
- Students often make mistakes by applying the wrong formula, confusing "OR" with "AND", or ignoring dependency and overlap.
- Probability rules tell us how to combine events correctly.

---

## 2. Types of Probability Questions
Before solving any question, identify what is being asked:
- **"A OR B"** $\rightarrow$ Addition Rule
- **"A AND B"** $\rightarrow$ Multiplication Rule
- **"B Given A"** $\rightarrow$ Conditional Probability

---

## 3. Part 1: Addition Rule of Probability
- The addition rule is used when we want the probability that either Event $A$ or Event $B$ occurs.
- **"OR" means:** Event $A$ occurs, or Event $B$ occurs, or both occur.
- **General Addition Rule Formula:** 
  $$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

### Why Do We Subtract the Intersection?
- When we add $P(A)$ and $P(B)$, the common part $P(A \cap B)$ gets counted twice.
- To correct this, we subtract it once.
- This logic comes directly from the Venn diagram.

### Example: Cards (Club OR King)
- In a standard deck of $52$ cards:
  - Event A (Drawing a Club): $P(A) = \frac{13}{52}$
  - Event B (Drawing a King): $P(B) = \frac{4}{52}$
  - Intersection (King of Clubs - 1 card): $P(A \cap B) = \frac{1}{52}$
- **Applying the Formula:** 
  $$P(A \cup B) = \frac{13}{52} + \frac{4}{52} - \frac{1}{52} = \frac{16}{52}$$

### Special Case: Mutually Exclusive Events
- If two events cannot occur together, then $P(A \cap B) = 0$.
- The formula simplifies to: 
  $$P(A \cup B) = P(A) + P(B)$$
- *Example (King OR Queen):* A card cannot be both a King and a Queen, so $P = \frac{4}{52} + \frac{4}{52} = \frac{8}{52}$.

---

## 4. Part 2: Multiplication Rule of Probability
- The multiplication rule is used when we want the probability that Event $A$ and Event $B$ occur together (joint occurrence).
- **General Multiplication Rule (Dependent Events):** 
  $$P(A \cap B) = P(A) \times P(B|A)$$
- Where $P(B|A)$ is the probability of $B$ given that $A$ has already occurred.

### Why Conditional Probability Is Needed
- When Event $A$ occurs, the sample space changes.
- As a result, the probability of $B$ is no longer the same.

### Example: Balls Without Replacement
- Box contents: $5$ red balls and $3$ blue balls (Total = $8$).
- **Event A:** First ball is red ($P(A) = \frac{5}{8}$).
- **Event B:** Second ball is red after the first red.
  - Remaining red $= 4$
  - Remaining total $= 7$
  - $P(B|A) = \frac{4}{7}$
- **Joint Probability:** 
  $$P(A \cap B) = \frac{5}{8} \times \frac{4}{7} = \frac{5}{14}$$

### Special Case: Independent Events
- If events are independent, $P(B|A) = P(B)$.
- The formula simplifies to: 
  $$P(A \cap B) = P(A) \times P(B)$$
- *Note:* There is no multiplication rule for mutually exclusive events because $P(A \cap B) = 0$.

---

## 5. Part 3: Conditional Probability
- Conditional probability is the probability that Event $B$ occurs given that Event $A$ has already occurred, written as $P(B|A)$.
- **Formula:** 
  $$P(B|A) = \frac{P(A \cap B)}{P(A)}, \quad P(A) > 0$$
- This reduces the sample space to focus only on outcomes where $A$ has already occurred.

---

## 6. Summary: How All Rules Are Connected

| Situation | Rule |
| :--- | :--- |
| **A OR B** | Addition Rule |
| **A AND B (Dependent)** | Multiplication Rule |
| **A AND B (Independent)** | Simple Multiplication |
| **B Given A** | Conditional Probability |