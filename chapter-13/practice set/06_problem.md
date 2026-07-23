# Run pip freeze for the system interpreter. Take the contents and create a similar virtual environment.

1. Check installed packages in the system Python
   pip freeze

2. Save all packages to a requirements file
   pip freeze > requirements.txt

3. Create a new virtual environment
   python -m venv env_name

4. Activate the virtual environment
   Windows: env_name\Scripts\activate
   macOS/Linux: source env_name/bin/activate

5. Install all packages from the requirements file
   pip install -r requirements.txt

6. Verify the installation (optional)
   pip freeze