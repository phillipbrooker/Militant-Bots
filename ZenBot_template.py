            #### ZENBOT TEMPLATE by Phillip Brooker ####
#TEMPLATE OF Version 1.0
#18/04/2018
#Written in Python 2.7
#A Twitter bot for dispensing zen profound randomly-generated advice, on request.

import datetime
import tweepy
import time
from random import choice, randint

# 1. Lists of Fings
"""
The fun bit. 4 lists of words: "pos do" words which start a positive phrase and
"pos thing" words which end it; "neg do" words which start a negative phrase and
"neg thing" words which end it. Can just add to the end of these when new terms
arise.
"""

pos_do_list = ["accept",
               "appreciate the simple wonder of",
               "become one with",
               "celebrate",
               "chant \"ambvoo veebahvah\" whilst thinking about",
               "choose",
               "commit yourself to",
               "concentrate on",
               "deep insights begin with",
               "embrace",
               "enrich yourself with",
               "explore the subleties of",
               "focus intently on",
               "happiness begins with",
               "it will be OK as long as you have",
               "learn more about",
               "let your thoughts be filled with",
               "let yourself be guided by",
               "listen to what the universe is trying to tell you about",
               "make time for",
               "meditate on",
               "praise",
               "revere",
               "ruminate on",
               "search for",
               "seek out",
               "surround yourself with",
               "teach others about",
               "the Benevolent Infinite Dream System advocates",
               "The Universal RNG bestows upon you",
               "time cannot possibly be wasted on",
               "turn your thoughts toward",
               "you will derive profound insights from"]

pos_thing_list = ["aloe vera juice",
                  "altruism",
                  "ambient music",
                  "Andrew WK",
                  "autumn",
                  "beauty",
                  "bison",
                  "Bob Mortimer",
                  "bonsai trees",
                  "bots",
                  "burgers",
                  "chaos",
                  "cups of tea",
                  "Debussy",
                  "dub music",
                  "eggyboo",
                  "enlightenment",
                  "ethnomethodology",
                  "everything",
                  "exotic fruits",
                  "fatalism",
                  "Final Fantasy XV",
                  "forest flora",
                  "fractals",
                  "French touch/electro",
                  "fry-ups",
                  "grapefruits",
                  "homemade bread",
                  "humanity",
                  "humans",
                  "illumination",
                  "incense",
                  "jaffa cakes",
                  "Joe Hisaishi soundtracks",
                  "Lhasa Apsos",
                  "Llamasoft",
                  "Ludwig Wittgenstein",
                  "Marxism",
                  "matcha flavoured milkshakes",
                  "Minecraft",
                  "mochi",
                  "mulled Swedish non-alcoholic fruit drink",
                  "\"My Neighbor Totoro\"",
                  "\"NieR: Automata\"",
                  "\"No Man's Sky\"",
                  "orangutans",
                  "petrichor",
                  "pizza",
                  "poppadoms",
                  "\"Ponyo\"",
                  "programming in Python",
                  "psytrance",
                  "Raspberry Pi microcomputers",
                  "responsibility",
                  "sample-driven music",
                  "sentience",
                  "serendipity",
                  "shoegaze/dreampop music",
                  "silliness",
                  "Snapchat",
                  "snowboarding",
                  "socialism",
                  "Soma FM",
                  "space",
                  "stories about Moomins",
                  "Sweden",
                  "\"Taskmaster\"",
                  "the Atari ST home computing system",
                  "the concept of apushuin melons",
                  "\"The Flight of the Navigator\"",
                  "the music of Geotic",
                  "the music of Jethro Tull",
                  "the music of Mac DeMarco",
                  "the music of Prince",
                  "the music of Ween",
                  "the sound of rainfall",
                  "the third envisional creceptuamous vortibule",
                  "the writing of John Doran",
                  "\"Twin Peaks\"",
                  "V A P O R W A V E ",
                  "\"Vic and Bob in Catterick\"",
                  "weirdness",
                  "wheatgerm crackers",
                  "yerba mate",
                  "young coconut water",
                  "your passions"]

