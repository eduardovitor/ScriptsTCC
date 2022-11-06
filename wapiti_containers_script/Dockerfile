FROM debian:bullseye-slim as build

ENV DEBIAN_FRONTEND=noninteractive \
  LANG=en_US.UTF-8

WORKDIR /usr/src/app

RUN apt update \
  && apt install python3 python3-pip python3-setuptools ca-certificates -y \
  && apt clean -yq \
  && apt autoremove -yq \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
  && truncate -s 0 /var/log/*log

COPY . .

RUN python3 setup.py install

FROM debian:bullseye-slim

WORKDIR /home

ENV DEBIAN_FRONTEND=noninteractive \
  LANG=en_US.UTF-8 \
  PYTHONDONTWRITEBYTECODE=1 \
  EXP_ROUND=1 \
  REPORT_DIR=/home/wapiti_reports \
  SEVERITY_DICT_PATH=owasp_severity_dict_pyformat.txt \
  CITY_DICT_PATH=url_cidade_dict.txt

 # URLS_PATH=lista_urls_atualizada.txt \

RUN apt update \
  && apt install python3 python3-setuptools -y \
  && apt clean -yq \
  && apt autoremove -yq \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
  && truncate -s 0 /var/log/*log \
  && mkdir $REPORT_DIR

COPY --from=build /usr/local/lib/python3.9/dist-packages/ /usr/local/lib/python3.9/dist-packages/
COPY --from=build /usr/local/bin/wapiti /usr/local/bin/wapiti-getcookie /usr/local/bin/
COPY ./experiment_setup /home

ENTRYPOINT ["/usr/bin/python3"]
CMD ["wapiti_exec_docker.py"]
