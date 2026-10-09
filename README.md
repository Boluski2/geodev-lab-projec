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
