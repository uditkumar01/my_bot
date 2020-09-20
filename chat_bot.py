from utils import wake_up,greeting,getDate,getName,getTime,end_conv,get_emoji,spell_check
import wikipedia
import datetime
import emoji
import random
from chat_ask import replying

def search_wiki(person):
    if "udit" in person.lower():
        my_ans = ["Well, he is the one who made me","My best friend", "My bestie", "A Human, just kidding.","He is Me."]
        return random.choice(my_ans)
    elif "buddy" in person.lower():
        my_ans = ["Its Me.","I am buddy, don't like teddy, but i still love candy. HA HA HA!!!","Your companion."]
        return random.choice(my_ans)
    elif "piyush" in person.lower():
        my_ans = ["Busiest guy","One of my friend.","A human. Yeah i am serious.","A cool developer","Pro bunda"]
        return random.choice(my_ans)
    elif "abhi" in person.lower():
        my_ans = ["Busiest guy","One of my friend.","A human. Yeah i am serious.","A cool developer","Pro bunda"]
        return random.choice(my_ans)
    else:

        try:
            return wikipedia.summary(f"{person}",sentences = 3)
        except:
            return "Sorry, right now server is busy."

def bot_reply(text):
    # text = input()
    response = ""
    if text == None:
        return f"{get_emoji()}"


    if text != None:
        for i in text:
            if i in emoji.UNICODE_EMOJI:
                response = response + f"{get_emoji()}"
    else:
        response = response + f"{get_emoji()}"
    if text != None:
        for i in text.split():
            
            if i.lower() in ["bye","leave","exit","quit",'bye','see you','goodbye','good bye','exit','leave','go','tata','see ya']:
                
                return end_conv(i)

    response = response + greeting(text)

    if "who are you" == text.lower() or "name yourself" == text.lower() or "tell your name" == text.lower() or "" in text.lower() == "whats you name" in text.lower() or "what's your name" == text.lower() or "what is your name" == text.lower() or "what your name" == text.lower():
        response+= random.choice(["I am buddy, don't like teddy, but i still love candy. HA HA HA!!!","Buddy Here. ","Buddy your friend. "])

    if "who is your botmaster" in text.lower() or "name of your botmaster" in text.lower() or "name your botmaster" in text.lower() or "who is your master" in text.lower() or "name of your master" in text.lower() or "name your master" in text.lower():
        return random.choice(["Udit is the one who made me ... ","U.D.I.T <- He is the one."])

    if "tell me about your botmaster" in text.lower() or "tell about botmaster" in text.lower() or "about botmaster" in text.lower() or "tell me about your master" in text.lower() or "tell about master" in text.lower() or "about master" in text.lower():
        response+= "Well, he is a programmer. To know more about him check this out https://github.com/uditkumar01"

    if 'date' in text.lower():
        get_date = getDate()
        response = response + ' ' + get_date

    if 'what is the time' in text.lower() or 'Tell me the time' in text.lower() or 'Tell me time' in text.lower() or 'what\'s the time' in text.lower() or 'whats the time' in text.lower() or 'check the time' in text.lower() or 'check the clock' in text.lower() or 'check time' in text.lower() or 'check clock' in text.lower():
        get_time = getTime()
        response = response + ' ' + get_time
    

    if 'who is' in text.lower():
        # print(text)
        words = text.split()
        person = " ".join(words[2:])
        # person = wikipedia.suggest(person)
        print("person",person)
        my_results = wikipedia.search(text)
        all_results = []
        for i in my_results:
            if person.lower() == i.lower():
                return response + ' ' + search_wiki(person)
            if "bill" in i.lower():
                all_results.append(i)
        print("check1",all_results)
        if len(all_results) > 1:
            return f"Which {person} you are talking about:    {'  ,'.join(all_results)}"
        
        # response = person
        response = response + ' ' + search_wiki(person)

    if 'what is' in text.lower():
        words = text.split()
        person = " ".join(words[2:])
        # response = person
        response = response + ' ' + search_wiki(person)

    text = spell_check(text.split())

    if response == "":
        response = replying(text)


    return response


