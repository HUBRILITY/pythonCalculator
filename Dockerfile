FROM python:3.9.6

ADD . .

CMD ["python", "-m", "unittest", "discover", "-s", "src"]