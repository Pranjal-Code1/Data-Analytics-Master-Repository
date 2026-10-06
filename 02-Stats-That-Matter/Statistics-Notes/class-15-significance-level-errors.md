# Class - 15: Significance Level, Errors, and P-Values

## 1. Significance Level ($\alpha$)
- **What Is Significance Level?** Denoted by $\alpha$ (alpha), it is a cut-off probability used in hypothesis testing to decide whether to reject the null hypothesis ($H_0$).
- **Risk Assessment:** It tells us how much risk we are willing to take when making a decision and represents the chance of making a wrong decision.
- **Meaning of $\alpha = 0.05$:** 
  - We accept a 5% risk of rejecting $H_0$ when it is actually true.
  - In other words: "I am okay with being wrong 5 times out of 100 decisions." Even after rejecting $H_0$, a small 5% chance of error remains.
- **Why It Is Important:** Controls errors, adds discipline to decision-making, and makes hypothesis testing scientific and fair.
- **Common Values:**
  - $0.10$: Very Lenient
  - $0.05$: Standard (Most Common)
  - $0.01$: Very Strict
- **Confidence Level Relationship:** Confidence Level $= 1 - \alpha$. If $\alpha = 0.05$, the confidence level is $0.95$ ($95\%$).

---

## 2. Type I and Type II Errors

### Type I Error (False Alarm)
- Occurs when we reject the null hypothesis even though it is actually true.
- **Probability:** $P(\text{Type I Error}) = \alpha$.
- Smaller $\alpha \rightarrow$ fewer Type I errors; larger $\alpha \rightarrow$ more risk of a false alarm.
- **Court Example:** $H_0$: The person is innocent. Reality: Person is innocent. Decision: We say "Guilty" (Type I Error).

### Type II Error (Missing a Real Problem)
- Occurs when we fail to reject the null hypothesis even though it is actually false.
- **Probability:** Denoted by $\beta$ (Beta). Smaller $\beta \rightarrow$ better test.
- **Power of a Test:** $= 1 - \beta$.
- **Court Example:** $H_0$: The person is innocent. Reality: Person is guilty. Decision: We say "Not Guilty" (Type II Error).

### Confusion Matrix View
| Reality | Accept $H_0$ | Reject $H_0$ |
| :--- | :--- | :--- |
| **$H_0$ True** | Correct | Type I Error |
| **$H_0$ False** | Type II Error | Correct |

*Note: This follows the exact same logic used in classification models for True Positives, False Positives, True Negatives, and False Negatives.*

---

## 3. One-Tailed and Two-Tailed Tests

### One-Tailed Test
- The rejection region lies entirely in one tail of the probability distribution.
- **Used When:** We care about only one direction (greater than or less than).
- *Examples:* Is the new drug better than the old one? Has production increased?
- **Property:** The entire significance level ($\alpha$) goes into one tail.

### Two-Tailed Test
- The rejection region is split between both tails of the distribution.
- **Used When:** We care about any difference (both increase and decrease matter).
- *Examples:* Has the mean changed? Is the coin biased?
- **Property:** Significance level is divided equally ($\alpha / 2$ in each tail).

### Comparison Table
| Feature | One-Tailed | Two-Tailed |
| :--- | :--- | :--- |
| **Direction** | One | Both |
| **$\alpha$ Placement** | One Tail | Split into two |
| **Used When** | Only More or Less | Any Difference |
| **Power** | Higher | Lower |

---

## 4. P-Value
- **Definition:** The probability of getting results as extreme as (or more extreme than) the observed result, assuming the null hypothesis is true.
- **Intuitive Meaning:** Tells us how surprising our data is if $H_0$ were true.
  - Small P-value $\rightarrow$ Very surprising $\rightarrow$ Strong evidence against $H_0$.
  - Large P-value $\rightarrow$ Not surprising $\rightarrow$ Weak evidence.
- **Decision Rule:** 
  - If $\text{P-Value} < \alpha \Rightarrow$ Reject $H_0$.
  - If $\text{P-Value} \ge \alpha \Rightarrow$ Fail to reject $H_0$.
- **Common Misconceptions:** 
  - P-value is *not* the probability that $H_0$ is true.
  - A small P-value does not automatically mean a big effect.
  - P-value only measures evidence against $H_0$.

---

## 5. Test Statistics
- **Definition:** A numerical value calculated from sample data that measures how far the sample result is from what we expect under the null hypothesis.
- **Role:** Converts data into a single number, helps compare sample vs $H_0$, and is used to calculate the P-value or compare with a critical value.
- **Examples:** Z-test, T-test, Chi-Square test, F-test.