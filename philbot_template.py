                #### PHILBOT TEMPLATE by Phillip Brooker ###
#TEMPLATE OF Version 1.3
#18/04/2018
#Written in Python 2.7
#A social media status generator indistinguishable from the real thing

import facebook
from random import randint
from random import choice
from time import sleep

# 1. CLASSES AND ENTRIES

#Don't use the same variants for both Do and Be lists, otherwise there's the
#chance that you will get repetitions which will look fucky.

                ###   DO LIST VARIANTS   ###

def randomFruit():
        return choice(["mango", "pomelo", "guava", "grapefruit", "watermelon"])

def randomJob():
        return choice(["postman", "fireman", "greengrocer", "window cleaner"])

def randomBadAnimal():
        return choice(["moth", "daddylonglegs", "catfish"])

def randomBodyPart():
        return choice(["face", "hands", "arse", "feet"])

def randomTVShow():
        return choice(["The X-Files", "Seinfeld", "Twin Peaks", "Frasier", "Adventure Time", "Trailer Park Boys"])
        
def randomShitMusician():
        return choice(["Herb Alpert", "Max Bygraves", "Barbra Streisand", "Anne Murray"])

def randomNiceDrink():
        return choice(["chai tea", "yerba mate", "coffee", "Fanta", "young coconut water", "Fujian oolong tea", "club mate soda"])
        
def randomGuitarSoloist():
        return choice(["Frank Zappa", "Ween", "Prince"])

def randomGuiltyPleasureSong():
        return choice(["Paul Young's \"Every Time You Go (Away)\"", "Dionne Warwick's \"Heartbreaker\"", "The Bee Gees' \"You Should Be Dancing\"", "Rick James' \"Superfreak\"", "Meat Loaf's \"I Would Do Anything For Love (But I Won't Do That)\""])

def randomVegetable():
        return choice(["tin of tomatoes", "tin of anchovies", "courgette", "butternut squash"])
        
def randomMaverick():
        return choice(["David Emanuel", "Gazza", "Kris Akabusi", "Nosferatu", "Vincent Price", "Mr. Blobby", "John Cooper Clarke", "Neil Diamond", "William Shatner", "Johnny Cash"])

def randomNoise():
        return choice(["yelling", "screeching", "screaming", "bellowing", "shrieking"])

def randomCompilation():
        return choice(["\"48 Vuvuzela Love Songs\"", "\"Sounds of the Car Park\"", "\"The Wurzels' Greatest Hits\"", "\"The Muppets Play the Songs of GG Allin\""])

def randomSlur():
        return choice(["cadfael", "longshanks", "mustard tiger", "poo fingers"])

def randomFavouriteMeal():
        return choice(["a steak (feat. peppercorn sauce)", "a tandoori chicken", "a plateful of tater hash", "a hoi-sin duck", "an avocado bacon burger", "a bowl of chicken kare lomen", "a breakfast pizza", "some sausages", "a gala pie"])

def randomVideoGame():
        return choice(["Wipeout: Omega Collection", "NieR: Automata", "Llamatron", "No Man's Sky", "Space Giraffe", "Final Fantasy VII", "Assassin's Creed", "Sid Meier's Alpha Centauri", "Myst", "Doom II"])

def randomHerb():
        return choice(["garam masala", "cinnamon", "chai spice mix", "ras el hanout"])

def randomSmell():
        return choice(["Vicks Vapo-Rub", "freshly-cut grapefruit", "Buddha's Blessing incense", "petrichor", "freshly-baked bread", "exotic fruits and sun cream"])

def randomSwear():
        return choice(["prick", "gobshite", "dickhead", "bozo", "bonehead", "tit", "div"])

                ###   BE LIST VARIANTS   ###

def randomTacheMan():
        return choice(["Richard Pryor", "Borat", "Burt Reynolds", "Freddie Mercury", "Dick Van Dyke", "Tom Selleck", "Lemmy", "Danny Trejo"])

def randomShallabrity():
        return choice(["Bruce Willis", "Keith Lemon", "Gordon Burns", "Noel Edmonds", "Russell Brand", "Michael Ball", "Timmy Mallet", "Tinie Tempah", "Trevor McDonald", "Gok Wan", "Phillip Schofield"])

def randomRestrictivePlace():
        return choice(["the gulag", "jail", "a containment facility in Roswell (New Mexico)", "a ditch"])

def randomInsult():
        return choice(["stinky", "fucky", "riggy", "greasy", "shitty", "beshitted", "lumpy"])

def randomVideo():
        return choice(["http://bit.ly/2qOaCap", "http://bit.ly/1tOKwRE", "http://bit.ly/2zSEXKA", "http://bit.ly/2ApXHRb","http://bit.ly/2irbZtE"])

def initialiseRandomElements():
#DoListVariants
        randomFruit()
        randomJob()
        randomBadAnimal()
        randomBodyPart()
        randomTVShow()
        randomShitMusician()
        randomNiceDrink()
        randomGuitarSoloist()
        randomGuiltyPleasureSong()
        randomVegetable()
        randomMaverick()
        randomNoise()
        randomCompilation()
        randomSlur()
        randomFavouriteMeal()
        randomVideoGame()
        randomHerb()
        randomSmell()
        randomSwear()
#BeListVariants
        randomTacheMan()
        randomShallabrity()
        randomRestrictivePlace()
        randomInsult()
        randomVideo()

        # 1.1. DoTable

class DoTable():
        def __init__(self, text):
                self.text = text

