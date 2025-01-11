# Use the official image as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Install PostgreSQL development packages, need this to install psycopg2 in requirements.txt
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    git \
    curl \
    telnet \
    openssh-client \
    iputils-ping \
    net-tools
    
# Copy the dependencies file to the working directory
COPY requirements.txt requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code to the working directory
COPY . .

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=app

# Run app.py when the container launches
CMD ["tail", "-f", "/dev/null"]