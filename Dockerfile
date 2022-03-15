#python version 3.6
FROM  tensorflow/tensorflow:2.2.3-py3

COPY requirements.txt /backend/
EXPOSE 5000
WORKDIR /backend

#opencv-python을 위해 필요하다
RUN apt-get -y update && apt-get -y upgrade && apt-get install -y build-essential
RUN apt-get install libgl1-mesa-glx -y 

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


