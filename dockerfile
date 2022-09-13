FROM python:3
COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5001
#ENTRYPOINT [ "python" ]
#CMD [ "application.py" ]

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
