FROM python

WORKDIR /app

COPY src ./

COPY requirements.txt .

RUN pip install -r requirements.txt

ENV FLASK_APP=main

CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]