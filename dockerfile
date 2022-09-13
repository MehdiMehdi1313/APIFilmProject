FROM python:3
WORKDIR E:\IMT\S9\APIFilmProject
ADD application.py /

CMD ["setx", "FLASK_APP", "application.py", "flask", "run"]