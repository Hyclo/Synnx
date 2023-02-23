FROM python:latest

WORKDIR /SynnxBot/Synnx

COPY SynnxBot/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./main.py"]