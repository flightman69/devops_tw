FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install dependencies first (to leverage Docker layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .

COPY . .
# Expose port and run application
EXPOSE 3000
CMD ["python", "app.py"]