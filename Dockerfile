# 1. Use a lightweight version of Python as the base
FROM python:3.10-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy our requirements file first (for better caching)
COPY requirements.txt .

# 4. Install the dependencies inside the container
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of our code
COPY . .

# 6. Command to run when the container starts
# Note: host 0.0.0.0 is required for Docker containers to be accessible
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]