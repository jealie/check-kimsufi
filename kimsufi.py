import requests
import os
import configparser
import time
import random

config = configparser.ConfigParser()
config.read(['kimsufi.conf'])
serv_list = config.get('DEFAULT','serv').split(',')
zone_list = config.get('DEFAULT','zon').split(',')
command = config.get('DEFAULT','command')

while True:
  # Parse the json:
  url='https://ws.ovh.com/dedicated/r2/ws.dispatcher/getAvailability2'
  headers = {'content-type': 'application/json'}
  r = requests.get(url, headers=headers)
  rep = r.json()
  # See if the server is available
  for r in rep['answer']['availability']:
    serv_parsed = r['reference']
    if serv_parsed not in serv_list:
      continue

    for zone in r['zones']:
      zone_parsed = zone['zone']
      if zone_parsed not in zone_list:
        continue
      avail_parsed = zone['availability']
      if avail_parsed != 'unavailable':
        print("Server : %s @ %s, Delay before delivery: %s\n" % (serv_parsed, zone_parsed, avail_parsed))
        command = command.replace('%server%', serv_parsed)
        os.system(command)
  time.sleep(random.randint(20,40)) # check every 30-ish seconds
