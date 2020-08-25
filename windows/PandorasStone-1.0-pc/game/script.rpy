# The script of the game goes in this file.

# Transition declarations

define flashbulb = Fade(0.2, 0.0, 0.8, color = '#fff')


# Character declarations

define r = Character("Robin", who_color = "#ff0000")
define rj = Character("James (Robin)", who_color = "#ff0000")
define j = Character("Jayden", who_color = "#0000ff")
define l = Character("Lance", who_color = "#00ffff")
define h = Character("Hazel", who_color = "#ff00ff")
define b = Character("Nicholas", who_color = "#ff0808")
define tg = Character("Sophocles", who_color = "#ffff00")
define m = Character("Puck", who_color = "#ffffff")
define e = Character("Eris", who_color = "#ffffff")

# The game starts here.

label start:

    scene living room_alt
    with dissolve

    "Hmm.."
    "..."

    show rb surprised
    play music 'images/the_kings_crowning_v1.mp3'
    with moveinleft

    "Huh?"

    show rb laugh

    r "Oh! Hey there! Didn't quite see you."

    show rb neutral

    r "The name's Robin. Nice to meet you!"
    r "Hmm... Wanna know a secret?"

    show rb laugh

    r "I was actually born a girl."

    show rb awkward

    r "It's not something you tell someone you just met huh?"

    show rb laugh

    r "Well... I guess I'm just different!"

    show rb awkward

    r "Tell me something... Don't my baggy clothes make my curvy figure like totally disappear?"

    show rb laugh

    r "That's probably why you couldn't tell!"

    show rb neutral

    r "Just to be clear though - I am a guy. Pronouns: He/Him/His."
    r "There was a time I'd be pretty offended for being referred to as a girl."

    show rb laugh

    r "But things are easier now."
    r "Thanks to my friends and the support they gave me I was finally able to accept my true feelings."

    show rb neutral

    r "I once completely shunned the idea that I might actually be born in the wrong body and tried my best to be more, you know, girl-ish."


    r "That all changed when my best friend introduced me to this super popular game."

    show rb laugh

    r "His name is Jayden BTW."

    show rb awkward

    r "You could say he's quite athletic, considering the ammount of time he spents working out. But more than that, he's a gamer. And so am I."

    show rb neutral

    r "The two of us were a team - Void we used to call it."

    show rb laugh

    r "No one could beat us."
    r "In fact, we held the first spot on the leaderboards of many popular online games."

    hide rb
    play music 'images/No More Magic_3.mp3'
    scene jayden room
    with fade
    show j happy
    with moveinleft

    j "Boy that was too easy!"

    show j happy at right
    with move
    show r notlistening at left
    with moveinleft

    r "Well what did you expect? We were up against amateurs!"

    show j nervous

    j "I thought they'd at least be more of a challenge you know? Hmph! I guess they just don't make em like us anymore eh?"

    show r dejected

    r "Uh... Sure."

    show j normal

    j "Oh BTW check this out! I just bought this new VR game and it has like mad reviews!"

    show r confused

    r "That a good thing?"

    show j normal

    j "Uh-huh. They say it's so fun that you'll wanna stay in there forever."

    show r dejected

    r "Too bad virtual food isn't enough nourishment to survive huh?"

    show j happy

    j "That's not all though! Wanna know the best part? Character customization! You can literally personalize your avatar any way you want!"
    j "Like you can literally be anyone!"

    show r uncaring

    r "(Hmm... Anyone huh?)"

    show j normal

    j "So? Wanna play? We can on quests together!"

    show r neutral

    r "I think I'll pass. I still have to complete DxD Heroes and Stein's Gate. Not to mention Code Geass and Chaos Child as well."

    show j shocked

    j "My! For a girl, you sure do play a lot of video games, don't you?"

    show r angry

    r "We just spent 12 straight hours playing SAO Fatal Bullet, defeating almost a thousand NPCs together and you say THAT sounds a lot?"

    show j nervous

    j "Relax! It was a compliment!"

    show r annoyed

    r "Fine! Anyway, I gotta go."
    r "Need to get home before 8 pm or else I won't hear the end of it from my mom. Enjoy your VR-whatever game it was!"

    show j happy

    j "Cools! Catch ya later!"

    hide j
    with moveoutright
    scene street night
    with fade
    show r neutral

    r "."
    r "..."
    r "Hmm...Anyone huh?"

    show r notlistening

    r "Well, I don't see any harm in giving it a shot."

    hide r
    with moveoutleft
    scene living room_alt
    with fade

    "Later that day... After purchasing the required gear for the VR game."

    show r smile
    with moveinleft

    r "Here we go! No turning back now!"

    scene black dark
    play music 'images/Soliloquy_0.p3.mp3'
    with fade

    "."

    show r neutral

    "..."
    "Welcome!"
    "This is the realm of Azeroth!"
    "You who dares enter these lands, what is your name?"

    show r confused

    r "My name? Umm...How about James? Yup! James sounds good. JAMES!"
    "..."
    "Welcome James!"
    "Now please state your gender."

    show r dejected

    r "MALE?"
    "..."
    "Now then. Please proceed to character customization room."

    show r neutral

    r "This will be fun."

    hide r
    play music 'images/DarkWinds.mp3'
    with moveoutleft
    scene fantasy forest
    with fade

    "..."

    show ra neutral
    with moveinleft

    "..."
    rj "Where am I?"
    rj "What is this place?"

    show ra sad

    rj "Hmm.. I wonder where everyone else is."

    show ra shocked at left
    with move
    show snake monster at right
    with moveinright

    rj "Ahh!!!"

    show ja angry at right
    with moveinright
    play sound 'images/Slap.mp3'

    j "Hyah!"

    hide snake
    with fade

    j "Take that you blood sucking demon! Or was it just a filthy snake? Ah! Who cares?! A monster is a monster is a monster."

    show ja laugh
    play music 'images/carnivalrides.mp3'

    j "Oh! Hey there! Are you alright?"

    show ra happy

    rj "Yes. Thanks to you I am!"

    show ja smile

    j "No problemo! I Jayden Williams am at your service."

    show ra shocked

    rj "Eh? J-jayden?"

    show ja shocked

    j "Hmm... Something wrong?"

    show ra laugh

    rj "No no! Nothing at all! \n (Geez who uses their real name in a game anyway!)"
    rj "(I just hope he doesn't figure out who I am.)"
    rj "(I mean how would I explain this?)"
    rj "(First I refuse to play the game with him, and then literally a few hours later I do. That too as a guy!)"
    rj "(No! I have to prevent him from finding out!)"

    show ja laugh

    j "So I didn't really catch your name."

    show ra shocked

    rj "Oh? My name? I-it's a boy's name - James."

    show ja smile

    j "James huh? Well! Nice to meet ya!"

    show ra happy

    rj "Likewise."
    j "Considering the circumstances, I guess it's pretty safe to assume that you are new to this game."

    show ja laugh

    j "How about I show you around? Whatd'ya say?"

    show ra laugh

    rj "That would be great! Thanks! What is this place anway?"

    show ja smile

    j "We are in what they call \"The Dark Forest.\" It's situated among the hills to the north of \"Revenale,\" which is like one of the major towns in this realm."

    show ja laugh

    j "When newcomers play this game, they usually spawn at a random location in this realm. And trust me, you've had better luck than most."

    show ja smile

    j "Moving on. Let me explain the basics."

    scene forest path
    with fade
    show ra laugh at left
    show ja smile at right


    j "In this realm there are 5 warrior races - Lancers, Beserkers, Spellcasters, Archers as yourself, and finally Assassins like moi."
    j "Each race has its own unique abilites that are pretty nifty when fighting dungeon bosses or other players."

    show ja shocked

    j "Why did you choose to be an Archer though?"
    j "I mean I'm not saying it's lame or anything. It's just not that popular."

    show ra happy

    rj "Um...Well..You know...I guess I just picked the first thing I saw."
    rj "(Obviously I'm not stupid to pick the Archer class for a reason like that!)"
    rj "(I'm actually a pretty good shot thanks to all those first person shooter games that dominated my childhood years.)"
    rj "(But I can't really tell him that! He might figure out who I am!)"

    show ja laugh

    j "Hahah! I guess that's one way of doing things."

    show ja smile

    scene town center
    with fade
    show ra happy at left
    show ja smile at right

    j "Okay! Back to business!"
    j "So there are \"Mainland Missions\" where you can like gather coins and boost your XP."
    j "And then there are smaller, and much easier, \"Quests.\""

    show ja laugh

    j "They usually involve low level monsters and so are pretty easy to clear."

    show ja smile

    j "For the missions however, it's better to go in groups."

    show ja shocked

    j "Speaking of... Since you're not part of any guild yet, how about joining ours?"

    show ra sad

    rj "You sure you want an inexperienced beginner like me?"

    show ja laugh

    j "Of course! Not to say that you're weak or anything! I just think it would be fun you know!"

    show ra happy

    rj "Um... It's not like I have anywhere else to go."

    show ja smile

    j "Then it's settled! Welcome to \"The Soul Society!\""

    show ra laugh

    rj "Thanks?"

    show ja laugh

    j "Oh hey! I finally found you guys!"

    hide ra
    with moveoutleft
    show ll annoyed at left
    with moveinleft

    l "We decided to meet back at this exact spot after 2 hours. Where else did you expect us to be? And why are you so late?!"

    show ja smile

    j "I just got a little sidetracked. Doesn't look like I was missing out on anything interesting anyway."

    show ll sad

    l "Moron!"

    show hs happy at center
    with moveinleft

    h "Cut him some slack, Lance. You know punctuality is not one of his strong suits."

    show ll annoyed

    l "Couldn't kill him to try!"
    j "Never mind that! I have someone I'd like you to meet."
    j "Guys, meet James. He's gonna be the newest member of \"The Soul Society!\""

    show ll smile

    l "Hey!"

    show hs blush

    h "Hello! It's so nice to meet you! I hope we can be great friends!"

    hide ll
    with moveoutleft
    show ra shocked at left
    with moveinleft

    rj "Uh... Yeah, sure!"
    j "Don't be fooled by her attitude. Hazel may look weak, but she's a pretty skilled magi. In fact, she's the Healer of our party so she's pretty much indispensible."

    show hs happy

    h "If you ever need to be healed during a fight, please, don't hesitate to ask!"

    show ra laugh

    rj "I sure will!"

    hide hs
    with moveoutright
    show ll smile at center
    with moveinright

    j "The tall, mean looking guy here is Lance. He's pretty good with his sword and has one of the highest kill records in all of Azeroth."

    show ja laugh

    j "Of course, he's lacking in many other areas, but what else can you expect from a guy who actually thinks clothes like those looks cool, am I right?"

    show ll sad

    l "I'm standing right here you know."

    show ja smile

    j "Why thank you for the information. Your service won't go unnoticed."

    show ll annoyed

    l "Hmph!"

    show ja sad

    j "Anyway, I'm starved!"

    show ja laugh

    j "Whatd'ya say we go to the town's square and get some yummy meat eh?"

    hide ra
    with moveoutleft
    show hs happy at left
    with moveinleft

    h "That sounds wonderful!"

    show ll smile

    l "Fine!"

    hide hs
    with moveoutleft
    show ra laugh at left
    with moveinleft

    rj "Um.. Sure, let's go!"

    hide ra
    hide ja
    hide ll
    play music 'images/Soliloquy_0.p3.mp3'
    scene black dark
    with fade

    "And that's how I became part of the infamous \"Soul Society.\""
    "The name's kinda weird, but I'm not complaining."
    "After that day, we went on several missions together."
    "We defeated numerous and all kinds of monsters."
    "My aim was pretty good and so I was able to level up pretty quickly."
    "And though I would not have admitted it before, I felt that being a guy suited me."
    "I felt more normal than I ever did."
    "It was a lot of fun!"
    "Until one day..."

    play music 'images/No More Magic_3.mp3'
    scene ruins dark
    with fade

    "While on a mission..."

    show ll annoyed
    with moveinleft

    l "Don't leave your post Jayden! Dammit! Why can't you follow the plan for once!"

    show ll annoyed at right
    with move
    show ja laugh at left
    with moveinleft

    j "For one, this way is a lot more fun!"

    hide ll
    with moveoutright
    show hs sad at right
    with moveinright

    h "Watch out Jayden!"

    show ja shocked

    j "Hmm? Ahhh!!!"

    hide hs
    hide ja
    play sound 'images/Loud_Bang.mp3'
    scene pandoras place
    with flashbulb
    play music 'images/Heroic Demise.mp3'

    "..."

    show r angry
    with moveinleft

    r "Urghh..."
    r "What just happened?"

    hide r
    with moveoutleft
    show l angry
    with moveinleft

    l "Is everyone alright?"

    hide l
    with moveoutleft
    show j confused
    with moveinleft

    j "Yeah, I'm fin..wait...Robin?!! Is that you?!!"

    show j confused at right
    with move
    show r confused at left
    with moveinleft

    r "Hmm? Wahh!! Your face!"

    show r annoyed

    r "Wait, that means... No! Why are we back to our real selves! What happened to our avatars!"

    hide j
    with moveoutright
    show h tearingup at right
    with moveinright

    h "Guys? What's going on?"

    hide h
    with moveoutright
    show l appoligetic at right
    with moveinright

    l "Hold on a minute! James is a girl!"

    show l neutral

    l "That's so messed up! Why would you choose to play as guy?"

    show r uncaring

    r "No! I am a guy!"

    show l neutral

    l "Look like a regular girl to me."

    show r angry

    r "My body may be that of a girl, but that doesn't change the fact that I am a boy! At least I've always felt like one!"

    hide l
    with moveoutright
    show j sad at center
    with moveinright

    j "..."

    show h sad at right
    with moveinright

    h "..."

    hide h
    with moveoutright
    show l annoyed at right
    with moveinright

    l "Geez! You're actually telling me you believe in stuff like that! Grow up! You're born a girl and so you are a girl. Stop pretending to be someone you're not! I can't believe we let someone like you in our guild!"

    show j angry

    j "Shut up Lance!"

    show l angry

    l "Why don't you make me?!"

    hide l

    play audio 'images/Sonic Boom-SoundBible.com-876321507.mp3'

    play music 'images/No More Magic_3.mp3'
    hide r
    hide j
    with flashbulb

    "..."
    tg "Um..Hmm.."
    tg "Testing..1..2..Okay good..."

    show tg normaltalking
    with moveinleft

    tg "Greetings one and all! Welcome to this very special event!"

    show tg normal

    tg "My name is \"Sophocles.\" I'm sure you all have heard of me. After all, I am the one who created this game you'll have been enjoying so much."

    show rguy angry at left
    with moveinleft

    "Random Player 1" "Wait really?"

    show rgirl upset at right
    with moveinright

    "Random Player 2" "No way! That \"Sophocles!\" How wonderful!!"

    hide rgirl
    with moveoutright
    hide rguy
    with moveoutleft
    show tg normaltalking

    tg "I would like to thank each and every one of you for making this game as successful as it is."
    tg "To show you my appreciation, I am here to present to you an exclusive mission. I'm sure you have heard rumours about the Philosopher's Stone, haven't you?"

    show rguy upset at left
    with moveinleft
    show tg normaltalking

    "Random Player 1" "I think I heard something like that... Isn't it like the ultimate weapon of Azeroth?"

    show rgirl worried at right
    with moveinright

    "Random Player 2" "Yeah! I've heard that the one who possesses it shall become invincible!"

    hide rgirl
    with moveoutright
    hide rguy
    with moveoutleft
    show tg sadsmile

    tg "No one has been able to find it yet, so I now offer you a chance to get your hands on it."
    tg "It's right here. Right inside this box. The so called \"Pandora's Box!\""

    show tg sadtalking

    tg "I'll leave it right here. It's your's to open."

    show tg normaltalking

    tg "However, you will first need to collect 7 gems from the 7 tricksters that were once trapped inside this box."
    tg "Place them into the sides of the box and it shall open."

    show tg normal

    tg "The current whereabouts of the 7 tricksters have been added to your world map feature, so feel free to go monster hunting whenever you are ready."
    tg "Also, to make things a bit more interesting, I have decided to change the rules of this game."

    show tg normaltalking

    tg "From now on, all dealings in this realm shall be in accordance with 3 simple rules."
    tg "Rule No 1. \"Any dispute amongst players, or players and NPCs shall be resolved through games.\""
    tg "Rule No 2. \"The players will go up against each other in any game of their choice and must make wagers considered of equal value to both opposing players.\""

    show tg sadsmile

    tg "That said, if you play against one of the tricksters, if you win you get the gem."
    tg "But if you lose, you lose the right to challenge that trickster again."

    show tg normaltalking

    tg "And finally, Rule No 3. \"The player that loses the game must comply by the set wagers or he shall disappear.\""

    show tg sly

    tg "Oh and when I say disappear, I don't just mean from the game!"
    tg "I'm sure that by now some of you must have noticed that you cannot log out of the game. The option has been removed from your game disks."

    show tg smile

    tg "That will remain until someone acquires the Philosopher's Stone, so I suggest you better hurry."

    show rguy angry at left
    with moveinleft

    "Random Player 1" "No way! What sort of crap is that? Let us out!"

    show rgirl worried at right
    with moveinright

    "Random Player 2" "Are we really going to be stuck in here? What should we do!"

    hide rgirl
    with moveoutright
    hide rguy
    with moveoutleft

    tg "Ah! How could I have forgotten the most important part! Listen well, because your lives depend on it."

    show tg normaltalking

    tg "As you know, there are 5 warrior races in Azeroth - Lancer, Beserker, Spellcaster, Archer and Assassin."
    tg "I'm sure you all will do your best to get the Philosopher's Stone. However..."

    show tg normal

    tg "Only the race of the team that acquires it shall live. The rest shall be erased right out of existence!"

    show rguy upset at left
    with moveinleft

    "Random Player 1" "Is he serious?"

    show rgirl worried at right
    with moveinright

    "Random Player 2" "Are we all going to die then?"

    hide rgirl
    with moveoutright
    hide rguy
    with moveoutleft
    show tg smile

    tg "Well then! I wish you all good luck! Let the games begin!"

    hide tg
    with moveoutleft

    "..."

    show j angry
    with moveinleft

    j "Geez! Do you believe this guy? What a total wackjob!"

    show j angry at left
    with move
    show h sad at right
    with moveinright

    h "He isn't lying though, is he? The log out option has indeed disappeared from my gear."

    hide h
    with moveoutright
    show l neutral at right
    with moveinright

    l "Well, I guess that's that. I'm outta here."

    show j confused

    j "Wait...You're leaving?"

    show l angry

    l "Of course I am! We are all of different warrior races remember? Only one shall survive! And even if we were in the same race, I don't think I have the stomach to be around you lot a second longer."

    hide j
    with moveoutleft
    show h sad at left
    with moveinleft

    h "Oh Lance...I know you don't mean that..."

    hide h
    with moveoutleft
    show j angry at left
    with moveinleft

    j "Jerk..."

    show l neutral

    l "I'm off."

    hide l
    with fade
    show h sad at right
    with moveinright

    h "Um..Guys?"
    h "I don't really want to part with you guys but..."

    show h embarassed

    h "I'm sorry!"

    hide j
    with moveoutleft
    show r notlistening at left
    with moveinleft

    r "It's alright. It's probably for the best."

    show h happy

    h "Stay safe guys! Let's all do our best!"

    hide h
    with fade
    show j sad at right
    with moveinright

    j "..."

    show r sad

    r "Aren't you gonna leave too?"
    j "Robin..."
    j "..."

