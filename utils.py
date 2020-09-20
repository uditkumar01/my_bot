# import speech_recognition as sr
import os
# from gtts import gTTS
import warnings
import calendar
import random
import wikipedia
import datetime
# from playsound import playsound
import pytz
import autocorrect


# ignoring warnings
warnings.filterwarnings('ignore')

spell = autocorrect.Speller(lang='en')

# # recording audio and return it as a string
# def record_audio():

#     # record audio
#     r = sr.Recognizer() # Recognizer object

#     # opening mic to record
#     with sr.Microphone() as source:
#         print('Say Something')
#         audio = r.listen(source)

#     data = ""
#     try:
#         data = r.recognize_google(audio)
#         print(data)
#     except sr.UnknownValueError: # check for unknown errors
#         return ('Speech not recognised')
#     except sr.RequestError:
#         return ('You got disconnected, please try again !')

#     return data

# # function to convert text to speech
# def assistant_response(text):
#     if text == "":
#         text = "Sorry"
#     t_t_s = gTTS(text=text, lang = 'en', slow = False)

#     # getting current path
#     current_path = os.path.realpath(__file__)
#     # saving audio
#     t_t_s.save(current_path[:-9].replace('\\','/') + "/audio_response/assistant_reply.mp3")

#     playsound(current_path[:-9].replace('\\','/') + "/audio_response/assistant_reply.mp3")



# check it to wake up
def wake_up(text):
    wake_words = ["hey buddy","hi buddy","hello buddy","listen buddy"]
    for word in wake_words:
        if word in text.lower():
            return True

    return False

# get date
def getDate():

    now = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]
    month = now.strftime("%B")

    date_today = now.strftime("%d")

    if date_today == '1':
        date_today += 'st'
    elif date_today == '2':
        date_today += 'nd'
    elif date_today == '3':
        date_today += 'rd'
    else:
        date_today += 'th'

    return f"Today is {weekday} ,{month} {(date_today)} {now.year}"

# get time
def getTime():

    now = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
    hr = now.hour
    minute = now.minute
    mer = "a.m."

    if hr >= 12:
        mer = 'p.m.'
        hr = int(hr) - 12
    

    return f"Its {hr} : {minute} {mer}"

# greetings
def greeting(text):

    # user inputs
    greets = ['hi','hello','hey','greetings','wassup','what\'s up','whats up','hello','hey there']

    # buddy response
    my_greets = ['hi','hello','hey','greetings','wassup','what\'s up','whats up','hello','hey there']

    for word in greets:
        if word in text.lower():
            return random.choice(my_greets) + '.'

    return ''

def end_conv(text):

    # user inputs
    greets = ['bye','see you','goodbye','good bye','exit','leave','go','tata','see ya']

    # buddy response
    my_greets = ['bye','see you later',"see you soon","your are really cool","will talk to you later","byeee",'goodbye','good bye','tata','see ya']

    for word in greets:
        if word in text.lower():
            return random.choice(my_greets) + '.'

    return ''

def getName(text):
    wordList = text.split()
    return text
    for i in range(len(wordList)):
        if i+3 <= len(wordList) - 1 and wordList[i].lower() == 'who' and wordList[i] == 'is':
            return wordList[i+2] + ' ' + wordList[i+3]
        elif i+2 <= len(wordList) - 1 and wordList[i].lower() == 'who' and wordList[i] == 'is':
            return wordList[i+2]

def spell_check(word_list):
    # checked_list = []
    for i in range(len(word_list)):
        word_list[i] = spell(word_list[i])
    return " ".join(word_list)

# search for keywords
# def wiki_search(text):


def get_emoji():

    # user inputs
    my_icons=[ "😀", "😃", "😄", "😁", "😆", "😅", "😂", "🤣", "☺️", "😊", "😇", "🙂", "🙃", "😉", "😌", "😍", "🥰", "😘", "😗", "😙", "😚", "😋", "😛", "😝", "😜", "🤪", "🤨", "🧐", "🤓", "😎", "🤩", "🥳", "😏", "😒", "😞", "😔", "😟", "😕", "🙁", "☹️", "😣", "😖", "😫", "😩", "🥺", "😢", "😭", "😤", "😠", "😡", "🤬", "🤯", "😳", "🥵", "🥶", "😱", "😨", "😰", "😥", "😓", "🤗", "🤔", "🤭", "🤫", "🤥", "😶", "😐", "😑", "😬", "🙄", "😯", "😦", "😧", "😮", "😲", "🥱", "😴", "🤤", "😪", "😵", "🤐", "🥴", "🤢", "🤮", "🤧", "😷", "🤒", "🤕", "🤑", "🤠", "😈", "👿", "👹", "👺", "🤡", "💩", "👻", "💀", "☠️", "👽", "👾", "🤖", "🎃", "😺", "😸", "😹", "😻", "😼", "😽", "🙀", "😿", "😾"  ]
    

    return random.choice(my_icons)




    