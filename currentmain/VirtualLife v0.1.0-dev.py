import time
import os
def clear_console(): return os.system('clear')
newSession = False
div = "==============="
print("=============== VirtualLife STARTED ===============")
while True:
    time.sleep(1)
    print("Enter a command, or use 'help' for a list of available commands...")
    cmdinput = str(input("Enter command: "))
    if cmdinput == 'help':
        print(div)
        print("COMMANDS as of v0.1.0")
        print(div)
        print("setup | start a new session (mandatory to use most commands)")
        print("info | shows current virtuallife information")
        print("sessioninfo | current information regarding the session")
        print("onlinebanking | enter the online banking module")
        print("shop | go shopping")
        print("inventory | view your inventory")
        print(div)
    if cmdinput == "setup":
        print(div)
        print("Setup (Step 1/3)")
        print(div)
        charfname = str(input("Enter your character's first name: "))
        charlname = str(input("Enter your character's last name: "))
        print(div)
        print("Hi ", charfname, "!", sep="")
        print(div)
        balsetting = int(input("How much money would you like to begin with? (Step 2/3): "))
        if balsetting >= 100000:
            print(div)
            print("Sorry, that's too high! Try a number under 100,000.")
            balsetting = int(input("How much money would you like to begin with? "))
        while balsetting >= 100000:
            print(div)
            print("Sorry, that's too high! Try a number under 100,000.")
            balsetting = int(input("How much money would you like to begin with? "))
        else:
            print("Balance recorded! Proceeding to next step...")
            balance = balsetting
        print("Making finishing touches... (Step 3/3)")
        newSession = True
        print("Returning to menu...")
        clear()
        
        
        
        
            
        
