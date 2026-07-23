# Explore the Flask module and create a web server using Flask and Python.

1. Create and activate a virtual environment (recommended)

2. Install Flask
   pip install flask

3. Create a Python file (e.g., app.py)

4. Import Flask and create a Flask application
   from flask import Flask
   app = Flask(__name__)

5. Create a route
   @app.route("/")
   def home():
       return "Hello, World!"

6. Run the application
   app.run()

7. Open the browser and visit
   http://127.0.0.1:5000

8. Verify that the message "Hello, World!" is displayed.

Flask is a lightweight Python framework used to build web applications, websites, and APIs by creating a web server and handling user requests.