FROM python:3

ADD main.py /

ADD pic.jpg /

ADD Rajdhani-Bold.ttf /

ADD requirements.txt /

ADD .session /

RUN pip install -r requirements.txt

CMD [ "python", "./main.py" ]
