# Class - 14: Introduction to Hypothesis Testing

## 1. What Is Hypothesis Testing? (Core Idea)
- Hypothesis testing is a statistical decision-making framework.
- It helps us answer this question: Can we use sample data to make a reliable decision about the population?
- In hypothesis testing:
  - We start with a claim about the population.
  - We collect sample data.
  - We use statistics to decide whether the claim is reasonable or not.
- We take data from a sample and test whether what we observe is true for the whole population.

---

## 2. Hypothesis Testing as a Decision Process
- Hypothesis testing is often compared to being a judge in a court:
  - Evidence = Sample data
  - Claim = Statement about population
  - Decision = Accept or reject the claim
- We do not prove things with certainty; we decide based on the strength of evidence.

---

## 3. Why Hypothesis Testing Is Needed
- In real life:
  - Population data is too large or impossible to collect.
  - Sample data always has randomness.
  - We need a formal method to avoid biased decisions.
- Hypothesis testing provides:
  - Objectivity
  - Probability-based reasoning
  - Controlled risk of making wrong decisions

---

## 4. What Is a Hypothesis?
- A hypothesis is a testable statement about a population parameter.
- *Examples:* "The coin is fair," "The average score is 50," "The new medicine is effective."

### Types of Hypotheses
1. **Null Hypothesis ($H_{0}$):**
   - Represents "no difference", "no effect", or "no change".
   - Assumes that nothing unusual is happening.
   - *Examples:* Coin is fair, Mean $= 50$, No improvement in results.
   - We **always assume the null hypothesis is true** at the beginning.
2. **Alternative Hypothesis ($H_{1}$):**
   - Competes with $H_{0}$.
   - Represents a difference, effect, or change.
   - *Examples:* Coin is not fair, Mean $\neq 50$, New method performs better.
- **The Goal:** See whether there is enough evidence to reject $H_{0}$ in favor of $H_{1}$.
- **Important Principle:** We do not prove the alternative hypothesis directly; we try to reject the null hypothesis using evidence. If evidence is weak, we *fail to reject* $H_{0}$ (which is not the same as proving $H_{0}$ is true).

---

## 5. Step-by-Step Hypothesis Testing Process
1. Define the null hypothesis ($H_{0}$).
2. Define the alternative hypothesis ($H_{1}$).
3. Perform the experiment and collect sample data.
4. Use statistical reasoning to accept or reject $H_{0}$.

### Example: Testing a Coin
- **Step 1: Define Hypotheses**
  - $H_{0}$ (Null): Coin is fair.
  - $H_{1}$ (Alternative): Coin is unfair.
- **Step 2: Perform the Experiment**
  - Coin is flipped 100 times.
  - Observed number of heads $= 30$.
- **Step 3: Intuition Behind the Decision**
  - If the coin is fair, the expected mean number of heads is $50$, and results should be close to $50$.
  - We observed only $30$ heads. The key question becomes: How far from the mean is "Too Far"?

---

## 6. Role of Mean, Standard Deviation, and Distribution
- Assumed parameters: Mean $= 50$, Standard Deviation $= 10$, Normal Distribution.
- This helps us measure how unusual the observed result is and compare observations with expected behavior.

---

## 7. Significance Level and Confidence Level
- **Significance Level ($\alpha$):** The probability of rejecting the null hypothesis when it is actually true. Common values are $0.05$ (5%) or $0.01$ (1%).
- **Confidence Level:** Tells us how confident we want to be in our decision (Confidence Level $= 1 - \alpha$). 
  - If $\alpha = 0.05$, Confidence Level $= 1 - 0.05 = 0.95$ ($95\%$).
- **Meaning of Confidence Level:** We accept a 5% risk of making a wrong rejection and want strong evidence before rejecting $H_{0}$.

### What Hypothesis Testing Does NOT Mean
- It does not prove something is absolutely true.
- It does not eliminate uncertainty.
- It does not guarantee correctness.
- It simply provides a controlled, logical decision under uncertainty.