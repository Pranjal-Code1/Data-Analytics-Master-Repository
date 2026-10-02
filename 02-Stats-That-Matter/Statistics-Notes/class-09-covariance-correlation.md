# Class - 09: Covariance & Correlation

## 1. Why Covariance & Correlation?
- Until now, we studied one variable at a time (such as mean and variance).
- In real life, variables are related (for example: hours studied & marks, height & weight).
- We need specialized tools to measure the relationship between two variables.

---

## 2. Covariance
- Covariance tells us whether two variables move together or in opposite directions.
- It answers whether variables increase together or if one increases while the other decreases.

### Covariance Formula
$$Cov(X, Y) = \frac{\sum(X_i - \bar{X})(Y_i - \bar{Y})}{n}$$

- **$X_i, Y_i$** = Data Values
- **$\bar{X}, \bar{Y}$** = Means
- **$n$** = Number Of Observations

### Types Of Covariance
1. **Positive Covariance:** Both variables increase together (Example: More hours studied $\rightarrow$ Higher marks).
2. **Negative Covariance:** One variable increases while the other decreases (Example: Rank increases $\rightarrow$ Marks decrease).
3. **Zero Covariance:** No relationship between the variables.

### Covariance Limitations
- Covariance has no fixed range, depends heavily on units, and is hard to compare directly, which is why we use correlation.

---

## 3. Correlation
- Correlation tells us how strong and in which direction two variables are related.
- It is a scaled version of covariance.

### Correlation Formula
$$r = \frac{Cov(X, Y)}{\sigma_X \sigma_Y}$$
- Where **$\sigma_X$** and **$\sigma_Y$** are the standard deviations of $X$ and $Y$.

### Range Of Correlation ($r$)
- Correlation always lies between $-1$ and $+1$.
- **$+1$:** Perfect Positive Correlation.
- **$-1$:** Perfect Negative Correlation.
- **$0$:** No Correlation.

---

## 4. Covariance vs. Correlation

| Feature | Covariance | Correlation |
| :--- | :--- | :--- |
| **Direction** | Shows Direction | Shows Direction + Strength |
| **Range** | Unbounded | Between $-1$ And $+1$ |
| **Units** | Unit-Dependent | Unit-Free |
| **Interpretation** | Hard To Interpret | Easy To Interpret |