
FROM openjdk:11-jdk-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


RUN apt-get update && apt-get install -y python3 python3-pip


WORKDIR /app

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .


EXPOSE 5000


CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
