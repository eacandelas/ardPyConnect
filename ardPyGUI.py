from tkinter import *
from tkinter import ttk

top = Tk()
top.wm_title("ArdPy Console")
frame = ttk.Frame(top, width= 200, relief=SUNKEN)
frame.grid(column=0, row=0)


############### list to hold GUI elements ##########################
oldButtonsStates = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
lstButtons = []
lstLabels = []
lstScales = []
lstPWM = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]

############### variable creation for PWM states ##################
var3 = IntVar()
var5 = IntVar()
var6 = IntVar()
var10 = IntVar()
var11 = IntVar()

############## variable creations active / deactive labels setup #####################
strLblPin0 = StringVar()
strLblPin0.set("Deactive")
lstLabels.append(strLblPin0)

strLblPin1 = StringVar()
strLblPin1.set("Deactive")
lstLabels.append(strLblPin1)

strLblPin2 = StringVar()
strLblPin2.set("Deactive")
lstLabels.append(strLblPin2)

strLblPin3 = StringVar()
strLblPin3.set("Deactive")
lstLabels.append(strLblPin3)

strLblPin4 = StringVar()
strLblPin4.set("Deactive")
lstLabels.append(strLblPin4)

strLblPin5 = StringVar()
strLblPin5.set("Deactive")
lstLabels.append(strLblPin5)

strLblPin6 = StringVar()
strLblPin6.set("Deactive")
lstLabels.append(strLblPin6)

strLblPin7 = StringVar()
strLblPin7.set("Deactive")
lstLabels.append(strLblPin7)

strLblPin8 = StringVar()
strLblPin8.set("Deactive")
lstLabels.append(strLblPin8)

strLblPin9 = StringVar()
strLblPin9.set("Deactive")
lstLabels.append(strLblPin9)

strLblPin10 = StringVar()
strLblPin10.set("Deactive")
lstLabels.append(strLblPin10)

strLblPin11 = StringVar()
strLblPin11.set("Deactive")
lstLabels.append(strLblPin11)

strLblPin12 = StringVar()
strLblPin12.set("Deactive")
lstLabels.append(strLblPin12)

strLblPin13 = StringVar()
strLblPin13.set("Deactive")
lstLabels.append(strLblPin13)


################# Labels for pin state ############################5978213

labelPin0 = Label(frame, text= "State Pin 2: ")
labelPin0.grid(column = 0, row=0 ,padx = 10 )
labelPin1 = Label(frame, text= "State Pin 2: ")
labelPin1.grid(column = 0, row=1 ,padx = 10 )
labelPin2 = Label(frame, text= "State Pin 2: ")
labelPin2.grid(column = 0, row=2 ,padx = 10 )
labelPin3 = Label(frame, text= "State Pin 3: ")
labelPin3.grid(column = 0, row=3 ,padx = 10)
labelPin4 = Label(frame, text= "State Pin 4: ")
labelPin4.grid(column = 0, row=4 ,padx = 10)
labelPin5 = Label(frame, text= "State Pin 5: ")
labelPin5.grid(column = 0, row=5 ,padx = 10)
labelPin6 = Label(frame, text= "State Pin 6: ")
labelPin6.grid(column = 0, row=6 ,padx = 10)
labelPin7 = Label(frame, text= "State Pin 7: ")
labelPin7.grid(column = 0, row=7 ,padx = 10)
labelPin8 = Label(frame, text= "State Pin 8: ")
labelPin8.grid(column = 0, row=8 ,padx = 10)
labelPin9 = Label(frame, text= "State Pin 9: ")
labelPin9.grid(column = 0, row=9 ,padx = 10)
labelPin10 = Label(frame, text= "State Pin 10: ")
labelPin10.grid(column = 0, row=10 ,padx = 10)
labelPin11 = Label(frame, text= "State Pin 11: ")
labelPin11.grid(column = 0, row=11 ,padx = 10)
labelPin12 = Label(frame, text= "State Pin 12: ")
labelPin12.grid(column = 0, row=12 ,padx = 10)
labelPin13 = Label(frame, text= "State Pin 13: ")
labelPin13.grid(column = 0, row=13 ,padx = 10)

