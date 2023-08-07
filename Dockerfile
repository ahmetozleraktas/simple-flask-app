FROM python:3.8-slim-buster

# Set the working directory to /app
WORKDIR /app

COPY requirements.txt requirements.txt
# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Run app.py when the container launches
CMD ["python3", "app.py"]