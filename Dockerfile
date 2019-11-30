FROM python:3.7

MAINTAINER reOiL
ENV DEBIAN_FRONTEND noninteractive

COPY ./ /app
WORKDIR /app
RUN pip3 install -r requirements.txt
RUN chmod +x /app/entrypoint.sh
EXPOSE 8000
ENTRYPOINT ["/app/entrypoint.sh"]