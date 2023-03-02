FROM python:latest

WORKDIR /Synnx/SynnxBot

COPY SynnxBot/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python3", "main.py"]