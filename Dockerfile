FROM ubuntu:16.04	
FROM python:3.6

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# CMD [ "python", "./run.py" ]
CMD ["gunicorn", "--config", "gunicorn_config.py", "flaskblog:app"]