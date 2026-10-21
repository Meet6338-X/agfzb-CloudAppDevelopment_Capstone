FROM python:3.11-slim-bookworm

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .

# The VADER sentiment lexicon that the analyser loads at start up.
ENV NLTK_DATA=/python-docker/sentiment

EXPOSE 5050

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=5050"]
