# Use the official Python 3.9 image as the base image for the new Docker image
FROM python:3.9 

# Copy the contents of the current directory (the `.`) to the `/api` directory inside the Docker image
COPY . /api

# Install the Python packages listed in the `requirements.txt` file located in the `/api` directory
RUN pip install -r /api/requirements.txt

# Set the `PYTHONPATH` environment variable to the root directory inside the Docker container
ENV PYTHONPATH=/

# Set the working directory inside the Docker container to the root directory
WORKDIR /

# Expose port 8000 on the Docker container
EXPOSE 8000

# Specify that the entry point for the Docker container is the `uvicorn` command
ENTRYPOINT ["uvicorn"]

# Specify the default command to run when the container starts. This command starts the Uvicorn server, serving the `app` object in the `api.app` module, listening on all available network interfaces (`0.0.0.0`)
CMD ["api.app:app", "--host", "0.0.0.0"]