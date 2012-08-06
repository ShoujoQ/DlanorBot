'''Created on 06/08/2012'''
'''Last Modified on 06/08/2012'''
'''@author: Rebecca Miyamoto'''

import botCore, botStandard, string, time

#Read the config file
botConfig = botCore.readConfig()

#Create the sock and connect
sock = botCore.connect(botConfig)

while True:
    
    #Create, receive to and read from the buffer
    readBuffer = botCore.readBuffer(sock)
    
    for line in readBuffer:
        
        #Do some formatting
        line = botCore.formatLine(line)
        
        if (len(line) >= 1):
            #Handler for NickServ identification and ajoining channels
            for x in range(0, len(line)):
                if (line[x] == "/MOTD"):
                    botCore.sendLine(sock, "NickServ", "IDENTIFY " + botConfig.get('Bot', 'bot_nickserv_password'))
                    time.sleep(1)
                    botCore.joinChannels(sock, string.split(botConfig.get('Bot', 'ajoin_channels'), " "))
                
            #Ping response
            if (line[0] == "PING"):
                sock.send("PONG %s\r\n" % line[1])
            
            if (len(line) >= 4):
                #Version response
                if (line[3] == ":VERSION"):
                    botCore.sendNotice(sock, botStandard.getUsername(line), ("VERSION " + botConfig.get('Bot', 'version_text') + ""))
                
                #Command processing (public and private), looking for & command delimiter
                if (len(list(line[3])) >= 2):
                    if ((list(line[3]))[1] == "&"):
                        #Public command processing
                        caughtPublic = botStandard.publicCommands(sock, line)
                        
                        #Private command processing (only if it wasn't a public command, to save time)
                        if (caughtPublic == False):
                            botStandard.privateCommands(sock, line, botConfig)