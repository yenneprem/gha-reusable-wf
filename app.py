from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flask App</title>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #4facfe, #00f2fe);
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }

            .card {
                background: white;
                padding: 40px;
                border-radius: 15px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.2);
                text-align: center;
                width: 400px;
            }

            h1 {
                color: #2c3e50;
                margin-bottom: 10px;
            }

            p {
                color: #555;
                font-size: 18px;
            }

            .status {
                display: inline-block;
                margin-top: 20px;
                padding: 10px 20px;
                background: #28a745;
                color: white;
                border-radius: 20px;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🚀 Flask Application</h1>
            <p>Welcome to my Flask application running in Docker & Kubernetes!</p>
            <div class="status">Status: Running ✅</div>
        </div>
    </body>
    </html>
    """

@app.route('/health')
def health_check():
    return {
        "status": "ok"
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)