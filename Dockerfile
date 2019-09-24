FROM python:3-alpine

WORKDIR /soup.py

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . ./

CMD [ "python", "soup.py" ]