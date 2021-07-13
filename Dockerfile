# Base image will be built on the python
FROM python:3.7

# Docker will create working directory
WORKDIR /project_02

# Copying all files from our location to the designed folder in container
# (we are already inside it)
COPY . .

# Installing all dependencies from requirements.txt
RUN pip install -r requirements.txt

# Assigning environment variable
ENV FLASK_ENV=development

# Docker will run these commands when container
# is initialized
CMD ["flask", "run", "-h", "0.0.0.0", "-p", "8000" ]

# IMPORTANT: The Docker wants that your application file is to
# be named as app.py by default otherwise the above CMD
# will not work.

# CLI command: docker run -d --rm  -p 5000:5000 <id of image>
# -d optional param to start container in background mode
# -rm optional param will remove container after it is stopped
# Biuld initial docker image: docker build -t flask_blog_prj_02 .
