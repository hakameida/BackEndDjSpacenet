# Base image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


# Working directory
WORKDIR /app

EXPOSE 8000
# create media dir
RUN mkdir -p /app/media

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
# Copy project files
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Start server
CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]
