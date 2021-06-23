#----------------------------------------------------------MODULES------------------------------------------------
from just_playback import playback
from rich.console import Console
from rich.text import Text
import time
import os
from time import sleep
from rich.progress import Progress
import questionary
from tetraslam import tetra
from just_playback import Playback
#lmao
# csprint, z, asktext, askpassword, askfilepath, askconfirmation, askoneoption, askcheckbox, askautocomplete, raiseError
#---------------------------------------------------------CONSOLES---------------------------------------------------
console=Console()
whitehighlight=Console(style="black on white") #white highlight
greenhighlight=Console(style="black on bright_green") #green highlight
pinkhighlight=Console(style="white on orchid") #pink highlight
cyanhighlight=Console(style="black on bright_cyan") #cyan highlight
darkredhighlight=Console(style="white on dark_red") #dark red highlight
purplehighlight=Console(style="white on purple4") #purple highlight
yellowhighlight=Console(style="yellow1 on black") #yellow highlight
bluehighlight=Console(style="white on blue") #Blue highlight
redhighlight=Console(style="white on red") #Red highlight
orangehighlight=Console(style="black on orange_red1") #orange highlight
magentahighlight=Console(style="white on magenta") #magenta highlight


white=Console(style="white on black") #white console
green=Console(style="bright_green on black") #bright green console
pink=Console(style="orchid on black") #pink console
cyan=Console(style="bright_cyan on black") #cyan console
darkred=Console(style="dark_red on black") #dark red console
purple=Console(style="purple4 on black") #purple console
yellow=Console(style="yellow1 on black") #yellow console
blue=Console(style="blue on black") #blue console
red=Console(style="red on black") #red console
orange=Console(style="orange_red1 on black") #orange console
magenta=Console(style="magenta on black")#magenta console

#-------------------------------------------------------FUNCTIONS------------------------------------------------

def csprint(printtext, speed):
    if speed==0:
        text = Text.from_markup(printtext)
        console = Console()
        for c in text:
            console.print(c)
            sleep(0.04)
    else:
        text = Text.from_markup(printtext)
        console = Console()
        for c in text:
            console.print(c)
            sleep(speed)

def wait():
    time.sleep(2)

playback = Playback()


class music:
    """play, pause, resume, stop, setposition, volume"""
    
    def play(filename):
      playback.load_file(filename)
      playback.play()
    def pause():
      playback.pause()
    def resume():
      playback.resume()
    def stop():
      playback.stop()
    def setposition(seconds):
      playback.seek(seconds)
    def volume(volume):
      playback.set_volume(volume)



                
        



import hashlib
def Encryption(data):
    return hashlib.sha224(data).hexdigest()





def intro():
    #WORK ON THIS PART
    csprint("\n\n[yellow1]THE TRUTHBRINGERS  :grinning: ", 0)
    intromusic=r"C:\\Users\\conta\\Music\\intro.mp3"
    music.play(intromusic)
    csprint("\n\n[bright_cyan]1. Start new game", 0.02)
    csprint("\n\n[bright_cyan]2. Log in", 0.02)
    csprint("\n\n[bright_cyan]3. Options", 0.02)
    csprint("\n\n[bright_cyan]4. Credits", 0.02)
    csprint("\n\n[bright_cyan]5. Exit", 0.02)
    
user_input=0
def whee():
    csprint("[bright_cyan]\n\n>>>", 0)
    user_input=int(input())
