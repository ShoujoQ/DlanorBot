from __future__ import print_function

'''Created on 05/08/2012'''
'''Last Modified on 06/08/2012'''
'''Version 0.1.3'''
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
    #versionText = botConfig.get('Bot', 'version_text')
    #channelPart = botConfig.get('Bot', 'channel_part')

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
    
    lineOut = string.split(readBuffer, "\r\n")
    
    return lineOut

def consoleOutputLine(sock, outputLine):
    #Conditional line display filtering
    if (len(outputLine) >= 2):
        
        #Talking in channels and query
        if (outputLine[1] == "PRIVMSG"):
            print(("[" + datetime.now().strftime('%H:%M:%S') + "] {" + outputLine[2] + "} <" + getUsername(outputLine) + "> " + condenseLine(outputLine, 3)), end='\n')
        
        #Mode changes
        elif ((outputLine[1] == "MODE") and (len(outputLine) >= 5)):
            print(("[" + datetime.now().strftime('%H:%M:%S') + "] {" + outputLine[2] + "} " + getUsername(outputLine) + " " + "has set mode " + outputLine[3] + " on user " + outputLine[4]), end='\n')
        
        #Channel topic displays
        elif (outputLine[1] == "332"):
            print(("[" + datetime.now().strftime('%H:%M:%S') + "] Channel topic for " + outputLine[3] + " is " + condenseLine(outputLine, 4)), end='\n')
        
        #Channel join messages
        elif ((outputLine[1] == "JOIN")):
            print(("[" + datetime.now().strftime('%H:%M:%S') + "] " + getUsername(outputLine) + " has joined " + outputLine[2]), end='\n')
        
        #Channel part messages
        elif ((outputLine[1] == "PART")):
            print(("[" + datetime.now().strftime('%H:%M:%S') + "] " + getUsername(outputLine) + " has left " + outputLine[2]), end='\n')
        
        #Notices
        elif((outputLine[1] == "NOTICE")):
            print(("[" + datetime.now().strftime('%H:%M:%S') + "] NOTICE from " + getUsername(outputLine) + ": " + condenseLine(outputLine, 3)), end='\n')
        
        #Suppress nickname stuff and NAMES lists
        elif (outputLine[1] == "333", "353", "366"):
            1 + 1#Do nothing
        
        #Suppress MOTD
        elif (outputLine[1] == "372", "375", "376"):
            1 + 1#Do nothing
        
        #Suppress Welcome message
        elif (outputLine[1] == "001", "002", "003", "004", "005", "042", "251", "252", "253", "254", "255", "265", "266"):
            1 + 1#Do nothing
        
        #Suppress server usermode set
        elif ((outputLine[1] == "MODE") and (len(outputLine) >= 4)):
            if (outputLine[3] == ":+ix"):
                1 + 1#Do nothing
        
        #All others
        else:
            print(("[" + datetime.now().strftime('%H:%M:%S') + "] " + condenseLine(outputLine, 0)), end='\n')
        
    #Catch for all others that don't get past the length check earlier
    else:
        print(("[" + datetime.now().strftime('%H:%M:%S') + "] " + condenseLine(outputLine, 0)), end='\n')

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

def getUsername(line):
    username = "null"
    lineTemp = string.split(line[0], ":")
    
    if (len(lineTemp) >= 2):
        lineTemp = string.split(lineTemp[1], "!")
        username = lineTemp[0]

    return username

def condenseLine(line, start):
    condLine = ""
    for x in range(start, len(line)):
        if (x == start):
            condLine += line[x]
        else:
            condLine = condLine + " " + line[x]
    return condLine