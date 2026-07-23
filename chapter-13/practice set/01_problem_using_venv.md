# Create two virtual environments, install few packages in the first one. How do you create a similar environment in the second one?python -m venv env1

# Creating an Identical Virtual Environment

## Objective
Create two virtual environments and make the second one identical to the first by installing the same packages with the same versions.

---

## Step 1: Create Two Virtual Environments

```bash
python -m venv env1
python -m venv env2
```

---

## Step 2: Activate the First Environment

```powershell
.\env1\Scripts\Activate.ps1
```

---

## Step 3: Install Required Packages

Example:

```bash
pip install numpy pandas requests
```

---

## Step 4: Save Installed Packages

```bash
pip freeze > requirements.txt
```

### What does this do?

- `pip freeze` lists all installed packages along with their versions.
- `>` redirects the output into a file.
- `requirements.txt` stores all dependencies of the project.

Example:

```text
numpy==2.3.1
pandas==2.3.0
requests==2.32.4
```

---

## Step 5: Deactivate the First Environment

```bash
deactivate
```

---

## Step 6: Activate the Second Environment

```powershell
.\env2\Scripts\Activate.ps1
```

---

## Step 7: Install the Same Packages

```bash
pip install -r requirements.txt
```

### What does `-r` mean?

`-r` stands for **read**.

`pip` reads the `requirements.txt` file and installs **all the packages with the exact same versions**, creating an identical environment.

---

## Complete Workflow

```bash
python -m venv env1
python -m venv env2

.\env1\Scripts\Activate.ps1

pip install numpy pandas requests

pip freeze > requirements.txt

deactivate

.\env2\Scripts\Activate.ps1

pip install -r requirements.txt
```

---

## Key Commands

| Command | Purpose |
|---------|---------|
| `python -m venv env1` | Create a virtual environment |
| `pip install package_name` | Install packages |
| `pip freeze` | Show all installed packages with versions |
| `pip freeze > requirements.txt` | Save installed packages to a file |
| `deactivate` | Exit the virtual environment |
| `pip install -r requirements.txt` | Install all packages from the file |

---

## Interview / Exam Answer

To create a similar virtual environment, first save the installed packages from the first environment using:

```bash
pip freeze > requirements.txt
```

Then activate the second environment and run:

```bash
pip install -r requirements.txt
```

This installs the same packages with the same versions, creating an identical environment.