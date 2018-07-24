#! /bin/bash
#
# web-app-backend/start_gunicorn.sh
# Copyright (C) 2018 Toran Sahu <toran.sahu@yahoo.com>
#
# Distributed under terms of the Copyright (C) 2018 Ethereal Machines Pvt. Ltd. All rights reserved license.

APP_NAME=main
REPO_NAME=web-app-backend
ROOT_DIR=/home/ubuntu/workspace/MoD-i

REPO_DIR=$ROOT_DIR/$REPO_NAME

LOGFILE=$REPO_DIR/'gunicorn.log'
ERRORFILE=$REPO_DIR/'gunicorn-error.log'

NUM_WORKERS=3

ADDRESS=0.0.0.0:8000

                                                                                
cd $REPO_DIR/                                                                   
                                                                                
#source ~/.bashrc                                                               
#workon $APPNAME                                                                
                                                                                
# activate anaconda venv                                                        
source /home/ubuntu/miniconda3/bin/activate &&
                                                                                
# activate pipenv shell                                                         
source /home/ubuntu/.local/share/virtualenvs/web-app-backend-jwQjN8m2/bin/activate &&

# cd source dir
cd $REPO_DIR/src/
exec gunicorn $APP_NAME.wsgi:application \
        --name $APP_NAME \
        -w $NUM_WORKERS --bind=$ADDRESS \
        --log-level=debug \
        --log-file=$LOGFILE 2>>$LOGFILE  1>>$ERRORFILE \
        --pid /tmp/gunicorn.pid
