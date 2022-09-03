#!/usr/bin/env python
# coding: utf-8

# In[18]:


from tkinter import *
 
from tkinter import ttk
 
window = Tk()
window.geometry("800x500")
window.title("Welcome to Cold Chain")
temp = []
j = 0 
tab_control = ttk.Notebook(window)
 
tab1 = ttk.Frame(tab_control)
 
tab2 = ttk.Frame(tab_control)

tab3 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Options')
 
tab_control.add(tab2, text='Result')

tab_control.add(tab3, text='Graph')

lbl4 = Label(tab1,text='Food Storage Temperature range:',font='times 12 ')
lbl4.grid(row=3, column=0,sticky=W+E+N+S, padx=8, pady=5)

CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
C1 = Checkbutton(tab1, text = "Chilled", variable = CheckVar1,                  onvalue = 1, offvalue = 0, height=1,                  width = 10)
C2 = Checkbutton(tab1, text = "Superchilled", variable = CheckVar2,                  onvalue = 1, offvalue = 0, height=1,                  width = 10)
C3 = Checkbutton(tab1, text = "Frozen", variable = CheckVar3,                  onvalue = 1, offvalue = 0, height=1,                  width = 10)
C1.grid(row=4, column=0,sticky=W+E+N+S, padx=8, pady=5)
C2.grid(row=5, column=0,sticky=W+E+N+S, padx=8, pady=5)
C3.grid(row=6, column=0,sticky=W+E+N+S, padx=8, pady=5)

lbl5 = Label(tab1,text='Type of Food:',font='times 12 ')
lbl5.grid(row=3, column=1,sticky=W+E+N+S, padx=50, pady=5)

CheckVar4 = IntVar()
CheckVar5 = IntVar()
CheckVar6 = IntVar()
CheckVar7 = IntVar()
CheckVar8 = IntVar()
CheckVar9 = IntVar()
CheckVar10 = IntVar()

C4 = Checkbutton(tab1, text = "Meat", variable = CheckVar4,                  onvalue = 1, offvalue = 0, height=1,                  width = 10)
C5 = Checkbutton(tab1, text = "Fish", variable = CheckVar5,                  onvalue = 1, offvalue = 0, height=1,                  width = 10)
C6 = Checkbutton(tab1, text = "Fruits", variable = CheckVar6,                  onvalue = 1, offvalue = 0, height=1,                  width = 10)
C7 = Checkbutton(tab1, text = "Vegitables", variable = CheckVar7,                  onvalue = 1, offvalue = 0, height=1,                  width = 10)
C8 = Checkbutton(tab1, text = "Milk", variable = CheckVar8,                  onvalue = 1, offvalue = 0, height=1,                  width = 10)
C9 = Checkbutton(tab1, text = "Mixed", variable = CheckVar9,                  onvalue = 1, offvalue = 0, height=1,                  width = 10)
C10 = Checkbutton(tab1, text = "Other", variable = CheckVar10,                  onvalue = 1, offvalue = 0, height=1,                  width = 10)
C4.grid(row=4, column=1,sticky=W+E+N+S, padx=8, pady=5)
C5.grid(row=5, column=1,sticky=W+E+N+S, padx=8, pady=5)
C6.grid(row=6, column=1,sticky=W+E+N+S, padx=8, pady=5)
C7.grid(row=7, column=1,sticky=W+E+N+S, padx=8, pady=5)
C8.grid(row=8, column=1,sticky=W+E+N+S, padx=8, pady=5)
C9.grid(row=9, column=1,sticky=W+E+N+S, padx=8, pady=5)
C10.grid(row=10, column=1,sticky=W+E+N+S, padx=8, pady=5)

#Tab2

from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import time
dataset = pd.read_csv("/home/pi/Dataset/temp1.csv")
x = dataset.iloc[:,[0,1,2,3,4,5,6,7,8,9]].values
y = dataset.iloc[:,[10]].values
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.33,random_state=0)
SV = SVC(kernel='linear')
svstart = time.time()
SV.fit(x_train,y_train)
svend = time.time()
y_sv = SV.predict(x_test)
acc = accuracy_score(y_test,y_sv)*100
timeq = svend-svstart

