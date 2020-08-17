import pyttsx3
import os
from colorama import init, Fore,Style,Back
import emoji
init()
print()
print(Fore.GREEN + '\t\t\t\t\t\tWELCOME TO MY TUI')
print("\t\t\t\t\t\t-----------------")
print()
print(Fore.RED + "Hello user, Chat with us and let us know what we can launch for you.")
print(Fore.YELLOW)
print("1: Chrome ",emoji.emojize(":check_mark:"))
print("2: Notepad",emoji.emojize(":check_mark:"))
print("3: Visual Studio Code",emoji.emojize(":check_mark:"))
print("4: Spotify",emoji.emojize(":check_mark:"))
print("5: Oracle Virtualbox",emoji.emojize(":check_mark:"))
print("6: Discord",emoji.emojize(":check_mark:"))
print()

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

