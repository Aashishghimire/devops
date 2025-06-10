# Use official Python base image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements first (for caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the application files
COPY . .

# Expose port (optional, e.g., for Flask)
EXPOSE 3030

# Command to run the app (adjust based on your app)
ENTRYPOINT ["python", "app.py"]
