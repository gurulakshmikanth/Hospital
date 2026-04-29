FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["gunicorn", "Hospital.wsgi:application", "--bind", "0.0.0.0:8080"]
