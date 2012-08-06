from __future__ import print_function

'''Created on 05/08/2012'''
'''Last Modified on 06/08/2012'''
'''Version 0.1.2'''
'''@author: Rebecca Miyamoto'''

import ConfigParser, socket, string
from datetime import datetime

botConfig = ConfigParser.RawConfigParser()
botConfig.read('config.con')

def readConfig():
    return botConfig
    
    # Assign the values from the config file to their variables
    #networkName = botConfig.get('Server', 'network_name')
    #networkAddress = botConfig.get('Server', 'network_address')
    #networkPort = botConfig.getint('Server', 'network_port')
    
    #botNickname = botConfig.get('Bot', 'bot_nickname')
    #botUsername = botConfig.get('Bot', 'bot_username')
    #botRealname = botConfig.get('Bot', 'bot_realname')
    #botNickServPassword = botConfig.get('Bot', 'bot_nickserv_password')
    #botVhostCommand = botConfig.get('Bot', 'bot_vhost_command')
    #ajoinChannels = botConfig.get('Bot', 'ajoin_channels')
    #ownerPassword = botConfig.get('Bot, 'owner_password')
    #quitMessage = botConfig.get('Bot', 'quit_message')

def connect(botConfig):
    #Create the socket and connect to it, sending ident info to the network
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((botConfig.get('Network', 'network_address'), botConfig.getint('Network', 'network_port')))
    sock.settimeout(0.1)
    sock.send("NICK %s\r\n" % botConfig.get('Bot', 'bot_nickname'))
    sock.send("USER %s %s bla :%s\r\n" % (botConfig.get('Bot', 'bot_username'), botConfig.get('Network', 'network_address'), botConfig.get('Bot', 'bot_realname')))

    return sock

def readBuffer(sock):
    #Intialise the read buffer
    readBuffer = ""
    
    #Read from it, catching errors
    while True:
        try:
            readBuffer += sock.recv(1)
        except socket.error:
            break
    
    #Echo it to the terminal if it's not an empty line
    if not (readBuffer == ""):
        print(("[" + datetime.now().strftime('%H:%M:%S') + "] " + readBuffer), end='')
    
    #Split the line
    lineOut = string.split(readBuffer, "\r\n")
    return lineOut

def formatLine(line):
    line=string.rstrip(line)
    line=string.split(line)
    
    return line

def sendAction(sock, destination, string):
    sock.send("PRIVMSG " + destination + " :ACTION " + string + "\r\n")

def sendLine(sock, destination, string):
    sock.send("PRIVMSG " + destination + " :" + string + "\r\n")

def sendNotice(sock, destination, string):
    sock.send("NOTICE " + destination + " :" + string + "\r\n")

def joinChannels(sock, channels):
    for x in range(0, len(channels)):
        sock.send("JOIN #" + channels[x] + "\r\n")

def leaveChannels(sock, channels):
    for x in range(0, len(channels)):
        sock.send("PART #" + channels[x] + " " + botConfig.get('Bot', 'channel_part') + "\r\n")