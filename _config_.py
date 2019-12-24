#coding: utf-8

'''
Fichier pour l'adressage des différents équipement

'''
_MQTT_ip='127.0.0.1'				#Adresse IP du broker mqtt
_MQTT_port=1883						#Port du broker mqtt
_MQTT_authentication=False          # Mqtt use authentication? 
_MQTT_user=''			            # Mqtt User name
_MQTT_pass=''			            # Mqtt password
_MQTT_TOPIC_SUB='SUBmcz'			#Topic général de souscription
_MQTT_TOPIC_PUB='PUBmcz'			#Topic général de publication
_MZC_INTERFACE='wlan0';             # Wlan interface for auto detecting MZC Lan. 
_MCZip='auto'				        #Adresse IP du poêle. Use 'auto' for auto-detecting
_MCZport='81'						#Port du serveur embarqué du poele
_VERSION='1.1'						#Version
_AUTHOR='Anthony L.'				#Auteur
