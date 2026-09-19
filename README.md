# dsa

Practice Repository for DSA

# Problem Title

## 1. State the problem clearly. Identify the input & output formats.

### Problem Statement

> Add a clear, abstract explanation of the problem here.

### Input

1. **variable_1**: Description and data type.
2. **variable_2**: Description and data type.

### Output

1. **output_variable**: Description and expected data type.

---

## 2. Come up with some example inputs & outputs. Try to cover all edge cases.

Create a list of test scenarios (dictionaries are recommended for structured testing):

```python
tests = []

# Test Case 1: Standard/Generic case
tests.append({
    'input': {
        'variable_1': None,
        'variable_2': None
    },
    'output': None
})

# Test Case 2: Edge case (e.g., empty array, negative numbers, extreme values)
tests.append({
    'input': {
        'variable_1': None,
        'variable_2': None
    },
    'output': None
})
```

---

## 3. Come up with a correct solution for the problem. State it in plain English.

1. Explain step 1 of your brute-force approach.
2. Explain step 2.
3. Define how you will loop, slice, or track states.

---

## 4. Implement the solution and test it using example inputs. Fix bugs, if any.

```python
def solve_problem(variable_1, variable_2):
    # Write your code here
    pass
```

### Testing the Solution

```python
# Evaluate test cases
for i, test in enumerate(tests):
    result = solve_problem(**test['input'])
    print(f"Test {i}: Passed" if result == test['output'] else f"Test {i}: Failed")
```

---

## 5. Analyze the algorithm's complexity and identify inefficiencies, if any.

- **Time Complexity:** O(N) or O(N²) — explain why.
- **Space Complexity:** O(1) or O(N) — explain memory layout.

---

## 6. Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6.

### Optimized Strategy

> Explain your optimization technique (e.g., Binary Search, Hash Map, Two Pointers).

```python
def solve_problem_optimized(variable_1, variable_2):
    # Write your optimized code here
    pass
```
