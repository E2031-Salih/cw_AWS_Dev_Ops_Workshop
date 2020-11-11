FROM python:3.7-alpine
WORKDIR /phonebook-app
COPY ./folder/ .
RUN pip install -r requirements.txt
EXPOSE 80
CMD python ./phonebook-app.py