DoDict = {
        "do0": DoTable("sitting on the roof, completely naked, throwing " + randomShitMusician() + " records at a dog like they were frisbees"),
        "do1": DoTable("eating a " + randomFruit() + " like it's a handfruit"),
        "do2": DoTable("lurching around a supermarket"),
        "do3": DoTable("saying the words to " + randomGuiltyPleasureSong() + " in " + randomMaverick() + "'s voice"),
        "do4": DoTable("looking like a nutter and feeling kind of dreamy"),
        "do5": DoTable("having a one minute silence out of respect for the " + randomFruit() + " I'm about to butcher"),
        "do6": DoTable("twitching uncontrollably"),
        "do7": DoTable("watching a bee trying to relieve itself on a prickly thistle"),
        "do8": DoTable("eating hotdogs in the style of a pelican"),
        "do9": DoTable("delicately sipping " + randomNiceDrink() + " and " + randomNoise() + " along to a " + randomGuitarSoloist() + " guitar solo"),
        "do10": DoTable("licking a stick"),
        "do11": DoTable("loading up a pillowcase with as many potatoes as I can"),
        "do12": DoTable("carrying an egg around in a dirty flannel"),
        "do13": DoTable("intermittently barking like a dog"),
        "do14": DoTable("talking about pencils with some dickhead on the train"),
        "do15": DoTable("punching through all the fence panels in my garden"),
        "do16": DoTable("trying to convince my wife that the banker from \"Deal or No Deal\" is actually Mr. Blobby"),
        "do17": DoTable("watching YouTube videos of old analog TV static"),
        "do18": DoTable("eating a " + randomFruit() + " the size of a fucking basketball and letting the juice run down the entire front of my body"),
        "do19": DoTable("swaggering around the house smugly because no-one knows I've got a kiwi fruit in my dressing gown pocket"),
        "do20": DoTable("playing an arcade game where I'm trying to prevent a constantly farting robot from trying to pull my " + randomBodyPart() + " off"),
        "do21": DoTable("weeping uncontrollably over the " + randomVegetable() + " in my fridge that has gone off before I could finish it"),
        "do22": DoTable("forcing a takeaway chopstick into my eyeball"),
        "do23": DoTable("stomping around a hotel room like a T-Rex and " + randomNoise() + " along to " + randomGuitarSoloist() + " songs"),
        "do24": DoTable("scraping algae off an old plank to mix in my wife's coffee"),
        "do25": DoTable("very carefully placing all my crayons end to end on the driveway"),
        "do26": DoTable("merrily plunging my " + randomBodyPart() + " into a pan of boiling water"),
        "do27": DoTable("sifting through the shit I found in the gutter last year"),
        "do28": DoTable("launching pint glasses out my front room window every time I get that stabbing pain in my " + randomBodyPart()),
        "do29": DoTable("eating instant coffee straight out of the jar by the handful"),
        "do30": DoTable("sitting with my neck retracted to try and fool my wife into thinking I'm Clive Anderson"),
        "do31": DoTable("crumbling thousands of oxo cubes straight into a storm drain"),
        "do32": DoTable("passionately kissing a packet of crisps"),
        "do33": DoTable("screaming at a " + randomVegetable() + " because it won't love me back"),
        "do34": DoTable("walking around town like Kryten"),
        "do35": DoTable("slapping a leg of lamb"),
        "do36": DoTable("pouring a litre of cream directly down my throat"),
        "do37": DoTable("curiously following the hoover around the house just to see where it goes next"),
        "do38": DoTable("burying all my wrestling figurines in the back garden"),
        "do39": DoTable("being a " + randomSwear()),
        "do40": DoTable("thinking about what it must be like to be " + randomMaverick()),
        "do41": DoTable("absolutely leathering a " + randomBadAnimal() + " at ping pong"),
        "do42": DoTable("burning all my underpants"),
        "do43": DoTable("thrashing about on a lilo in the middle of the living room"),
        "do44": DoTable("boiling my slippers"),
        "do45": DoTable("trying to put out a raging chip-pan fire with an eggcup and a bowlful of advocaat"),
        "do46": DoTable("hiding under the sofa with all my rations and supplies"),
        "do47": DoTable("dressing like a " + randomSwear() + " and heading up Arfscarfendale Pike to see Edward the Booble"),
        "do48": DoTable("watching " + randomTVShow() + " and practicing my obnoxious jazz-fusion dance moves"),
        "do49": DoTable("maliciously attacking a " + randomBadAnimal() + " with an inordinate amount of firepower"),
        "do50": DoTable("gently humming the theme to " + randomTVShow() + " whilst peeling all the skin off my fingers"),
        "do51": DoTable("trying to lighten the mood for a devastated squirrel"),
        "do52": DoTable("stinking up the place with my rancid recipes"),
        "do53": DoTable("splicing my farting clapper"),
        "do54": DoTable("constantly saying \"boglins\" under my breath"),
        "do55": DoTable("\"Keeping it Ghengis\"(TM)"),
        "do56": DoTable("\"Bringing it Back\"(TM)"),
        "do57": DoTable("invoking the wrath of the sun god Ra"),
        "do58": DoTable("sweet-talking a dirty old lion"),
        "do59": DoTable("making \"cloudy\" \"lemonade\" out of the overflow from the septic tank"),
        "do60": DoTable("furtively following a " + randomJob() + " and shouting \"KALIMAR!\" at him whenever he thinks I've gone away"),
        "do61": DoTable("forcing my " + randomBodyPart() + " into a jam jar"),
        "do62": DoTable("pretending to be a rootin' tootin' cowboy and going \"PYOWN PYOWN\" with my two finger pistols at all the staff in Dixons"),
        "do63": DoTable("re-enacting that bit in \"Sleepless in Seattle\" where Meg Ryan is pretending to be an angry orangutan"),
        "do64": DoTable("disingenuously nodding and smiling at a particularly vicious " + randomBadAnimal() + " to try and get it to shut up and piss off"),
        "do65": DoTable("beating seven shades of shit out of a " + randomVegetable()),
        "do66": DoTable("barricading myself in my office"),
        "do67": DoTable("arguing with an air traffic controller over who has the biggest " + randomBodyPart()),
        "do68": DoTable("running away from a horrible robot"),
        "do69": DoTable("telepathically communicating with the compost bin"),
        "do70": DoTable("eyeing up a tasty duck"),
        "do71": DoTable(randomNoise() + " at the skeleton that lives in my body to get out and stop frightening me"),
        "do72": DoTable("licking the palm for " + randomFruit()),
        "do73": DoTable("stockpiling \"Billy Bear\" for my post-apocalyptic butties"),
        "do74": DoTable("drinking boiling hot " + randomNiceDrink() + " straight out of my cupped and blistering hands"),
        "do75": DoTable("fiddling with my genetics to try and grow an extra head"),
        "do76": DoTable("standing at the bedroom window and trying to flick tic-tacs off the sill into the grid where the goblin lives"),
        "do77": DoTable("racing around the house and " + randomNoise() + " out the theme tune to \"" + randomTVShow() + "\" for no reason at all"),
        "do78": DoTable("carving some harrowing religious imagery into the side of a " + randomVegetable()),
        "do79": DoTable("relentlessly driving dozens of home-made cheeseburgers into my belly"),
        "do80": DoTable("cheerfully talking shite with a happy little robot"),
        "do81": DoTable("combing Art Garfunkel's wispy hair"),
        "do82": DoTable("eating a " + randomJob() + "'s dinner"),
        "do83": DoTable("scraping my lovely nose along someone's gravel driveway"),
        "do84": DoTable("playing \"Bop It\" with a man who I know for a fact isn't The Pope"),
        "do85": DoTable("blowing bubbles at some bimbo grizzly bear"),
        "do86": DoTable("blasting around town in Joan Baez's transit van (which she doesn't know I've borrowed)"),
        "do87": DoTable("casually wiping a buttery teatowel along Hadrian's Wall"),
        "do88": DoTable("whispering awful awful rumours about Brian Cox to anyone who'll take me on"),
        "do89": DoTable("breathing in the contents of a hoover bag"),
        "do90": DoTable("soaking my smalls in the slimy water in the dog's dish"),
        "do91": DoTable("huffing Chanel No. 5 out of a paper bag with a lovely old lady"),
        "do92": DoTable("stretching my arms out to a guy that looks a bit like " + randomMaverick() + " to give him a great big lovely old warm soppy hug"),
        "do93": DoTable("walking past a power station"),
        "do94": DoTable("designing a fucking KILLER cummerbund"),
        "do95": DoTable("taking the piss out of my own " + randomBodyPart()),
        "do96": DoTable("re-enacting Samuel Beckett plays with my Sylvanian Families dolls"),
        "do97": DoTable("working on my Gregorian chants for karaoke night"),
        "do98": DoTable("resting a fig on my flattened palm then punching it clean across the room"),
        "do99": DoTable("brutally squeezing the living shit out of a lime jelly with my bare hands"),
        "do100": DoTable("crying into a bucket that I won in a raffle"),
        "do101": DoTable("displaying my local knowledge by pronouncing place names really counterintuitively"),
        "do102": DoTable("wearing my kaftan and frantically sprinting around a shopping centre barefoot"),
        "do103": DoTable("mindlessly tapping my feet to a particularly poignant " + randomShitMusician() + " album"),
        "do104": DoTable("setting out to sail the seven seas in a filthy gravyboat"),
        "do105": DoTable("travelling on cosmic ribbons of light across the third envisional creceptuamous vortibule"),
        "do106": DoTable("throwing up all over my " + randomBodyPart() + " after a terrifying encounter with a " + randomBadAnimal()),
        "do107": DoTable("blasting out " + randomGuiltyPleasureSong() + " on my phone on a packed bus"),
        "do108": DoTable(randomNoise() + " until my throat starts to bleed"),
        "do109": DoTable("obliterating what's left of our fine bone china with my big fat " + randomBodyPart()),
        "do110": DoTable("wiping a chimp"),
        "do111": DoTable("knitting a vest for a recently-purchased " + randomFruit() + " to which I've become hopelessly attracted"),
        "do112": DoTable("lighting some incense and slowly sinking into a bath filled with gallons and gallons of scalding hot " + randomNiceDrink()),
        "do113": DoTable("dressing up in a leopard-skin loincloth and going door-to-door trying to sell this dirty old " + randomVegetable()),
        "do114": DoTable("waltzing around my living room with a bratwurst"),
        "do115": DoTable("gluing googly eyes onto a " + randomVegetable() + " so it can watch " + randomTVShow() + " with me"),
        "do116": DoTable("drawing a picture of " + randomShitMusician() + " beat-boxing in the back of a bin wagon"),
        "do117": DoTable("mercilessly beating a " + randomBadAnimal() + " prison-style with a " + randomVegetable() + " in an argyle sock"),
        "do118": DoTable("re-filling my burp jar"),
        "do119": DoTable("watching you eat your dinner"),
        "do120": DoTable("hunting for The Shitivus"),
        "do121": DoTable("singing a self-penned 147-versed epic love ballad called \"All My Base Are Belong To You\" to the tune of " + randomGuiltyPleasureSong()),
        "do122": DoTable("controlling you with my mind"),
        "do123": DoTable("crying in shame because the " + randomJob() + " called me a " + randomSlur()),
        "do124": DoTable("dancing around the house to my " + randomCompilation() + " compilation"),
        "do125": DoTable("working on my " + randomCompilation() + " mixtape"),
        "do126": DoTable("sending shitty emails to the bigwigs at EMI who rejected my " + randomCompilation() + " compilation idea"),
        "do127": DoTable("angrily spray-painting \"" + randomSlur() + "\" on the " + randomJob() + "'s van (and he knows why)"),
        "do128": DoTable("following an ant back to it's nest so I can call the queen a " + randomSlur() + " to her face"),
        "do129": DoTable("trying to force " + randomFavouriteMeal() + " through a trumpet with the power of my musical breath"),
        "do130": DoTable("lovingly and patiently grinding " + randomFavouriteMeal() + " into the living room carpet"),
        "do131": DoTable("blocking up the letterbox with " + randomFavouriteMeal()),
        "do132": DoTable("hiding " + randomFavouriteMeal() + " in my wife's work shoes as a present"),
        "do133": DoTable("ritually sacrificing " + randomFavouriteMeal() + " to the ghosts of my ancestors to help prevent shaving cuts"),
        "do134": DoTable("trying to convince my mate Chris that a bot produces all of my Facebook statuses"),
        "do135": DoTable("breathing heavily whilst sat surrounded by hundreds of empty packets of haribo"),
        "do136": DoTable("feeding Philbot(TM) his delicious monthly API access token (nomnomnomnomnom)"),
        "do137": DoTable("feverishly writing " + randomVideoGame() + " fanfiction for the baying hordes of idiots that read my blog"),
        "do138": DoTable("playing a self-developed extra hard difficulty setting of " + randomVideoGame() + " (i.e. sitting 60 feet away from the screen, in a stinking glass tank filled with hundreds of " + randomBadAnimal() + ", with " + randomCompilation() + " playing through my headphones at tinnitus-inducing volumes)"),
        "do139": DoTable("trying to explain the degree to which " + randomVideoGame() + " has influenced my life choices to my completely disinterested wife"),
        "do140": DoTable("filming myself excitedly re-enacting my most recent playthrough of " + randomVideoGame()),
        "do141": DoTable("watching all my old tapes of my re-enactments of " + randomVideoGame()),
        "do142": DoTable("organising my thousand-strong collection of tapes of my re-enactments of " + randomVideoGame()),
        "do143": DoTable("building shit-talking social media bots"),
        "do144": DoTable("saying \"Banquo's Ghost\" in a Geordie accent"),
        "do145": DoTable("walking in and out of all the rooms in the house carrying my glass of \"sippin' bleach\" in the style of Julian from Trailer Park Boys"),
        "do146": DoTable("drawing you doing that face you do when you're brushing your teeth and you think no-one is looking"),
        "do147": DoTable("smelling smelly smells"),
        "do148": DoTable(randomNoise() + " out \"VAPOURS VAPOURS VAPOURS VAPOURS VAPOURS VAPOURS VAPOURS VAPOURS VAPOURS\" over and over again"),
        "do149": DoTable("chewing a brick"),
        "do150": DoTable("making Michael Jackson noises"),
        "do151": DoTable("dressing up a cactus to look like " + randomMaverick()),
        "do152": DoTable("grooving along to the Winter 2014 Sky TV menu music"),
        "do153": DoTable("doing it for the Vine (RIP)"),
        "do154": DoTable("pointing at my own bare feet and saying \"what are thoooooossseee?\""),
        "do155": DoTable("battling The Grand Egg"),
        "do156": DoTable("bringing tha phonk"),
        "do157": DoTable("making a vaporwave album out of the incidental music from The Poddington Peas"),
        "do158": DoTable("making sick beats from samples of Gene Wilder and Richard Pryor swearing"),
        "do159": DoTable("drawing vaporwave aesthetic designs for bus seat covers"),
        "do160": DoTable("pricking about with one of those little wooden things that makes the noise when you wiggle it"),
        "do161": DoTable("treating stray dogs to makeovers"),
        "do162": DoTable("recharging my time crystals in preparation for yet another bogus journey"),
        "do163": DoTable("throwing a " + randomFruit() + " at Dr. Gonzo just as \"White Rabbit\" peaks"),
        "do164": DoTable("drinking black milk"),
        "do165": DoTable("doing the dance of life with all the flies in the melon patch"),
        "do166": DoTable("making sure my eyebrows are still on fleek"),
        "do167": DoTable("letting Lei Wulong win me at Tekken 2 (because even though he's computer-controlled he looks like he could do with the confidence boost more than me)"),
        "do168": DoTable("trying to convince my wife she's just had a curry by presenting her with a shot glass of Bailey's and a bill for sixteen pounds and forty pence"),
        "do169": DoTable("throwing a stupid old turnip over a wall"),
        "do170": DoTable("coughing my guts up"),
        "do171": DoTable("sitting waiting outside a service station bathroom whilst " + randomMaverick() + " has yet another thunderous piss"),
        "do172": DoTable("farting about with peppercorns"),
        "do173": DoTable("getting into an argument with the " + randomJob() + " over who dislikes mushrooms more"),
        "do174": DoTable("trying to convince the " + randomJob() + " to let me plant his prosthetic leg in the garden so I can grow enough to be self-sufficient"),
        "do175": DoTable("wolfing down a \"The Usual\" from Subway (i.e. a single black olive slice on a burnt 12-inch rye)"),
        "do176": DoTable("pouring a jar of " + randomHerb() + " directly down my gullet"),
        "do177": DoTable("sniffing that spiky thing I found down the back of the radiator that smells like " + randomHerb()),
        "do178": DoTable("prodding my collection of rice pudding skins and taking in all the spores that fly out"),
        "do179": DoTable("carving \"No session for PID 732\" into the front surface of every brick in my house"),
        "do180": DoTable("\"Turtle-Bustin'\""),
        "do181": DoTable("consolidating myself as one of the realest bufty grifters around"),
        "do182": DoTable("spending a couple of hours in my laborotoire refining my \"" + randomSmell() + "\" candle scent (pat pend pat pend pat pend!)"),
        "do183": DoTable("hunting in the garage for \"the thing that is probably some dead animal or other but smells exactly like " + randomSmell() + "\""),
        "do184": DoTable("painstakingly writing down, in full detail, all of my memories which are signified and brought to mind by the smell of " + randomSmell()),
        "do185": DoTable("huffing a paper bag full of " + randomSmell() + " right in the nostrils (both barrels)"),
        "do186": DoTable("rehearsing my impassioned argument for " + randomSmell() + " in the upcoming \"World's Nicest Smells and That\" championship debate"),
        "do187": DoTable("walking around the house extremely slowly, eating sesame mochi and listening to massive dub cuts at thunderous volumes"),
        "do188": DoTable("making preparations for next year's Flant Day"),
        "do189": DoTable("hiding in the fruit bowl and pretending to be a " + randomFruit()),
        "do190": DoTable("making hyper-realistic raspberries out of play-doh and lacquer"),
        "do191": DoTable("whispering modem sounds into the bathroom vent"),
        "do192": DoTable("harvesting my crop of apushuin melons"),
        "do193": DoTable("singing TV themes in the style of that fella from The B-52s"),
        "do194": DoTable("re-sheathing my field grips"),
        "do195": DoTable("saying \"Welcome to Blobbytown\" with a battle-hardened grimace"),
        "do196": DoTable("ruminating on all the ways bananas have hindered me or caused me some kind of grievance over the years"),
        "do197": DoTable("fabricating a Kheddis to keep the shitbirds off my back"),
        "do198": DoTable("humming an ancient madrigal about " + randomSmell()),
        "do199": DoTable("piling up billions and billions and billions and billions of cruciferous vegetables underneath the dining room table"),
        "do200": DoTable("learning the hard way that re-enacting King Kong at Beaconscott Model Village inevitably leads to a hefty fine and a lifetime ban"),
        "do201": DoTable("screwing an entire victoria sponge up into a ball and eating it like an apple")
        }

        # 1.2. BeTable

