
#json= javascript object notation used to send data used to play with data n make string to list or something
#fc5b69bf6b704344b926ebeaf63b8e25
# importing requests package 


#music
'''import os  

music_dir='D:\pratham baabu\wassup'
songs = os.listdir(music_dir)
print(songs)    
os.startfile(os.path.join(music_dir, songs[0]))'''
#cricket score
'''import requests
from bs4 import BeautifulSoup
from time import sleep
import sys

print('Live Cricket Matches:')
print('=====================')
url = "http://static.cricinfo.com/rss/livescores.xml"
r = requests.get(url)
soup = BeautifulSoup(r.text,'lxml')

i = 1
for item in soup.findAll('item'):
 print(str(i) + '. ' + item.find('description').text)
 i = i + 1

links = []    
for link in soup.findAll('item'):
 links.append(link.find('guid').text)

print('Enter match number or enter 0 to exit:')
while True:
    try:
        userInput = int(input())
        if userInput < 0 or userInput > 30:
            print('Invalid input. Try Again!')
            continue
        elif userInput == 0:
            sys.exit() 
        else:
            break
    except:
        pass
url =links[userInput-1]
r = requests.get(url)
soup = BeautifulSoup(r.text,'lxml')  

while True:
 matchUrl = links[userInput - 1]
 r = requests.get(matchUrl)
 soup = BeautifulSoup(r.text,'lxml') 
 score = soup.findAll('title')       
 try:
  r.raise_for_status()
 except Exception as exc:
  print ('Connection Failure. Try again!')
  continue
 print(score[0].text + '\n')
 sleep(20)'''
#background
'''import speech_recognition as sr
import pywhatkit
import os
import random
import pafy


 
  
    if "play" in command:
        query=command.replace("play","")
        url=(pywhatkit.playonyt(query))
        video = pafy.new(url)
        time.sleep(video.length)
    if "exit" in command:
        exit()
r = sr.Recognizer()
r.listen_in_background(sr.Microphone(device_index=mic), callback)
import time
while True: 
    time.sleep(0.1)'''
'''import math as m
fact=1
res=0
n= int(input("enter the value of n(odd value): "))
x= float(input("enter the value of X:" ))
flag= True
for i in range(1,n+1):
    fact*=i
    if i%2==0:
        flag= False
        continue
    else:
        if flag==True:
            res+=(m.pow(x,i))/fact
        elif flag== False:
            res-=(m.pow(x,i))/fact
        else:
            pass
print(res)'''

'''binary=input("enter ")
num=len(binary)-1
result=0


for i in binary:
    result= result + int(i)*(2**num)
    num=num-1
print("the decimal equivalent is",result)'''
'''a=type(float(0))
print(a)'''

'''import requests
from tkinter import *
import tkinter as tk
from tkinter import ttk
class CurrencyConverter():
    def __init__(self,url):
        self.data= requests.get(url).json()
        self.currencies = self.data['rates']
def convert(self, from_currency, to_currency, amount): 
    initial_amount = amount 
   
    if from_currency != 'USD' : 
        amount = amount / self.currencies[from_currency] 
  
    # limiting the precision to 4 decimal places 
    amount = round(amount * self.currencies[to_currency], 4) 
    return amount
url = 'https://api.exchangerate-api.com/v4/latest/USD'
converter = CurrencyConverter(url)
print(converter.convert('INR','USD',100))

 

def __init__(self, converter):
    tk.Tk.__init__(self)
    self.title = 'Currency Converter'
    self.currency_converter = converter
    
self.geometry("500x200")

 

#Label
self.intro_label = Label(self, text = 'Welcome to Real Time Currency Convertor',  fg = 'blue', relief = tk.RAISED, borderwidth = 3)
self.intro_label.config(font = ('Courier',15,'bold'))

 

self.date_label = Label(self, text = f"1 Indian Rupee equals = {self.currency_converter.convert('INR','USD',1)} USD \n 
                        /Date : {self.currency_converter.data['date']}", relief = tk.GROOVE, borderwidth = 5)

 

self.intro_label.place(x = 10 , y = 5)
self.date_label.place(x = 170, y= 50)

 

# Entry box
valid = (self.register(self.restrictNumberOnly), '%d', '%P')
# restricNumberOnly function will restrict thes user to enter invavalid number in Amount field. We will define it later in code
self.amount_field = Entry(self,bd = 3, relief = tk.RIDGE, justify = tk.CENTER,validate='key', validatecommand=valid)
self.converted_amount_field_label = Label(self, text = '', fg = 'black', bg = 'white', relief = tk.RIDGE, justify = tk.CENTER, width = 17, borderwidth = 3)
 
# dropdown
self.from_currency_variable = StringVar(self)
self.from_currency_variable.set("INR") # default value
self.to_currency_variable = StringVar(self)
self.to_currency_variable.set("USD") # default value
 
font = ("Courier", 12, "bold")
self.option_add('*TCombobox*Listbox.font', font)
self.from_currency_dropdown = ttk.Combobox(self, textvariable=self.from_currency_variable,values=list(self.currency_converter.currencies.keys()), font = font, state = 'readonly', width = 12, justify = tk.CENTER)
self.to_currency_dropdown = ttk.Combobox(self, textvariable=self.to_currency_variable,values=list(self.currency_converter.currencies.keys()), font = font, state = 'readonly', width = 12, justify = tk.CENTER)
 
# placing
self.from_currency_dropdown.place(x = 30, y= 120)
self.amount_field.place(x = 36, y = 150)
self.to_currency_dropdown.place(x = 340, y= 120)

 

self.converted_amount_field_label.place(x = 346, y = 150)

 

# Convert button
self.convert_button = Button(self, text = "Convert", fg = "black", command = self.perform) 
self.convert_button.config(font=('Courier', 10, 'bold'))
self.convert_button.place(x = 225, y = 135)

 

def perform(self,):
        amount = float(self.amount_field.get())
        from_curr = self.from_currency_variable.get()
        to_curr = self.to_currency_variable.get()
 
        converted_amount= self.currency_converter.convert(from_curr,to_curr,amount)
        converted_amount = round(converted_amount, 2)
     
        self.converted_amount_field_label.config(text = str(converted_amount))
        
def restrictNumberOnly(self, action, string):
        regex = re.compile(r"[0-9,]*?(\.)?[0-9,]*$")
        result = regex.match(string)
        return (string == "" or (string.count('.') <= 1 and result is not None))
    
if __name__ == '__main__':
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    converter = RealTimeCurrencyConverter(u"""
 
    App(converter)
    mainloop'''
hlo=input("emter sjnaww\
qwwr")
import os 
print("\n")
print("ssupu")
print("yo")