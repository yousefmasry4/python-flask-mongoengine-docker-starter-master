FROM python:3.9.7
WORKDIR /code
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5100
CMD [ "python", "api/app.py" ]