class BeTable():
        def __init__(self, start_text, end_text):
                self.start_text = start_text
                self.end_text = end_text

BeDict = {
        "be0": BeTable("I guess ", " is what my life has come to."),
        "be1": BeTable("", ", just waiting for the police to arrive."),
        "be2": BeTable("If ", " is wrong, then I don't ever want to be right!"),
        "be3": BeTable("Left untreated, \"" + randomTacheMan() + "'s Disease\" can result in loss of teeth, egg-ness, sulphuric feelings, and even ", ". So, don't delay; get to your local apothecary quick sharp, for maximum healings."),
        "be4": BeTable("", " gives me an enormous sense of well-being."),
        "be5": BeTable("Whenever I'm ", " it makes me wonder where in the hell my life went so wrong."),
        "be6": BeTable("I dreamt last night that I was ", " and I woke up in floods of tears."),
        "be7": BeTable("", " has made my face start to hurt again."),
        "be8": BeTable("I don't know what it is about ", ", but it makes my legs go all wibbly."),
        "be9": BeTable("I always find ", " to be a deeply profound and humbling experience."),
        "be10": BeTable("", " is always a complete fucking waste of time."),
        "be11": BeTable("Well EXCUSE ME for ", "!"),
        "be12": BeTable("If I wasn't ", " I'd be in " + randomRestrictivePlace() + "."),
        "be13": BeTable("", " really makes me ask a lot of deeply personal questions of myself."),
        "be14": BeTable("Just biding my time, ", ". Playing the long game."),
        "be15": BeTable("When I'm gone, I guess I'll be remembered mostly for ", "."),
        "be16": BeTable("", " is a wonderful way to kill off a couple of hours."),
        "be17": BeTable("If you ever see me ", ", it's probably in your best interest to just leave me the fuck alone."),
        "be18": BeTable("It's been AGES since I last booked time off work specifically for just ", "!"),
        "be19": BeTable("Getting a sign made up for my caravan that says \"If I'm ", "... DON'T COME A-KNOCKIN'!\""),
        "be20": BeTable("It's like my father always says, ", " will be the death of me."),
        "be21": BeTable("If I couldn't spend a little bit of my week just ", ", I think I'd go completely insane."),
        "be22": BeTable("Just ", "... It's the little things in life that get you through!"),
        "be23": BeTable("Look Mum, I'm ", " again!"),
        "be24": BeTable("I'm glad you caught me ", ". I WANT you to watch."),
        "be25": BeTable("I've always enjoyed ", " and now I'm seeking like-minded individuals with similar interests to start a club."),
        "be26": BeTable("", " always brings back fond memories of my childhood."),
        "be27": BeTable("Some work expenses I'd claimed have just come through unexpectedly, so I'm blowing it all on ", ". Costs more than you'd think!"),
        "be28": BeTable("That black dog that follows me told me to start ", " and now I can't stop."),
        "be29": BeTable("I must say, ", " is proving to be a massive confidence boost."),
        "be30": BeTable("I remember Paris; " + randomShallabrity() + " holding my hand tight as I'm ", ". A perfect moment. Actually, maybe I DON'T remember Paris..."),
        "be31": BeTable("If you see me ", ", say \"hello\"! But don't expect a reply."),
        "be32": BeTable("For reasons I don't really want to go into here, I'll be ", "... so don't expect me to answer any texts for a bit."),
        "be33": BeTable("If I'm ever close to death, I'm going to feel MASSIVELY cheated when my life flashes before my eyes and it's just me ", "."),
        "be34": BeTable("In my experience, a lot of life's problems can be quite easily solved by taking a deep breath, then ", "."),
        "be35": BeTable("In the not too distant past, I would have been arrested for ", ". Just goes to show how far we've come!"),
        "be36": BeTable("I'd like it if in the future I could just get on with ", ", without anybody bothering me."),
        "be37": BeTable("The only way you're going to stop me ", " is by removing my reinforced titanium spine. Can't be done, brother."),
        "be38": BeTable("I'm a fucking whiz at ", ". So, if you ever want me to show you the ropes, holla!"),
        "be39": BeTable("It's amazing that even after all these years, I still find ", " absolutely fucking gripping."),
        "be40": BeTable("Writing my memoirs. Pretty much just a long series of different times when I've been ", "."),
        "be41": BeTable("A leathery old man asked me if I wouldn't mind ", " and letting him watch, and I was like, \"Of course, no worries!\" and just as I start doing it he says \"Actually, don't bother.\" and walks off and I was like \"What's all that about?\""),
        "be42": BeTable("Trying to tell a " + randomInsult() + " old seagull that I've been ", ", but she's like \"Yeah, whatever, dickhead\"."),
        "be43": BeTable("And the award for ", " goes to... MEEEEE!!!!"),
        "be44": BeTable("Painting a beautiful self-portrait of me ", ". Actually, it's not that beautiful."),
        "be45": BeTable("When MI6 asked me to work for a new department they were setting up, I would never have guessed that my first mission would be ", "."),
        "be46": BeTable("Every day, the same old thing. I'm waking up, I'm brushing my teeth, I'm ", ", then I'm getting back in bed ready to do it all again tomorrow!"),
        "be47": BeTable("It was just like a movie; you, tears streaming down your face as you watched me ", ". One of those perfect moments that I'll never forget."),
        "be48": BeTable("Laughing my head off, ", ". BEST DAY EVER!"),
        "be49": BeTable("Andrew W.K. may party very hard indeed, but does that level of partying even come close to me ", "? I think not!"),
        "be50": BeTable("Spitting a completely FIRE freestyle rap about ", ". That shit is going STRAIGHT on my mixtape, bruh!"),
        "be51": BeTable("Staggering around an allotment in a state of shock after having been ", ". What a fucking day!"),
        "be52": BeTable("Been conducting experiments, the biggest success being the one where I was ", ". I forget what the findings were to be honest, but FUCK, that was some good science!"),
        "be53": BeTable("This really condescending old priest is trying to tell me all about ", ". Obviously doesn't know that I wrote the fucking book on it!"),
        "be54": BeTable("I don't care if you call me a hipster, I was ", " WAY before it was cool."),
        "be55": BeTable("Just been completely awestruck and inspired by seeing a poster that advised me to \"keep calm and carry on ", ".\""),
        "be56": BeTable("Only ", " can save me now!"),
        "be57": BeTable("I wrote a bot that just spews out garbage like \"", "\" as facebook status updates. Proper stupid, me!"),
        "be58": BeTable("You know, there's not ONE mention in " + randomShallabrity() + "'s memoirs about when we were stuck in " + randomRestrictivePlace() + " together and I was trying to lift his spirits by ",  ". Ungrateful bastard!"),
        "be59": BeTable("Never mind \"Chicken Tonight\", what I REALLY feel like is ", "!"),
        "be60": BeTable("Picked up a book at the library called \"Zen and the art of ", ".\" Sounds like it's RIGHT up my street!"),
        "be61": BeTable("I was hanging out with a radical dude and I was like \"Dude, it would be so extreme if I were ", "\" and he was like \"Hell yes, dude!\" so I did it and it was totally rad."),
        "be62": BeTable("The weirdest thing just happened. I bumped into this " + randomInsult() + " old guy who claims he's me from the future and he said I've got to do everything I can to avoid ever ", "... But now that's all I can think about doing and I'm really scared!"),
        "be63": BeTable("Found a bitcoin down the back of the sofa, so I'm spending it all on ", ". NOHODL/YOLO."),
        "be64": BeTable("Playing Bob Dylan covers is fun anyway, but I'm upping the ante by working in the odd lyric about ", " and seeing if anyone notices."),
        "be65": BeTable("I used to be an adventurer, but then I took an arrow to the knee. Now I'm just ", ". So my life has just been one massive downhill slide I guess."),
        "be66": BeTable("Who knew that ", " was tax-deductible??? I could make on this!"),
        "be67": BeTable("A super scary clown coerced me into ", "... so I pretended I was terrified and got on with it, secretly loving every minute!"),
        "be68": BeTable("I think I shocked the whole police station when I walked straight up to the desk, bold as brass, and turned myself in for ", "."),
        "be69": BeTable("Kind of feel like I shouldn't have listed \"", "\" as a hobby or interest on that job application."),
        "be70": BeTable("Scientists are always banging on about this \"Theory of Everything\", but I don't see how it could ever explain why I'm so obsessed with ", "."),
        "be71": BeTable("There's no chance I'll ever be able to compete professionally at my age, but I can still enjoy ", " as an amateur I guess."),
        "be72": BeTable("I started a blog about ", "... But there's really not that much to say about it to be honest."),
        "be73": BeTable("I get caught ", " ONE TIME, and I'm forever known throughout the community as \"Howlin' Mad Phillip\". FML!"),
        "be74": BeTable("My wife kicked me out the house for ", ". So I've been sat on the doorstep for a few hours, waiting for the tension to subside."),
        "be75": BeTable("They ran out of burgers at GBK, so I turned over the table and drew something rude with the squeezy mustard and the police came and there was a lot of fuss and bother. So I'm feeling a bit sheepish. Just going to be ", " until it all blows over."),
        "be76": BeTable("Well, I did it! You're looking at the Guiness World Record holder for ", "!"),
        "be77": BeTable("Hosting a seminar where I get to talk about my personal experiences of ", ". Sometimes work is WEIRD, man!"),
        "be78": BeTable("Spending some time tweaking my approach to ", "; getting it juuussssttt right."),
        "be79": BeTable("Never thought I'd be in a position to be ", ". Just really proud of where my life is at right now."),
        "be80": BeTable("Remember when I was always going on about ", "? It must have made sense at the time, but fucked if I can remember what I was thinking now!"),
        "be81": BeTable("I drank this cup of red water that Pissy Gary offered me and it made me start hallucinating about ", ". Good old Pissy Gary!"),
        "be82": BeTable("When I was in the cubs, they had to MAKE me a badge for ", "; I was THAT proficient!"),
        "be83": BeTable("Tonight, you're going to dream about me ", ". And it's going to completely ruin your life."),
        "be84": BeTable(randomTacheMan() + " knocked on for me saying he wanted to go to the park and have me push him on the swings but last time he wouldn't let me have I turn so I said nah bruc and closed the door on him and now I'm ", " while he looks at me through the window."),
        "be85": BeTable("Need some advice: if I was going to be ", " should I go formal, casual, smart-casual, or just the dressing gown?"),
        "be86": BeTable("Had a dream that " + randomTacheMan() + " was trying to convince me to start ", ". And then I wake up, drenched in sweat, and I'm finding evidence that it really happened all over the house. Freaked. Out."),
        "be87": BeTable("Out of me and " + randomShallabrity() + ", who do you think is more likely to be ", "? HINT: It's me."),
        "be88": BeTable("Got the night off, so I'm gonna be ", ". RESULT!"),
        "be89": BeTable("I told a friend at work that I've been ", " and he said he does it too...weirdo!"),
        "be90": BeTable("Maybe if I hadn't spent most of my honeymoon ", " my wife wouldn't have left me."),
        "be91": BeTable("Years from now, when humanity has completely fucked up the planet and left nothing but decaying remnants for those who will come to pick through the ashes, an alien being will come across my journal and read about me ", ". And at that point, those guys will probably presume that the whole human race are fucking freaks and hop straight back on their spaceship."),
        "be92": BeTable("Getting myself mentally prepped for ", ". If you have to ask, you don't need to know."),
        "be93": BeTable("WOW, a lot can change in a year! This time last year, I was ", "...and now...well, still doing it I guess. BUT BETTER!"),
        "be94": BeTable("Don't you DARE presume to tell me how to go about ", ". DON'T direct me."),
        "be95": BeTable("There's something about ", " that I just find innately soothing."),
        "be96": BeTable("", ". Rediscovering my roots."),
        "be97": BeTable("Listening to the gentle sound of the rain always makes me nostalgic for the time I've spent ", ". Need to get back on that!"),
        "be98": BeTable("Beating myself over the head with a shovel so I'm not constantly obsessing over ", ". It's the only way!"),
        "be99": BeTable("All I really wanted to be doing today was ", " but loads of little things have conspired against me and, yet again, I've ended up having to individually wash hundreds of these " + randomInsult() + " little caterpillars."),
        "be100": BeTable("If I can only prove my love to you by ", ", then so help me, I'll do it!"),
        "be101": BeTable("Don'tcha wish your girlfriend was ", ", like me?"),
        "be102": BeTable("Whenever I'm ", ", you can be sure I'll be thinking of you."),
        "be103": BeTable("I ever tell you about the time I caught naughty old " + randomTacheMan() + " stroking his moustache and spying on me ", "? Turns out, he just wanted to join in, but was a bit shy to ask! Awww, we had a belting day together too, good times!"),
        "be104": BeTable("OK, so a woman who looks like " + randomTacheMan() + "'s grandma sidled up to me and asked me to start ", "...well, take it from me, if it happens to you, just don't. It'll end in tears."),
        "be105": BeTable("I know for a fact that " + randomShallabrity() + " has a video of me ", " on his iPad. But the public will almost certainly never see it."),
        "be106": BeTable("Take it from me that trying to impress " + randomShallabrity() + " by ", " is NOT a good idea."),
        "be107": BeTable("Let me tell you; ", " is WAY more fun than it probably sounds!"),
        "be108": BeTable("Sat in my back garden drinking pint after pint of some ancient " + randomInsult() + " homebrew I found in the garage. Dunno what I put in it but it's compelled me to start ", "!"),
        "be109": BeTable("No, YOU'RE ", "."),
        "be110": BeTable("There's a verse in John Lenman's \"Imagine That\" that always sticks with me: You may say that I'm " + randomInsult() + ". But I'm not the only one. I hope someday you'll join me in ", ". And the world will be as one."),
        "be111": BeTable("OBJECTIVES: peace, serenity, spiritual well-being. ACTIONS TO TAKE: ", ". SUCCESS: guaranteed."),
        "be112": BeTable("If it's advice you want, ", " always works for me!"),
        "be113": BeTable("Crazy. Crazy for feeling so lonely. I'm crazy. Crazy for feeling so blue. I'm crazy for trying, crazy for crying, and crazy for ", "."),
        "be114": BeTable("Taking a leaf out of Dr. Gonzo's book. As my own attorney, I advise myself to start ", ". It'll be a goddamn miracle if I can finish before I turn into a wild animal."),
        "be115": BeTable("That feeling when I'm watching the CCTV footage back and see myself ", ", just as the security guard said...but I must have blacked out because I don't remember any of it."),
        "be116": BeTable("This 1984 Chateaux Beaumheule is REALLY pairing well with ", "."),
        "be117": BeTable("I get that same weird sickly feeling in my stomach ", " as I do when when I'm eating a meal that contains both chicken and egg."),
        "be118": BeTable("I found this red root in my back garden. So obviously I pulled it up and started chewing on it and the next thing I remember is waking up about 5 hours later mid-way through ", "...and I'm like \"whatsalldattaboutden???\""),
        "be119": BeTable("\"Dear My Local MP. What with all the Brexit and suchname that's about these days, I just wanna know if I can carry on ", "? If not, no worries, I'm probably getting too old for that shit now anyway, like Danny Glover (lol). Anyway, thanks and that, lots of love, Phippin Brikkin.\""),
        "be120": BeTable("Sometimes, when I'm ", ", I just take a minute to look up to the sky and see the gigantic head of Burt Bacharach smiling down on me. And when we're there, me and Burt Bacharach, smiling at each other, I just know that everything is going to be OK."),
        "be121": BeTable("In Sweden, I'd be free to go about ", " without anyone batting a Swedish eyelid (probably)."),
        "be122": BeTable("Love is... ", ". Isn't it?"),
        "be123": BeTable("If I wrote a novel about ", ", would you read it?"),
        "be124": BeTable("If you EVER catch me ", " I want you to break my back with a railway sleeper."),
        "be125": BeTable("Imagine me ", ". Go on. Imagine it. Go on. GO ON. IMAGINE IT. GO ON. GO ON."),
        "be126": BeTable("Really on my \"", "\" game today. Absolutely smashing it!"),
        "be127": BeTable("Great. There's a sign gone up at Athy train station that says all services are cancelled tomorrow because the guy in the ticket office is \"taking personal time for the purposes of ", "\". Fucking TYPICAL."),
        "be128": BeTable("For my CV, does \"", "\" count as \"Key Skills\"? I kind of feel like it SHOULD be on there somewhere..."),
        "be129": BeTable("Some say I'll never win The Turner Prize, but I just smile to myself and keep building my life-size Duplo (TM) diorama of me ", "."),
        "be130": BeTable("I fell asleep writing Final Fantasy XV fan-fiction, and when I woke up there were like 30 extra pages, all in my handwriting, about Prompto, Ignis and Gladiolus leaving Noctis sulking in the Regalia while they were watching me ", "."),
        "be131": BeTable("SPOILER ALERT: there's an easter egg in my latest text adventure game where if you can figure out how to unlock the attic, you'll be treated to a half-hour pixel animation of me ", ". And there's more secrets besides that, it really is fun fun fun for the whole family! Download it here: https://haziamusic.tumblr.com/software"),
        "be132": BeTable("\"...and if you can proudly say \"I've spent my time ", "\", yours is the world and everything that's in it, and what's more you'll be a man/woman my son/daughter.\""),
        "be133": BeTable("JUST as I'm about to start ", ", " + randomShallabrity() + " finds me and starts mithering about some about some aggro he's been getting on Twitter. And I'm like, \"I haven't got time for this trivial shit!\", nahmean?"), 
        "be134": BeTable("So " + randomShallabrity() + " caught me ", ". And, for reasons I'm still not fully clear on, this really pissed him off. So we got into a bit of a tussle and I ended up on the wrong side of a pretty vicious judo chop to the neck. All of which is to say no, this is NOT an \"Avid Merrion impression\"."),
        "be135": BeTable("Used to dream of a future where I could be ", ". And now I'm living it baby, yeah!"),
        "be136": BeTable("Who's got two thumbs and is currently ", "? Me. #visualjoke"),
        "be137": BeTable("I ate WAY too much lemon curd, blacked out, then woke up half-way through ", ". AND I SAID LAST TIME WOULD BE THE LAST TIME!!!"),
        "be138": BeTable("You're dreaming again. You must have fallen asleep. Not to worry, it's a pleasant dream. You're walking down a white corridor, past dozens and dozens and dozens of doors. The sun streams through the glass-covered roof, too brightly for you to see anything outside. Each door you walk past is different than the last; some freshly-painted and gleaming under the light of the sun as it pours down from above, some old and rotting with the paint flaking away, some are weathered plastic/PVC-type front doors with frosted glass panels, others are cut from thick ancient oak wrought with cast-iron. You walk down the corridor, with no frame of reference for the time that must be passing. You feel vaguely apprehensive as you spot an aberration in the far distance: a ladder poking out of a hatch in the floor of the never-ending corridor. You walk towards it, for an unspecified and unspecifiable period of time. Without thinking, as soon as you reach the ladder, you grasp it and descend. Your eyes adjust from the unrelenting brightness of the sun in the corridor, and you take stock of your surroundings. You see me, ", ". You wake up. You've pissed the bed."),
        "be139": BeTable("Wanna see a picture of me and " + randomShallabrity() + " ", "? bit.ly/IqT6zt "),
        "be140": BeTable("Triumphantly ", ", with all the bombast and grandeur of Meat Loaf's \"Greatest Hits\""),
        "be141": BeTable("Word on the street is that there's gonna be a surprise Flant Day tomorrow. But rather than preparing for it, I'm spending the day ", " #rebel"),
        "be142": BeTable("When I'm alone and life is getting me down, I just spend some time ", " and that sometimes makes me feel a bit better. Downtown."),
        "be143": BeTable("The bell rings for vespers, and in doing so, gently eases you out of your scholarly work. The light from the high window plays through the room, lowering a golden hue across the day's work. You notice Brother Abelard smiling at you from his lectern. You are pleased he has such an interest in improving his calligraphy; your tutelage seems to be appreciated at least. But has it had any effect? You rest your quill on the block and go to view Abelard's papers. As you approach, it becomes ever clearer that Abelard is delighted for you to review his progress. His smile broadens, and that instigates a similar effect on your own. He steps back and allows you to position yourself in front of the lectern. You see no calligraphy; only a crude drawing of me, ", ". You immediately let forth a inhuman screech, cast off your robes and run into the sea."),
        "be144": BeTable("Wanna see a video of me ", "? " + randomVideo()),
        "be145": BeTable("Been browsing the old YouTube and came across this video of me ", "...not sure who put it on there, but it's a deeply unnerving insight into my dark dingy past: " + randomVideo()),
        "be146": BeTable(randomShallabrity() + " and me have been making daft videos all day, and chortling happily ho ho ho at the results - here's one of me ", ": " + randomVideo()),
        "be147": BeTable("I think it was Meat Loaf that said \"I would do anything for love, except ", ". I just won't do it!\". And you know what? I believe him."),
        "be148": BeTable("Just been browsing YouTube and evidently some pervert has uploaded hours and hours of footage of me ", ". Not sure how they've got hold of it, but I guess I can only own it if I leak it myself: " + randomVideo()),
        "be149": BeTable("Dr. Bollocks from the Bakerloo Line says: \"", " never did me any harm, so fill yer bizoots!\""),
        "be150": BeTable("Apparently some bots have hacked into me with FAKE NEWS and have been claiming that I like ", ". So, for clarity, I do do that, but I don't like it."),
        "be151": BeTable("Some big dickhead movie mogul from Hollywood and that rang me up last month mithering me about the rights to my \"", "\" story. So I sold them the IP for an exorbitant amount, and regardez vous at the trailer they sent! " + randomVideo()),
        "be152": BeTable("Hallelujah! My every wish has been granted! Overnight, my wife has grown a moustache like " + randomTacheMan() + "! I'm so overjoyed that I've spent the day celebrating by ", ". Just goes to show, dunnit?")
        }

        # 1.3. TagTable