def svmalgo():
    #pred = SV.predict([[one.get(),two.get(),three.get(),four.get(),five.get(),six.get(),seven.get(),eight.get(),nine.get(),ten.get()]])
    pred = SV.predict([temp])
    accvalue.set(int(acc))
    predvalue.set(pred)
    timevalue.set(timeq)
    one.set(temp[0])
    two.set(temp[1])
    three.set(temp[2])
    four.set(temp[3]) 
    five.set(temp[4]) 
    six.set(temp[5])
    seven.set(temp[6])
    eight.set(temp[7])
    nine.set(temp[8])
    ten.set(temp[9])
    temp.clear()

import Adafruit_DHT as dht
import numpy as np
import matplotlib.pyplot as plt
import http.client, urllib, time

#def show():
l1 = Label(tab2,text='Temperature after each 15 min:')
l1.grid(row=0, column=1)

for i in range(1,11):
    j = Label(tab2,text=i)
    j.grid(row=i)

one= StringVar()
two= StringVar()
three= StringVar()
four= StringVar()
five= StringVar()
six= StringVar()
seven=StringVar()
eight= StringVar()
nine= StringVar()
ten=StringVar()

j = Entry(tab2,textvariable=one).grid(row=1,column = 1)
j = Entry(tab2,textvariable=two).grid(row = 2,column = 1)
j = Entry(tab2,textvariable=three).grid(row = 3,column =1)
j = Entry(tab2,textvariable=four).grid(row = 4,column =1)
j = Entry(tab2,textvariable=five).grid(row = 5,column =1)
j = Entry(tab2,textvariable=six).grid(row = 6,column =1)
j = Entry(tab2,textvariable=seven).grid(row = 7,column =1)
j = Entry(tab2,textvariable=eight).grid(row = 8,column =1)
j = Entry(tab2,textvariable=nine).grid(row = 9,column =1)
j = Entry(tab2,textvariable=ten).grid(row = 10,column =1)

accvalue = StringVar()
timevalue = StringVar()
predvalue = StringVar()
prediction = Label(tab2,text='Prediction:')
prediction.grid(row=1,column=10)

predentry = Entry(tab2,textvariable=predvalue).grid(row=1,column=11)

accuracy = Label(tab2,text='Accuracy:')
accuracy.grid(row=2,column=10)

accentry = Entry(tab2,textvariable=accvalue).grid(row=2,column=11)

time = Label(tab2,text='Time:')
time.grid(row=3,column=10)

timeentry = Entry(tab2,textvariable=timevalue).grid(row=3,column=11)

submit = Button(tab2,text = 'Calculate', command = svmalgo).grid(row = 12,column=5)

#TAB3

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from tkinter import *
import matplotlib.pyplot as plt
class mclass:
    def __init__(self,  tab3):
        self.button = Button (tab3, text="Show Graph", command=self.plot)
        self.button.pack(side=TOP,padx=50,pady=100)

    def plot (self):
        plt.axis([0, 100, 0, 35])
        plt.title('Temperature Changes Graph')
        plt.ylabel('Temperature 0c')
        plt.xlabel('Time')
        key = 'TWZ1OMFWCMDS2YTP'
        i = 0
        j = 0
        while True:
            h,t =dht .read_retry(11,4)
            print("Temp:",t)
            params = urllib.parse.urlencode({'field1': t, 'key':key})
            headers = {"Content-typZZe": "application/x-www-form-urlencoded", "Accept":"text/plain"}
            conn = http.client.HTTPConnection("api.thingspeak.com:80")
            try:
                    conn.request("POST", "/update", params,headers)
                    response=conn.getresponse()
                    print(response.status, response.reason)
                    data = response.read()
                    conn.close()
            except:
                    print ("connection failed")
            i = i+1
            j = j+1
            plt.plot(i, t, color='red',marker='.')
            plt.pause(1)
            if j<=10:
                temp.append(t)
            else:
                j=0
                svmalgo()
        plt.show()
        plt.gcf().canvas.draw()
        fig = plt.figure()
        canvas = FigureCanvasTkAgg(fig, master=tab3)
        canvas.get_tk_widget().grid(row=1,column=24)
        canvas.draw()

start= mclass(tab3)


tab_control.pack(expand=1, fill='both')
window.mainloop()

#EndOfTheCode :)



