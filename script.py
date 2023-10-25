#Custom clear command
clearall () {
	clear && printf '\e[3J'
}
#Run a Django project
run(){
	python3 manage.py runserver 
}

#Migrate database
migrate(){
	python3 manage.py migrate
}

#Make migrations
migrations(){
	python3 manage.py makemigrations
}

#Delete database sqlite3 Django project
deletedb(){
	rm db.sqlite3
}
