# Class - 16: Z-Test in Hypothesis Testing

## 1. What Is a Z-Test?
- A Z-test is a type of hypothesis test used when the sample mean is significantly different from the population mean.
- It is used when the population variance ($\sigma^2$) is known, or when the sample size is large ($n > 30$).

---

## 2. Z-Test Formula
The formula for a Z-test is:
$$z = \frac{\bar{x} - \mu_{0}}{\frac{\sigma}{\sqrt{n}}}$$

Where:
- $\bar{x}$ = sample mean
- $\mu_{0}$ = claimed population mean
- $\sigma$ = population standard deviation
- $n$ = sample size

---

## 3. Step-by-Step Example (Two-Tailed Test)
- **Problem Setup:** 
  - A school claims that the average height of students is $150\text{ cm}$.
  - Sample size ($n$) = $40$ students.
  - Sample average height ($\bar{x}$) = $154\text{ cm}$.
  - Population standard deviation ($\sigma$) = $10\text{ cm}$.
  - Significance level ($\alpha$) = $5\%$ ($0.05$).

- **Step 1: Write the Hypotheses**
  - Null Hypothesis ($H_0$): $\mu = 150$ (no difference).
  - Alternative Hypothesis ($H_1$): $\mu \neq 150$ (there is a difference).

- **Step 2: Calculate the Z-Value**
  - $Z = \frac{154 - 150}{\frac{10}{\sqrt{40}}} = \frac{4}{1.58} \approx 2.53$.
  - This means the sample mean is $2.53$ standard deviations away from the population mean.

- **Step 3: Compare with Critical Value**
  - Our calculated Z-value is $2.53$.
  - For a two-tailed test at $\alpha = 0.05$, the critical Z-value is $1.96$.
  - Since $2.53 > 1.96$, our result falls in the rejection region.

- **Step 4: Conclusion**
  - We reject the null hypothesis ($H_0$).
  - The average height of students is significantly different from $150\text{ cm}$ at the $5\%$ significance level.

---

## 4. Practice Problem from Slide
- **Scenario:** A company claims that the average weight of its packed sugar bags is $1\text{ kg}$ ($1000\text{ grams}$). A quality control officer suspects that the average weight is less than claimed.
- **Sample Data:** Random sample of $50$ sugar bags, sample mean = $990\text{ grams}$, population standard deviation = $20\text{ grams}$.
- **Question:** At a $5\%$ significance level, can we conclude that the average weight of sugar bags is less than $1000\text{ grams}$? (Hint: Use a one-tailed Z-test).