# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 16:39:03 2019

@author: Pravesh Singh
"""

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp
import speech_recognition as s
import threading
import nltk

# pyttsx3 for responces speaking purpose
engine = pp.init()
voices = engine.getProperty('voices')
print(voices)

engine.setProperty('voice',voices[1].id)

def speak(word):
    engine.say(word)
    engine.runAndWait()

 

# creating the object of chatbot class
chatbot = ChatBot("Nitesh")

# loading dataset and use of nlp

file = open('global.txt','r',errors = 'ignore')

raw = file.read()
raw = raw.lower()
sent_tokens = nltk.sent_tokenize(raw)



conversation = [
        "hi",
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome.",
    "what is your name?",
    "my name is Anjali raghuvanshi",
    "who are you?",
    "i am a chatbot and created by pravesh singh and his group mates",
    "i don't know what to say",
    "can you help me?",
    "yes i can help you by talking with you.",
    "in which city do you live?",
    "i live in  bareilly",
    "tell me about your self",
    "i am good how about you"
    
]

conversation = sent_tokens

trainer = ListTrainer(chatbot)

#now training the bot with the help of trainer

trainer.train(conversation)

#response = chatbot.get_response("Good morning!")
#print(response)
'''print("chatbot is ready to chat...")
while True:
    query = input("user:")
    if query == 'exit()':
        break
    response = chatbot.get_response(query)
    print("bot:", response)'''
    
main = Tk()

main.geometry("500x700")
main.title("My Chatbot")

#Insert an image
'''img = PhotoImage(file="bot.png")
photoL = Label(main , image = img)

photoL.pack(pady = 5)'''
canvas = Canvas(width = 300, height = 190)   #, bg = 'blue')
canvas.pack()

photo = PhotoImage(file='bot.png')

canvas.create_image(40,0, image = photo , anchor=NW)

# take query: it take input from user and convert in into string

def takeQuery():
    sr = s.Recognizer()
    sr.pause_threshold=1
    print("your bot is listening try to speak")
    with s.Microphone() as m:
        audio = sr.listen(m)
        query = sr.recognize_google(audio , language = 'eng-in')
        print(query)
        textF.delete(0, END)
        textF.insert(0,query)
        ask_from_bot()
        



def ask_from_bot():
    query = textF.get()
    answer_from_bot = chatbot.get_response(query)
    msgs.insert(END,"you : "+ query)
    msgs.insert(END, "bot : "+ str(answer_from_bot))
    speak(answer_from_bot)
    textF.delete(0, END)
    msgs.yview(END)

frame = Frame(main)

sc = Scrollbar(frame)
msgs = Listbox(frame , width = 80 , height = 20, yscrollcommand = sc.set)

sc.pack(side=RIGHT , fill =Y)

msgs.pack(side = LEFT , fill = BOTH , pady= 10)

frame.pack()

# creating text field

textF = Entry(main , font =("verdana", 20))
textF.pack(fill=X , pady=10)

# creating button
btn = Button(main, text = "Ask from bot" , font=("verdana",20), command= ask_from_bot)
btn.pack()

# creating a event function
def enter_function(event):
    btn.invoke()
    
# going to bind main window with enter key...
main.bind('<Return>',enter_function) 
   
def repeatL():
    while True:
        takeQuery()

t = threading.Thread(target =repeatL)
t.start()

main.mainloop()    
    
    
    
    
    
    
    
    
    
    
    