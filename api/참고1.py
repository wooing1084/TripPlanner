import sys
import os
import hashlib
import hmac
import base64
import requests
import time

def	make_signature():
	timestamp = int(time.time() * 1000)
	timestamp = str(timestamp)

	access_key = "vq5s61guie"				# access key id (from portal or Sub Account)
	secret_key = "c97RkT0yyNKSmX4I4YGUjnaSMjCEzzh3uc2gs5ht"				# secret key (from portal or Sub Account)
	secret_key = bytes(secret_key, 'UTF-8')

	method = "GET"

	message = method + " " + "\n" + timestamp + "\n" + access_key
	message = bytes(message, 'UTF-8')
	signingKey = base64.b64encode(hmac.new(secret_key, message, digestmod=hashlib.sha256).digest())
	return signingKey
	print(signingKey)
make_signature()