# Class - 10: Inferential Statistics & Probability

## 1. What Is Inferential Statistics?
- From classes 1 to 9, we focused primarily on **Descriptive Statistics** (such as mean, median, standard deviation, graphs, and correlation), which only describe the given data.
- In real life, we rarely have full population data and usually only observe a sample.
- **Inferential Statistics** is the branch of statistics that uses sample data to make predictions, estimates, or conclusions about an entire population.
- *Infer* means to conclude beyond the observed data.

### Intuition & Example
- **Population:** All students in India.
- **Sample:** 1,000 students.
- We use the sample to estimate average heights, predict exam performance, or guide government policies. This leap from a sample to a population is inferential statistics.

---

## 2. Descriptive vs. Inferential Statistics

| Aspect | Descriptive Statistics | Inferential Statistics |
| :--- | :--- | :--- |
| **What It Does** | Describes data | Predicts / concludes |
| **Data Used** | Given data only | Sample data |
| **Output** | Exact values | Probabilistic statements |
| **Uncertainty** | No | Yes |
| **Example** | Average height = $165\text{ cm}$ | Average height $\approx 165 \pm 2\text{ cm}$ |

*Note: Inferential results are never 100% certain—they are probability-based.*

---

## 3. Techniques in Inferential Statistics
- Sampling
- Hypothesis Testing
- Confidence Intervals
- Regression
- Statistical Tests
- *Conceptually, everything is founded on **Probability**.*

---

## 4. Introduction to Probability
- Probability is a numerical measure of how likely an event is to occur.
- It always lies between $0$ (impossible) and $1$ (certain).
- Probability does not state what *will* happen; it states what *can* happen with a specific likelihood.

### Core Language
- **Experiment:** An action (e.g., tossing a coin).
- **Outcome:** A result (e.g., head or tail).
- **Event:** A collection of outcomes (e.g., "getting a head").

### Probability Formula
$$\text{Probability} = \frac{\text{Number of Favorable Outcomes}}{\text{Total Number of Possible Outcomes}}$$
*(This formula applies when all outcomes are equally likely.)*

---

## 5. Practical Examples

### Coin Toss Experiment
- Total outcomes $= 2$ (Head or Tail).
- $P(\text{Head}) = \frac{1}{2}$
- $P(\text{Tail}) = \frac{1}{2}$
- **Fundamental Rule:** Total probability always equals $1$ ($P(\text{Head}) + P(\text{Tail}) = 1$).

### Dice Roll Experiment
- Total outcomes $= 6$ (Numbers 1 through 6).
- Probability of getting a $6$: $P(6) = \frac{1}{6}$.
- Probability of getting an **Even** number (2, 4, 6): $P(\text{Even}) = \frac{3}{6} = \frac{1}{2}$.
- Probability of getting an **Odd** number (1, 3, 5): $P(\text{Odd}) = \frac{3}{6} = \frac{1}{2}$.

---

## 6. Why Probability Matters in Data Science
- Inferential statistics relies on probability to measure uncertainty, estimate population parameters, and define confidence levels (e.g., being "95% confident").
- It is heavily utilized in:
  - Machine learning predictions
  - A/B testing
  - Risk analysis
  - Bayesian models and classification confidence