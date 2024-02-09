FROM ubuntu:latest
COPY calculator.sh /app/calculator.sh
# CMD sed -i 's/\r$//' /app/calculator.sh
COPY app.py /app/app.py
