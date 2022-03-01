FROM python:latest

COPY sp.py sp.py

COPY install.txt install.txt

RUN pip install -r install.txt

ENTRYPOINT ["python","sp.py"]