#!/usr/bin/env bash

# create roles and login
echo "-- creating postgres users"
# the admin user
if $(which psql) postgres -tAc "select 1 from pg_roles where rolname='blue_space'" | grep -q 1; then
  echo "blue_space user exists"
else
  echo "creating blue_space user"
  $(which psql) -c "create role blue_space with superuser createdb createrole login password '4d_fragment';"
fi

# create airflow_docker user
if $(which psql) postgres -tAc "select 1 from pg_roles where rolname='airflow_docker'" | grep -q 1; then
  echo "airflow_docker user exists"
  $(which psql) -c "alter default privileges in schema public grant all privileges on tables to airflow_docker;"
else
  echo "creating airflow_docker user"
  $(which psql) -c "create role airflow_docker with password 'airflow_docker';"
  $(which psql) -c "alter default privileges in schema public grant all privileges on tables to airflow_docker;"
fi

# create a generic read-only user
if $(which psql) postgres -tAc "select 1 from pg_roles where rolname='big_eye'" | grep -q 1; then
  echo "big_eye user exists"
  $(which psql) -c "alter default privileges in schema public grant all privileges on tables to big_eye;"
else
  echo "creating big_eye user"
  $(which psql) -c "create role big_eye with password 'elder';"
  $(which psql) -c "alter default privileges in schema public grant all privileges on tables to big_eye;"
fi

echo "-- finished creating postgres users"

# create databases
echo "-- creating databases"
# create the airflow_docker database for airflow backend
if $(which psql) -lqt | cut -d \| -f 1 | grep -qw airflow_docker; then
  echo "airflow_docker db already exists"
else
  echo "creating airflow_docker db"
  createdb airflow_docker
fi

# create the starplucker database, for user-defined data
if $(which psql) -lqt | cut -d \| -f 1 | grep -qw starplucker; then
  echo "starplucker db already exists"
else
  echo "creating starplucker db"
  createdb starplucker
fi

service postgresql restart