menu:

    "Have Jayden be considerate towards Robin.":
        $ choice1 = True
        jump choice1a

    "Let Jayden be indifferent towards Robin.":
        $ choice1 = False
        jump choice1b

label choice1a:

    show j nervous

    j "You know I can't do that!"

    show j normal

    j "You and I, we are a team, and as a team we gotta stick together!"
    j "And please. Don't tell me you actually believe that any of these low-breeds have what it takes to beat us to the Philospher's Stone!"

    show j happy

    j "I mean, Void is unbeatable after all!"

    show r dejected

    r "Jayden..."
    r "What about...?"
    r "What about the other thing?"

    show j shocked

    j "Huh? What other thing?"

    show r annoyed

    r "Don't play dumb! You know exactly what I'm talking about!"

    show j confused

    j "If this is about earlier, I'm sorry for how Lance reacted. He was totally out of line. And I should have been more supportive!"

    show r sad

    r "Or maybe you should have reacted exactly the way he did! I mean, that is how one would normally react to something like that, isn't it?"

    show j happy

    j "No way! I could never do that!"
    j "I don't care if you say you are a guy or a girl! To me, you are Robin, my best friend. And more importantly, you're the cofounder of Void!"

    show r smile

    r "We're the only 2 members you know."

    show j nervous

    j "All the more reason why I can't lose you."
    j "Come on!"

    show j happy

    j "Let's show these amateurs what real gamers look like! Whatd'ya say?"

    show r neutral

    r "..."

    show r smile

    r "Hmph! Alright! I'm in."

    jump continue1

