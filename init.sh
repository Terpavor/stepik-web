cd `dirname $0`

sudo rm /etc/nginx/sites-enabled/default
sudo ln -sf etc/nginx.conf \
            /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart


mkdir -p /etc/gunicorn.d
sudo ln -sf etc/gunicorn.conf \
            /etc/gunicorn.d/test
gunicorn3                   \
    --bind 0.0.0.0:8080     \
    hello:app
# sudo /etc/init.d/gunicorn restart
#    --chdir "$0"            \
