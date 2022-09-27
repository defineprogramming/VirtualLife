import time
div = "==============="
print("=============== VirtualLife STARTED ===============")
time.sleep(1)
print("Enter a command, or use 'help' for a list of available commands...")
cmdinput = str(input("Enter command: "))
if cmdinput == 'help':
    print(div)
    print("COMMANDS as of v0.1.0")
    print(div)
    print("info | shows current virtuallife information")
    print("sessioninfo | current information regarding the session")
    print("onlinebanking | enter the online banking module")
    print("shop | go shopping")
    
