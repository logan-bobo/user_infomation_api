FROM python:3.10.4

WORKDIR /app

COPY user_information_api /app

CMD ["./app/user_information_api/main.py"]


