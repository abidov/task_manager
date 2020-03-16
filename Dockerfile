FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /task_manager_site
WORKDIR /task_manager_site
COPY requirements.txt /task_manager_site/
RUN pip install -r requirements.txt
COPY . /task_manager_site/