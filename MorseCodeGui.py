import RPi.GPIO as GPIO
import tkinter as tk
import time

GPIO.setwarnings(False)
window = tk.Tk()
window.title("5.DC GUI")
window.geometry('600x350+700+200')
canvas = tk.Canvas(window, height=50, width=50)
light = canvas.create_oval(40,40,0,0)


LED_GREEN = 26

abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
morsecode =[
    '.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....',
    '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.',
    '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-',
    '-.--', '--..'
  ]

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_GREEN, GPIO.OUT)

#turns leds on 
def ledOn(dur):
    reset_leds()
    GPIO.output(LED_GREEN, GPIO.HIGH)
    canvas.itemconfig(light, fill='red')
    print(dur)
    time.sleep(dur)
    reset_leds()
    


def reset_leds():
    GPIO.output(LED_GREEN, GPIO.LOW)
    canvas.itemconfig(light, fill='black')
    print("Off")

    
def displayMorseCode(codeString):
    print(codeString)
    for i, code in enumerate(codeString):
        if(code == "-"):
            ledOn(0.6)
        else:
            ledOn(0.1)
        time.sleep(0.4)
    return
    
    
def convertToMorseCodeString(textInput):
    for i, c in enumerate(textInput):
        for idx, d in enumerate(abc):
            if(c.upper() == d):
                displayMorseCode(morsecode[idx])
    return
        
        

    
def getInputText():
    input=text.get("1.0","end")
    convertToMorseCodeString(input)
    
#reset leds every time it starts
reset_leds()

#GUI components
text = tk.Text(window, height=1)
btn = tk.Button(window, height=1, width=10, text="Test", command=getInputText)


text.pack()
btn.pack()
canvas.pack()

#try:
#    raise SystemExit
#    except SystemExit:
#    print "It works!"

window.mainloop()



