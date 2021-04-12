FROM python:3.9
LABEL maintainer="mr.naveen8@hotmail.com"
COPY . /src
WORKDIR /src
RUN python -m pip install poetry
RUN python -m poetry config virtualenvs.create false
RUN python -m poetry install
EXPOSE 80
ENTRYPOINT ["poetry", "run", "uvicorn", "dockerdive.views:app", "--host", "0.0.0.0", "--port", "80"]