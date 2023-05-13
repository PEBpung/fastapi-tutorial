FROM python:3.11.3-alpine

WORKDIR /app
COPY ./ /app

RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "api.py"]