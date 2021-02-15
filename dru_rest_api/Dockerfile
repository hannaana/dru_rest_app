FROM python:3.7

WORKDIR /flask_app

COPY requirements.txt ./
RUN pip3 install -r requirements.txt

RUN export PYTHONPATH='${PYTHONPATH}:/flask_app'
ENV PYTHONPATH "${PYTHONPATH}:/flask_app"
COPY . .

CMD ["python", "./app/run.py"]
