FROM mcr.microsoft.com/powershell:latest

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
ADD ./web /app
