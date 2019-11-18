FROM python:3.8

MAINTAINER ferdi.gueran@edeka.de

RUN pip install kazoo

COPY zxid_gen.py /

ENV ZK_HOST localhost:2181
ENV ZXIDS_INCREASE 100

CMD ["python", "/zxid_gen.py"]