class TagTable():
        def __init__(self, text):
                self.text = text

TagDict = {
        "tag0": TagTable(" #realtalk"),
        "tag1": TagTable(" #thuglife"),
        "tag2": TagTable(" #dealwitit"),
        "tag3": TagTable(" :-)"),
        "tag4": TagTable(" ;-)"),
        "tag5": TagTable(" #livingthedream"),
        "tag6": TagTable(" #yolo"),
        "tag7": TagTable(" #inthebigleaguesnow"),
        "tag8": TagTable(" #lovinglife"),
        "tag9": TagTable(" #sorrynotsorry"),
        "tag10": TagTable(" #blessed"),
        "tag11": TagTable(" #yagetme?"),
        "tag12": TagTable("...NOT!"),
        "tag13": TagTable("...OR SUTIN!"),
        "tag14": TagTable(" #PartyOnWayne #PartyOnGarth"),
        "tag15": TagTable(" #keepingitghengis"),
        "tag16": TagTable(" #bringingitback"),
        "tag17": TagTable(" #animal"),
        "tag18": TagTable(" :-o"),
        "tag19": TagTable(" #justsayin"),
        "tag20": TagTable(" #makesyathink"),
        "tag21": TagTable(" #relatable"),
        "tag22": TagTable(" #kmt"),
        "tag23": TagTable(" #eggyboo"),
        "tag24": TagTable(" #justcallmeTheFunkyKheddis")
        }

