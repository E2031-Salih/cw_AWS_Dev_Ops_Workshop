FROM python:3.7-alpine
WORKDIR /bookstore-app
COPY ./folder/ .
RUN pip install -r requirements.txt
EXPOSE 80
CMD python ./bookstore-api.py