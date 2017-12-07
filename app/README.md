ejecutar >> docker-compose up -d
----------------
daemon
----------------
-al inicio el demonio se ejecuta cada 1 min y recoje los datos de hace 3 dias en las 10 primeras paginas y guarda un log de la ejecución

* * * * * root /usr/local/bin/python3 /usr/src/app/daemon.py -d 3 -p 10 -allp 1 >> /var/log/

modificar archivo crontab de product
---------------
parametros del daemon.py
  -d DAY, --day DAY     Hace Cuantos Dias
  -m MONTH, --month MONTH Hace Cuantos meses
  -y YEAR, --year YEAR  Hace Cuantos años
  -f DATE, --date DATE  Rango Fecha AA-MM-DD::AA-MM-DD
  -p PAG, --pag PAG     Pages
  -pi PINI, --pini PINI Pag inicio
  -allp ALLPAGES, --allpages ALLPAGES
  -t TYPE, --type TYPE  type 1,2,3

ejemplo
	daemon.py -d 10 -p 20 -allp 1 
	daemon.py -f 2017-06-20::2017-07-01 -p 20 -allp 1
	daemon.py -d 10 -pi 100 -p 20 -allp 1 
	daemon.py -d 10 -p 20 -allp 1 -t 1 

_____________
api
_____________
-abrir browser
ejemplos

	http://127.0.0.1:8000/all.json/all.json/
	http://127.0.0.1:8000/all.json/asc
	http://127.0.0.1:8000/exploit/desc
	http://127.0.0.1:8000/exploit/
	http://127.0.0.1:8000/tool/
	http://127.0.0.1:8000/advisory/
	http://127.0.0.1:8000/all.json/all.json/page1
	http://127.0.0.1:8000/exploit/page1
	http://127.0.0.1:8000/exploit/page1/asc
	http://127.0.0.1:8000/exploit/page1/desc
	agregar parametro GET para filtrar por fecha #?rangedate=2017-6-26::2017-6-28

