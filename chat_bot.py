from utils import wake_up,greeting,getDate,getName,getTime,end_conv,get_emoji
import wikipedia
import datetime
import emoji



def bot_reply(text):
    # text = input()
    response = ""
    
    for i in text:

        if i in emoji.UNICODE_EMOJI:
            
            response = response + f"{get_emoji(i)}"
        
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
                return response + ' ' + wikipedia.summary(person,sentences = 3)
            if "bill" in i.lower():
                all_results.append(i)
        print("check1",all_results)
        if len(all_results) > 1:
            return f"Which {person} you are talking about:    {'  ,'.join(all_results)}"
        
        # response = person
        response = response + ' ' + wikipedia.summary(person,sentences = 3)

    if 'what is' in text.lower():
        words = text.split()
        person = " ".join(words[2:])
        # response = person
        response = response + ' ' + wikipedia.summary(person,sentences = 3)


    return response


