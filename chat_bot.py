from utils import wake_up,greeting,getDate,getName,getTime,end_conv,get_emoji
import wikipedia
import datetime
import emoji
import random

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
    
    if text != None:
        for i in text:
            if i in emoji.UNICODE_EMOJI:
                response = response + f"{get_emoji()}"
    else:
        response = response + f"{get_emoji()}"
    for i in text.split():
        
        if i.lower() in ["bye","leave","exit","quit",'bye','see you','goodbye','good bye','exit','leave','go','tata','see ya']:
            
            return end_conv(i)

    response = response + greeting(text)

    if 'date' in text.lower():
        get_date = getDate()
        response = response + ' ' + get_date

    if 'time' in text.lower():
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


    return response


