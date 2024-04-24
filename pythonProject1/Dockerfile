FROM python

WORKDIR /balot
COPY . /balot

RUN pip install --no-cache-dir nltk
RUN python -m nltk.downloader stopwords

CMD ["python", "balot.py"]