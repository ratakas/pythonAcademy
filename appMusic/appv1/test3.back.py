import urllib.request
import urllib.parse
import http.client
from bs4 import BeautifulSoup
import json
import threading, time
import wget

def verificarVideo(idVideo):
	lines = []
	with open("musica/log",'r+') as file:
		for line in file: 
			line = line.strip() #or some other preprocessing
			lines.append(line) #storing everything in memory!
		file.close()
	
	if idVideo not in lines:	
		return True
	else:
		return False

def logVideoAdd(idVideo):
	with open("musica/log", "a") as myfile:
		myfile.write(idVideo)
		myfile.write("\n")
		myfile.close()

def downloadFile(idVideo,nameVideo):
	try:	
		url='www2.onlinevideoconverter.com'
		urlVideo='https://www.youtube.com/watch?v='+str(idVideo)
		data = urllib.parse.urlencode({'function': 'validate','args[dummy]':'1','args[urlEntryUser]':urlVideo,'args[fromConvert]':'urlconverter','args[requestExt]':'mp3','args[nbRetry]':'0','args[videoResolution]':'-1','args[audioBitrate]':'192','args[audioFrequency]':'0','args[channel]':'stereo','args[volume]':'0','args[startFrom]':'-1','args[endTo]':'-1','args[custom_resx]':'-1','args[custom_resy]':'-1','args[advSettings]':'true','args[aspectRatio]':'-1'})

		h = http.client.HTTPSConnection(url)
		headers = {"Content-type": "application/x-www-form-urlencoded; charset=UTF-8","Origin":"https://www.onlinevideoconverter.com","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36","Accept-Language":"es-ES,es;q=0.9,en;q=0.8","Referer":"https://www.onlinevideoconverter.com/es/video-converter"}
		h.request('POST', '/webservice', data, headers)
		r = h.getresponse()
		jdata = json.loads(r.read())

		url='https://www.onlinevideoconverter.com/es/success?id='+str(jdata['result']["dPageId"])
		headers = {}
		headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
		headers['Upgrade-Insecure-Requests']="1"
		headers['Accept-Language']="es-ES,es;q=0.9,en;q=0.8"
		headers['Referer']="https://www.onlinevideoconverter.com/es/video-converter"
		req = urllib.request.Request(url, headers = headers)
		resp = urllib.request.urlopen(req)
		respData = resp.read()

		soup = BeautifulSoup(str(respData), "html.parser")
		
		#print("pasa")
		#print(soup.find('a', {'id': "downloadq"}).text)
		link=str(soup.find('a', {'id': "downloadq"})['href'])

		print(link)
		
		#urllib.request.urlretrieve(link, 'musica/'+str(idVideo)+'.mp3')
		wget.download(link, 'musica/'+str(nameVideo)+'.mp3')

		

	except Exception as e:
	    print(str(e))




#downloadFile('1_Px1mF7Dt8')

arrayVideos=[["test1","1_Px1mF7Dt8"],["test2","ooHII67__Sg"]  ]

x=0
while x<len(arrayVideos):

	print("total ativos: ",threading.active_count())
	if threading.active_count() < 3:

		if verificarVideo(arrayVideos[x][1]):
			hilo = threading.Thread(target=downloadFile, 
                            args=(arrayVideos[x][1],arrayVideos[x][0],))
			print("Creado en num: : ",x)
			logVideoAdd(arrayVideos[x][1])
			hilo.start()
		else:
			print("ya esta",arrayVideos[x][1])

		x+=1


	time.sleep(5)
print( len(arrayVideos) )
print("finish")
exit(0)



parser = argparse.ArgumentParser(description='This is a demo script by nixCraft.')
parser.add_argument('-i','--input', help='Input file name',required=True)
parser.add_argument('-o','--output',help='Output file name', required=True)
args = parser.parse_args()
 
## show values ##
print ("Input file: %s" % args.input )
print ("Output file: %s" % args.output )