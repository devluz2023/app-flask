FROM python:3.10
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENV FLASK_ENV=development
COPY . .
CMD ["python", "run.py"]
