sudo ln                              `# make links between files         `\
	--symbolic                       `# symbolic link, not hard link     `\
	--force                          `# delete existing destination file `\
	/home/box/web/etc/nginx.conf     `# source file                      `\
	/etc/nginx/sites-enabled/default `# destination symlink              `

service nginx restart

mkdir -p /etc/gunicorn.d
sudo ln -sf /home/box/web/etc/gunicorn.conf \
            /etc/gunicorn.d/test
gunicorn                    \
    --chdir /home/box/web/  \
    --bind 0.0.0.0:8080     \
    hello:app

sudo /etc/init.d/gunicorn restart

exit 0