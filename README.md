# geodev-lab-projec
Which woredas in Ikosi Ketu Lagos have settlements located more than 5 km by road from the nearest health facility?


## Month 2: Preparation of the enviroment section of the project, install Python and write my first python line of code 

-week 5: Setup python and also install uv and also did hello.py run

# Week 6: Python Project Management with uv

## Overview

This week, I learned how to manage Python projects using **uv**, a fast Python package and project manager.

## What I Learned

* **Initialize a project:** Use `uv init` to create a new Python project.
* **Add a dependency:** Use `uv add package_name` to install a package and record it in `pyproject.toml`.
* **Remove a dependency:** Use `uv remove package_name` to uninstall a package and update the project configuration.
* **Install project dependencies:** Use `uv sync` to install the dependencies specified in `pyproject.toml` and synchronize the project environment with `uv.lock`.
* **Run a Python file:** Use `uv run filename.py` to execute a Python script within the project's environment.

## Practical Exercise

I added the `pandas` library to my project and created a `check.py` file to print the installed pandas version.

```python
import pandas as pd

print(pd.__version__)
```

To run the script, I used:

```powershell
uv run check.py
```

I also verified my uv installation using:

```powershell
uv --version
```

## Key Takeaway

I learned how uv simplifies Python project setup, dependency management, environment synchronization, and script execution. I also learned how `pyproject.toml` and `uv.lock` help keep project dependencies organized and reproducible.



## Week 7: Learning Python Fundamentals — Analysing Ward Data

### Overview

This week, I learned the fundamentals of programming in Python and applied them to real-world ward data using a CSV file. I practised reading data, converting values, applying conditions, and classifying wards based on their area in square kilometres.

### What I Learned

- **Variables:** Understanding how variables store values and why the equals sign (`=`) assigns a value.
- **Data types:** Learning the difference between strings and numbers, including why `"5" + "5"` produces `"55"`.
- **Lists:** Understanding how lists work and how indexing starts from zero.
- **Loops:** Using `for` loops to process multiple wards in a CSV file.
- **Conditions:** Using `if` and `else` statements to classify wards based on their area.
- **Functions:** Learning how functions help organize reusable code.
- **Error handling:** Practising how to read Python error messages calmly, starting from the bottom of a traceback.

### Practical Project: `analyse.py`

I worked with a `wards.csv` file containing ward names and their areas. The script reads the CSV file, processes each ward, converts its area to a numeric value, and classifies the ward as either large or small.

The classification rule is:

- **Large:** Ward area is greater than 9 km².
- **Small:** Ward area is 9 km² or less.

### Code Example

```python
with open("wards.csv") as f:
    lines = f.readlines()

for line in lines[1:]:
    parts = line.strip().split(",")
    ward = parts[0]
    area_km2 = float(parts[1])

    if area_km2 > 9:
        size = "large"
    else:
        size = "small"

    print(ward, "is", size)
```

### Key Takeaway

I learned how to move from basic Python concepts to writing a practical script that processes and classifies geographical data. I also practised understanding code line by line, reading errors, and building a working solution step by step.

**Week 7 deliverable:** `analyse.py` reads `wards.csv`, converts each ward's area to a numeric value, and classifies each ward as large or small based on the 9 km² threshold.
