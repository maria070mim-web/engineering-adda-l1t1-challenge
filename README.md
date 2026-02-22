# Engineering Adda - First Semester Integrated Programming Challenge

## Overview

You are required to build a Student Performance and Productivity Analyzer using Python. This challenge integrates programming fundamentals, mathematical reasoning, and logical thinking.

The main implementation must be a Command Line Interface (CLI) application written in Python.

An optional FastAPI implementation is available as a bonus challenge.

[PDF Problemset (Generated from this .md)](https://drive.google.com/file/d/1tLf9TpGWT3NhuwZCo7MUhcj-ZIwpKDBG/view?usp=sharing)

**Deadline: 11:59 PM, 22nd February 2026**

## Prizes & Rewards

### Core Challenge Gift

The **top 3 participants** with the best core implementations will each receive a copy of:

> **Structured C/C++ Programming**
> (কাঠামোমুখী সি/সি-প্লাস-প্লাস পরিগণনা)
>
> - ড. মোহাম্মদ কায়কোবাদ, ড. মো. মোস্তফা আকবর, ড. মু. আ. হাকিম নিউটন

3 copies will be awarded in total.

### Bonus Challenge Prize

A special prize awaits the best bonus (FastAPI) submission. Details to be announced soon, stay tuned!

---

## Part 1: CGPA Calculator

### Problem Description

A student takes 5 courses. For each course, you are given:

- Credit hours (may be a decimal value, e.g. 1.5)
- Marks (out of 100)

You must:

1. Convert marks into grade points using the grading table below.
2. Calculate total credits.
3. Calculate weighted CGPA.
4. Display final CGPA rounded to 2 decimal places.

### Grading System

| Marks Range      | Grade | Grade Point |
| ---------------- | ----- | ----------- |
| 80% and Above    | A+    | 4.0         |
| 75% to below 80% | A     | 3.75        |
| 70% to below 75% | A-    | 3.5         |
| 65% to below 70% | B+    | 3.25        |
| 60% to below 65% | B     | 3.0         |
| 55% to below 60% | B-    | 2.75        |
| 50% to below 55% | C+    | 2.5         |
| 45% to below 50% | C     | 2.25        |
| 40% to below 45% | D     | 2.0         |
| Below 40%        | F     | 0.0         |

### Requirements

- Take input for 5 courses.
- Use conditional statements to determine grade points.
- Use loops to process courses.
- Use proper formula for weighted CGPA:

$$
\text{CGPA} = \frac{\sum (\text{Grade Point} \times \text{Credit})}{\text{Total Credits}}
$$

## Part 2: Study Efficiency During Ramadan

### Story Context

It is Ramadan. The student is fasting from dawn to sunset. During fasting, energy levels fluctuate depending on sleep quality, hydration before dawn, and study timing.

The student studied for 7 days before the exam during Ramadan.

Daily study hours:

```python
hours_list = [2, 3, 4, 5, 6, 4, 3]
```

Studying longer while fasting does not always mean higher productivity. After a certain point, fatigue reduces effective learning.

### Productivity Model

Assume:

- Productivity increases steadily up to 4 hours of study.
- After 4 hours, fatigue during fasting reduces effective productivity.

$$
\text{Effective Hours} =
\begin{cases}
  \text{hours} & \text{if } \text{hours} \leq 4 \\
  \max\left(4 - 0.5 \times (\text{hours} - 4),\ 0\right) & \text{if } \text{hours} > 4
\end{cases}
$$

### Tasks

1. Compute effective study hours for each day.
2. Calculate total actual study hours.
3. Calculate total effective study hours.
4. Identify the most productive fasting day.
5. In your `README.md`, write 2–3 sentences explaining why fasting may change productivity patterns.

## Part 3: Energy Modeling During Fasting (Calculus-Inspired Model)

### Story Context

During fasting, the body has limited stored energy. Mental performance typically peaks at moderate effort and decreases if effort is too low or too high.

We model mental energy using a quadratic function:

$$
E(\text{hours}) = k + a \cdot (\text{hours} - h)^{2}
$$

Where the variables are defined as:

| Variable     | Value                   | Meaning                                      |
| ------------ | ----------------------- | -------------------------------------------- |
| `k`          | 100                     | Peak energy level (maximum possible energy)  |
| `a`          | -8                      | Steepness of decline (negative = opens down) |
| `h`          | 3                       | Optimal study hours (vertex of the parabola) |
| `hours`      | varies                  | Actual study hours for that day              |
| `hours_list` | `[2, 3, 4, 5, 6, 4, 3]` | Study hours across 7 days                    |

So the formula expands to:

$$
E(\text{hours}) = 100 - 8 \cdot (\text{hours} - 3)^{2}
$$

This represents a downward-opening parabola.

Interpretation:

- Maximum energy occurs when `hours = h = 3`.
- Energy decreases symmetrically if study hours move away from 3.
- If the result is negative, treat energy as 0.

### Tasks

1. Define the variables `k`, `a`, `h`, and `hours_list` explicitly in your code.
2. Write a function `calculate_energy(hours, k, a, h)` that computes energy for a given day.
3. Calculate energy level for each of the 7 days using that function.
4. Identify:
   - Day with maximum energy
   - Day with minimum energy

5. **Plot a graph** using `matplotlib` with the following requirements:
   - X-axis: continuous range of hours from 0 to 8 (use `range` or `numpy`).
   - Y-axis: energy values computed from the formula.
   - Draw the **smooth quadratic curve** across the full range.
   - **Mark the 7 actual study days** as individual points (dots) on the curve.
   - Label the axes and add a title: `"Mental Energy Model During Fasting"`.
   - Save the graph as `energy_graph.png`.

6. In your `README.md`, write 3–4 sentences explaining:
   - Why moderate study hours may be optimal during fasting.
   - How this relates to the shape of a quadratic function in calculus.
   - Embed `energy_graph.png` in the README directly below the explanation.

## Required Function Signatures

Your `main.py` must define the following functions at module level with these **exact names and parameters**. The submission is evaluated by an automated test suite that imports `main.py` and calls each function directly.

### Part 1

```python
def get_grade_point(marks: float) -> float:
    """
    Convert a marks value (0-100) to its grade point.
    Returns one of: 4.0, 3.75, 3.5, 3.25, 3.0, 2.75, 2.5, 2.25, 2.0, 0.0
    """

def calculate_gpa(courses: list) -> tuple:
    """
    courses -- list of dicts, each with keys 'credit' (int or float) and 'marks' (float)
    Returns (gpa: float rounded to 2 dp, total_credits: float)
    """
```

### Part 2

```python
def calculate_effective_hours(hours: float) -> float:
    """
    Apply the fasting productivity model to one day's study hours.
    Returns effective hours (>= 0).
    """

def get_study_analysis(hours_list: list) -> dict:
    """
    Returns a dict with keys:
      'total_actual_hours'    : float
      'total_effective_hours' : float
      'most_productive_day'   : int  (1-indexed)
    """
```

### Part 3

```python
def calculate_energy(hours: float, k: float, a: float, h: float) -> float:
    """
    Compute E = k + a*(hours - h)^2, clamped to >= 0.
    """

def get_energy_analysis(hours_list: list, k: float, a: float, h: float) -> dict:
    """
    Returns a dict with keys:
      'energies'       : list of float (one per day)
      'max_energy_day' : int  (1-indexed)
      'min_energy_day' : int  (1-indexed)
    """

def plot_energy_graph(
    hours_list: list,
    k: float,
    a: float,
    h: float,
    output_path: str = 'energy_graph.png',
) -> None:
    """
    Plot the energy curve and mark the actual study days.
    Save the figure to output_path.
    """
```

All CLI interaction must be inside a `main()` function called under `if __name__ == '__main__'`.

---

## README Requirements

Your repository must include a `README.md` file written in proper Markdown.

### Required Structure

The README must follow this heading hierarchy:

```markdown
# Student Performance and Productivity Analyzer

## Part 2 - Study Efficiency: Fasting and Productivity

[Your 2-3 sentence explanation here]

## Part 3 - Energy Model Explanation

[Your 3-4 sentence explanation here]

### Energy Graph

![Mental Energy Model During Fasting](energy_graph.png)

## How to Run

[Instructions to run main.py]
```

### README Rules

- Must use `#` for the document title and `##` / `###` for sections.
- The `energy_graph.png` image must be **embedded** using Markdown image syntax, not just linked.
- Written in clear, grammatically correct English.
- No placeholder or template text left in.

## Implementation Rules

- Use functions for each major task.
- Do not write all logic inside the main section.
- Use meaningful variable names.
- Avoid hardcoding CGPA results.
- Code must run without crashing.
- All seven functions listed in **Required Function Signatures** must be present and importable.
- CLI input/output must live inside `main()` only -- all computation functions must work independently of user input.

---

## Bonus Challenge: FastAPI Version

Students who complete the CLI version correctly may implement a FastAPI version to receive a **special bonus prize** (to be announced). Only valid, working implementations will be considered.

### Requirements for Bonus

1. Install required packages:

```bash
pip install fastapi uvicorn
```

2. Create a FastAPI application.

3. Implement the following endpoints:

```text
POST /calculate-gpa
    Input:  JSON list of courses (credit and marks)
    Output: CGPA and total credits

GET /study-analysis
    Output:
        - Total actual hours
        - Total effective hours
        - Most productive fasting day

GET /energy-analysis
    Output:
        - Energy per day
        - Maximum energy day
        - Minimum energy day
```

### Important Conditions

- All calculation logic must be separated into reusable functions.
- Routes must call those functions.
- JSON responses must be properly formatted.
- Application must run successfully using:

```bash
uvicorn main:app --reload
```

If logic is incorrect or the application crashes, the bonus will not be awarded.

---

## Evaluation Criteria

Core Implementation (Mandatory)

| Criterion                                | Marks |
| ---------------------------------------- | ----- |
| Correct CGPA calculation                 | 20    |
| Correct fasting efficiency logic         | 20    |
| Correct energy computation               | 20    |
| Proper use of loops and functions        | 10    |
| Code quality and clarity                 | 10    |
| README - proper heading structure        | 10    |
| README - energy graph correctly embedded | 10    |

### Total: 100 marks

Bonus Implementation (Optional)

- Working FastAPI application
- Proper API structure
- Clean separation of logic
- Correct JSON responses

---

## Submission Instructions

### Step 1 - Create a GitHub Repository

1. Go to [github.com](https://github.com) and sign in (or create a free account).
2. Create a **new public repository** named:

   ```text
   engineering-adda-l1t1-challenge
   ```

3. Upload your project files to the repository. Your repository should contain at minimum:

   | File                  | Description                                  |
   | --------------------- | -------------------------------------------- |
   | `main.py`             | Your main CLI application                    |
   | `README.md`           | Explanations and embedded energy graph       |
   | `energy_graph.png`    | The matplotlib energy graph (also in README) |
   | `app.py` _(optional)_ | FastAPI application (bonus)                  |

4. Make sure your repository is set to **Public** so it can be reviewed.

### Step 2 - Submit the Form

Once your repository is ready, fill in the submission form below:

> **[Submit Here -- https://forms.gle/jNFjW9Q5DGWcty5T6](https://forms.gle/jNFjW9Q5DGWcty5T6)**

The form will ask for:

- Your GitHub repository link
- Your `energy_graph.png` file (upload directly to the form)

**Submissions without a working GitHub repository link will not be evaluated.**

---

End of Challenge. Happy Ramadan!


Fasting changes productivity patterns because the body relies on stored energy, which often leads to a peak in mental clarity and focus. However, as energy levels deplete over time, productivity may decrease, creating a specific window of high performance.
During fasting, mental energy does not follow a linear path; instead, it peaks at a certain point and then declines as physical exhaustion sets in. Moderate study hours are optimal because they allow a student to utilize their peak cognitive window before reaching the point of diminishing returns.
​In calculus, this is represented by a downward-opening quadratic function (a parabola where the leading coefficient is negative). The "optimal" study time corresponds to the vertex of the parabola, where the derivative of the energy function is zero (f'(x) = 0), marking the maximum point of efficiency. Beyond this point, any additional study hours lead to a decrease in overall mental energy and retention.
