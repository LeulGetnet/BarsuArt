# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files into the container
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Run migrations and collect static files (optional)
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

# Start the Django application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "barsuart.wsgi:application"]
