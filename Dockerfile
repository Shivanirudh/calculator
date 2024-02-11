FROM ubuntu:latest
COPY calculator.sh /app/calculator.sh
# CMD sed -i 's/\r$//' /app/calculator.sh
COPY app.py /app/app.py
COPY testing.py /app/testing.py
RUN apt-get update -y && \
    apt-get install -y python3
