# --- 1. nginx ------
sudo ln                              `# make links between files         `\
    --symbolic                       `# symbolic link, not hard link     `\
    --force                          `# delete existing destination file `\
    /home/box/web/etc/nginx.conf     `# source file                      `\
    /etc/nginx/sites-enabled/default `# destination file (symlink)       `

sudo nginx -s reload
# ^ запускает ли это nginx?..


# --- 2. gunicorn ---
sudo gunicorn               `#          				`\
    --chdir /home/box/web/  `# to application folder	`\
    --bind 0.0.0.0:8080     `# socket to bind         	`\
    hello:app				`# module:function         	`




read -p "Press enter to continue..."





sudo service nginx stop
exit 0



# sudo service nginx restart
# bash "$(dirname "$0")/gunicorn_start.sh"

#sudo gunicorn               `#          				`\
#    --chdir /home/box/web/  `# to application folder	`\
#    --bind 0.0.0.0:8080     `# socket to bind         	`\
#    hello:app				 `# module:function         	`



#sudo mkdir -p /etc/gunicorn.d
#sudo ln -sf 						\
#	/home/box/web/etc/gunicorn.conf \
#	/etc/gunicorn.d/test
#sudo /etc/init.d/gunicorn restart