#!/usr/bin/env python
# -*- coding: utf-8 -*-            
import requests
import os
import time
import json


#####################################################################
#                           VARIABLE                                #
#####################################################################
CLOUDFLARE_EMAIL = ""                   
CLOUDFLARE_CLAVE = ""
DOMAIN = ""
SUBDOMAIN = ""
#   ⬇️ Fill it in only if you are going to use the Telegram BOT ⬇️    #
TOKEN = ""
CID = ""
#####################################################################



headers = {"X-Auth-Email":CLOUDFLARE_EMAIL, "X-Auth-Key":CLOUDFLARE_CLAVE, "Content-Type": "application/json"}
if (SUBDOMAIN == ""):
	subdomain = DOMAIN
else:
	subdomain = SUBDOMAIN+"."+DOMAIN


def get_ip():
	global my_ip

	my_ip = requests.get('http://icanhazip.com/').text
	my_ip = my_ip.strip()

def get_zones():
	global my_zone_name
	global my_zone_id

	url = "https://api.cloudflare.com/client/v4/zones/"
	zones = requests.get(url,headers=headers).text
	open('zones.json', 'w').write(zones)
	f = open('zones.json')
	json_file = json.load(f)
	json_str = json.dumps(json_file)
	zonas = json.loads(json_str)
	zones_number = zonas['result_info']['count']
	for i in range (zones_number):
		my_zone_name = zonas['result'][i]['name']
		if (my_zone_name == DOMAIN):
			my_zone_id = zonas['result'][i]['id']
			break
		else:
			i = i+1


def get_dns():
	global my_dns_name
	global my_dns_id
	global my_dns_ip
	global my_dns_proxied

	url = "https://api.cloudflare.com/client/v4/zones/"+my_zone_id+"/dns_records?per_page=100"
	dns = requests.get(url,headers=headers).text
	open('dns.json', 'w').write(dns)
	f = open('dns.json')
	json_file = json.load(f)
	json_str = json.dumps(json_file)
	dns = json.loads(json_str)
	dns_number = dns['result_info']['count']
	for i in range (dns_number):
		my_dns_name = dns['result'][i]['name']
		if (my_dns_name == subdomain):
			my_dns_id = dns['result'][i]['id']
			my_dns_ip = dns['result'][i]['content']
			my_dns_proxied = dns['result'][i]['proxied']
			break
		else:
			i = i+1


def change_dns():
	global STATUS
	if (my_dns_ip == my_ip):
		print ("THE IP ADDRESS HAS NOT CHANGED")
	else:
		parametros ={"type":"A","name":subdomain,"content":my_ip,"ttl":120,"proxied":my_dns_proxied}
		url = "https://api.cloudflare.com/client/v4/zones/"+my_zone_id+"/dns_records/"+my_dns_id
		r = requests.patch(url, json=parametros, headers = headers)
		print ("THE IP ADDRESS HAS CHANGED")
		STATUS = r.text


while True:
	try:
		print ("-------------------------------------------")
		print ("WEB ["+subdomain+"]")
		get_ip()
		print ("CURRENT IP ["+my_ip+"]")
		get_zones()
		get_dns()
		print ("CLOUDLFARE IP ["+my_dns_ip+"]")
		change_dns()
		print ("WAITING 5 MINUTES BEFORE THE NEXT EXECUTION")
		print ("-------------------------------------------\n\n")
		time.sleep(300)
	except:
		if (TOKEN == ""):
			pass
		else:
			requests.post('https://api.telegram.org/bot'+TOKEN+'/sendMessage',data={'chat_id': CID, 'text': "Ha habido un problema al actualizar los DNS del dominio"+subdomain+"\n STATUS: "+STATUS})
			time.sleep(300)
