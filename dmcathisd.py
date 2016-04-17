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
		ps = subprocess.check_output(['ps', 'alx'])
		if 'deluged' not in ps:
			print 'Starting deluged'
			# subprocess.call(['python', '/usr/bin/deluged', '-d'])
		if 'deluge-web' not in ps:
			print 'Starting deluge-web'
			subprocess.call(['python', '/usr/bin/deluge-web', '-L', 'info', '-l', '/var/log/delugeweb.log'])
	def when_vpn_down(self):
		print 'Uh oh, VPN is down! Killing deluge, starting OpenVPN.'
		subprocess.call(['killall', 'deluged'])
		subprocess.call(['killall', 'deluge-web'])
		subprocess.call(['sudo', '/etc/init.d/openvpn', 'start'])

if __name__ == '__main__':
	DmcaThis().run()
