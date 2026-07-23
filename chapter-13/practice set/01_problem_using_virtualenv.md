# Creating a Virtual Environment Using `virtualenv`

## Step 1: Install `virtualenv` (Only Once)

```bash
pip install virtualenv
```

> `virtualenv` is an external package used to create isolated Python environments.

---

## Step 2: Create a Virtual Environment

```bash
virtualenv env1
```

This creates a new virtual environment named **env1**.

---

## Step 3: Activate the Environment

**PowerShell (Windows):**

```powershell
.\env1\Scripts\Activate.ps1
```

**Command Prompt (CMD):**

```cmd
env1\Scripts\activate.bat
```

When activated, you'll see:

```text
(env1) PS C:\Your\Project>
```

---

## Step 4: Install Packages

```bash
pip install numpy pandas requests
```

Packages are installed **only inside this virtual environment**.

---

## Step 5: Check Installed Packages

```bash
pip freeze
```

Shows all installed packages with their versions.

---

## Step 6: Deactivate the Environment

```bash
deactivate
```

This exits the virtual environment and returns to the system Python.

---

## Quick Workflow

```bash
pip install virtualenv

virtualenv env1

.\env1\Scripts\Activate.ps1

pip install numpy pandas requests

pip freeze

deactivate
```

---

## Notes

- `virtualenv` must be installed first using `pip install virtualenv`.
- Activate the environment before installing packages.
- Use `deactivate` to exit the virtual environment.
- `virtualenv` is an external tool, whereas `venv` comes built into Python (Python 3.3+).