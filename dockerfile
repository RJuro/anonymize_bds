FROM python:3.9

COPY . /api

RUN pip install -r /api/requirements.txt

ENV PYTHONPATH=/
WORKDIR /

EXPOSE 8000

ENTRYPOINT ["uvicorn"]
CMD ["api.app:app", "--host", "0.0.0.0"]