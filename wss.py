try: input=raw_input
except: pass

try: from websocket_server import WebsocketServer
except:
	print('I need to install websocket-server. Enter y if this is OK.')
	if input()!='y': import sys; sys.exit(1)
	import subprocess
	subprocess.check_call('pip install websocket-server', shell=True)

from websocket_server import WebsocketServer

import json

def handle_message(client, server, message):
	try: j=json.loads(message)
	except Exception as e:
		print(e)
		return
	j['result']={}
	j['result']['success']=True
	try:
		if j['command']=='load':
			with open(j['path'], 'r') as file: j['result']['contents']=file.read()
		if j['command']=='save':
			import os
			try: os.makedirs(os.path.split(j['path'])[0])
			except: pass
			with open(j['path'], 'w') as file: file.write(j['contents'])
	except Exception as e:
		j['result']['success']=False
		j['result']['error']=str(e)
	server.send_message(client, json.dumps(j))

server=WebsocketServer(9160, host='localhost')
server.set_fn_message_received(handle_message)
server.run_forever()
