FROM python:3.9.7
WORKDIR /code
RUN apt-get update && apt-get install -y python3-opencv
RUN pip install opencv-python-headless
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5100
CMD [ "python", "api/app.py" ]