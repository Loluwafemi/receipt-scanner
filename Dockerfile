FROM python:3.12-slim

# Set the working directory
WORKDIR /app

ENV ENVIROMENT='production'

# Install Tesseract OCR and its development libraries
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    tesseract-ocr-eng \
    libtesseract-dev \
    libleptonica-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY main.py .
COPY index.html .

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

# Use the ASGI middleware to serve the Flask app
# Note: Ensure that the Flask app is properly integrated with FastAPI using ASGIMiddleware