# base python
FROM python:3

# add requirements and install in root
ADD requirements.txt /requirements.txt

RUN pip install -r requirements.txt

# expose server port for other containers
EXPOSE 5000