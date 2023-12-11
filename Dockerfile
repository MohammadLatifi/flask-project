FROM python:3.8

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000

COPY . .
RUN chmod +x wait-for-it.sh

