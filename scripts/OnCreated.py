#!/usr/bin/python
"""

		@file		OnCreated.py
		@author		xy
		@since		2013-09-01

		@brief		Automatic coloring of newly created nodes.

		Location: $HIH/scripts/

		Note: this script is automatically reloaded on each node creation!

"""

import hou

import os
import sys
import datetime


def msg(m):
	msg = "[%s OnCreated.py] %s" % (datetime.datetime.now().strftime("%y%m%d %H:%M.%S"), m)
	sys.__stderr__.write(msg+"\n")
	#print msg


def dbg(m):
	msg('(debug) %s' % m)


def colorize_op(kwargs):
	'''.'''

	# node type names and default colors
	#
	cs = {
		'cam':           (0.5, 0.5, 0.5),
		'geo':           (0.6, 0.6, 0.6),
		'hlight':        (1.0, 1.0, 0.8),
		'indirectlight': (1.0, 1.0, 0.6),
		'instance':      (1.0, 0.8, 0.8),

		'shopnet':       (1.0, 1.0, 0.8),
		'material':      (0.6, 0.6, 1.0),
		'cache':         (0.0, 0.0, 0.0),
		'object_merge':  (0.8, 1.0, 0.8),
		'dopnet':        (0.8, 0.8, 1.0),
		'ropnet':        (0.2, 0.0, 0.4),
		'rop_geometry':  (0.2, 0.0, 0.4),
		'rop_alembic':   (0.2, 0.0, 0.4),

		'explodedview':  (0.0, 0.4, 1.0),

		'ifd':           (0.8, 0.8, 1.0),

		'oceansource':       (1.0, 1.0, 1.0),
		'whitewatersource':  (1.0, 1.0, 1.0),

		'lastone':       (0,0,0)
	}

	# list of nodes to be created as bypassed by default
	#
	bypass = [
		'cache',
		'lastone'
	]


	try:
		N = kwargs['node']
		n = kwargs['node'].name()
		t = kwargs['type'].name()

		dbg('node=%s type=%s' % (n, t, ))


		# set all solver nodes to white
		#
		if 'solver' in t.lower():
			N.setColor( hou.Color((1, 1, 1)) )


		# set node types to certain colors
		#
		if t in cs:
			N.setColor( hou.Color( cs[t] ) )


		# bypass some node types by default
		#
		if t in bypass:
			N.bypass(True)


	except:
		pass # ignore errors silently




colorize_op(kwargs)


