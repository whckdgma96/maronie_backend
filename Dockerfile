FROM  tensorflow/tensorflow:latest-gpu-py3

COPY requirements.txt /app/
EXPOSE 5000
WORKDIR /app

RUN apt install -y python3

RUN pip install --upgrade pip \
    &&  pip install --requirement requirements.txt

COPY . .

CMD ["python", "app.py"]

# FROM python:3.8-alpine 

# WORKDIR /app

# COPY requirements.txt requirements.txt 
# RUN python -m pip install --upgrade pip
# RUN pip3 install -r requirements.txt 

# COPY . .


