# Class - 18: Chi-Square Test in Hypothesis Testing

## 1. What Is a Chi-Square Test?
- A Chi-Square Test is a statistical test used to check if there is a significant relationship between categorical variables or if the observed frequencies match the expected frequencies.

---

## 2. Chi-Square Formula & Degrees of Freedom
- **Formula:** 
  $$\chi^{2} = \frac{\sum(O - E)^{2}}{E}$$
  Where:
  - $O$ = Observed frequency
  - $E$ = Expected frequency
- **Degrees of Freedom (df):** 
  $$df = (rows - 1) \times (columns - 1)$$

---

## 3. Steps in Chi-Square Test of Independence
1. **State the Hypotheses:**
   - Null Hypothesis ($H_0$): There is no association (or no difference) between the variables.
   - Alternative Hypothesis ($H_1$): There is an association (or a difference).
2. **Calculate Expected Frequencies ($E$):**
   - For each cell, the expected frequency is calculated as:
     $$E = \frac{\text{Row Total} \times \text{Column Total}}{\text{Grand Total}}$$
3. **Calculate the Chi-Square Statistic:** Apply the formula across all cells.
4. **Determine Critical Value and Compare:** Compare the calculated statistic against the critical value based on the significance level ($\alpha$) and degrees of freedom.

---

## 4. Step-by-Step Example: Gender vs. Choice of Drink
- **Scenario:** Survey of $100$ people examining the relationship between Gender and Choice of Drink.

### Observed Frequencies ($O$)
| Gender | Coffee | Tea | Juice | Row Total |
| :--- | :--- | :--- | :--- | :--- |
| **Male** | 30 | 10 | 5 | 45 |
| **Female** | 15 | 20 | 20 | 55 |
| **Col Total** | 45 | 30 | 25 | 100 |

### Expected Frequencies ($E$)
| Gender | Coffee | Tea | Juice | Row Total |
| :--- | :--- | :--- | :--- | :--- |
| **Male** | 20.25 | 13.5 | 11.25 | 45 |
| **Female** | 24.75 | 16.5 | 13.75 | 55 |
| **Col Total** | 45 | 30 | 25 | 100 |

### Calculation Summary
- Summing $\frac{(O - E)^2}{E}$ across all categories yields a total Chi-Square statistic of **$16.49$**.
- **Degrees of Freedom:** $df = (2 - 1) \times (3 - 1) = 1 \times 2 = 2$.
- **Conclusion:** The critical value at the given significance level is $5.991$. Since $16.49 > 5.991$, we **reject the null hypothesis ($H_0$)**, concluding that there is a significant relationship between gender and drink choice.