# 2. STATUS BUILDER

def statusBuilder():
#This builds a random delay of four hours max into the function, since this
#was a pain in the arse to do with cron in Dash. Not ideal, but it'll work.
        sleep(randint(0, 14400))
#Then the function begins...
        initialiseRandomElements()
#DoDict and BeDict will always have one entry selected from each, though
#BeDict will always have two attributes selected as part of the one entry.
#TagTable will not necessarily always be selected, so there is an RNG
#to determine whether a tag is included at all on a percentage basis
#(i.e. 1-2 means no tag included, 0 means a tag, 33% chance) then a 
#further RNG to determine which tag is selected (IF one is included).
        DoRNG = randint(0,len(DoDict)-1)
        BeRNG = randint(0,len(BeDict)-1)
        TagIncRNG = randint(0,2)
        TagSelRNG = randint(0,len(TagDict)-1)
#Logic to display concatenated strings depending on whether or not Tag
#entry will be present.
        if TagIncRNG == 0:
                phrase = BeDict["be" + str(BeRNG)].start_text + DoDict["do" + str(DoRNG)].text + BeDict["be" + str(BeRNG)].end_text + TagDict["tag" + str(TagSelRNG)].text
        else:
                phrase = BeDict["be" + str(BeRNG)].start_text + DoDict["do" + str(DoRNG)].text + BeDict["be" + str(BeRNG)].end_text
#print the status with the first letter always capitalised.
        cfg = {"profile_id": "INSERT PROFILE ID HERE", "access_token": "INSERT ACCESS TOKEN HERE"}
        api = get_api(cfg)
        msg = phrase[0].capitalize() + phrase[1:]
        status = api.put_wall_post(msg)

def get_api(cfg):
        graph = facebook.GraphAPI(cfg["access_token"])
        return graph

statusBuilder()
