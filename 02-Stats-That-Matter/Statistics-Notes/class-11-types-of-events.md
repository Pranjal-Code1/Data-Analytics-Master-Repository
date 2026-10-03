# Class - 11: Types of Events

## 1. Why "Types of Events" Matter (The Big Picture)
- In probability numericals, students frequently make mistakes by using the wrong formula, confusing independent and dependent events, or mistakenly treating mutually exclusive events as independent.
- Identifying the correct type of event determines which formula must be applied.

---

## 2. What Is an Event? (Foundation)
- An event is a specific outcome or a set of outcomes of an experiment.
- Tossing a coin is an experiment, while getting a head is an event.
- Rolling a dice is an experiment, while getting an even number is an event.
- Event = Condition we are interested in.

---

## 3. Type 1: Independent Events
- Two events $A$ and $B$ are independent if the occurrence of one event does **not** affect the probability of the other event.
- Event $A$ happening leaves the chance of Event $B$ exactly the same because there is no connection between them.
- Mathematical Condition: 
  $$P(A \cap B) = P(A) \times P(B)$$
- If this relation is satisfied, the events are independent.

### Intuition & Example (Dice + Coin)
- Separate processes (like today's weather and a dice roll, or a dice roll and a coin toss) do not affect each other.
- Event A: Roll a dice $\rightarrow$ Get $6$ ($P(A) = \frac{1}{6}$).
- Event B: Flip a coin $\rightarrow$ Get Head ($P(B) = \frac{1}{2}$).
- Since the dice has no relation to the coin:
  $$P(A \cap B) = \frac{1}{6} \times \frac{1}{2} = \frac{1}{12}$$

---

## 4. Type 2: Dependent Events
- Two events $A$ and $B$ are dependent if the occurrence of one event **changes** the probability of the other event.
- After Event $A$ happens, the chance of Event $B$ changes.
- Mathematical Formula: 
  $$P(A \cap B) = P(A) \times P(B|A)$$
- $P(B|A)$ is the probability of $B$ given that $A$ has already occurred.
- "Given that" serves as the dependency signal.

### Why Simple Multiplication Fails Here
- Simple multiplication does not work because the sample space changes and total outcomes are reduced.

### Example: Cards Without Replacement
- Event A: First card is an Ace ($P(A) = \frac{4}{52}$).
- Event B: Second card is an Ace given the first was an Ace.
- Remaining cards $= 51$.
- Remaining Aces $= 3$.
- $P(B|A) = \frac{3}{51}$.
- Calculation: 
  $$P(A \cap B) = \frac{4}{52} \times \frac{3}{51} = \frac{1}{221}$$.
- Here, events are dependent because the card is not replaced.

---

## 5. Type 3: Mutually Exclusive Events
- Two events are mutually exclusive if they **cannot occur at the same time** in a single trial.
- If $A$ happens, $B$ cannot happen (zero overlap).
- Mathematical Condition: 
  $$P(A \cap B) = 0$$
- The intersection is empty.

### Example (Dice)
- Event A: Get $3$.
- Event B: Get $6$.
- In a single roll, you can get either $3$ **or** $6$, but never both, meaning $P(A \cap B) = 0$.

### Important Clarification (Common Student Confusion)
- Mutually Exclusive $\neq$ Independent.
- Mutually exclusive events are always dependent because if $A$ occurs, $B$ cannot occur, which alters the probability.

---

## 6. Venn Diagram Understanding
- Independent $\rightarrow$ Circles may overlap.
- Dependent $\rightarrow$ Overlap exists, but probabilities change.
- Mutually Exclusive $\rightarrow$ No overlap at all.