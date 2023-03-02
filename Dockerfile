FROM python:latest

WORKDIR /root/Synnx/SynnxBot

COPY SynnxBot/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "main.py"]