def tutorial():
    music.stop()
    tetra.z()
    tutorialmusic=r"C:\\Users\\conta\\Music\\tutorial.mp3"
    music.play(tutorialmusic)
    csprint("\n\n[bright_cyan]Welcome to Ayro-Ni (pronounced AH-EE-ROH-NEE), newly born subject of the Flaming Hot One, his divine flameness, the God of Fire, the Everflame himself, Skald!", 0.03)
    time.sleep(0.8)
    csprint("\n\n[bright_cyan]In Ayro-Ni, it is the duty of every citizen to choose a Fealty, a Purpose and an Aspiration.", 0.03)
    time.sleep(0.8)
    csprint("\n\n[bright_cyan]Your Fealty is to be pledged to one of the Eight Gods of Ayro-Ni, and cannot be changed unless you gain spoken permission from your chosen god, and it is anyways inadvisable to do so due to the gods' spiteful temperament towards their former subjects.", 0.03)
    time.sleep(0.8)
    csprint("\n\n[bright_cyan]Your Purpose is a skill to which you will dedicate your life to, although it is by no means the only thing you are allowed to pursue. You may change your Purpose twice in your life, apart from the point when you choose your Purpose.", 0.03)
    time.sleep(0.8)
    csprint("\n\n[bright_cyan]Your Aspiration can be related to your Purpose, but it is not necessary. It is a goal which you aspire to achieve, and if you fulfill you may choose a new Aspiration, and each time you complete an Aspiration, you will have the chance to receive a new Gift from the god you have sworn your Fealty to, which brings me to the final bit of this starting knowledge you must possess.", 0.03)
    time.sleep(0.8)
    csprint("\n\n[bright_cyan]The gods are generous beings, but Ayro-Ni's 15 million inhabitants are a tiresome lot. So the gods give each new citizen of the Eight Hierocracies a chance to receive gifts each time they complete an Aspiration which they deem worthy. Some legendary Ayronites have attained several dozen Gifts from their god(s). Will you ascend to their level? It will depend on whether you win their favor or you go against their ideals. in which case you will get a well-deserved and painful death.", 0.03)
    time.sleep(2)
    csprint("[bright_cyan]\n\nShall we begin with the action, then? (Type yes or no.)", 0)
    user_input=str(input("\n\n>>>"))
    proceed=False
    while proceed==False:
        if user_input=="yes" or user_input=="Yes" or user_input=="y" or user_input=="Y" or user_input=="ye" or user_input=="Ye":
            proceed=True
            continue
        elif user_input=="no" or user_input=="No" or user_input=="n" or user_input=="N":
            csprint("\n\n[bright_cyan]Well, I suppose nobody is really ready for life. I will ignore your cheeky answer and continue.", 0)
            proceed=True
            continue
        else:
            csprint("\n\n[bright_cyan]I'm sorry, did you stutter? Say that again.", 0)
            proceed=False
    csprint("[bright_cyan]\n\nTutorial finished", 0)
            
def Chapter1():
    file=open("names.txt", "r")
    name=file.readline()
    csprint("[red3]\n\nChapter 1: Initium Ignis", 0)
    wait()
    csprint("[red3]\nYou wake up in a small wooden house, wiping the sleep from your curiously grey eyes, and look at yourself on the large mirror opposite your bed with a slightly rusted edge. You are around 12 [i]reshya[/i] tall. Then it all comes back to you...", 0)
    csprint("[red3]\nYou are a trainee in the Shrine of Skald. The small clock above the mirror tells you that the time is 0620, or 6 hours and twenty minutes into the day.", 0)
    tetra.askoneoption("What do you want to do?", ["Get up from the bed and get ready for training", "Exit game"])
    file.close()
#---------------------------------------------------------INTRO------------------------------------------

with Progress() as progress:

    task1 = progress.add_task("[bright_cyan]LOADING IRONY...", total=1000)

    while not progress.finished:
        progress.update(task1, advance=50)
        time.sleep(0.02)
intro()
csprint("[bright_cyan]\n\n>>>", 0)
user_input=int(input())
if user_input==1: #new game with tutorial and no skipping
    tutorial()
    
    username=questionary.text("Enter your new username: ").ask()
    password=questionary.password("Enter your new password: ").ask()
    usernamefile=open("names.txt", "w")
    usernamefile.write(username)
    usernamefile.close
    passwordfile=open("passwords.txt", "w")
    passwordfile.write(password)
    passwordfile.close
    savefile=open("savefile.txt", "w")
    savefile.write("0")
    savefile.close()
    csprint("[bright_cyan]Do not close the program without saving. There is no autosave.", 0)
    Chapter1()
    tetra.z(5)



elif user_input==2: #open save file automatically or manually, read save file and start game from checkpoint
    loginsuccess=False
    while loginsuccess!=True:
        username=questionary.text("\nUsername: ").ask()
        password=questionary.password("\nPassword ").ask()
        loggedin=False
        with open("names.txt", "r") as file:
            actualname = file.readline()
        with open("passwords.txt", "r") as passwords:
            actualpass = passwords.readline()
        with open("savefile.txt", "r") as save:
            actualsave = save.readline()
        if username==actualname and password==actualpass:
            csprint("[bright_cyan]Welcome back, "+username, 0)
            loginsuccess=True
            checkpoint=actualsave
            def checkpoint(number):
                save.write(number)
            Chapter1()
        elif username!=actualname or password!=actualpass:
            csprint("[bright_cyan]Username or password incorrect.", 0)

        
    
        
        
elif user_input==3: #settings and options, including music, sound fx, commands, difficulty and documentation
    csprint("Options", 0)
elif user_input==4: #list out credits for programming, concept and music
    csprint("Credits", 0)
elif user_input==5: #instant exit, however exiting during a game saves at a checkpoint.
    csprint("Exit", 0)






#-----------------------------------------------------MAIN----------------------------------------------------------


    
wait()
