label choice1b:

    show j sad

    j "I don't wanna do that..."
    j "..."
    r "Jayden..."

    show j normal

    j "Let's just stick together for now alright?"
    r "Yeah... Okay..."

label continue1:

    hide j
    hide r
    scene cave inside
    with fade
    play music 'images/DarkWinds.mp3'

    "..."

    show j normal
    with moveinright

    j "I'm back!"

    show j normal at right
    with move
    show r notlistening at left
    with moveinleft

    r "Did you find out anything?"

    show j confused

    j "Geez! Do you have to hide out in a place like this?"
    j "I mean this cave is super awesome and all, but don't you think it's time you come out already?"

    show r dejected

    r "I just don't wanna have to deal with other people for a bit..."

    show j sad

    j "..."

    show r neutral

    r "Never mind that! What did you find out?"

    show j normal

    j "Oh right!"
    j "Well. As expected, people have started dividing into their respective races and are going for the win."

    show j sad

    j "There are others who have just given up. I kinda feel bad for them you know?"

    show r sad

    r "Hmm... I knew that was a possibility."

    show j happy

    j "Well then, let's go already!"
    j "We need to hurry and get those gems before someone else gets all of em!"

    show r dejected

    if choice1:
        r "Alright! Alright!"
        r "But whom should we challenge first?"
    else:
        r "Okay... But whom should we challenge first?"

    show j normal

    j "How about this guy? - \"Puck.\""
    j "His location is pretty close by... considering where we are."

    show r sad

    if choice1:
        r "Puck it is then."
    else:
        r "Yeah...Alright..."

    hide r
    hide j
    play music 'images/No More Magic_3.mp3'
    scene puck place
    with fade
    show r confused at center
    with moveinleft

    r "You sure this is the right place?"

    show r confused at left
    with move
    show j nervous at right
    with moveinright

    j "Hey, I'm just following the map you know."

    hide j
    with moveoutright
    play music 'images/Soliloquy_0.p3.mp3'
    hide r
    with moveoutleft
    show m sly
    with moveinleft

    m "Hahaaha!"

    show m neutral

    m "Welcome my dear friends!"

    show m neutral

    m "I'm Puck!"

    show m sly

    m "Surely you must have heard of me! Hahaa!"

    show m sly
    with move
    show j nervous at right
    with moveinright

    j "He's pleasant."

    hide m
    with moveoutleft
    show r dejected at left
    with moveinleft

    if choice1:
        r "No kidding."
    else:
        r "I guess..."

    hide j
    with moveoutright
    show m neutral at right
    with moveinright

    m "So you wanna play a game with me? I'm assuming that's why you're here, aren't you?"

    show r sad

    r "Um... Yeah. That's right."
    r "But what sort of game is it gonna be?"

    show m sly

    m "Well, I'm really generous you know. How about I let you decide?"

    hide m
    with moveoutright
    show j normal at right
    with moveinright

    j "I can live with that!"
    j "Whatd'ya say Robin? Wanna show this guy what a true gamer can do?"

    show r dejected

    r "Me?! Well..."

    show j sad

    j "Too soon huh? Never fear! I'll take this one."

    show r sad

    j "So... We can pick any game we like yeah? That's what you said right?"

    hide r
    with moveoutleft
    show m sly at left
    with moveinleft

    m "Of course! I always stand by my word!"
    j "Great! Then how about a coin toss?"

    show m neutral

    m "A coin toss?"

    show j normal

    j "Yeah. I mean that is a game too you know."
    j "How about it? You pick either Heads or Tails. If you are correct, you win. If you are not, I do. Sounds pretty simple right?"

    show m sly

    m "Hahaaha! Sure! If that's the game you choose, I shall humour you!"
    j "Alright, here goes. Pick one."

    show m neutral

    m "Heads."

    show coin heads

    "..."

    play sound 'images/Dropped Wooden Floor-SoundBible.com-382418821.mp3'
    show coin heads:
        xalign 0.5
        yalign 0.5
    with move

    show coin tails:
        xalign 0.5
        yalign 0.0
    with move
    show coin heads:
        xalign 0.5
        yalign 0.5
    with move
    show coin tails:
        xalign 0.5
        yalign 1.0
    with move

    "The coin flips in the air. Lands on the ground. And sticks into the thick soil stopping on its edge."

    show m sly

    m "Hahaaha! Neither Heads nor Tails. I guess we have to have a do over."

    show j happy
    hide coin

    j "Actually. I win."

    show m sad

    m "Oh?"

    show j normal

    j "You see. When I mentioned the rules, I said that you'd only win if you got it right."
    j "You picked Heads. But since it's neither Heads nor Tails, no matter which one you'd pick, you'd still lose."

    show m sly

    m "Hahaaha! So you made it fall on it's edge on purpose?"

    show j nervous

    j "You bet! When we came here, I noticed that the ground was pretty damp."

    show j normal

    j "I tossed around a couple stones on the way and noticed that they were instantly stuck in the soil upon hitting it."
    j "That game me an idea."
    j "If I made sure that the coin landed on it's edge, I knew it would stop in that position as well."
    j "And based on probability, we know that a coin is more likely to land on the side that is initially up. It's like a 52-48 kinda odds."
    j "Also, I spun the coin instead of flipping it."
    j "That way, because of centripetal force, it was sure to hit the ground when on it edge."

    show j nervous

    j "So my win was guaranteed before the game even began."
    m "Hahaaha! What an amusing guy you are!"
    m "Very well then. You have defeated me. The gem is yours."

    hide m
    with flashbulb

    "..."

    show j happy

    j "Got it!"
    j "Yeah! Our very first gem!"

    show j normal

    j "It doesn't look that valuable."

    show j normal at right
    with move
    show r smile at left
    with moveinleft

    if choice1:
        r "You did well!"

        show j happy

        j "Of course! No one should underestimate the power of Void!"

        show r notlistening

        r "Sure..."

    else:
        r "Um... You were...You were great!"

        show j happy

        j "Of course! No one can beat Void!"

        show r sad

        r "Um..."

    scene cave inside
    with fade
    play music 'images/DarkWinds.mp3'

    "The next day..."

    show j angry
    with moveinleft

    j "Urgh.."
    j "Man, sleeping in a VR game sucks!"
    j "I doesn't even feel like sleeping."
    j "I was literally just staring at a blank screen the whole time."

    show j angry at right
    with move
    show r dejected at left
    with moveinleft

    if choice1:
        r "Well, what did you expect?"
        r "It was created by humans."
    else:
        r "I guess..."

    show j normal

    j "Onto the second gem then. Let's go!"

    show r sad

    if choice1:
        r "Urgh... Do you have to be so energetic about it?"

        show j happy

        j "Of course! If I don't we'll never get all the gems in time! And then we'll be stuck in here for good!"

        show r neutral

        r "Fine! How about \"Eris\" next?"
        r "She's at a nearby lake."

    else:
        r "Um... Okay..."
        r "But where should we go first?"
        j "Which one's the nearest?"

        show r dejected

        r "There's \"Eris\"... She's at a nearby lake."

    show j nervous

    j "A gorgeous lady and a lake? You know I'm in!"

    hide j
    hide r
    play music 'images/No More Magic_3.mp3'
    show lake view
    with fade

    "At the lake..."

    show j shocked
    with moveinleft

    j "Woah! This place is so awesome!"
    j "If I could live here, I don't think I'd mind being stuck in the game forever!"

    show j shocked at right
    with move

    if choice1:
        show r annoyed at left
        with moveinleft

        r "Get a grip dude!"

    else:
        show r dejected at left
        with moveinleft

        r "I guess..."

    hide r
    with moveoutleft
    hide j
    with moveoutright
    play music 'images/Soliloquy_0.p3.mp3'
    show e smiling
    with moveinleft

    e "Oh my! Do I have guests?"
    e "Are you here for my tea party?"

    show e smiling at left
    with move
    show j nervous at right
    with moveinright

    j "I wouldn't mind having some! Especially with someone as beautiful as you are!"
    e "Why thank you young man!"

    hide e
    with moveoutleft
    show r sad at left
    with moveinleft

    if choice1:
        r "Seriously?"

        show r neutral

        r "Rather than the tea, would you mind giving us the gem instead? That would be a big help thanks!"
    else:
        r "Umm..."
        r "Is there a way to settle this without a fight?"


        r "Like maybe... Would you mind just giving us the gem?"


    hide j
    with moveoutright
    show e uncaring at right
    with moveinright

    e "Oh. I wouldn't, but you still have to beat me in a game first you know. Rules are rules."

    show r dejected

    if choice1:
        r "Figured as much. So what's it going to be?"
    else:
        r "Um, Yeah..."

    show e assertive

    e "Hmm... Let me see."

    show e gentle

    e "Oh! How about a word game? It'll be so fun!"

    show r sad

    r "How do we play it?"

    show e uncaring

    e "Each of us will take turns saying any word we like."

    show e firm

    e "But you must follow these 3 rules..."
    e "First, if the word we say is an object that is not present in our surroundings, it will appear. If if it present, it will disappear."
    e "Second, if either of us repeats a word that has already been used, they lose."
    e "And finally, If one is unable to come up with a word within 30 seconds, they lose."

    show e smiling

    e "Pretty simple, don't you think?"

    show r dejected

    r "Um?"

    show e creepy

    e "So which one of you cuties is going to be my opponent?"

    hide e
    with moveoutright
    show j normal at right
    with moveinright

