'''Created on 06/08/2012'''
'''Last Modified on 06/08/2012'''
'''@author: Rebecca Miyamoto'''

import botCore, botExtra, string, sys

def publicCommands(sock, line):
    caught = False
    
    if (line[3] == ":&knox"):
        botExtra.knox(sock, line)
        caught = True
    
    elif (line[3] == ":&witch"):
        botExtra.witch(sock, line)
        caught = True
        
    return caught

def privateCommands(sock, line, botConfig):
    #Check for the password
    if (len(line) >= 5):
        if (len(line) >= 6):
            if (checkPassword(line[4], botConfig)):
                if (line[3] == ":&join"):
                    botCore.joinChannels(sock, [line[5]])
                
                elif (line[3] == ":&leave"):
                    botCore.leaveChannels(sock, [line[5]])
                
                elif (line[3] == ":&quit"):
                    sock.send("QUIT :" + botConfig.get('Bot', 'quit_message') + "\r\n")
                    sys.exit()
                
                elif (line[3] == ":&say"):
                    lineToSend = ""
                    for x in range(6, len(line)):
                        lineToSend += line[x]
                    botCore.sendLine(sock, line[5], lineToSend)
                
                elif (line[3] == ":&act"):
                    lineToSend = ""
                    for x in range(6, len(line)):
                        lineToSend += line[x]
                    botCore.sendAction(sock, line[5], lineToSend)
                
            else:
                botCore.sendLine(sock, getUsername(line), "That password is INCORRECT.")
        else:
            botCore.sendLine(sock, getUsername(line), "You did not specify any parameters. The correct format for the private bot commands is /msg " + botConfig.get('Bot', 'bot_nickname') + " &command password parameter, please try AGAIN.")
    else:
        botCore.sendLine(sock, getUsername(line), "You did not specify a PASSWORD. The correct format for the private bot commands is /msg " + botConfig.get('Bot', 'bot_nickname') + " &command password parameter, please try AGAIN.")

def getUsername(line):
    username = "null"
    lineTemp = string.split(line[0], ":")
    
    if (len(lineTemp) >= 2):
        lineTemp = string.split(lineTemp[1], "!")
        username = lineTemp[0]

    return username

def checkPassword(password, botConfig):
    isCorrect = False
    
    if ((botConfig.get('Bot', 'owner_password')) == password):
        isCorrect = True
    
    return isCorrect