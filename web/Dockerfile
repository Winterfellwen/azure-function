FROM tiangolo/uwsgi-nginx-flask:python3.6

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

RUN curl https://packages.microsoft.com/keys/microsoft.asc | sudo gpg --yes --dearmor --output /usr/share/keyrings/microsoft.gpg

RUN sh -c 'echo "deb [arch=amd64 signed-by=/usr/share/keyrings/microsoft.gpg] https://packages.microsoft.com/repos/microsoft-debian-bullseye-prod bullseye main" > /etc/apt/sources.list.d/microsoft.list'

RUN apt update && sudo apt install -y powershell

RUN pwsh -Command "Write-Host 'Hello, World!'"

ADD ./web /app
