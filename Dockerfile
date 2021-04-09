FROM python:3.9-slim

RUN pip3 install sqlalchemy psycopg2-binary pandas

WORKDIR /src