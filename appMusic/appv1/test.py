import urllib.request

try:

	url= 'http://ytinmp3.site/api/128.php?id=hT_nvWreIhg'
	req = urllib.request.urlretrieve(url)
	with open('test.mp3','wb') as output:
		output.write(req.read())
		output.close()
	"""

    url = 'http://www.yt-mp3-api.com/q.php?v=hT_nvWreIhg&h=2495839'

    # now, with the below headers, we defined ourselves as a simpleton who is
    # still using internet explorer.
    



    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    req = urllib.request.Request(url, headers = headers)
    resp = urllib.request.urlopen(req)
    respData = str(resp.read()).split("|")
    



    url2= 'https://www.pt2.yt-mp3-api.com/dl.php?id=%s'%respData[2]

    print(url2)
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    req = urllib.request.urlretrieve(url2)
    
    with open('test.mp3','wb') as output:
    	output.write(mp3file.read())
    	output.close()
	"""

except Exception as e:
    print(str(e))