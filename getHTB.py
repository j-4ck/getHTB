import requests
import json
import base64

def getEnc(url):
	r = requests.post(url)
	data = json.loads(r.content.replace("'","\""))
	return data['data']['code']

def decrypt64(hash):
	return base64.b64decode(hash)

def main():
	print decrypt64(getEnc('https://www.hackthebox.eu/api/invite/generate'))

if __name__ == '__main__':
	main()
