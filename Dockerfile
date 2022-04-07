FROM python:2.7-stretch

RUN pip install tox

WORKDIR /opt/django-piston3

ADD VERSION .
ADD tox.ini .
ADD requirements.txt .
ADD README.md .
ADD setup.py .
ADD ez_setup.py .
ADD MANIFEST.in .
ADD piston/ ./piston
ADD tests/ ./tests

CMD ["bash"]