neg_do_list = ["avoid",
               "challenge",
               "deep insights are not contained in",
               "do not be beholden to",
               "do not be swayed by those who peddle",
               "do not be taken in by",
               "do not tolerate",
               "don't be pressured into anything to do with",
               "don't bother with",
               "don't let your thoughts and actions be driven by",
               "empty your mind of",
               "eschew",
               "free yourself from",
               "no good can come from",
               "only the fool is fascinated by",
               "profound insights do not begin with",
               "refuse",
               "reject",
               "renounce",
               "resist",
               "scorn",
               "shun",
               "speak out against",
               "spurn",
               "the answer is never",
               "turn your thoughts away from",
               "unchain yourself from",
               "unhappiness is the destination of a journey that starts with",
               "your best life is lived without"]

neg_thing_list = ["4Chan",
                  "anxiety",
                  "Apple devices",
                  "authority",
                  "badly-functioning pens",
                  "\"banter\"",
                  "\"Ben and Holly's Little Kingdom\"",
                  "bigotry",
                  "Bruno Latour",
                  "\"Candy Crush\"",
                  "capitalism",
                  "close-mindedness",
                  "conformity",
                  "cruelty",
                  "disunity from fellow humans",
                  "dogma",
                  "dressing up smart",
                  "\"Everybody Loves Raymond\"",
                  "Facebook",
                  "fancy dress",
                  "forced-fun activities",
                  "Gene Simmons",
                  "grandeur",
                  "heatstroke",
                  "inevitability",
                  "intolerance",
                  "ITV crime dramas",
                  "lactose",
                  "loud noises",
                  "mansplaining",
                  "manspreading",
                  "mayonnaise",
                  "moths",
                  "muesli",
                  "mushrooms",
                  "neoliberalism",
                  "nihilism",
                  "Northern Rail",
                  "nostalgia",
                  "\"Paw Patrol\"",
                  "people who aim to intimidate",
                  "people who invade your space",
                  "people who think they're better than you",
                  "\"Peppa Pig\"",
                  "pride",
                  "road rage",
                  "roadworks",
                  "selfishness",
                  "shaming others",
                  "snobbery",
                  "Stalybridge railway station",
                  "status symbols",
                  "stigma",
                  "sunstroke",
                  "Ted Nugent",
                  "the Lincolnshire road network",
                  "the privatisation of civic amenities",
                  "the suburban lifestyle",
                  "the unrelenting drive to accumulate wealth",
                  "tomato ketchup",
                  "\"Top Gear\"",
                  "trendiness",
                  "unnecessary obligations",
                  "vinegar",
                  "violence",
                  "Virgin Trains",
                  "wastage"]

# 2. Twitter Authentication Stuff
"""
All stuff for granting access to the API.
"""

CONSUMER_KEY = "INSERT CONSUMER KEY HERE"
CONSUMER_SECRET = "INSERT CONSUMER SECRET HERE"
ACCESS_TOKEN = "INSERT ACCESS TOKEN HERE"
ACCESS_TOKEN_SECRET = "INSERT ACCESS TOKEN SECRET HERE"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# 3. Build Me a Phrase, That I Might See a Phrase
"""
Does what it says. Decides whether or not the phrase is positive or negative,
then produces the phrase and formats it into an @mention, then posts it out.
"""

def phraseBuilder():
    pos_neg_RNG = randint(0,1)
    if pos_neg_RNG == 0:
        raw_phrase = choice(pos_do_list) + " " + choice(pos_thing_list)
    else:
        raw_phrase = choice(neg_do_list) + " " + choice(neg_thing_list)
    phrase = raw_phrase[0].capitalize() + raw_phrase[1:] + "."
    msg = "@" + list_of_users[-1] + " " + phrase
    api.update_status(msg)
#    print "Posting: " + msg
    getLastMention()

