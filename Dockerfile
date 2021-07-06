# Base image will be built on the python
FROM python:3.7.2

# Docker will create working directory
WORKDIR /flask_project_02

# Copying all files from our location to the designed folder in container
COPY . /flask_project_02

# Installing all dependencies from requirements.txt
RUN pip install -r requirements.txt

# Opening port
EXPOSE 5000

# Docker will run these commands when container
# is initialized
CMD ["flask", "run", "-h", "0.0.0.0"]

# IMPORTANT: The Docker wants that your application file is to
# be named as app.py by default otherwise the above CMD
# will not work.

# CLI command: docker run -p 5000:5000 <id of image>
