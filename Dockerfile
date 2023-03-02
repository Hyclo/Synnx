FROM python:latest

WORKDIR /appo

COPY SynnxBot/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY /SynnxBot/main.py /appo/main.py

CMD [ "python3", "main.py"]