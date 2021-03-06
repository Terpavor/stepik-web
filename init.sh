

if [ "$1" == "prepare" ]; then # создаём симлинки
	# --- 0. virtualenv -
	virtualenv -p python3 ~/.virtualenv/web
	source ~/.virtualenv/web/bin/activate

	pip install --upgrade pip
	pip install django
	pip install gunicorn

	python3 /home/box/web/ask/manage.py makemigrations
	python3 /home/box/web/ask/manage.py migrate

	# --- 1. nginx ------
	sudo ln                              `# make links between files         `\
		--symbolic                       `# symbolic link, not hard link     `\
		--force                          `# delete existing destination file `\
		/home/box/web/etc/nginx.conf     `# source file                      `\
		/etc/nginx/sites-enabled/default `# destination file (symlink)       `
else
	sudo service nginx restart


	# --- 3. mysql ------
	#sudo /etc/init.d/mysql start

	# --- 2. gunicorn ---

	venv_gunicorn="/home/box/.virtualenv/web/bin/gunicorn"
	proj_dir="/home/box/web/ask/"
	$venv_gunicorn              `#          				`\
		--chdir $proj_dir		`# to application folder	`\
		--bind 0.0.0.0:8000     `# socket to bind         	`\
		ask.wsgi:application	`# module:function         	`
fi


	

# --- 2. gunicorn для первого задания с ним  ---
#sudo gunicorn               `#          				`\
#    --chdir /home/box/web/  `# to application folder	`\
#    --bind 0.0.0.0:8080     `# socket to bind         	`\
#    hello:app				`# module:function         	`




# read -p "Press enter to continue..."





sudo service nginx stop
exit 0



# sudo service nginx restart
# bash "$(dirname "$0")/gunicorn_start.sh"

#sudo gunicorn               `#          				`\
#    --chdir /home/box/web/  `# to application folder	`\
#    --bind 0.0.0.0:8080     `# socket to bind         	`\
#    hello:app				 `# module:function         	`


# sudo nginx -s reload
# sudo nginx --signal reload
# ^ это не запускает nginx


#sudo mkdir -p /etc/gunicorn.d
#sudo ln -sf 						\
#	/home/box/web/etc/gunicorn.conf \
#	/etc/gunicorn.d/test
#sudo /etc/init.d/gunicorn restart