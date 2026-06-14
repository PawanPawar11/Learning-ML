# NOTE:

The data has to be huge in order to ensure that the accuracy of both r2_score and mean_absolute_error is good otherwise it will fail humongously!

---

# What is coefficient that you created for each column in X?

When you train a Multiple Linear Regression model, it learns **how much each feature affects the final prediction**.

Suppose the model learns:

- StudyHours coefficient = 4.5
- Attendance coefficient = 0.8
- Assignments coefficient = 2.0
- Intercept = -20

Then the model's equation becomes:

Marks=-20+4.5(StudyHours)+0.8(Attendance)+2.0(Assignments)

### Meaning of each coefficient

**StudyHours coefficient = 4.5**

- If StudyHours increases by 1 hour,
- Marks increase by approximately 4.5 marks,
- assuming Attendance and Assignments stay the same.

**Attendance coefficient = 0.8**

- If Attendance increases by 1%,
- Marks increase by approximately 0.8 marks,
- assuming other features stay the same.

**Assignments coefficient = 2.0**

- If Assignments increase by 1,
- Marks increase by approximately 2 marks,
- assuming other features stay the same.

---

### Why did we print them?

```python
for feature, coef in zip(X.columns, model.coef_):
    print(feature, ":", coef)
```

Example output:

```python
StudyHours : 4.5
Attendance : 0.8
Assignments : 2.0
```

This tells us **which feature has the strongest influence on Marks**.

In this example:

- StudyHours → strongest impact
- Assignments → medium impact
- Attendance → smaller impact

---

### What is `zip()` doing here?

```python
zip(X.columns, model.coef_)
```

Combines:

```python
['StudyHours', 'Attendance', 'Assignments']
```

with

```python
[4.5, 0.8, 2.0]
```

to create pairs:

```python
('StudyHours', 4.5)
('Attendance', 0.8)
('Assignments', 2.0)
```

so we can print a readable result.

### In one line

**A coefficient tells how much the predicted value changes when that feature increases by 1 unit while all other features remain constant.**

---

# Then about intercept, what does that mean?

The **intercept** is the value of the prediction when **all input features are 0**.

For example, if the model equation is:

Marks=-20+4.5(StudyHours)+0.8(Attendance)+2.0(Assignments)

then:

- StudyHours = 0
- Attendance = 0
- Assignments = 0

gives:

```text
Marks = -20
```

So the **intercept is -20**.

---

### Simple Interpretation

Think of the intercept as the **starting point** of the prediction before any feature contributes.

```text
Predicted Value
=
Starting Point (Intercept)
+
Contribution from Feature 1
+
Contribution from Feature 2
+
...
```

---

### Real-World Note

Sometimes the intercept has a meaningful interpretation.

For example:

```text
Salary = 30000 + 5000 × YearsOfExperience
```

Here, **30000** could represent the base salary when experience is 0 years.

---

### In our student marks example

If the intercept is -20:

```text
Marks = -20 + ...
```

it doesn't necessarily mean a student can get -20 marks.

It simply means that the mathematical line that best fits the data happens to cross the y-axis at -20.

Many times, the intercept is just a mathematical adjustment used to fit the data better.

### Exam/Viva One-Liner

**Intercept is the predicted value of the dependent variable when all independent variables are equal to zero.**
