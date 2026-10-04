# Class - 13: Bayes' Theorem

## 1. What Is Bayes' Theorem? (Core Idea)
- Bayes' Theorem is a fundamental rule of probability that helps us update the probability of an event when new information (evidence) is available.
- We start with an initial belief, observe new evidence, and use Bayes' Theorem to update that belief logically.

---

## 2. Why Bayes' Theorem Is Needed
- In real life, we rarely know the full truth in advance and make assumptions based on past knowledge.
- When we receive new evidence, Bayes' Theorem provides a mathematical way to revise our assumptions.
- *Example:* Before a medical test, disease probability is low; after a positive test, probability increases, and Bayes' Theorem explains how much it increases.

---

## 3. Conditional Probability - The Foundation & Formula
- Bayes' Theorem is built on conditional probability, where $P(A|B)$ is the probability of event $A$ given that $B$ has occurred.
- **Standard Formula:**
  $$P(A|B) = \frac{P(B|A)P(A)}{P(B)}$$

### Meaning of Each Term
1. **Posterior Probability ($P(A|B)$):** Probability of $A$ after seeing $B$; what we want to calculate.
2. **Likelihood ($P(B|A)$):** Probability of seeing $B$ if $A$ is true; measures how strongly evidence supports the event.
3. **Prior Probability ($P(A)$):** Initial belief about event $A$ based on past data or intuition before seeing evidence.
4. **Evidence / Normalizing Constant ($P(B)$):** Overall probability of evidence $B$, often calculated using the total probability rule.

---

## 4. Step-by-Step Example
- **Given Information:** A school has 60% boys and 40% girls; 30% of boys wear glasses, and 50% of girls wear glasses.
- **Step 1: Define Events:** $G$ = Girl, $B$ = Boy, $\text{Gl}$ = Wears glasses.
- **Step 2: Write Given Probabilities:** $P(G) = 0.4$, $P(B) = 0.6$, $P(\text{Gl}|G) = 0.5$, $P(\text{Gl}|B) = 0.3$.
- **Step 3: Calculate Total Probability of Glasses:** 
  $$P(\text{Gl}) = P(\text{Gl}|G)P(G) + P(\text{Gl}|B)P(B)$$
  $$P(\text{Gl}) = (0.5 \times 0.4) + (0.3 \times 0.6) = 0.20 + 0.18 = 0.38$$
- **Step 4: Apply Bayes' Theorem:**
  $$P(G|\text{Gl}) = \frac{P(\text{Gl}|G)P(G)}{P(\text{Gl})} = \frac{0.5 \times 0.4}{0.38} = \frac{0.20}{0.38} \approx 0.526$$
- **Final Answer:** There is a 52.6% probability that a student wearing glasses is a girl.

---

## 5. Applications in Data Science & Machine Learning
- Bayes' Theorem is the backbone of Naive Bayes classifiers, spam detection, medical diagnosis systems, and recommendation engines.
- In machine learning: Prior = model's initial assumption, Likelihood = data likelihood, Posterior = updated prediction.