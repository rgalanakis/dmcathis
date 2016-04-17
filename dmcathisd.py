#!/usr/bin/env python

import os
import subprocess
import time
import urllib2


class DmcaThis(object):
	def __init__(self):
		pass
	def run(self):
		while True:
			print 'looping'
			if self.is_vpn_running():
				self.when_vpn_up()
			else:
				self.when_vpn_down()
			time.sleep(1)
	def is_vpn_running(self):
		try:
			ip = urllib2.urlopen('http://icanhazip.com', timeout=1).read().strip()
		except urllib2.URLError:
			return False
		check_endpoint = 'http://' + ip + ':8888/speedtest/'
		try:
			urllib2.urlopen(check_endpoint, timeout=1)
		except urllib2.URLError:
			return False
		return True
	def when_vpn_up(self):
		subprocess.call(['sudo', 'python', '/usr/bin/deluged', '-d'])
		subprocess.call(['sudo', 'python', '/usr/bin/deluge-web', '-L', 'info', '-l', '/var/log/delugeweb.log'])
  	def when_vpn_down(self):
		subprocess.call(['sudo', 'killall', 'deluged'])
		subprocess.call(['sudo', '/etc/init.d/openvpn', 'start'])

print 'calling!'
if __name__ == '__main__':
	print 'running'
	DmcaThis().run()
