
FROM python:3.11

WORKDIR /iris_model


COPY req.txt /iris_model/req.txt


RUN pip install --no-cache-dir -r /iris_model/req.txt


COPY . /iris_model


EXPOSE 8000


CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
