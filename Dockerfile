# 1️⃣ Base image: a clean Linux image with Python pre-installed
FROM python:3.11-slim

# 2️⃣ Set working directory inside the container
WORKDIR /app

# 3️⃣ Copy requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4️⃣ Copy the rest of the app
COPY . .

# 5️⃣ Tell Docker how to start the app
CMD ["python", "app.py"]