################# Pin state label #########################3
labelPin0 = Label(frame, textvariable = strLblPin0)
labelPin0.grid(column = 1, row=0 ,padx = 10 )
labelPin1 = Label(frame, textvariable = strLblPin1)
labelPin1.grid(column = 1, row=1 ,padx = 10 )
labelPin2 = Label(frame, textvariable = strLblPin2)
labelPin2.grid(column = 1, row=2 ,padx = 10 )
labelPin3 = Label(frame, textvariable = strLblPin3)
labelPin3.grid(column = 1, row=3 ,padx = 10)
labelPin4 = Label(frame, textvariable = strLblPin4)
labelPin4.grid(column = 1, row=4 ,padx = 10)
labelPin5 = Label(frame, textvariable = strLblPin5)
labelPin5.grid(column = 1, row=5 ,padx = 10)
labelPin6 = Label(frame, textvariable = strLblPin6)
labelPin6.grid(column = 1, row=6 ,padx = 10)
labelPin7 = Label(frame, textvariable = strLblPin7)
labelPin7.grid(column = 1, row=7 ,padx = 10)
labelPin8 = Label(frame, textvariable = strLblPin8)
labelPin8.grid(column = 1, row=8 ,padx = 10)
labelPin9 = Label(frame, textvariable = strLblPin9)
labelPin9.grid(column = 1, row=9 ,padx = 10)
labelPin10 = Label(frame, textvariable = strLblPin10)
labelPin10.grid(column = 1, row=10 ,padx = 10)
labelPin11 = Label(frame, textvariable = strLblPin11)
labelPin11.grid(column = 1, row=11 ,padx = 10)
labelPin12 = Label(frame, textvariable = strLblPin12)
labelPin12.grid(column = 1, row=12 ,padx = 10)
labelPin13 = Label(frame, textvariable = strLblPin13)
labelPin13.grid(column = 1, row=13 ,padx = 10)


################# Buttons for pin activation #######################

pin0    = Button(frame, text ="Pin  0", command = lambda:dw(0))
pin0.grid(column=2, row=0, sticky = W, padx=10, pady=5)
lstButtons.append(pin0)

pin1    = Button(frame, text ="Pin  1", command = lambda:dw(1))
pin1.grid(column=2, row=1, sticky = W, padx=10, pady=5)
lstButtons.append(pin1)

pin2    = Button(frame, text ="Pin  2", command = lambda:dw(2))
pin2.grid(column=2, row=2, sticky = W, padx=10, pady=5)
lstButtons.append(pin2)

pin3    = Button(frame, text ="Pin  3", command = lambda:dw(3))
pin3.grid(column=2, row=3, sticky = W, padx=10, pady=5)
lstButtons.append(pin3)

pin4    = Button(frame, text ="Pin  4", command = lambda:dw(4))
pin4.grid(column=2, row=4, sticky = W, padx=10, pady=5)
lstButtons.append(pin4)

pin5    = Button(frame, text ="Pin  5", command = lambda:dw(5))
pin5.grid(column=2, row=5, sticky = W, padx=10, pady=5)
lstButtons.append(pin5)

pin6    = Button(frame, text ="Pin  6", command = lambda:dw(6))
pin6.grid(column=2, row=6, sticky = W, padx=10, pady=5)
lstButtons.append(pin6)

pin7    = Button(frame, text ="Pin  7", command = lambda: dw(7))
pin7.grid(column=2, row=7, sticky = W, padx=10, pady=5)
lstButtons.append(pin7)

pin8    = Button(frame, text ="Pin  8", command = lambda: dw(8))
pin8.grid(column=2, row=8, sticky = W, padx=10, pady=5)
lstButtons.append(pin8)

pin9    = Button(frame, text ="Pin  9", command = lambda: dw(9))
pin9.grid(column=2, row=9, sticky = W, padx=10, pady=5)
lstButtons.append(pin9)

pin10   = Button(frame, text ="Pin 10", command = lambda: dw(10))
pin10.grid(column=2, row=10, sticky = W, padx=10, pady=5)
lstButtons.append(pin10)

pin11   = Button(frame, text ="Pin 11", command = lambda: dw(11))
pin11.grid(column=2, row=11, sticky = W, padx=10, pady=5)
lstButtons.append(pin11)

pin12   = Button(frame, text ="Pin 12", command = lambda: dw(12))
pin12.grid(column=2, row=12, sticky = W, padx=10, pady=5)
lstButtons.append(pin12)

pin13   = Button(frame, text ="Pin 13", command = lambda: dw(13))
pin13.grid(column=2, row=13, sticky = W, padx=10, pady=5)
lstButtons.append(pin13)

########################Checkboxes for PWM selection ############################333

pwm3 = Checkbutton(frame, text="PWM", variable=var3, command = lambda: act(3, var3, scalePwm3))
pwm3.grid(column = 3, row =3, padx=10, pady=5)