menu:

    "Have Jayden encourage Robin to play the game.":
        $ choice2 = True
        jump choice2a

    "Let Jayden stay indifferent towards Robin":
        $ choice2 = False
        if not choice1:
            jump choice2b
        else:
            jump choice2a

label choice2a:

    j "How about you take her on?"

    show r confused

    r "Wait what? Why don't you do it?"

    if choice2:
        show j happy

        j "Oh come on! We both know that you are better suited for these kind of games. After all, between the two of us, you are the better tactician."

        show r dejected

        r "But...I'm not sure I'm ready..."

        show j normal

        j "I know you are! You just gotta believe in yourself!"

        show r sad

        r "Um..."

        show r smile

        r "Okay fine. I'll do my best."

        show j nervous


        j "Oh yeah! Show her that no one messes with Void!"
    else:
        show j confused

        j "Oh come on! I already took the last one! It's only fair!"

        show r dejected

        r "Um... Okay..."

        show j nervous

        j "I just hope you do well..."



    show r neutral

    r "..."

    hide j
    with moveoutright
    show e creepy at right
    with moveinright

    e "So you then?"
    e "Let's have a great time! I'll start with \"Sun!\""

    scene black dark
    with dissolve
    show e creepy at right
    show r neutral at left

    "It became dark."

    show r uncaring
    show candles item

    r "Hmm... I think I get it now. \"Candles!\""

    show flowers item
    show e smiling

    e "\"Flowers!\""

    show r angry
    show apples item:
        xalign 0.25
        yalign 1.0

    r "\"Apples!\""

    show book item:
        xalign 0.75
        yalign 1.0

    e "\"Book!\""

    hide e
    hide r
    with fade
    show ship item:
        xalign 0.5
        yalign 0.0
    show elephant item:
        xalign 1.0
        yalign 0.0
    show giraffe item:
        xalign 1.0
        yalign 0.5
    show pudding item:
        xalign 0.3
        yalign 0.0
    show cola item:
        xalign 0.25
        yalign 0.55
    show emp item:
        xalign 0.0
        yalign 0.0
    show e assertive at right
    show r confused at left

    "A few hours later..."

    show cupcake item:
        xalign 0.4
        yalign 1.0

    r "\"Cupcake!\""

    show fish item:
        xalign 0.0
        yalign 1.0
    hide r
    show r confused at left

    e "\"Golfish!\""

    show lemonade item:
        xalign 0.75
        yalign 1.0

    r "\"Lemonade!\""

    show r notlistening

    r "Aren't you gonna eat anything? This game makes it pretty convenient."

    show e uncaring

    e "Unlike you mortals, I do not need organic matter for sustenance."

    show r annoyed

    r "(Then why the hell do you drink tea?)"

    show e assertive
    show rainbow item:
        xalign 0.5
        yalign 0.0
    hide e
    show e assertive at right
    hide r
    show r annoyed at left
    hide cola
    show cola item:
        xalign 0.25
        yalign 0.55

    e "\"Rainbow!\""

    hide e
    with moveoutright
    show j nervous at right
    with moveinright

    j "Come on Robin! Get this over already! I don't wanna be stuck here all day!"

    show r dejected

    if choice1:
        if choice2:
            r "Just earlier you said that you wouldn't mind staying here forever!"

            show r uncaring

            r "Anyway. I think I know to end this. Just hang back a little longer."
        else:
            r "Um... I'll try and get this done quick... promise."
    else:
        r "Um... I'll try and get this done quick... promise."

    hide j
    with moveoutright
    show r neutral

    r "(Inhales deeply)\"Oxygen!\""

    show e dangerous at right
    with moveinright

    e "Ack! You won't get me that easy! Or are you forgetting that you need oxygen to survive too?"
    e "\"Air!\""

    show e assertive

    e "There! All better!"

    show r smile

    if choice1:
        if choice2:
            r "(Talking only by exhaling.) You fell for it!"
            r "I said \"Oxygen\" first, and so that disappeared from around us."
        else:
            r "(Talking only by exhaling.) Yes! It worked!"
            r "Thing is, you didn't realize that I said \"Oxygen\" first, and so that disappeared from around us."
    else:
        r "(Talking only by exhaling.) Yes! It worked!"
        r "Thing is, you didn't realize that I said \"Oxygen\" first, and so that disappeared from around us."

    r "I said \"Oxygen\" first, and so that disappeared from around us."
    r "But when you said \"Air,\" all the surrounding air disappeared, but since oxygen was already gone, it came back."
    r "So this air is now pure oxygen. Even for someone like you inhaling that concentrated oxygen is dangerous."

    show e dangerous

    e "But that affects you too!"

    show r notlistening

    if choice1:
        if choice2:
            r "Sure! But before all this I inhaled as much regular air as possible."
            r "Right now, I'm only exhaling it little by little."
        else:
            r "Yes... Um... But before all this I inhaled as much regular air as possible."
            r "You see... Right now, I'm only exhaling it little by little."
    else:
        r "Yes... Um... But before all this I inhaled as much regular air as possible."
        r "You see... Right now, I'm only exhaling it little by little."

    show r angry

    r "Now to end this - \"Atmosphere!\" (Exhales the remaining air.)"

    show e scary

    e "(Ahh! What's wrong with me?)"
    e "(Why am I all bloated? Huh? Why can't I speak?!)"

    show r neutral

    r "(Since you inhaled all that concentrated oxygen, now that there is no atmosphere around, all that oxygen is trying to come out all at once.)"

    if choice1:
        if choice2:
            r "(And did you forget? Sound waves don't travel in space.)"
        else:
            r "(And one thing you forgot to consider... Sound waves don't travel in space.)"
    else:
        r "(And one thing you forgot to consider... Sound waves don't travel in space.)"

    show r smile

    r "(So in 30 seconds I'll win because of the third rule!)"
    e "(No! I can't lose like this!)"
    e "(Arghh!!!)"

    hide e
    hide r
    show lake view
    with flashbulb
    show r smile at left
    with moveinleft
    show j normal at right
    with moveinright

    if choice1:
        if choice2:
            j "Nicely done! Of course I didn't expect any thing less from you!"
        else:
            j "You did good..."
    else:
        j "You did good..."

    show r smile

    if choice2:
        r "Thanks for the push! I really needed that."

        show j happy

        j "Of course! I've always got your back!"

        show j normal

        j "Just promise me you'll have more faith in yourself! Don't let what anyone else says get to ya!"

        show r smile

        r "Yeah...Thanks!"
    else:
        r "Thanks..."

    hide j
    hide r
    play music 'images/DarkWinds.mp3'
    scene beserk place
    with fade

    "Later that day..."

    show j confused
    with moveinleft

    j "Uh Robin?"
    j "Isn't that - Hazel?"

    show j confused at right
    with move
    show r notlistening at left
    with moveinleft

    r "Yeah, you're right!"

    show j happy

    j "Hey Hazel! Over here!"

    hide r
    with moveoutleft
    show j happy at left
    with move
    play music 'images/Soliloquy_0.p3.mp3'
    show h neutral
    with moveinright
    show b serious at right
    with moveinright

    h "Hmm?"

    show h happy

    h "Oh! Jayden, Robin."
    h "I'm glad you both are alright!"

    show j confused

    j "Woah! Who is this scary looking guy?"

    show b angry

    b "Hmph!"

    show j nervous
    show h sad

    j "Okay... Why are you with him anyway?"
    h "You see..."

    show h sadpout

    h "I lost a game to him."
    h "As per the wagers we made, I now have to be his follower and do what he says."

    show j normal
    show h neutral

    j "Ah! But why would you even agree to the game? I never thought of you as the kind of person to pick a fight with someone."
    h "He may not look like it, but he's really good at games."
    h "In fact, he's already collected 2 of the 7 gems."

    show h sadpout

    h "That's why I challenged him."
    h "I thought I could beat him and get those gems."

    show j happy

    j "Wow! 2 gems huh?"
    j "You must be pretty good!"

    show b serious

    b "Hmph!"

    show j normal

    j "Whatd'ya say to a little game?"
    j "If you win we'll give you the two gems we have collected and will be your followers too."
    j "If we win, you'll hand over your gems and be ours. How about it?"

    show b surprise

    b "You have gems?"

    show j nervous

    j "I said I did, didn't I? Here... See for yourself..."

    show b serious
    hide h
    with moveoutright

    b "Hmm..."
    b "Alright. I accept your challenge!"
    b "What game do you have in mind?"

    show j normal

    j "How about the ol\' Rock Paper Scissors?"

    show b smile

    b "That's the best you got?"

    show j nervous

    j "Relax! How about I make it a little more interesting for you?"

    show j normal
    show rps 0:
        xalign 0.45
        yalign 0.25

    j "I can only win this game if I play Paper."

    show b serious

    b "Hmm?"

    show rps 1

    j "But say I beat you with Rock or Scissors, you lose too. And so it ends up being a tie."

    show rps 2

    j "Again. If we both play Paper, it still ends up being a tie."

    show rps 3

    j "But if you can play anything besides paper you can acually win."

    show b angry

    b "Then what happens if we tie?"

    show j nervous

    j "Well...How about this?"
    j "If we tie, neither of us will be the other's followers."

    show j normal

    j "Instead, we'll join forces and work together to collect the remaining gems."

    show b serious

    b "Very well then. Let's do this."
    b "(I'm not going to fall for his tricks that easy.)"
    b "(I bet he's shooting for a tie, so he'll play either Rock or Scissors.)"

    show rps 4

    b "(If I play Rock, I have a 2/3 chance of winning.)"

    show rps 5

    b "(Same with Scissors, a 2/3 chance of winning.)"

    show rps 6

    b "(But if I play Papper, only a 1/3 chance.)"
    b "(So as long as I play Rock or Scissors, I should win.)"
    b "(But wait! Since he said that he can only win with Paper, he'll expect me to play Scissors.)"
    b "(But if I use Rock, he'd beat me with Scissors.)"
    b "(Hmm, let's see.)"

    show rps 7

    b "(If he chooses Paper, he'll risk a 1/3 chance of losing.)"

    show rps 8

    b "(But if he doesn't, he has a 2/3 chance of losing.)"
    b "(So he must choose Paper!)"

    hide rps

    j "Ready? 3...2...1..."

    show b happy
    show j happy
    show rock rps:
        xalign 0.3
        yalign 0.5
    show scissors rps:
        xalign 0.7
        yalign 0.5

    "..."

    show b surprise
    hide rock
    hide scissors

    b "No way! I lost!"

    show j nervous

    j "Hehe! Good try! But not good enough!"

    show j normal

    j "You probably thought I was trying to goad you into playing Rock."
    j "But you realized that I couldn't win unless I played paper, and so you chose Scissors."
    j "In this case, your best bet would have been Paper."

    show b angry

    b "But with Scissors, I could double my chances of winning!"

    show j happy

    j "Of course! That's how I knew you'd play Scissors."

    show b depressed

    b "Damn you! This sucks!"

    show b nervous

    b "But a deals a deal. I guess joining forces with you guys couldn't hurt."

    show j normal

    j "Awesome! Welcome to the pack!"

    hide j
    with moveoutleft
    show r neutral at left
    with moveinleft

    r "You too Hazel!"

    hide b
    show h happy at right
    show h at right
    with moveinright

    h "I'm so glad! Let's all work together and do our best!"

    show r smile

    r "Took the words right out of my mouth!"

    hide r
    hide h
    scene ravens nest
    play music 'images/DarkWinds.mp3'
    with fade

    "The next day..."

    show j confused
    with moveinleft

    j "Hmm... Let's see..."

    show j normal

    j "Yup! \"Raven\"s right up ahead. We're pretty close."

    show j normal at right
    with move
    show r annoyed at left
    with moveinleft

    r "Great! This walking is killing me!"

    show j nervous

    j "We are in a virtual world you know. We don't get tired here."

    show r uncaring

    r "Doesn't mean you don't get bored!"

    hide j
    hide r
    scene ravens nest
    with flashbulb
    play music 'images/No More Magic_3.mp3'
    show h scold
    with moveinleft

    h "Guys? What was that?"

    show h scold at right
    with move
    show r notlistening at left
    with moveinleft

    r "Wasn't that just like when we beat those tricksters?"

    hide h
    with moveoutright
    show j confused at right
    with moveinright

    j "Did look the same... Don't tell me someone beat us to the punch!"

    hide j
    with moveoutright
    show l condescending at right
    with moveinright

    l "Well if it isn't you guys!"

    show r uncaring

    r "Hmm? Lance?"

    show l angry

    l "So Hazel? Seems like you decided to stick with those losers huh?"

    hide r
    with moveoutleft
    show h sad at left
    with moveinleft

    h "Um..."

    hide h
    with moveoutleft
    show j angry at left
    with moveinleft

    j "Who are you calling losers! We have already collected 4 of the 7 gems you know!"
    l "Oh my! What a coincidence! I have the remaining 3."

    show l condescending

    l "Seems like it was meant to be a showdown between us."

    hide j
    with moveoutleft
    show r annoyed at left
    with moveinleft

    r "It doesn't have to be that way."

    show r notlistening

    r "We could team up and work together as we did before."

    show l annoyed

    l "And why exactly would I trust you?"
    l "It's not like you've been so forthcoming about who you are."

    show r angry

    r "It wasn't like that!"

    show l condescending

    l "Either way, if you want these gems, you'll have to beat me in a game."

    hide l
    with moveoutright
    show j angry at right
    with moveinright

    j "Fine by me. I'll take you on!"

    show r confused

    r "Jayden wait! Let me."

    show j confused

    j "Hmm? You sure?"

    show r neutral

    r "Yeah... This is something I gotta do..."
    r "I have to face up to Lance sooner or later."

    show j normal

    if choice1:
        if choice2:
            j "Well then I'll leave it you!"
            j "Show him who the real Robin is!"

            show r smile

            r "I will!"
        else:
            j "Well I hope you know what you're doing..."
    else:
        j "Well I hope you know what you're doing..."

    show j happy


    hide j
    with moveoutright

    r "So Lance? How does a game of Tic-Tac-Toe sound?"

    show l sly at right
    with moveinright

    l "It doesn't matter. No matter what game you pick, I will show you that I am better!"

    show r notlistening

    r "Although, I do propose a slight change in the game."
    r "How about instead of playing X\'s and O\'s, we both play X\'s?"

    show r uncaring

    r "And... The first one to make 3 X\'s in a row...Loses!"

    show l condescending

    l "Fine by me! I'll beat you no matter what! You can have the first move."

    show r smile
    show tictactoe 0:
        xalign 0.45
        yalign 0.2

    r "My pleasure!"

    show l neutral
    show tictactoe 1
    show r neutral

    r "..."

    show tictactoe 2

    l "..."

    show tictactoe 3

    r "..."

    show tictactoe 4

    l "..."

    show tictactoe 5
    show r smile

    r "And...That's game!"

    show l angry

    l "Hmph! You just got lucky, that's all."

    show l condescending

    l "You only won cuz I let you go first."

    show r notlistening

    r "Actually...No."
    r "I would have won either way."

    show r neutral

    r "You see, you lost the game the minute you agreed to the rules I set."
    r "It didn't matter if I went first or second."
    r "There was just one simple thing I needed to do."

    show tictactoe 1

    r "If I were first, I had to select the middle spot first."

    show r smile
    show tictactoe 6

    r "On the other hand, If I were to go second, I just had to avoid the middle spot throughout the game. Simple as that!"

    show l neutral

    l "Hmm... So you tricked me."

    show l smiling
    hide tictactoe

    l "Well, I guess you're not as bad as I thought..."
    l "Here. The gems are yours. I guess this is the end of the road for me huh?"

    show j happy
    with moveinright

    j "Not necessarily."

    show r notlistening

    r "Hmm?"

    show j normal

    j "I think there's a way to make sure no one dies."

    show r uncaring

    r "Really? How?"

    show j happy

    j "All we have to do is get Lance to join our team."

    show l neutral

    l "Me? But how would that help?"

    show j normal

    j "Remember what \"Sophocles\" said? \"Only the race of the team that acquires the Philospher's Stone shall live.\""

    show j happy

    j "If Lance joins our team, we'll have a member from each of the 5 races. And so if we get the stone, no one has to die!"

    show r neutral

    r "Oh! You're right!"
    r "Lance is a... well Lancer, Hazel is a Spellcaster, Nicholas is a Beserker, you're an Assassin and I'm an Archer. We'll have all 5!"

    show r smile

    r "This could work!"

    show j normal

    j "So whatd'ya say Lance? Will you join us?"

    show l smiling

    l "Hmm... I guess I don't have a choice, do I?"

    hide r
    with moveoutleft
    show h happy at left
    with moveinleft

    h "Yay! Welcome back Lance!"

    show j happy

    j "Alright! Let's win the whole thing! GO SOUL REAPERS!"

    hide j
    hide l
    hide h
    play music 'images/DarkWinds.mp3'
    scene pandoras place
    with fade
    "Back at the initial location..."

    show r smile at center
    with moveinleft

    r "We finally made it you guys!"

    show r smile at left
    with move
    show j nervous at right
    with moveinright
    show pandora box
    with moveinbottom

    j "Oh yeah! Let's open the box and get this over with already! It's been days since I've logged on to VRG. I can't let anyone swipe my no. 1 spot!"

    show r uncaring

    r "Geez! Is that your biggest concern right now?"

    hide j
    hide r
    with fade

    "The gems are put into the sides of the box."
    "The box opens"

    hide pandora

    play audio 'images/Sonic Boom-SoundBible.com-876321507.mp3'

    scene pandoras place
    with flashbulb

    play music 'images/Soliloquy_0.p3.mp3'
    show tg doubtful
    with moveinright

    tg "Well, well. I didn't expect any players to make it this far so quickly."

    show tg doubtful at left
    with move
    show j shocked at right
    with moveinright

    j "Wahh! Pandora's a guy?!"

    hide tg
    with moveoutleft
    show r angry at left
    with moveinleft
    show j confused

    r "It's not Pandora you doofus! It's \"Sophocles!\""

    show j nervous

    j "Oh! Yeah! For a minute there I was questioning my whole reality!"

    show r annoyed

    r "Idiot..."

    show r neutral at left

    r "So \"Sophocles!\" We made it here didn't we? Hand over the Philospher's Stone and let us leave this place already!"

    hide j
    with moveoutright
    show tg sadsmile at right
    with moveinright

    tg "Now now. You did't really think it'd be that simple, did you?"

    show tg sly

    tg "Of course, you have to beat me in a game first!"
    tg "So which one of you is up for the task?"

    hide tg
    with moveoutright
    show j happy at right
    with moveinright

    j "I vote Robin!"

    show h smile
    with moveinright

    h "Yes! I know you can do it Robin!"

    show r sad

    r "Wait, are you guys really sure about this?"
    r "Lance?"

    hide j
    with moveoutright
    hide h
    with moveoutright
    show l condescending at right
    with moveinright

    l "I wouldn't usually be the first one to let someone else have an opportunity like this."

    show l sly

    l "But back when we faced off in that game, you showed me what you are capable of."

    show l appoligetic

    l "I know I said a lot of mean stuff earlier, but I was wrong."
    l "Basing a person's abilities on the gender they identify with isn't right, but I did just that."

    show l smiling

    l "I know you can do this, so I'm just gonna cheer you on from the sidelines this once."

    show r smile

    r "Lance..."
    r "Thanks!"

    show r neutral

    r "Nicholas?"

    hide l
    with moveoutright
    show b serious at right
    with moveinright

    b "I know that I haven't known you guys for long, but my gut tells me that I can trust you."

    show b laugh

    b "So go ahead and win this!"

    show r smile

    r "You guys! I won't let you down!"

    hide b
    with moveoutright
    show tg sly at right
    with moveinright

    tg "Let's get started then, shall we?"

    show r notlistening

    r "What game are we gonna play?"

    show tg doubtful

    tg "Hmm... Let's see..."

    show tg normal

    tg "How about a classic? Like Connect-4? I'm sure you've played it before?"

    show r neutral

    r "I have. Mind if I take the first move?"

    show tg smile
    show connect 0:
        xalign 0.4
        yalign 0.5

    tg "Sure! It's not like I have anything to worry about."

    show r smile
    show connect 1

    r "Great! I'll start by placing my coin in the middle row."

    show tg normal
    show connect 2

    tg "Very well! I'll put mine on top of yours."

    show r neutral

    scene pandoras place
    with fade
    show tg normal at right
    show r neutral at left
    show connect 36:
        xalign 0.4
        yalign 0.5

    "35 moves later..."

    show connect 37

    r "Here's my move."

    show tg sadsmile
    show connect 38

    tg "Well, then I'll place my coin here."

    show r smile
    show connect 39

    r "Hehe! And check mate!"

    show r neutral

    r "There's only one row that's not filled, and so you have no other choice to put your coin there."

    show connect 40

    show r smile

    r "And when you do, I'll put a coin on it and get 4 in a row!"

    show tg doubtful

    tg "My my! Well played! And even after I gave it my all..."

    show r notlistening

    r "Actually, it had nothing to do with how you played."
    r "You see Connect-4 belongs to the class P-complexity. So it's already been mathematically solved."

    show r neutral
    show connect w

    r "Even if two experts face off against each other, the winner is always the one who goes first. At least as long as they place their coin in the center slot."
    r "If done right, the game will end within 41 moves!"

    show connect l
    show r notlistening

    r "If I were to start by placing my coin in one of the four corner slots, I would surely lose."

    show r neutral
    show connect d

    r "And if I were to place it in one of remaining two slots, the game would end in a draw."


    r "Matches like these are always decided before they start"

    show r smile
    hide connect

    r "So don't be too upset about it!"

    show tg sadsmile

    tg "Hmm..."
    tg "I was hoping to meet a challenger like you. And now I have..."
    tg "There's nothing more for me to do here..."

    show tg sadsmile at right
    with flashbulb
    show philospher stone:
        xalign 0.5
        yalign 0.5
    with moveinbottom

    tg "Take the Philsopher's Stone. You win."

    hide tg
    with moveoutright
    hide philospher
    with fade
    show j happy at right
    with moveinright
    play music 'images/the_kings_crowning_v1.mp3'

    j "Great job Robin!"

    show h happy
    with moveinright

    h "Yes! You were really good!"

    hide j
    with moveoutright
    show b laugh at right
    with moveinright

    b "I knew I was right to trust you!"

    hide h
    with moveoutright
    show l smiling
    with moveinright

    l "Indeed! That was a well played match! You suprise me even now."

    hide b
    with moveoutright
    hide r
    with moveoutleft
    hide l
    with moveoutright
    show j nervous at center
    with moveinleft

    j "Haha! Now that we can finally go home let me just say..."

    show j normal

    j "It's been a pleasure hanging out with you guys!"
    j "Sure we were stuck in here and all."

    show j happy

    j "But being with you guys made it a whole lot of fun!"

    show j happy at right
    with move
    show h happy at left
    with moveinleft

    h "I feel the same!"

    show h happy at center
    with move
    show r smile at left
    with moveinleft

    r "Hear. Hear."

    hide j
    with moveoutright
    hide h
    with moveoutright
    show b happy at right
    with moveinright

    b "Well. I'm off. Maybe I'll see you guys in another game some day!"

    show r smile

    r "I'm sure we will!"

    hide b
    with moveoutright
    show l smiling at right
    with moveinright

    l "It's time I leave too."

    show h smile
    with moveinright

    h "Yeah! Me too!"
    r "Goodbye guys! Thank you for everytghing!"

    hide l
    with moveoutright
    hide h
    with moveoutright
    show j nervous at right
    with moveinright

    j "So! I guess in the end it's just us as always huh?"

    show r notlistening

    r "And still it seems that's how it's always been..."

    show r neutral

    r "Thinking back I don't know if I would have been able to get this far if it weren't for you."

    show r dejected

    r "I'd probably still be hiding in that cave all this time..."

    show j normal

    j "Nah! Like I told you before, you gotta have more faith in yourself!"
    j "And stop worrying about what others think! Worry about what you do!"
    j "I believe if there's something you wanna do, you should do it! And if there's someone you wanna be, you should give your all for it!"

    show r smile

    r "I will! Thank you so much Jayden!"

    show j nervous

    j "No worries! Let's meet up after school tomorrow okay? After all we are still members of Void aren't we?"
    r "Always!"
    r "See you tomorrow!"

    hide j
    hide r
    scene black dark
    play music 'images/DarkWinds.mp3'
    with fade

    "."
    "..."

    show living room_day
    with fade
    show rb laugh
    play music 'images/the_kings_crowning_v1.mp3'

    r "And so when I returned home, I finally had enough courage to talk to my parents about me wanting to be a guy."
    r "They were pretty understanding about it."
    r "They even let me cut my hair short so that I could look more boy-ish."
    r "And as you can see, they even let me dress like a boy to school now-a-days."

    show rb surprised

    r "Wait... SCHOOL?"

    show rb awkward

    r "Crap! I'm totally late!"
    r "Maybe we can talk more some other time?"

    show rb laugh

    r "Great! See ya later then!"

    hide rb
    with moveoutright
    scene black dark
    with fade
    stop music

    "..."
    "Good Ending."

    jump credits

