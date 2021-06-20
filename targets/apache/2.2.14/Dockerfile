FROM ubuntu
RUN apt-get update && apt-get install wget zlib1g-dev build-essential -y
RUN wget http://archive.apache.org/dist/httpd/httpd-2.2.14.tar.gz
RUN tar -xvf httpd-2.2.14.tar.gz
WORKDIR /httpd-2.2.14
RUN ./configure --prefix=/usr/local/apache2 --enable-mods-shared=all --enable-deflate
RUN make
RUN make install
COPY ./htdocs /usr/local/apache2/htdocs/
CMD /usr/local/apache2/bin/apachectl -D FOREGROUND