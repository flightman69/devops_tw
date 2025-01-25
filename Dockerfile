FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install dependencies first (to leverage Docker layer caching)
COPY app/ /app
RUN pip install --no-cache-dir -r /app/requirements.txt

# Expose port and run application
EXPOSE 3000
CMD ["python", "app.py"]