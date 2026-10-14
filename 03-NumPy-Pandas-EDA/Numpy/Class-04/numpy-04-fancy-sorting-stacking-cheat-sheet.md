# Class 04: Fancy Indexing, Conditional Selection, Sorting, and Stacking

## 1. Fancy Indexing
* Allows picking non-contiguous elements from specific index lists (e.g., `arr[[0, 2, 4]]`).
* Supports 2D coordinate lookups by passing row and column index arrays together (e.g., `matrix[[0, 1], [1, 2]]`).

## 2. Conditional Selection (`np.where`)
* `np.where(condition)` returns index locations matching criteria.
* `np.where(condition, x, y)` acts like an element-wise conditional operator, returning `x` where true and `y` where false.

## 3. Sorting & Ordering
* **`np.sort()`**: Returns sorted values directly.
* **`np.argsort()`**: Returns index positions that would sort the array.
* **Axis control**: Use `axis=1` to sort row-wise and `axis=0` to sort column-wise.

## 4. Concatenation & Stacking
* **`np.concatenate()`**: Merges sequences together.
* **`np.vstack()`**: Combines arrays vertically (row-wise growth).
* **`np.hstack()`**: Combines arrays horizontally (column-wise growth).