#!/usr/bin/env python

import sys, string, urllib2, json

# populate queue
alphabet = string.lowercase
queue = []

for letter1 in alphabet:
	for letter2 in alphabet:
		for letter3 in alphabet:
			queue.append(letter1 + letter2 + letter3 + '.ca')

# modify queue if needed
if len(sys.argv) > 1:
	del queue[:int(sys.argv[1])]

# query whois
num = 1

for domain in queue:
	response = urllib2.urlopen('http://whomsy.com/api/' + domain)
	json_msg = json.loads(response.read())['message']

	status = json_msg.split('\n')[1].replace(' ', '').split(':')[1]

	if status == 'registered':
		expiry = json_msg.split('\n')[3].replace(' ', '').split(':')[1]
		print '[' + str(num) + ']: ' + domain + ' is registered (expires: ' + expiry + ')'
	elif status == 'available':
		print '[' + str(num) + ']: ' + domain + ' is available'
		available_domains = open('/home/s-gough_adam/available-domains.txt', 'a')
		available_domains.write(domain + "\n")
		available_domains.close()
	else:
		print '[' + str(num) + ']: ' + domain + ' is not available'

	num += 1

