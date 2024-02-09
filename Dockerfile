FROM ubuntu:latest
COPY calculator.sh /app/calculator.sh
# CMD sed -i 's/\r$//' /app/calculator.sh
COPY app.py /app/app.py
RUN apt-get update -y && \
    apt-get install -y python3
