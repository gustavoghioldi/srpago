FROM python:3

WORKDIR /usr/src/apps

COPY . .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


CMD ["python", "/usr/src/apps/app/api.py"]