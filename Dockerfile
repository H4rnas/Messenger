FROM python:latest

COPY okok.py okok.py

COPY install.txt install.txt

RUN pip install -r install.txt

ENTRYPOINT ["python","okok.py"]