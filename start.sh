#!/usr/bin/env bash

exit_func() {
        echo "SIGTERM detected"            
        exit 1
}
trap exit_func SIGTERM SIGINT

service nginx start
uwsgi --ini uwsgi.ini