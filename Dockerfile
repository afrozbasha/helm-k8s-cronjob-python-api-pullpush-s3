FROM python:3.11.1

RUN pip3 install requests

RUN pip3 install boto3

WORKDIR /usr/src/app

COPY python-scripts/* ./

CMD [ "python3", "pulldata.py" ]
