#!/usr/bin/python3
#
# sodack.py
# Script en python que utiliza la libreria de shodan para la busqueda de dispositivos.
# uso: python sodack.py
# Autor: Blackster


import os
import shodan
import random
from colorama import Fore, init
init()

banner = """
  ____            _            _    
 / ___|  ___   __| | __ _  ___| | __
 \___ \ / _ \ / _` |/ _` |/ __| |/ /
  ___) | (_) | (_| | (_| | (__|   < 
 |____/ \___/ \__,_|\__,_|\___|_|\_\\
"""
SHODAN_API_KEY = str(input("\n\n[*]Inserta tu api-key de shodan aqui:>> "))
api = shodan.Shodan(SHODAN_API_KEY)

def inicio():
	os.system('clear')
	print(Fore.RED)
	print(banner)
	print(Fore.CYAN)
	print("\t\tBy Blackster")
	print(Fore.YELLOW)
	print("\nAdvertencia: Este script ha sido creado con fines educativos, por lo tanto \nno me hago responsable del mal uso que se le de a esta herramienta.")
	menu = """
********************++[ Menu ]++*******************

1->> Busqueda en shodan.(Extensa, Libre).
2->> Obteniendo info de un Host.
3->> Buscar Dispositivos Android (ADB).
4->> Buscar Camaras.

99->> Salir.
	"""
	print(Fore.GREEN)
	print(menu)


if __name__=="__main__":
	while True:
		inicio()
		ask = int(input("[*]Escoge una opcion:>> "))
		if ask==1:
			keyword = str(input("[*]Introduce una palabra clave para la Busqueda:>> "))
			try:
				results = api.search(keyword)
				print("Results found: {}".format(results['total']))
				for result in results['matches']:
					print('IP: {}'.format(result['ip_str']))
					print(result['data'])
					print('')
					input()
			except shodan.APIError:
				print("Error la API no ha sido encontrada")
				input()

		elif ask==2:
			ask_for = input("Introduzca el Host/IP del objetivo: ")
			host = api.host(ask_for)
			print("""
				IP: {}
        Organizacion: {}
        Systema Operativo: {}
        """.format(host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a')))
			for item in host['data']:
				print("""
					puerto: {}
          Banner: {}

          """.format(item['port'], item['data']))
				print("Presiona una tecla para continuar")
				input()
				os.system('clear')

		elif ask==3:
			ale = random.randint(0, 1)
			if ale==0:
				print(Fore.CYAN)
				keyword = "Android Debug Bridge"
				try:
					results = api.search(keyword)
					print("Results found: {}".format(results['total']))
					for result in results['matches']:
						print('IP: {}'.format(result['ip_str']))
						print(result['data'])
						print('')
						print("\nPresiona enter para seguir mostrando resultados!!")
						input()
				except shodan.APIError:
					print("Error")
					input()
			else:
				if ale==1:
					print(Fore.CYAN)
					keyword = "Android Debug Bridge port:5555"
					try:
						results = api.search(keyword)
						print("Results found: {}".format(results['total']))
						for result in results['matches']:
							print('IP: {}'.format(result['ip_str']))
							print(result['data'])
							print('')
							print("\nPresiona enter para seguir mostrando resultados!!")
							input()
					except shodan.APIError:
						print("Error")
						input()

		elif ask==4:
			aleat = random.randint(0, 6)
			if aleat==0:
				print(Fore.CYAN)
				keyword = "ipcamera, 200"
				try:
					results = api.search(keyword)
					print("Results found: {}".format(results['total']))
					for result in results['matches']:
						print('IP: {}'.format(result['ip_str']))
						print(result['data'])
						print('')
						print("\nPresiona enter para seguir mostrando resultados!!")
						input()
				except shodan.APIError:
					print("Error")
					input()
			elif aleat==1:
				print(Fore.CYAN)
				keyword = "Server: Camera Web Server"
				try:
					results = api.search(keyword)
					print("Results found: {}".format(results['total']))
					for result in results['matches']:
						print('IP: {}'.format(result['ip_str']))
						print(result['data'])
						print('')
						print("\nPresiona enter para seguir mostrando resultados!!")
						input()
				except shodan.APIError:
					print("Error")
					input()
			elif aleat==2:
				print(Fore.CYAN)
				keyword = "Server: Camera Web Server"
				try:
					results = api.search(keyword)
					print("Results found: {}".format(results['total']))
					for result in results['matches']:
						print('IP: {}'.format(result['ip_str']))
						print(result['data'])
						print('')
						print("\nPresiona enter para seguir mostrando resultados!!")
						input()
				except shodan.APIError:
					print("Error")
					input()
			elif aleat==3:
				print(Fore.CYAN)
				keyword = "netcam"
				try:
					results = api.search(keyword)
					print("Results found: {}".format(results['total']))
					for result in results['matches']:
						print('IP: {}'.format(result['ip_str']))
						print(result['data'])
						print('')
						print("\nPresiona enter para seguir mostrando resultados!!")
						input()
				except shodan.APIError:
					print("Error")
					input()
			elif aleat==4:
				print(Fore.CYAN)
				keyword = "ipcam"
				try:
					results = api.search(keyword)
					print("Results found: {}".format(results['total']))
					for result in results['matches']:
						print('IP: {}'.format(result['ip_str']))
						print(result['data'])
						print('')
						print("\nPresiona enter para seguir mostrando resultados!!")
						input()
				except shodan.APIError:
					print("Error")
					input()
			elif aleat==5:
				print(Fore.CYAN)
				keyword = "yawcam"
				try:
					results = api.search(keyword)
					print("Results found: {}".format(results['total']))
					for result in results['matches']:
						print('IP: {}'.format(result['ip_str']))
						print(result['data'])
						print('')
						print("\nPresiona enter para seguir mostrando resultados!!")
						input()
				except shodan.APIError:
					print("Error")
					input()
			elif aleat==6:
				print(Fore.CYAN)
				keyword = "d-Link Internet Camera"
				try:
					results = api.search(keyword)
					print("Results found: {}".format(results['total']))
					for result in results['matches']:
						print('IP: {}'.format(result['ip_str']))
						print(result['data'])
						print('')
						print("\nPresiona enter para seguir mostrando resultados!!")
						input()
				except shodan.APIError:
					print("Error")
					input()

		else:
			if ask==99:
				print("See you...")
				break
