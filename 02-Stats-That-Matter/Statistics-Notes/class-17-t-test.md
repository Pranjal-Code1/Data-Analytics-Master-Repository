# Class - 17: T-Test in Hypothesis Testing

## 1. What Is a T-Test?
- A T-test is a statistical test used to compare means when the sample size is small ($n < 30$) or when the population standard deviation ($\sigma$) is unknown.
- **Rule of Thumb:** If the sample standard deviation ($s$) is given and the population standard deviation is unknown, you should use a T-test—even if the sample size is greater than $30$.

---

## 2. One-Sample T-Test Formula
The formula for a one-sample t-test is:
$$t = \frac{\bar{x} - \mu_{0}}{\frac{s}{\sqrt{n}}}$$

Where:
- $\bar{x}$ = sample mean
- $\mu_{0}$ = claimed population mean
- $s$ = sample standard deviation
- $n$ = sample size
- **Degrees of Freedom (df):** $df = n - 1$

---

## 3. Step-by-Step Example: One-Sample T-Test
- **Scenario:** A bakery claims that their cupcakes weigh at least $150\text{ grams}$ on average. A customer suspects this is not true.
- **Given Data:**
  - Claimed population mean ($\mu_0$) = $150\text{ grams}$
  - Sample size ($n$) = $10$
  - Sample mean ($\bar{x}$) = $145\text{ grams}$
  - Sample standard deviation ($s$) = $8\text{ grams}$
  - Significance level ($\alpha$) = $0.05$ ($5\%$)

- **Step 1: Calculate the T-Value**
  $$t = \frac{145 - 150}{\frac{8}{\sqrt{10}}} = -1.976$$

- **Step 2: Find Degrees of Freedom & Critical Values**
  - $df = n - 1 = 10 - 1 = 9$
  - From the t-table for $df = 9$ at a $5\%$ significance level (two-tailed), the critical t-values are $\pm 2.265$.

- **Step 3: Compare and Conclude**
  - Calculated $t$-value ($ -1.976 $) lies between $-2.265$ and $+2.265$ (does not fall in the rejection region).
  - **Conclusion:** We do not reject the null hypothesis ($H_0$). The sample does not provide enough evidence to say the population mean is significantly different from the hypothesized value.

---

## 4. Two-Sample T-Test
- **When to use:** Used when you have two independent groups and want to compare their means to see if the difference is statistically significant.
- **Formula:**
  $$t = \frac{\bar{x}_{1} - \bar{x}_{2}}{\sqrt{\frac{s_{1}^{2}}{n_{1}} + \frac{s_{2}^{2}}{n_{2}}}}$$
- **Degrees of Freedom:** 
  $$df = \min(n_{1} - 1, n_{2} - 1)$$

---

## 5. Step-by-Step Example: Two-Sample T-Test
- **Scenario:** A teacher wants to know if there's a difference in math scores between boys and girls.
- **Group 1 (Boys):** $n_1 = 30$, $\bar{x}_1 = 70$, $s_1 = 8$
- **Group 2 (Girls):** $n_2 = 28$, $\bar{x}_2 = 74$, $s_2 = 6$

- **Step 1: Calculate the T-Value and Degrees of Freedom**
  $$t = \frac{70 - 74}{\sqrt{\frac{8^2}{30} + \frac{6^2}{28}}} = -2.17$$
  $$df = \min(30 - 1, 28 - 1) = \min(29, 27) = 27$$

- **Step 2: Compare with Critical Values**
  - Critical $t$-values from the table for $df = 27$ at $\alpha = 0.05$ are $\pm 2.052$.
  - Calculated $t$-value is $-2.17$, which is less than $-2.052$ (falls in the rejection region).

- **Step 3: Conclusion**
  - We reject the null hypothesis ($H_0$). The sample provides enough evidence to conclude that the population mean scores are significantly different.