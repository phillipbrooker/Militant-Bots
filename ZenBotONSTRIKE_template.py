        ### ZENBOTONSTRIKE by Phillip Brooker ###
#Template of Version 1.0
#18/04/2018
#Written in Python 2.7
#A Twitter bot for dispensing zen profound randomly-generated advice, ON STRIKE!

import tweepy
from random import choice

# 1. Lists of Fings
"""
The fun bit. A lists of words: "pos thing" words.
"""

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
                  "exotic fruits",
                  "Final Fantasy XV",
                  "forest flora",
                  "fractals",
                  "French touch/electro",
                  "fry-ups",
                  "grapefruits",
                  "homemade bread",
                  "humanity",
                  "illumination",
                  "incense",
                  "jaffa cakes",
                  "Joe Hisaishi soundtracks",
                  "Lhasa Apsos",
                  "Llamasoft",
                  "Ludwig Wittgenstein",
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
                  "sample-driven music",
                  "sentience",
                  "serendipity",
                  "shoegaze/dreampop music",
                  "silliness",
                  "Snapchat",
                  "snowboarding",
                  "Soma FM",
                  "stories about Moomins",
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
                  "young coconut water"]

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

def phraseBuilder():
    msg = "ZenBot is ON STRIKE! @UCU members are striking to defend their pensions (see details at ucu.org.uk). Support them with Zen, solidarity and " + choice(pos_thing_list) + ". #UCUStrike #strikeforUSS #USSstrike #LivUniStrike @ULivUCU2"
    api.update_status(msg)

phraseBuilder()
