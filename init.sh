SCRIPT_PATH=$(dirname "$(realpath -s "$0")")

sudo rm /etc/nginx/sites-enabled/default
sudo ln -sf $SCRIPT_PATH/etc/nginx.conf \
            /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart


mkdir -p /etc/gunicorn.d
sudo ln -sf $SCRIPT_PATH/etc/gunicorn.conf \
            /etc/gunicorn.d/test
gunicorn3                   \
    --chdir $SCRIPT_PATH    \
    --bind 0.0.0.0:8080     \
    hello:app
# sudo /etc/init.d/gunicorn restart
