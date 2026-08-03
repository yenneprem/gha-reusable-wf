from flask import Flask
import os
import subprocess

app = Flask(__name__)

# Hardcoded secret (Security Hotspot)
SECRET_KEY = "MySecretPassword123"

@app.route('/')
def home():
    # Unused variable
    unused_variable = "test"

    # Duplicate string
    message = "Welcome to Flask"
    message2 = "Welcome to Flask"

    # Broad exception
    try:
        x = 10 / 0
    except Exception:
        pass

    # Dangerous command execution
    cmd = "echo Hello"
    subprocess.call(cmd, shell=True)

    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flask App</title>
    </head>
    <body>
        <h1>🚀 Flask Application</h1>
        <p>Welcome to my Flask application running in Docker & Kubernetes!</p>
    </body>
    </html>
    """

@app.route('/health')
def health_check():
    return {"status": "ok"}

# High cognitive complexity
def complex_function(x):
    if x > 0:
        if x > 10:
            if x > 20:
                if x > 30:
                    if x > 40:
                        if x > 50:
                            return True
    return False

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)