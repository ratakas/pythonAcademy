import urllib.request
import ssl
import sys
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from database.coneccion import exploit,db
import datetime

class Site():
	"""docstring for ClassName"""

	dias=None
	rango_ini=None
	rango_fin=None
	max_pages=10
	pag_ini=1
	all_pages=0
	urls=[]

	def __init__(self, arg):
		self.args=arg

	def loadArgs(self):

		if args.pag:
			self.max_pages=args.pag
	    if args.pini:
	        self.pag_ini=args.pini
	    if args.allpages:
	        self.all_pages=args.allpages


	    if args.date:
	        self.rango_aux=args.date.split('::')
	        self.rango_ini=datetime.datetime(int (rango_aux[0].split('-')[0]), int (rango_aux[0].split('-')[1]), int (rango_aux[0].split('-')[2]))
	        self.rango_fin=datetime.datetime(int (rango_aux[1].split('-')[0]), int (rango_aux[1].split('-')[1]), int (rango_aux[1].split('-')[2]))
	    if args.day:
	        self.dias=args.day
	    elif args.month:
	        self.dias=args.month*30
	    elif args.year:
	        self.dias=args.year*360
	    if self.dias!=None:
	        until_date=datetime.datetime.now()-datetime.timedelta(days=dias)


	        
	    if args.type:
	        self.typee=args.type
	        if self.typee==1:
	            self.urls=['https://packetstormsecurity.com/files/tags/exploit/page']
	        elif self.typee==2:
	            self.urls=['https://packetstormsecurity.com/files/tags/advisory/page']
	        elif self.typee==3:
	            self.urls=['https://packetstormsecurity.com/files/tags/tool/page']
	    else:
	        self.urls=['https://packetstormsecurity.com/files/tags/advisory/page',
	        'https://packetstormsecurity.com/files/tags/exploit/page',
	        'https://packetstormsecurity.com/files/tags/tool/page']
	    return True
		
	def site_parse(self):
		try:
	        ua = UserAgent()
	        
	       
	        for idx_url,url in enumerate(self.urls):
	            end_find=False
	            for key in range(self.pag_ini,self.max_pages+self.pag_ini):
	                url_temp =url+str(key)
	                print (url_temp)
	                headers = {}
	                headers['User-Agent'] = ua.random
	                req = urllib.request.Request(url_temp, headers = headers)
	                resp = urllib.request.urlopen(req)        
	                parsed_html = BeautifulSoup(resp.read(),"html.parser")
	                ngreds = parsed_html.find('div', {'id': 'm'})
	                for link in ngreds.find_all('dl'):    
	                    timepost=link.find('dd',{'class':'datetime'}).find('a')['href'].split('/')[3]
	                    timepost_temp=timepost.split('-')
	                    timepost_hour_temp=link.find('dd',{'class':'datetime'}).find('a')['title'].split(' ')
	                    timepost_hour=timepost_hour_temp[0].split(':')
	                    dt = datetime.datetime(int(timepost_temp[0]),int(timepost_temp[1]),int(timepost_temp[2]),int(timepost_hour[0]),int(timepost_hour[1]),int(timepost_hour[2]))
	                    if validartitulo(db,link['id']):
	                        me = exploit(id=link['id'],timestrap= datetime.datetime.now(),timepost= dt,category_id=(idx_url+1), title=link.find('dt').find('a').text,url='https://packetstormsecurity.com'+link.find('dt').find('a')['href'],content=link.find('dd',{'class':'detail'}).find('p').text)
	                        db.session.add(me)
	                    else:
	                        if self.all_pages==0:
	                            end_find=True #local
	                            break
	                    if self.rango_ini!=None:
	                        if dt<= self.rango_ini and dt >= (self.rango_fin+datetime.timedelta(days=1)):
	                            end_find=True #Vlocal
	                            break
	                    elif dias!=None:
	                        if dt<=until_date:
	                            end_find=True #Vlocal
	                            break
	                if end_find:
	                    break              
	                    
	        db.session.commit()
	        db.session.close()
	        print('Successful loading at: ->',datetime.datetime.now())
	    except Exception as e:
	        print(str(e))


	def validartitulo(self,db,id):
	    file = db.session.query(exploit).filter_by(id=id).first()
	    if file== None:
	        return True
	    else:
	        return False