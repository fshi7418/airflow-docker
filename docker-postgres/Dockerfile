FROM postgres:16

COPY scripts/docker-entrypoint.sh /usr/local/bin/
# /docker-entrypoint-initdb.d/ is part of the base image
COPY scripts/postgresql.sh /docker-entrypoint-initdb.d/

RUN chown -R postgres: /usr/local/bin/docker-entrypoint.sh \
    && chown -R postgres: /docker-entrypoint-initdb.d/postgresql.sh

ENTRYPOINT ["docker-entrypoint.sh"]
EXPOSE 5432
CMD ["postgres"]