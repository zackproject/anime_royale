import random
from time import sleep
from SupabaseQuery import *
from ImageDraw import *
from TweetPost import *
from Character import Character


def checkIsTheLastGame():
    #Check if is one alive, in this case there is a winner
    if(len(listAlive) == 1):
        #Tweet the winner message and image,
        tweetWinner()
        # Notify the bot will stop direct message twitter
        directMessage()
        #Write the secret code in the file
        saveCodeOnFile()


def playRoyale():
    # List all characters alive
    listAlive = queryAllAlive()
    # Choose the killer
    asesino = random.choice(listAlive)
    # Remove killer for list
    if asesino in listAlive:
        listAlive.remove(asesino)
    # Choose the victim
    victima = random.choice(listAlive)
    # Update on Supabase the new information
    queryUpdateMurder(victima.character_id, asesino.character_id)
    # Download Killer & Victim Images
    downImgKiller(asesino.image)
    downImgVictim(victima.image)
    # Wait 2 seconds last step & Generate eliminated Image
    sleep(2)
    generateImgEliminated()
    # Get all information and Generate Panel Royale
    listAll = queryAll()
    generatePanelImage(listAll)
    # Save future tweet to text wit names killer and victim and remaining characters
    saveTweetText(asesino.name, victima.name, len(listAlive))
    # Now we can tweet the result
    tweet_multimage()
    #Check status and make stop bot if is finished
    checkIsTheLastGame()



# Global values
asesino = None
victima = None
listAlive = []
listAll = []

# Check if bot finished with the secretcode in a file
if checkIsGameAvaliable():
    playRoyale()
else:
    #Default direct mensage = finished bot
    directMessage()
