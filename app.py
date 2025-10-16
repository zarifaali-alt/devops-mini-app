from flask import Flask
import os

app = Flask(__name__)

# 1️⃣ Read environment variables
APP_NAME = os.getenv("APP_NAME", "DevOps pipeline")
PORT = int(os.getenv("PORT", 5000))

# 2️⃣ Root route
@app.route('/')
def home():
    return f"Hello from {APP_NAME}!"

# 3️⃣ Health-check route
@app.route('/health')
def health():
    return {"status": "ok", "service": APP_NAME}, 200

# 4️⃣ Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)

