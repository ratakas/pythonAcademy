import urllib.request
import urllib.parse
import http.client
from bs4 import BeautifulSoup
import json

try:
	
	
	url='www2.onlinevideoconverter.com'
	data = urllib.parse.urlencode({'function': 'validate','args[dummy]':'1','args[urlEntryUser]':'https://www.youtube.com/watch?v=1_Px1mF7Dt8','args[fromConvert]':'urlconverter','args[requestExt]':'mp3','args[nbRetry]':'0','args[videoResolution]':'-1','args[audioBitrate]':'192','args[audioFrequency]':'0','args[channel]':'stereo','args[volume]':'0','args[startFrom]':'-1','args[endTo]':'-1','args[custom_resx]':'-1','args[custom_resy]':'-1','args[advSettings]':'true','args[aspectRatio]':'-1'})

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
	
	print("pasa")
	print(soup.find('a', {'id': "downloadq"}).text)
	link=str(soup.find('a', {'id': "downloadq"})['href'])

	print(link)
	
	urllib.request.urlretrieve(link, 'ggg.mp3')




except Exception as e:
    print(str(e))

def download_file(url, destination):
    """
    This will download whatever is on the internet at 'url' and save it to 'destination'.

    Parameters
    ----------
    url : str
        The URL to download from.
    destination : str
        The filesystem path (including file name) to download the file to.

    Returns
    -------
    bool
        Whether or not the operation was successful.
    """
    destination = os.path.realpath(destination)
    log.debug('Downloading data from %s to %s', url, destination)
    try:
        page = urlopen(url)
        if page.getcode() is not 200:
            log.warning('Tried to download data from %s and got http response code %s', url, str(page.getcode()))
            return False
        urlretrieve(url, destination)
        return True
    except:
        log.exception('Error downloading data from %s to %s', url, destination)
        return False