pwm5 = Checkbutton(frame, text="PWM", variable=var5, command = lambda: act(5, var5, scalePwm5))
pwm5.grid(column = 3, row =5, padx=10, pady=5)

pwm6 = Checkbutton(frame, text="PWM", variable=var6, command = lambda: act(6, var6, scalePwm6))
pwm6.grid(column = 3, row =6, padx=10, pady=5)

pwm10 = Checkbutton(frame, text="PWM", variable=var10, command = lambda: act(10, var10, scalePwm10))
pwm10.grid(column = 3, row =10, padx=10, pady=5)

pwm11 = Checkbutton(frame, text="PWM", variable=var11, command = lambda: act(11, var11, scalePwm11))
pwm11.grid(column = 3, row =11, padx=10, pady=5)


#######################Scale pwm #########################################3

scalePwm0 = Scale(frame, from_=0 , to = 255)
lstScales.append(scalePwm0)

scalePwm1 = Scale(frame, from_=0 , to = 255)
lstScales.append(scalePwm1)

scalePwm2 = Scale(frame, from_=0 , to = 255)
lstScales.append(scalePwm2)

scalePwm3 = Scale(frame, from_=0 , to = 255, orient= HORIZONTAL )
scalePwm3.grid(column= 4, row= 3, padx=10, pady=5)
lstScales.append(scalePwm3)

scalePwm4 = Scale(frame, from_=0 , to = 255)
lstScales.append(scalePwm4)

scalePwm5 = Scale(frame, from_=0 , to = 255, orient= HORIZONTAL )
scalePwm5.grid(column= 4, row= 5, padx=10, pady=5)
lstScales.append(scalePwm5)

scalePwm6 = Scale(frame, from_=0 , to = 255, orient= HORIZONTAL )
scalePwm6.grid(column= 4, row= 6, padx=10, pady=5)
lstScales.append(scalePwm6)

scalePwm7 = Scale(frame, from_=0 , to = 255)
lstScales.append(scalePwm7)

scalePwm8 = Scale(frame, from_=0 , to = 255)
lstScales.append(scalePwm8)

scalePwm9 = Scale(frame, from_=0 , to = 255)
lstScales.append(scalePwm9)

scalePwm10 = Scale(frame, from_=0 , to = 255, orient= HORIZONTAL )
scalePwm10.grid(column= 4, row= 10, padx=10, pady=5)
lstScales.append(scalePwm10)

scalePwm11 = Scale(frame, from_=0 , to = 255, orient= HORIZONTAL )
scalePwm11.grid(column= 4, row= 11, padx=10, pady=5)
lstScales.append(scalePwm11)

scalePwm12 = Scale(frame, from_=0 , to = 255)
lstScales.append(scalePwm12)

scalePwm13 = Scale(frame, from_=0 , to = 255)
lstScales.append(scalePwm13)

################## callbacks for console widgets events ###################
def dw(pinNum):
    if not(lstPWM[pinNum]):
        if oldButtonsStates[pinNum] :
            lstButtons[pinNum]["relief"] = "raised"
            oldButtonsStates[pinNum] = 0
            lstLabels[pinNum].set("Deactive")
            print ("Pin " + str(pinNum) + " Deactive")
        else :
            lstButtons[pinNum]["relief"] = "sunken"
            oldButtonsStates[pinNum] = 1
            lstLabels[pinNum].set("Active")
            print ("Pin " + str(pinNum) + " Active")
    else:
        if oldButtonsStates[pinNum] :
            lstButtons[pinNum]["relief"] = "raised"
            oldButtonsStates[pinNum] = 0
            lstLabels[pinNum].set("Deactive")
            print ("Pin " + str(pinNum) + " Deactive")
        else :
            lstButtons[pinNum]["relief"] = "sunken"
            oldButtonsStates[pinNum] = 1
            lstLabels[pinNum].set("PWM")
            print ("Pin " + str(pinNum) + " PWM")
            print ("Scale value: " + str(lstScales[pinNum].get()))


def act(pinNum, variable, scale):
    lstPWM[pinNum] = variable.get()
    if lstPWM[pinNum]:
        print (" ------------------- ")
        print ("Pin " + str(pinNum) + " selected for PWM")
        print ("Variable: " + str(variable) + " - estado:" + str(lstPWM[pinNum]))
        print ("Scale value: " + str(scale.get()))
    else:
        print (" ------------------- ")
        print ("Pin " + str(pinNum) + " removed for PWM")
        print ("Variable: " + str(variable) + " - estado:" + str(lstPWM[pinNum]))


################## init the console window and event tracking ##############


top.mainloop()