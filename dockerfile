FROM python:3
COPY . /app
WORKDIR /app

#ADD application.py /

#RUN setx FLASK_APP application.py
RUN pip install -r requirements.txt

EXPOSE 8080
#CMD ["setx", "FLASK_APP", "application.py", "flask", "run"]
ENTRYPOINT [ "python" ]
CMD [ "application.py" ]