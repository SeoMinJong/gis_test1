FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/SeoMinJong/gis_test1.git

WORKDIR /home/gis_test1/

RUN echo "SECRET_KEY=django-insecure-62@(le_*ut*zx61m-l)x6c$-19%vu_tpt^428v2^a#5v_oia!@" > .env

RUN pip install -r requirement.txt

RUN pip install gunicorn

RUN python manage.py migrate

EXPOSE 8000

CMD ["gunicorn", "gis_test1.wsgi", "--bind", "0.0.0.0:8000"]