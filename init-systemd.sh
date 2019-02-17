#!/usr/bin/env bash


if [ "$1" == "prepare" ]; then # создаём симлинки
	sudo ln                              `# make links between files         `\
		--symbolic                       `# symbolic link, not hard link     `\
		--force                          `# delete existing destination file `\
		/home/box/web/etc/nginx.conf     `# source file                      `\
		/etc/nginx/sites-enabled/default `# destination file (symlink)       `
	
	sudo systemctl enable /home/box/web/gunicorn.service
	
elif [ "$1" == "gunicorn" ]; then
	# команды для выполнения в systemctl start gunicorn.service
    venv_gunicorn="/home/box/.virtualenv/web/bin/gunicorn"
	$venv_gunicorn              `#          				`\
		--chdir /home/box/web/  `# to application folder	`\
		--bind 0.0.0.0:8080     `# socket to bind         	`\
		hello:app				`# module:function         	`
	
else # тестируем приложение
	sudo systemctl start nginx.service
	sudo systemctl start gunicorn.service

	read -p "Press enter to stop services..."

	sudo systemctl stop nginx.service
	sudo systemctl stop gunicorn.service
fi


# sudo service nginx restart
# bash "$(dirname "$0")/gunicorn_start.sh"

#sudo gunicorn               `#          				`\
#    --chdir /home/box/web/  `# to application folder	`\
#    --bind 0.0.0.0:8080     `# socket to bind         	`\
#    hello:app				 `# module:function         	`


# sudo nginx -s reload
# ^ это не запускает nginx


#sudo mkdir -p /etc/gunicorn.d
#sudo ln -sf 						\
#	/home/box/web/etc/gunicorn.conf \
#	/etc/gunicorn.d/test
#sudo /etc/init.d/gunicorn restart


#/home/box/.virtualenv/web/bin/gunicorn \
#	--chdir /home/box/web/  \
#	--bind 0.0.0.0:8080     				\
#	hello:app
	
#exit 0