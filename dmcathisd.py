#!/usr/bin/env python

import os
import urllib2


class DmcaThis(object):
	def __init__(self):
		pass
	def run(self):
		while True:
			pass
	def is_vpn_running(self):
		check_endpoint = 'http://' + self.ip() + ':8888/speedtest/'
		try:
			urllib2.urlopen(check_endpoint)
		except urllib2.URLError:
			return False
		return True
	def ip(self):
		return urllib2.urlopen('http://icanhazip.com').strip()
	def when_vpn_up(self):
		subprocess.call(['/usr/bin/python', '/usr/bin/deluged', '-d'])
		subprocess.call(['/usr/bin/python', '/usr/bin/deluge-web', '-L', 'info', '-l', '/var/log/delugeweb.log'])
  	def when_vpn_down(self):
  		subprocess.call(['sudo', 'killall', 'deluged'])
  		subprocess.call(['sudo', '/etc/init.d/openvpn', 'restart'])

if __name__ == '__main__':
	DmcaThis().run()
