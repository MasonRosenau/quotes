FROM python:3.12-slim
WORKDIR /code
EXPOSE 5001
COPY requirements.txt /code
RUN pip install -r requirements.txt
COPY . /code
CMD ["python3", "src/app.py"]