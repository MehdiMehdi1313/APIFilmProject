FROM python:3
ADD application.py /

CMD ["setx", "FLASK_APP", "application.py", "flask", "run"]