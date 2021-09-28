FROM python:3.9.0

WORKDIR /home/

RUN echo "ashweh"

RUN git clone https://github.com/SeoMinJong/gis_test1.git

WORKDIR /home/gis_test1/

RUN pip install -r requirement.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=gis_test1.settings.deploy && python manage.py migrate --settings=gis_test1.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=gis_test_of_test.settings.deploy gis_test1.wsgi --bind 0.0.0.0:8000"]