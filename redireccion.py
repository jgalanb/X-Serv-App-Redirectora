#!/usr/bin/python
# -*- coding: utf-8 -*-

# Jesús Galán Barba
# Ing. en Sistemas de Telecomunicaciones

import webapp
import random
import sys

hostname = "localhost"
port = 1234

class redireccion(webapp.webApp):

	def process(self, parsedRequest):
		num_aleat = random.randint(1,1000000)
		URL = "http://" + hostname + ":" + str(port) + "/" + str(num_aleat)
		htmlAnswer = '<html><head><meta http-equiv="Refresh" content="3; url=' + \
		 			str(num_aleat) + '"/></head' + \
 					'<body>Seras redirigido a la siguiente URL tras 3 segundos de espera: ' + \
					'<b>' + URL + '</b>' + \
					'<p><font color="red">Si no quieres esperar 3 segundos, accede a la siguiente URL: </font>' + \
					'<a href=' + URL + '>' + URL + '</a></p>' + \
					'</body></html>'
		return("307 Temporary Redirect", htmlAnswer)


if __name__ == "__main__":
	try:
		redireccion_app = redireccion(hostname, port)
	except KeyboardInterrupt:
		print "\nAplicación cerrada\n"
		sys.exit()
