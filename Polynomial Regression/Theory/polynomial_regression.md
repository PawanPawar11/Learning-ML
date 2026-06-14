# Useful article:

https://www.geeksforgeeks.org/machine-learning/python-implementation-of-polynomial-regression/
Read it with a calm mind, you'll understand a lot!

---

# What happens internally?

For `degree=2`, a feature like:

```python
X = [5]
```

becomes:

```python
[1, 5, 25]
```

where:

- `1` → Bias term
- `5` → x
- `25` → x²

The model learns an equation of the form:

y=b_0+b_1x+b_2x^2

Example:

```text
Salary = 30 + 2.5(Years) + 3.8(Years²)
```

Unlike Linear Regression (straight line), Polynomial Regression can fit curves, making it useful when the relationship between X and y is non-linear.

---

# Why is it that while taking X values you used double square brackets, while in for y values you used only a single square bracket?

```python
X = df[["Years"]]
y = df["Salary"]
```

The difference is because **scikit-learn expects X and y in different shapes**.

### X (Features) → Double Square Brackets

```python
X = df[["Years"]]
```

This returns a **DataFrame** (2D structure).

Shape:

```python
(10, 1)
```

Meaning:

```text
10 rows
1 column
```

Example:

```python
   Years
0      1
1      2
2      3
```

Scikit-learn expects features in this format:

```text
(number_of_samples, number_of_features)
```

Even if there is only one feature, it must still be 2D.

---

### y (Target) → Single Square Bracket

```python
y = df["Salary"]
```

This returns a **Series** (1D structure).

Shape:

```python
(10,)
```

Example:

```python
0     45
1     50
2     60
```

The target variable is usually a single column, so scikit-learn expects it as a 1D array.

---

### What if you use a single bracket for X?

```python
X = df["Years"]
```

Then X becomes a Series:

Shape:

```python
(10,)
```

which is 1D.

Many sklearn models will throw an error like:

```text
Expected 2D array, got 1D array instead
```

because they need:

```text
X = [[1],
     [2],
     [3]]
```

not:

```text
X = [1, 2, 3]
```

---

### Simple Rule

- **X (features)** → `df[["column"]]` → 2D DataFrame
- **y (target)** → `df["column"]` → 1D Series

I remember it as:

> X can contain multiple features, so keep it 2D.
>
> y is usually one target column, so keep it 1D.
