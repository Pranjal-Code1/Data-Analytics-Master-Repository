# Introduction to Matplotlib (welcome back Sher)

Matplotlib is one of the most widely used **data visualization libraries in Python**.  
It provides a flexible and powerful way to create plots, graphs, and charts, helping us **understand patterns, trends, and insights** in data.

---

## Key Points

- **Library type**: Low-level plotting library  
- **Core Idea**: Gives full control over every element of a figure (titles, axes, labels, colors, styles, etc.)  
- **Origin**: Inspired by MATLAB’s plotting system, hence its name **Matplotlib**  
- **Flexibility**: Can create anything from simple line plots to highly customized multi-plot figures  
- **Integration**: Works seamlessly with NumPy, Pandas, and SciPy

---

## Why Use Matplotlib?

- To **visualize data** effectively before analysis and modeling  
- To create **publication-quality figures**  
- To **customize every detail** of plots (size, colors, fonts, legends, grids)  
- Acts as the **foundation** for other visualization libraries like **Seaborn**, **Pandas .plot()**, and **Plotly (partially inspired)**

---

## Anatomy of a Matplotlib Figure

A Matplotlib figure consists of several key components:

1. **Figure** → The whole window or page that contains everything  
2. **Axes** → The actual area where data is plotted (x-axis, y-axis)  
3. **Axis** → The scales and ticks for x and y directions  
4. **Plot elements** → Titles, labels, legends, lines, bars, markers, etc.

---

## Typical Workflow

1. **Import the library**  
   ```python
   import matplotlib.pyplot as plt
   ```

   Basic Example: Plotting Two Arrays

    ```python
    import matplotlib.pyplot as plt
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]

    plt.plot(x, y, marker="o", linewidth=2.5, label="Meri Line",
            linestyle="--", markersize=10, markeredgecolor='red')
    plt.legend()
    plt.grid(True)
    plt.show()

