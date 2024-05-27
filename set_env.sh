#!/bin/sh
set HBNB_MYSQL_USER=hbnb_dev
set HBNB_MYSQL_PWD=hbnb_dev_pwd
set HBNB_MYSQL_HOST=localhost
set HBNB_MYSQL_DB=hbnb_dev_db
set HBNB_TYPE_STORAGE=db
set HBNB_API_HOST=0.0.0.0
set HBNB_API_PORT=5000

python3 -m api.v1.app

curl -X GET http://0.0.0.0:5000/api/v1/status
