#! /bin/bash
#
# web-app-backend/start_celery.sh
# Copyright (C) 2018 Toran Sahu <toran.sahu@yahoo.com>



APP_NAME=main
REPO_NAME=web-app-backend
ROOT_DIR=/home/ubuntu/workspace/MoD-i

REPO_DIR=$ROOT_DIR/$REPO_NAME

cd $REPO_DIR/

# activate anaconda venv
source /home/ubuntu/miniconda3/bin/activate &&

# activate pipenv shell
source /home/ubuntu/.local/share/virtualenvs/web-app-backend-jwQjN8m2/bin/activate &&

# cd source dir
cd $REPO_DIR/src/
exec celery -A $APP_NAME worker -l info
