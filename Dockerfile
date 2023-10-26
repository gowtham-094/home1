FROM python:3.11
ENV PYTHONUNBUFFERED 1
ADD . /Rent
WORKDIR /Rent
COPY ./requirements.txt /Rent/requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]