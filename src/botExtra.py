'''Created on 06/08/2012'''
'''Last Modified on 06/08/2012'''
'''@author: Rebecca Miyamoto'''

import botCore, botStandard, botFileIO, math, random

def knox(sock, line):
    botCore.sendLine(sock, line[2], randomKnox())

def randomKnox():
    knoxChoice = random.randint(1, 9)

    if (knoxChoice == 1):
        return "4Knox's 1st. It is forbidden for the culprit to be anyone not mentioned in the early part of the STORY."
    elif (knoxChoice == 2):
        return "4Knox's 2nd. It is forbidden for supernatural agencies to be employed as a detective TECHNIQUE."
    elif (knoxChoice == 3):
        return "4Knox's 3rd. It is forbidden for hidden passages to EXIST."
    elif (knoxChoice == 4):
        return "4Knox's 4th. It is forbidden for unknown drugs or hard to understand scientific devices to be USED."
    elif (knoxChoice == 5):
        return "4Knox's 6th. It is forbidden for accident or intuition to be employed as a detective TECHNIQUE."
    elif (knoxChoice == 6):
        return "4Knox's 7th. It is forbidden for the detective to be the CULPRIT."
    elif (knoxChoice == 7):
        return "4Knox's 8th. It is forbidden for the case to be resolved with clues that are not PRESENTED."
    elif (knoxChoice == 8):
        return "4Knox's 9th. It is permitted for observers to let their own conclusions and interpretations be HEARD."
    elif (knoxChoice == 9):
        return "4Knox's 10th. It is forbidden for a character to disguise themselves as another without any CLUES."
    else:
        return "An unexpected error has OCCURRED. Please report this to my MASTER."

def witch(sock, line):
    username = botStandard.getUsername(line)
    if (username == "Shoujo_Q"):
        botCore.sendLine(sock, line[2], "Shoujo_Q is the Territory Lord and therefore gets all the WITCHES!")
    
    else:
        if not (botFileIO.readTime("witch", username) == "null"):
            if (botFileIO.isThreeHour(botFileIO.readTime("witch", username), botFileIO.getCurrentDateTime()) == 0):
                botCore.sendLine(sock, username, "Be patient, collector of WITCHES. Three hours have not yet ELAPSED. There are yet " + str(botFileIO.timeLeft(botFileIO.readTime("witch", username), botFileIO.getCurrentDateTime())) + " seconds REMAINING.")
            
            else:
                witchEditing(sock, line, username, 0)
        else:
            witchEditing(sock, line, username, 1)

def witchEditing(sock, line, username, firstFlag):
    numWitches = random.randint(-3, 9)
    if(numWitches == 0):
        botCore.sendLine(sock, line[2], username + " is a loser and doesn't deserve any WITCHES.")
    else:
        if (firstFlag == 1):
            if(numWitches <= -1):
                botCore.sendLine(sock, line[2], username + " is absolutely terrible and has not managed to attract any witches at all to their SENATE!")
                botFileIO.editLine("witch", username, 0)
            elif(numWitches == 1):
                botCore.sendLine(sock, line[2], username + " is just sort of average and got " + str(numWitches) + " WITCH! " + username + " has " + str(numWitches) + " witches in their SENATE.")
                botFileIO.editLine("witch", username, numWitches)
            elif(numWitches <= 3):
                botCore.sendLine(sock, line[2], username + " is just sort of average and got " + str(numWitches) + " WITCHES! " + username + " has " + str(numWitches) + " witches in their SENATE.")
                botFileIO.editLine("witch", username, numWitches)
            elif(numWitches <= 6):
                botCore.sendLine(sock, line[2], username + " is fairly decent and got " + str(numWitches) + " WITCHES! " + username + " has " + str(numWitches) + " witches in their SENATE.")
                botFileIO.editLine("witch", username, numWitches)
            elif(numWitches <= 9):
                botCore.sendLine(sock, line[2], username + " is quite awesome and got " + str(numWitches) + " WITCHES! " + username + " has " + str(numWitches) + " witches in their SENATE.")
                botFileIO.editLine("witch", username, numWitches)
        else:
            if(numWitches <= -2):
                if (((numWitches) + (int((botFileIO.readLine("witch", username))[1]))) < 0):
                    botCore.sendLine(sock, line[2], username + " is absolutely terrible and managed to drive away " + str(int(math.fabs(numWitches))) + " witches from their Senate, leaving them with no witches REMAINING.")
                else:
                    botCore.sendLine(sock, line[2], username + " is absolutely terrible and managed to drive away " + str(int(math.fabs(numWitches))) + " witches from their SENATE. " + username + " has " + str((numWitches) + (int((botFileIO.readLine("witch", username))[1]))) + " witches in their SENATE.")
                botFileIO.editLine("witch", username, numWitches)
            
            if(numWitches == -1):
                if (((numWitches) + (int((botFileIO.readLine("witch", username))[1]))) < 0):
                    botCore.sendLine(sock, line[2], username + " is absolutely terrible and managed to drive away " + str(int(math.fabs(numWitches))) + " witch from their Senate, leaving them with no witches REMAINING.")
                else:
                    botCore.sendLine(sock, line[2], username + " is absolutely terrible and managed to drive away " + str(int(math.fabs(numWitches))) + " witch from their SENATE. " + username + " has " + str((numWitches) + (int((botFileIO.readLine("witch", username))[1]))) + " witches in their SENATE.")
                botFileIO.editLine("witch", username, numWitches)
                
            elif(numWitches <= 3):
                botCore.sendLine(sock, line[2], username + " is just sort of average and got " + str(numWitches) + " WITCHES! " + username + " has " + str((numWitches) + (int((botFileIO.readLine("witch", username))[1]))) + " witches in their SENATE.")
                botFileIO.editLine("witch", username, numWitches)
            elif(numWitches <= 6):
                botCore.sendLine(sock, line[2], username + " is fairly decent and got " + str(numWitches) + " WITCHES! " + username + " has " + str((numWitches) + (int((botFileIO.readLine("witch", username))[1]))) + " witches in their SENATE.")
                botFileIO.editLine("witch", username, numWitches)
            elif(numWitches <= 9):
                botCore.sendLine(sock, line[2], username + " is quite awesome and got " + str(numWitches) + " WITCHES! " + username + " has " + str((numWitches) + (int((botFileIO.readLine("witch", username))[1]))) + " witches in their SENATE.")
                botFileIO.editLine("witch", username, numWitches)