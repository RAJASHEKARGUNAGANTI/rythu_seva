FROM python:3.9.7
EXPOSE 5000
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD [ "python" ,"app.py" ,"--host" ,"0.0.0.0"]