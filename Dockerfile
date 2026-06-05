FROM python:3.12-slim
COPY first.py  /first.py
ENTRYPOINT ["python", "first.py"]