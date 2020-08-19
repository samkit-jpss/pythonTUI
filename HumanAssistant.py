import pyttsx3
import os
from colorama import init, Fore,Style,Back
import emoji
init()
print()

print(Fore.GREEN + '\t\t\t\t\t\t\tWELCOME TO MY TUI')
print("\t\t\t\t\t\t\t******************")
print()
print(Fore.RED + "Hello user, Chat with us and let us know what we can launch for you.")
print()
print(Fore.CYAN+"RUN PROGRAM")
print(Fore.YELLOW)
print("1: Chrome ",emoji.emojize(":check_mark:"))
print("2: Notepad",emoji.emojize(":check_mark:"))
print("3: Visual Studio Code",emoji.emojize(":check_mark:"))
print("4: Spotify",emoji.emojize(":check_mark:"))
print("5: Oracle Virtualbox",emoji.emojize(":check_mark:"))
print("6: Discord",emoji.emojize(":check_mark:"))
print("6: Paint",emoji.emojize(":check_mark:"))
print("7: Control Panel ",emoji.emojize(":check_mark:"))
print()
print(Fore.CYAN+"BASIC COMMANDS")
print(Fore.YELLOW)
print("7: To create a New Folder ",emoji.emojize(":check_mark:"))
print("8: Today's Date ",emoji.emojize(":check_mark:"))
print()
print(Fore.CYAN+"WATCH A MOVIE")
print()
print(Fore.YELLOW+"9: Star Wars ",emoji.emojize(":check_mark:"))



print()
pyttsx3.speak("Hello , Welcom , How can I help you?")

while True:
  print(Fore.RED + "What can we do for you: " , end = " ")
  print(Fore.GREEN)
  chat = input()
  if (("run" in chat) or ("launch" in chat)) and (("chrome" in chat) or ("google chrome" in chat)):
    print(Fore.CYAN + "\t\t\t\t\t\tCool! Running Google Chrome .. ")
    pyttsx3.speak("Launching Google krome for you.")
    print()
    os.system("chrome")
  elif (("run" in chat) or ("launch" in chat)) and (("notepad" in chat) or ("editor" in chat)):
    print(Fore.CYAN + "\t\t\t\t\t\tCool! Running Notepad .. ")
    pyttsx3.speak("Launching Notepad for you.")
    print()
    os.system("notepad")
  elif (("watch" in chat) or ("launch" in chat)) and (("movie" in chat) or ("star wars" in chat)):
    print(Fore.CYAN + "\t\t\t\t\t\tCool! Sit back and Relax ! .. ")
    pyttsx3.speak("Star wars launching in 3! 2! 1")
    print()
    os.system("Telnet Towel.blinkenlights.nl")    
  elif (("run" in chat) or ("launch" in chat)) and (("paint" in chat) or ("drawing" in chat)):
    print(Fore.CYAN + "\t\t\t\t\t\tCool! Running Paint .. ")
    pyttsx3.speak("Launching ms paint for you.")
    print()
    os.system("mspaint")
  elif (("todays" in chat) or ("tell me" in chat)) and (("date" in chat) or ("dates" in chat)):
    print(Fore.CYAN + "\t\t\t\t\t\t Today's date is displayed below  .. ")
    pyttsx3.speak("Today's date is .")
    print()
    os.system("date")
  elif (("make" in chat) or ("create" in chat)) and (("folder" in chat) or ("new folder" in chat)):
    print(Fore.CYAN + "\t\t\t\t\t\tCool! Creating a folder .. ")
    pyttsx3.speak("Created newfolder for you on the desktop")
    print()
    os.system(r"mkdir C:\Users\91811\Desktop\newfolder")
  elif (("run" in chat) or ("launch" in chat)) and (("control panel" in chat) or ("panel" in chat)):
    print(Fore.CYAN + "\t\t\t\t\t\tCool! Running Notepad .. ")
    pyttsx3.speak("Launching control panel for you.")
    print()
    os.system("control panel")
  elif (("run" in chat) or ("launch" in chat)) and ("discord" in chat):
    print(Fore.CYAN + "\t\t\t\t\t\tCool! Running Discord .. ")
    pyttsx3.speak("Launching Discord for you.")
    print()
    os.system("discord")
  elif (("run" in chat) or ("launch" in chat)) and (("vs code" in chat) or ("code" in chat) or ("visual studio code" in chat)):
    print(Fore.CYAN +  "\t\t\t\t\t\tCool! Running VS Code .. ")
    pyttsx3.speak("Launching Visual Studio code for you.")
    print()
    os.system("code")
  elif (("run" in chat) or ("play" in chat) or ("launch" in chat)) and (("spotify" in chat) or ("music" in chat)):
    print(Fore.CYAN + "\t\t\t\t\t\tCool! Running spotify .. ")
    pyttsx3.speak("Launching spotify for you.")
    print()
    os.system("spotify")
  elif("stop" in chat) or ("quit" in chat) or ("close" in chat) or ("bye" in chat):
    print(Fore.CYAN +  "\t\t\t\t\t\tHope to see you again !")
    pyttsx3.speak("Thank you for engaging with us . We would love to help you again.")
    print()
    break  
  elif (("run" in chat) or ("launch" in chat)) and (("vm" in chat) or ("virtaul box" in chat)):
    print(Fore.CYAN + "\t\t\t\t\t\tCool! Running Virtual Machine .. ")
    pyttsx3.speak("Launching virtual machine for you.")
    print()
    os.system("virtualbox")
  else:
    print(Fore.MAGENTA + "\t\t\t\t\t\tSorry! We did'nt get you , try writing again .. ")
    pyttsx3.speak("Sorry! I am afraid we dont have that program.")
    print()	

