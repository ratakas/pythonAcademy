from flask import Flask,request,jsonify
from exploits.models import exploit, ExploitSchema, db
import datetime

app = Flask(__name__)
app.config.from_object('config')
from exploits.models import db
db.init_app(app)
schema = ExploitSchema()
#------------------------------
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
@app.route('/<path:path>/')
@app.route('/<path:path>/<allorder>')
@app.route('/<path:path>/page<int:page>')
@app.route('/<path:path>/page<int:page>/<order>')
def get_dir(path,page=None,order=None,allorder=None):
	category_id=0
	alljson=False
	exploits_query=None

	rangedate = get_daterango()

	if path=='exploit':
		category_id=1
	elif path=='advisory':
		category_id=2
	elif path=='tool':
		category_id=3
	elif path=='all.json':
		alljson=True
	if page==None:
		if allorder==None or allorder=="desc":
			if alljson:
				print('pasaputo2222')
				exploits_query=record_query = exploit.query.filter(exploit.timepost.between(rangedate[0], rangedate[1] ) ).order_by(exploit.timepost.desc())
			else:
				exploits_query=record_query = exploit.query.filter(exploit.timepost.between(rangedate[0], rangedate[1] ) ).order_by(exploit.timepost.desc()).filter_by(category_id=category_id)
		elif allorder=="asc":
			if alljson:
				exploits_query=record_query = exploit.query.filter(exploit.timepost.between(rangedate[0], rangedate[1] ) ).order_by(exploit.timepost.asc())
			else:
				exploits_query=record_query = exploit.query.filter(exploit.timepost.between(rangedate[0], rangedate[1] ) ).order_by(exploit.timepost.asc()).filter_by(category_id=category_id)
	else:
		if order==None or order=="desc":
			if alljson:
				record_query = exploit.query.filter(exploit.timepost.between(rangedate[0], rangedate[1] ) ).order_by(exploit.timepost.desc()).paginate(page,10,False)
				exploits_query = record_query.items
			else:
				record_query = exploit.query.filter(exploit.timepost.between(rangedate[0], rangedate[1] ) ).order_by(exploit.timepost.desc()).filter_by(category_id=category_id).paginate(page,7,False)
				exploits_query = record_query.items
		elif order=="asc":
			if alljson:
				record_query = exploit.query.filter(exploit.timepost.between(rangedate[0], rangedate[1] ) ).order_by(exploit.timepost.asc()).paginate(page,10,False)
				exploits_query = record_query.items
			else:
				record_query = exploit.query.filter(exploit.timepost.between(rangedate[0], rangedate[1] ) ).order_by(exploit.timepost.asc()).filter_by(category_id=category_id).paginate(page,7,False)
				exploits_query = record_query.items	
	return Response_json(exploits_query)
def Response_json(query):
	results = schema.dump(query, many=True)
	return jsonify(results.data)
def get_daterango():
	rango_aux=request.args.get('rangedate', default=None)
	if rango_aux!=None:
		rango_aux2=rango_aux.split('::')
		if len(rango_aux2)==2:
			rango_ini_aux=rango_aux2[0].split('-')
			rango_fin_aux=rango_aux2[1].split('-')
			rango_ini=datetime.datetime(int(rango_ini_aux[0]), int(rango_ini_aux[1]),int(rango_ini_aux[2]))
			rango_fin=datetime.datetime(int(rango_fin_aux[0]), int(rango_fin_aux[1]),int(rango_fin_aux[2]))
			return rango_ini , rango_fin
		else:
			return datetime.datetime(1,1,1) , datetime.datetime.now()
	else:
		return datetime.datetime(1,1,1) , datetime.datetime.now()
	
if __name__ == '__main__':
    app.run(host=app.config['HOST'],
            port=app.config['PORT'],
            debug=app.config['DEBUG'],
            threaded=True)
#/all.json/
#/exploit/
#/tool/
#/advisory/
#/all.json/page1
#/exploit/page1
#/exploit/page1/asc
#/exploit/page1/desc
#/all.json/asc
#/exploit/desc
#?rangedate=2017-6-26::2017-6-28
#python daemon.py -d 7 -p 10 -allp 1