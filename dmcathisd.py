#!/usr/bin/env python

import os
import subprocess
import urllib2


class DmcaThis(object):
	def __init__(self):
		pass
	def run(self):
		while True:
			print 'looped'
			if self.is_vpn_running():
				self.when_vpn_up()
			else:
				self.when_vpn_down()
			sleep(1)
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
		print 'VPN UP'
		# subprocess.call(['/usr/bin/python', '/usr/bin/deluged', '-d'])
		# subprocess.call(['/usr/bin/python', '/usr/bin/deluge-web', '-L', 'info', '-l', '/var/log/delugeweb.log'])
  	def when_vpn_down(self):
  		print 'VPN DOWN'
  		# subprocess.call(['sudo', 'killall', 'deluged'])
  		# subprocess.call(['sudo', '/etc/init.d/openvpn', 'restart'])

print 'calling!'
if __name__ == '__main__':
	print 'running'
	DmcaThis().run()
