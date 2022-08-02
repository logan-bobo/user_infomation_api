FROM python

WORKDIR /app

COPY src .

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python3", "run.py"]