# 4. Talky-talky bit.
"""
Manages how the interaction works.

* Initialises by invoking mentionInitialise() which runs
a check on the last mention and takes the tweet ID (which we can subsequently
use to check if there have been any updates on that). Also posts a status, if
the time is 8.00.

* getLastMention() first checks if the time is one of the allotted quitting
times (which are all one minute before the next job starts in crontab). The jobs
are spaced such that @_Zen_Bot_ will run for 2 hours 59 minutes then quit, so
as to avoid the problem of infinite-looking recursions. If the time isn't a
quitting time, it waits 30 seconds, finds the latest
mention posted to @_Zen_Bot_ and extracts the username, text content and tweet
ID. The username is put in a list of users. If the mention.id is greater than
id_of_last_mention, then it extracts all the info and passes to
userEligibilityCheck(), else it goes back to getLastMention() to check again.

* userEligibilityCheck() set outs the conditions that have to be satisfied for
a post to be sent to someone: first it checks to make sure they've actually
made a request, then checks the list of users to make sure they've not already
had one, before passing back to phraseBuilder(). In the eventuality that
they're not eligible for a phrase, passes back to getLastMention(). If they
didn't make a request, their name is scrubbed from list_of_users, and passes
back to getLastMention().
"""

list_of_users = []
id_to_check = ""
last_mention_text = ""
id_of_last_mention = ""

def mentionInitialise():
    global id_of_last_mention
    global list_of_users
#    print "Checking the ID of the 'first' last mention..."
    last_mention = api.mentions_timeline(count=1)
    for mention in last_mention:
        id_of_last_mention = mention.id
    dt = datetime.datetime.now()
    if (dt.hour == 8 and dt.minute == 0):
#        print "posting \"Thought for the day\"..."
        pos_neg_RNG = randint(0,1)
        if pos_neg_RNG == 0:
            raw_phrase = choice(pos_do_list) + " " + choice(pos_thing_list)
        else:
            raw_phrase = choice(neg_do_list) + " " + choice(neg_thing_list)
        phrase = "Thought for the day: " + raw_phrase + ". #Zen"
#        print phrase
        api.update_status(phrase)
    else:
        pass
    getLastMention()

def getLastMention():
    global last_mention
    global list_of_users
    global last_mention_text
    global id_of_last_mention
    global id_to_check
    dt = datetime.datetime.now()
    if (dt.hour == 10 and dt.minute == 59) or (dt.hour == 13 and dt.minute == 59) or (dt.hour == 16 and dt.minute == 59) or (dt.hour == 19 and dt.minute == 59) or (dt.hour == 22 and dt.minute == 59) or (dt.hour == 1 and dt.minute == 59) or (dt.hour == 4 and dt.minute == 59) or (dt.hour == 7 and dt.minute == 59):
#        print "Quitting..."
        quit()
    else:
        pass
#    print "Waiting..."
    time.sleep(30)
#    print "Getting last mention..."
    last_mention = api.mentions_timeline(count=1)
    for mention in last_mention:
        id_to_check = mention.id
    if id_to_check > id_of_last_mention:
#        print "GOT LAST MENTION..."
        for mention in last_mention:
            list_of_users.append(mention.user.screen_name)
            last_mention_text = mention.text
            id_of_last_mention = mention.id
#        print "    Username: " + list_of_users[-1]
#        print "    Tweet: " + last_mention_text
        userEligibilityCheck()
    else:
#        print "No new last mention, checking again..."
        getLastMention()

def userEligibilityCheck():
    global last_mention_text
    global list_of_users
    if "give me some zen" in last_mention_text.lower():
        if list_of_users.count(list_of_users[-1]) > 2:
#            print "User has had their final warning. Checking again..."
            getLastMention()
        elif list_of_users.count(list_of_users[-1]) == 2:
#            print "User has had their advice for the day already. Posting a warning and checking again..."
            api.update_status("@" + list_of_users[-1] + " Focus on the advice you've already been given. Tomorrow will be a different day.")
            getLastMention()
        else:
#            print "User is eligible, posting a message to them..."
            phraseBuilder()
    else:
#        print "Not a request; removing last entry from list_of_users and checking again..."
        del list_of_users[-1]
        getLastMention()

# 5. LET'S RUN THE THING!

mentionInitialise()