label choice2b:

    show j nervous

    j "You do this one. These matches are pretty boring I tell you."

    show r sad

    r "Wait, me?"

    show j happy

    j "Oh come on! I took the last one, didn't I? It's only fair."

    show r dejected

    r "Um... Alright..."

    hide j
    with moveoutright
    show e creepy at right
    with moveinright

    e "So you then?"
    e "Let's have a great time! I'll start with \"Sun!\""

    scene black dark
    with dissolve
    show e creepy at right
    show r dejected at left

    "It became dark."

    show r confused
    show candles item

    r "Hmm... Oh! So that's how it works... \"Candles?\""

    show flowers item
    show e smiling

    e "\"Flowers!\""

    show r sad
    show apples item:
        xalign 0.25
        yalign 1.0

    r "\"Um... Apples?\""

    show book item:
        xalign 0.75
        yalign 1.0

    e "\"Book!\""

    r "Um..."
    r "..."

    scene black dark
    with fade
    play music 'images/DarkWinds.mp3'
    show l annoyed at right
    with moveinright

    l "Geez! You're actually telling me you believe in stuff like that! Grow up! You're born a girl and so you are a girl. Stop pretending to be someone you're not! I can't believe we let someone like you in our guild!"

    show j angry at left
    with moveinleft

    j "Shut up Lance!"

    show l angry

    l "Why don't you make me?!"

    hide l
    hide j

    scene black dark
    with fade
    show candles item
    show apples item:
        xalign 0.25
        yalign 1.0
    show book item:
        xalign 0.75
        yalign 1.0
    show e smiling at right
    show r sad at left
    with fade
    play music 'images/Soliloquy_0.p3.mp3'
    show r dejected

    r "Ahh! No! I can't do this!"

    hide r
    with moveoutleft

    "Runs away..."

    show e assertive

    e "Huh?"

    scene cave inside
    with fade
    play music 'images/DarkWinds.mp3'

    "Back at the cave..."
    "..."

    show j shocked
    with moveinright

    j "Hey... Why did you just give up like that? That's totally not like you!"

    show j shocked at right
    with move
    show r sad at left
    with moveinleft

    r "I'm sorry..."

    show r dejected

    r "I just couldn't stop thinking about what Lance said earlier..."

    show r sad

    r "I just need some time..."

    show j sad

    j "Hmm..."

    show j normal

    j "Alright... Maybe we can give it another shot tomorrow."

    show r dejected

    r "..."

    scene cave inside
    with fade
    play music 'images/No More Magic_3.mp3'

    "The next day..."

    show j shocked
    with moveinright

    j "Hey! Big problem! \"Eris\" isn't at the lake anymore!"
    j "I guess someone must have already defeated her!"

    show j shocked at right
    with move
    show r dejected at left
    with moveinleft

    r "I'm sorry... It's all my fault..."

    show j sad

    j "Hmm... There's no point crying over spoilt milk..."

    show j normal

    j "Let's just move on to the next one - \"Raven.\""

    show r sad

    r "Yeah..."

    scene ravens nest
    with fade
    play music 'images/DarkWinds.mp3'

    "Near Raven's location..."
    "..."

    show j sad
    with moveinright

    j "You alright?"

    show j sad at right
    with move
    show r dejected at left
    with moveinleft

    r "I guess..."

    show j sad at right
    show r dejected at left
    with flashbulb
    show r confused

    r "What was that?!"

    show j shocked
    play music 'images/Soliloquy_0.p3.mp3'

    j "Hey! Wasn't that just like after I beat Puck?"
    j "Crap! Don't tell me someone already beat us to the gem!"

    hide j
    with moveoutright
    show l condescending at right
    with moveinright

    l "Well if it isn't you guys!"

    show r dejected

    r "Hmm? Lance!"

    show l sly

    l "Since you guys came this way, I'm guessing you're here to challenge \"Raven\"?"
    l "Do guys happen to have any of the gems on you?"

    hide r
    with moveoutleft
    show j sad at left
    with moveinleft

    j "We have the one from Puck..."

    show l condescending

    l "Great! Just the one I was looking for!"
    l "I have the remaining 6. So hand it over!"

    show j angry

    j "We can't just give it to you like that!"

    show l angry

    l "You mean you want to challenge me to game?"

    show l smiling

    l "Hah! Amusing!"
    l "But very well! I'll accept..."

    show l sly

    l "Only if Robin agrees to go up against me!"

    hide l
    with moveoutright
    show j angry at right
    with move
    show r confused at left
    with moveinleft

    r "M-me?!"

    show j sad

    j "Robin, please..."
    j "This is our last chance!"

    show r annoyed

    r "Um... Okay! I'll do it!"

    hide j
    with moveoutright
    show l smiling at right
    with moveinright

    l "Good! Now how does a game of Tic-Tac-Toe sound? I'm sure even you know what that is."

    show r sad

    r "Yeah..."

    show l condescending

    l "Although, I do propose a slight change in the game."

    show l smiling

    l "How about instead of playing X\'s and O\'s, we both play X\'x?"

    show l condescending

    l "And... The first one to make 3 X\'s in a row...Loses!"

    show r dejected

    r "Um... Okay..."

    show l smiling

    l "Alright then! Let's begin!"

    show tictactoe2 0:
        xalign 0.45
        yalign 0.2

    show l sly

    l "I'll let you have the first move."

    show tictactoe2 1

    r "..."

    show tictactoe2 2

    l "..."

    show tictactoe2 3

    r "..."

    show tictactoe2 4

    l "..."

    show tictactoe2 5

    r "..."

    show tictactoe2 6
    show l condescending

    l "And that's how it's done!"

    show l smiling

    l "I knew there was no way you could ever beat me! Hahaa!"

    show r annoyed

    r "Urgh..."

    show l smiling
    show l condescending
    hide tictactoe2

    l "Now hand over that gem!"

    hide r
    with moveoutleft
    show j angry at left
    with moveinleft

    j "Here..."

    show l sly

    l "Hahaa! Thank you!"

    show l condescending

    l "If you will, I'll now be on my way!"

    hide j
    with moveoutleft
    show r dejected at left
    with moveinleft

    r "..."

    hide r
    with moveoutleft
    show j confused at left
    with moveinleft

    j "Wait!"

    show j normal
    show j nervous

    j "Why don't we team up?"

    show l annoyed

    l "And why would I do such a thing?"

    show j normal

    j "Think about what Sophocles said earlier..."
    j "\"Only the race of the team that acquires the Philospher's Stone shall live.\""
    j "If the two of us join you, we'd have three of the five races."
    j "You can easily find players of the other two races as well and get them to join you."

    show j happy

    j "And then, when you find the stone, having members of all 5 races on your team, no one will have to die!"

    show j nervous

    j "That way, you'll be the hero who saves the day!"

    show l neutral

    l "Hmm... That does sound enticing..."

    show l condescending

    l "Very well then! I guess I'll let the two you hang around for now."

    show j happy

    j "Thanks!"

    hide j
    with moveoutleft
    show r dejected at left
    with moveinleft

    r "Um... Yeah... Thanks..."

    scene living room_alt
    show rb neutral
    with fade
    play music 'images/the_kings_crowning_v1.mp3'

    r "And so... Lance won the entire thing and everybody was saved!"
    r "Thanks to Jayden's quick thinking back then, we were able to return to the real world."

    show rb awkward

    r "After that, things were a bit rough."

    show rb upset

    r "I told my parents that I wanted to be a boy and they were, well surprised to put it lightly."
    r "For the next few days, there was a constant tension in our daily interactions."

    show rb neutral

    r "But on the other hand, Jayden starting being more supportive of me!"
    r "He said he felt guilty for not having my back during the games and that is was his fault the way things turned out."

    show rb awkward

    r "Of course I didn't think that!"

    show rb neutral

    r "But nevertheless, he still put in a lot of effort to help me."

    show rb laugh

    r "It was only thanks to him that I am now able to freely dress like a boy and even go to school like one!"

    show rb surprised

    r "Wait... SCHOOL?"

    show rb awkward

    r "Crap! I'm totally late!"
    r "Maybe we can talk more some other time?"

    show rb laugh

    r "Great! See ya later then!"

    hide rb
    with moveoutright
    scene black dark
    with fade
    stop music

    "..."
    "Bad Ending."

label credits:
    $ credits_speed = 25
    scene black
    show credits_image at Move((0.5,1.0),(0.5,-4.5),credits_speed,xanchor=0.5,yanchor=0)
    with Pause(credits_speed+10)

    # This ends the game.

    return
