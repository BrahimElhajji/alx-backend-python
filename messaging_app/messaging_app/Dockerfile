# Use the official Python base image
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire messaging app code into the container
COPY . /app/

# Expose port 8000 (Django default)
EXPOSE -p 8000

# Default command to run Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

