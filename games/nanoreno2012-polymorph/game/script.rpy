# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

#Susan Sprites (oh god)

image Susan N = "SS/SN.png"
image side Susan neutral = "SS/SN.png"

image Susan SA = "SS/SA.png"
image side Susan angry = "SS/SA.png"

image Susan P = "SS/SP.png"
image side Susan puzzled = "SS/SP.png"

image Susan F = "SS/SF.png"
image side Susan frown = "SS/SF.png"

image Susan W1 = "SS/SW1.png"
image side Susan wat1 = "SS/SW1.png"

image Susan W2 = "SS/SW2.png"
image side Susan wat2 = "SS/SW2.png"

image Susan SH = "SS/SH.png"
image side Susan happy = "SS/SH.png"

image Susan S = "SS/SS.png"
image side Susan sad = "SS/SS.png"

image Susan VS = "SS/SVS.png"
image side Susan vsad = "SS/SVS.png"

image Susan SSP = "SS/SSP.png"
image side Susan surprised = "SS/SSP.png"

image Susan AY = "SS/SAY.png"
image side Susan annoyed = "SS/SAY.png"

image Susan VAY = "SS/SVAY.png"
image side Susan vannoyed = "SS/SVAY.png"

image Susan VA = "SS/SVA.png"
image side Susan vangry = "SS/SVA.png"

image Susan VH = "SS/SVH.png"
image side Susan vhappy = "SS/SVH.png"

#Mongoose Susan
image Susan MSAY = "SS/MSAY.png"
image side Susan msay = "SS/MSAY.png"

image Susan MSAN = "SS/MSAN.png"
image side Susan msan = "SS/MSAN.png"

image Susan MSH = "SS/MSH.png"
image side Susan msh = "SS/MSH.png"

image Susan MSN = "SS/MSN.png"
image side Susan msn = "SS/MSN.png"

image Susan MSS = "SS/MSS.png"
image side Susan mss = "SS/MSS.png"

image Susan MSSR = "SS/MSSR.png"
image side Susan mssr = "SS/MSSR.png"

image Susan MSVAN = "SS/MSVAN.png"
image side Susan msvan = "SS/MSVAN.png"

image Susan MSVS = "SS/MSVS.png"
image side Susan msvs = "SS/MSVS.png"

image Susan MSVSR = "SS/MSVSR.png"
image side Susan msvsr = "SS/MSVSR.png"

define s = Character("Susan", color="#000000", image="Susan")

#Derek Sprites
image dan = "DS/DAN.png"
image dam = "DS/DAM.png"
image day = "DS/DAY.png"
image dcs = "DS/DCS.png"
image dd = "DS/DD.png"
image dn = "DS/DN.png"
image dp = "DS/DP.png"
image ds = "DS/DS.png"
image dsur = "DS/DSUR.png"
image dvan = "DS/DVAN.png"
image dvn = "DS/DVN.png"
image dvp = "DS/DVP.png"
image dvsur = "DS/DVSUR.png"

image d2am = "DS/D2AM.png"
image d2an = "DS/D2AN.png"
image d2ay = "DS/D2AY.png"
image d2d = "DS/D2D.png"
image d2h = "DS/D2H.png"
image d2n = "DS/D2N.png"
image d2p = "DS/D2P.png"
image d2vn = "DS/D2VN.png"

#Becky sprites
image bam = "BS/Amused.png"
image bam2 = "BS/Amused2.png"
image bay = "BS/Annoyed.png"
image bd = "BS/Devious.png"
image bgla = "BS/Glare.png"
image bh = "BS/Happy.png"
image bheh = "BS/Heh.png"
image bheh2 = "BS/Heh2.png"
image bn = "BS/Neutral.png"
image boho = "BS/Oho.png"
image bp1 = "BS/Puzz.png"
image bp2 = "BS/Puzz2.png"
image bs = "BS/Sad.png"
image bs2 = "BS/Sad2.png"

#Candace Sprites
image can = "CS/Angry.png"
image cay = "CS/Annoyed.png"
image cc = "CS/Curious.png"
image cd = "CS/Devious.png"
image cp = "CS/Puzzled.png"
image cr = "CS/Rage.png"
image cvd = "CS/VDevious.png"

#BGs
image bg shack = "BGs/shack2.png"
image bg lr = "BGs/livingroom.png"
image bg lr2 = "BGs/livingroom2.png"
image bg dark = "BGs/darkbathroom.png"
image bg tv = "BGs/tv.png"
image bg street = "BGs/street.png"
image bg gate = "BGs/gate.png"
image bg bh = "BGs/house2.png"
image bg dine = "BGs/dine.png"
image bg st2 = "BGs/street3.png"
image bg rest = "BGs/restaurant.png"
image bg park = "BGs/park2.png"

#CGs
image cg ss = "CGs/SS.png"
image cg let = "CGs/The Letter2.png"
image cg dcg1 = "CGs/DCG1.png"
image cg dcg2 = "CGs/DCG2.png"
image cg dcg3 = "CGs/DCG3.png"
image cg dcg4 = "CGs/DCG4.png"
image cg dcg5 = "CGs/DCG5.png"
image cg dcg6 = "CGs/DCG6.png"
image cg dcg7 = "CGs/DCG7.png"
image cg dcg8 = "CGs/DCG8.png"
image cg dcg9 = "CGs/DCG9.png"

# Declare characters used by this game.
define d = Character('Derek', color="#000000")
#define s = Character('Susan', color="#000000")
define m = Character('Mom', color="#000000")
define b = Character('Becky', color="#000000")
define q = Character('???', color="#000000")
define c = Character('Candace', color="#000000")

# The game starts here.
label start:
   
    show bg shack with fade
    
    s neutral "..."
    
    s df "I looked at the building in front of me. It looked terrible."
    
    s df "Beyond terrible. I mean...this was a business, right?"
    
    s frown "(It looks as if it hasn't had any upkeep done on it in years...)"
    
    s df "I pulled out the old, faded letter I had."
    
    hide bg shack 
    
    show cg let with fade
    
    s df "My...former friend had given it to me a long time ago, because she knew I was concerned about supernatural things happening to me."
    
    s df "(It was not unfounded; my city was highly saturated in magic, which is uncommon for predominately human cities.)"
    
    s df "I peered at the letter and frowned heavily; I know this is the right address, but still..."
    
    s df "I shrugged. For all I knew it looked better on the inside."
    
    s dfl "(I folded the paper and put it away in my pocket.)"
    
    hide cg let
    
    show bg shack with fade
    
    s neutral "(Hm, no doorbell. Guess I'll just knock...)"
    
    "*KNOCK KNOCK*"
    
    s puzzled "..."
    
    s neutral "(Maybe that was too soft?)"
    
    s df "I knocked for a second time, when-"
    
    q "IT'S OPEN, DAMMIT!"
    
    s surprised "..."
    
    show bg lr with fade
    
    s df "Opening the door and walking inside, I noted that it really did look a lot better."
    
    s df "I glanced around to try to locate the voice I heard."
    
    s surprised "Uh, hello?"
    
    q "What is it?"
    
    s puzzled "Could you...could you come out so I can talk to you face to face?"
    
    q "Guh. FINE."
    
    #A wild Derek appears!
    
    stop music fadeout 5.0
    
    play music "Music/MP.ogg"
    
    show dn with dissolve
    
    q "Can I help you?"
    
    s surprised "Oh, um-! I-er-"
    
    hide dn
    
    show day
    
    q "Yes. I'm one of the Eared Ones."
    
    hide day
    
    show dan
    
    q "Yes I'm an adult, no I don't grow, no I'm NOT 'interested'."
    
    hide dan
    
    show dvan
    
    q "Call me cute and I'll bodily throw you out of here."
    
    hide dvan
    
    show dn
    
    q "Now. How can I help you?"
    
    s surprised "(...)"
    
    s neutral "Oh, um..."
    
    s puzzled "This...is this the Daly Insurance Agency?"
    
    hide dn
    
    show dvn
    
    q "Why? What do you want?"
    
    s sad "(I think I've gotten on his bad side already.)"
    
    s neutral "Ah, look. A couple of months ago I took out a policy in case I got cursed by a witch."
    
    s puzzled "And, well, I got cursed by a witch. I'd like to collect my money."
    
    hide dvn
    
    show dp
    
    q "Can you prove it?"
        
    #Mongoose!Susan
    
    show bg lr with fade
    
    s msn "..."
    
    s mss "Is that good?"
    
    hide dp
    
    show dsur
    
    q "...Is...are you a weasel?"
    
    hide dsur
    
    show dn
    
    s msan "MONGOOSE."
    
    #Normal!Susan
    
    show bg lr with fade
    
    s neutral "So as you can see, I've been cursed to turn into a mongoose."
    
    hide dn
    
    show dp
    
    d "...Why a mongoose?"
    
    s neutral "My fr-the witch who cursed me liked mongooses."
    
    d "That's not 'mongeese'?"
    
    s puzzled "Um, n-no?"
    
    hide dp
    
    show dn
    
    d "Whatever."
    
    hide dn
    
    show dp
    
    q "Last time I checked, that kind of magic generally made it so a person is, you know, ALWAYS an animal."
    
    s happy "Luckily for me, the witch who curse me is terrible at what she does."
    
    s vhappy "Now, about my money?"
    
    hide dp
    
    show dn
    
    q "Yeah...About that.... Okay, uh...you..."
    
    s puzzled "My name is Suzanna. You can call me Susan."
    
    d "Right; I'm Derek."
    
    d "But listen, Susie-"
    
    s vangry "SUSAN."
    
    hide dn 
    
    show dvn
    
    d "Whatever. Listen, Zanna-"
    
    s annoyed "(What's with this guy?)"
    
    d "-I can't pay you."
    
    s wat1"...What."
    
    hide dvn
    
    show dp
         
    d "I said I can't pay you; I don't have the money to."
    
    s wat2 "That 'what' was not me needing clarification."
    
    s wat1 "That 'what' was me expressing disbelief *that you can't pay me*."
    
    s vangry "Why? WHY can't you pay me? WHY don't you have the money??"
    
    hide dp
    
    show dn
    
    d "The thing is, I just took over this place for my friend's uncle."
    
    d "While I have his old clients, I don't have any money to actually pay anyone yet."
    
    s vsad "I-! But-! But what about the money I've been paying from *before* you took over?"
    
    hide dn
    
    show dvn
    
    d "My friend's uncle had a gambling problem."

    s wat2 "...I don't believe this."

    hide dvn
    
    show dn
    
    d "Well, don't feel bad. He's getting help for his addiction."
    
    s sad "That's great and all, but doesn't help me now."
    
    hide dn
    
    show dp
    
    d "What do you need the money for, anyway? Is it that big of a deal?"

    s vangry "It's a big deal because it's *owed* to me."
    
    s vsad "And I need it to pay my rent this month."
    
    hide dp
    
    show dvn
    
    d "Oh. That sucks."
    
    s angry "..."
    
    s angry "(Everything within me is being used to keep myself from turning into a mongoose and eating this guy's face.)"
    
    s neutral"(Okay, okay; deep breaths.)"
    
    s puzzled "Isn't there anything you can do?"
    
    hide dvn
    
    show dp
    
    d "I barely have enough money to keep myself alive, so that's a 'no'."
    
    s vannoyed "I really hate my life right now."
    
    hide dp
    
    show dn
    
    d "Mm."
    
    hide dn
    
    show dp
    
    d "There's no way you can find the witch you cursed you and have her change you back?"
    
    hide dp
    
    show dn
    
    d "It wouldn't solve your rent problem, but at least you wouldn't be, like, a weremongoose anymore."
    
    s neutral "I tried that. She refused."
    
    d "Did you call the cops?"
    
    s annoyed "It didn't help."
    
    hide dn
    
    show dp
    
    d "Did you call the MAGICAL cops?"
    
    s vannoyed "It. Didn't. Help."
    
    s annoyed "(I swear to god...)"
    
    s angry "This was an utter waste of time. I could've been job searching."
    
    hide dp
    
    show dn
    
    d "Tell you what. If you come back tomorrow, we can go to my friend's."
    
    s puzzled "Why?"
    
    d "She might be able to do something about your curse."
    
    s vhappy "Oh, really?!"
    
    hide dn
    
    show dvn
    
    d "I suppose time will tell."
    
    s sad"*sigh*"
    
    s neutral "Fine. I'll be here aroud 9; is that okay?"
    
    hide dvn
    
    show dp
    
    d "A.M. or P.M.?"
    
    s puzzled "...A.M....?"
    
    hide dp
    
    show dn
    
    d "That's fine, then."
    
    s puzzled "..."
    
    hide dn
    
    show dan
    
    q "...Shouldn't you be leaving now?"
    
    s angry "(Ugh, geez.)"
    
    hide dan
    
    stop music fadeout 5.0
    
    play music "Music/PK.ogg"
    
    show bg shack with fade
    
    s df "I sat on the ground and laid my head on my knees."
    
    s sad "This whole thing was a total bust."
    
    s df "I was stuck as a weremongoose."
    
    s df "I lost my job do to downsizing."
    
    s df "Now, I can't even pay my rent."
    
    s df "I heaved a sigh and stood back up."
    
    s df "Glancing back at the building, I frowned, then turned and trekked home."
    
    show bg lr2 with fade
    
    s df "When I got home, I threw myself onto the sofa and groaned."
    
    s sad "(So tired...Willingly turning into a mongoose is really hard.)"
    
    stop music fadeout 5.0
    
    show bg dark with fade
    
    s df "I closed my eyes."
        
    s df "And...zzz...."
    
    "*BRIIIIING! BRIIING*"
    
    show bg lr2 with fade
    
    play music "Music/SF.ogg"
    
    s vangry "GODDAMMIT!"
    
    s annoyed "(Whyyy...)"
    
    s df "I got up and answered the phone, intent on yelling at whoever was on the other line."
    
    s angry "*What*?"
    
    q "Don't you talk to me in that tone of voice."
    
    s df "...Or not."
    
    s sad "Oh. Sorry, Mom."
    
    m "Well?"
    
    s puzzled "Well, what?"
    
    m "Did you collect your money?"
    
    s df "I sighed and rolled my eyes, even though I know she couldn't see it."
    
    s puzzled "No, Mom. The agency changed hands and is completely broke."
    
    m "Oh. Well, that sucks."
    
    s wat2 "..."
    
    s annoyed "Thanks. Your concern is overwhelming"
    
    m "Don't be sarcastic, it's unladylike."
    
    s vangry "Unladylike, my A-!"
    
    m "Suzanna Hopkins!"
    
    s annoyed"(Why does God hate me today? Did I do something terrible and karma is biting me in the hindquarters?)"
    
    s annoyed "(Do I have to make a list of everyone I may or may not have wronged at some point and try to make amends just so-)"
    
    m "Susan, you're zoning out again."
    
    s sad "Sorry. I just...I have a lot on my mind."
    
    m "I could give you rent money the month. Will that help?"
    
    s sad "Yeah, but that doesn't solve my jobless...ness."
    
    m "Hopefully you can find something before then."
    
    m "If not, your dad and I will try to help you out, okay?"
    
    s sad "Yeah..."
    
    m "Mmkay. I'll talk to you later."
    
    s neutral "Tell Dad I said hi."
    
    m "I will."
    
    m "Oh, by the way. We've been having a bit of a mouse problem. Could you turn into a weasel and take care of that for us?"
    
    s angry "MONGOOSE. I turn into a MONGOOSE."
    
    m "Either way."
    
    s vangry "NO. And I'm hanging up now."
    
    m "Fine, fine. 'Bye."
    
    s annoyed"'Bye."
    
    s df "I hung up the phone, probably a bit harder than necessary."
    
    stop music fadeout 5.0
    
    show bg dark with fade
    
    s df "I lay back down and close my eyes again."
    
    s "..."
    
    s "......"
    
    s "........."
    
    show bg lr2 with fade
    
    play music "Music/SF.ogg"
    
    s annoyed "(Forget it. I'm not going back to sleep.)"
    
    s puzzled "(Meeeh...I guess I'll watch TV.)"
    
    show bg tv with fade
    
    s neutral "(Hm, let's see...)"
    
    s puzzled "(Some generic 'cute girls do cute things' anime...No...)"
    
    s neutral "(A crappy daytime talk show...Ugh, no...)"
    
    s puzzled "(A documentary about the second apocalypse...No...)"
    
    s neutral "(A terrible kids' movie...No...)"
    
    s puzzled "(A documentary about animal-eared people slavery...Possibly ironic, and no...)"
    
    s annoyed"(Ugh, 500 channels and there's nothing to watch.)"
    
    s puzzled "(Maybe I'll just go-)"
    
    "*RIIING RIIING*"
    
    s angry "Grrrr..."
    
    show bg lr2 with fade
    
    s df "I picked up the phone, hoping this would be the last call of the afternoon."
    
    s puzzled "Who is it?"
    
    stop music fadeout 5.0
    
    play music "Music/OM.ogg."
    
    q "Suuusaaan~"
    
    s vannoyed "Oh my god, it's *you*."
    
    q "Aw, is something wrong, Susan?"
    
    q "Do you not like your new found furry self?"
    
    s vangry "Candace, I swear to god..."
    
    c "Ah-ha-ha-ha~! Are you upset you couldn't get your money, Susan?"
    
    s vannoyed "Great. You're stalking me now?"
    
    c "Only because I find your pain amusing."
    
    s vangry"This isn't even so much PAINFUL as much as AGGRAVATING."
    
    c "WHICH MAKES IT WORSE! AH-HA-HA-HA!"
    
    s annoyed "...I'm hanging up."
    
    c "Don't you DARE-!"
    
    "*Click*"
    
    stop music fadeout 5.0
    
    play music "Music/SF.ogg"
    
    s happy "(Oops~)"
    
    s df "I laughed, then went to my bedroom, and laid down."
       
    s df "The rest of the afternoon, thankfully, passed uneventfully."
    
    stop music fadeout 5.0
    
    play music "Music/TV.ogg"
    
    show bg shack with fade
    
    s df "The next morning, I made sure to get up early enough to make it back to the insurance agency on time."
    
    s sad "(...Well, here I go again...)"
    
    "*KNOCK KNOCK*"
    
    d "WHO IS IT?!"
    
    s puzzled "Uh, it's me. Susan."
    
    d "...Yeah, you can come in."
    
    s annoyed "(Right.)"
    
    stop music fadeout 5.0
    
    play music "Music/MP.ogg"
    
    show bg lr with fade
    
    show dn
    
    d "I see you made it back."
    
    s neutral "Of course I did."
    
    s puzzled "By the way, do you answer all your customers like that?"
    
    d "Maybe I do."
    
    s neutral "That doesn't seem a very good way to do business."
    
    s puzzled "Maybe you could be less...confrontational?"
    
    hide dn
    
    show day
    
    d  "Maybe I have a legit reason for answering like that."
    
    s sad "Oh, w-well, I-"
    
    hide day
    
    show dn
    
    d "Whatever. You ready to go to Becky's?"
    
    s puzzled "Who?"
    
    d "My friend's name is Becky. Well, it's actually 'Rebecca', but no one calls her that."
    
    s happy "Ah. Should I call a cab or-?"
    
    hide dn
    
    show dvn
    
    d "We can just walk; she lives here in our area."
    
    s happy "Okay, great."
    
    hide dvn
    
    show dn
    
    d "Good. Shall we?"
    
    show bg street with fade
    
    d "-And it turns out, microwaving one of those things leaves a bloody mess."
    
    s annoyed "...There is something WRONG with you."
    
    hide dn
    
    show dvn
    
    d "You should've smelled it. It smelled like burnt sugar and mildew."
    
    s wat2 "Please stop."
    
    hide dvn
    
    show dn
    
    d "This is my thanks for trying to be coversational?"
    
    s annoyed "Oh, come on. That was just gross."
    
    d "You do better, then."
    
    s puzzled "It won't be hard."
    
    show bg street with fade
    
    s frown "-I didn't realize it was flammable."
    
    show dp
    
    d "You didn't read the container?"
    
    s puzzled "Do you?"
    
    hide dp
    
    show dn
    
    d "...Fair enough."
    
    s sad "It took forever for my eyebrows to grow back."
    
    s happy "Well? Was that better?"
    
    d "I wouldn't say that, exactly."
    
    d "Maybe it's less..."
    
    s puzzled "Horrifying?"
    
    hide dn
    
    show dvn
    
    d "I suppose you could put it that way."
    
    hide dvn
    
    show dp
    
    d "Here's Becky's house."
    
    show bg gate with fade
    
    hide dp
    
    show dn
    
    s puzzled "Her house is gated?"
        
    d "It keeps unwanted people out."
    
    s neutral "Yes, that's what gates are for."
    
    d "Yes, but it's done by magic. It's not even locked. Or closed."
    
    s df "He paused a moment, then pressed a button on the wall."
    
    "*BZZT!*"
    
    q "Who is it?"
    
    d "Derek. And the weasel woman."
    
    s vangry "MONGOOSE!"
    
    q "Alright, you can come on."
    
    q "I'll meet you outside."
    
    s puzzled "We aren't going in?"
    
    hide dn
    
    show dvn
    
    d "You'll have to take my word for it that it's best you don't go in there."
    
    show bg bh with fade
    
    s happy "Wow, this is one of the nicer houses in our area. It must've cost a fortune."
    
    d "Not really. The owners sold it relatively cheaply."
    
    s puzzled "Why?"
    
    hide dvn
    
    show dn
    
    d "There was a bad ghost infestation."
    
    s neutral "That would explain it."
    
    s puzzled "Wait. She's not bothered by the ghosts?"
    
    hide dn
    
    show dvn
    
    d "She got rid of them herself."
    
    s neutral "She can do that? That must be why she was willing to buy it, cheap or not."
    
    #Derp a derp, Becky here
    
    stop music fadeout 5.0
    
    play music "Music/KK.ogg"
    
    hide dvn
    
    show d2n at right with dissolve
    
    show bh at left with dissolve
    
    b "Hey there, I'm Becky!"
    
    hide bh
    
    show bp1 at left
    
    b "You are...?"
    
    s happy "Suzanna, but everyone calls me Susan."
    
    hide bp1
    
    show bh at left
    
    b "Pleased to meet you."
    
    b "Now, I heard you have a problem with-?"
    
    hide dvn
    
    show d2ay at right
    
    d "Nice to see you, too."
    
    hide bs
    
    show bp1 at left
    
    b "I see you nearly every day, Derek."
       
    b "I thought the greeting would be implied by now."
    
    hide d2ay
    
    show d2an at right
    
    d "You thought wrong."
    
    hide bp1
    
    show bp2 at left
    
    b "..."
    
    hide bp2
    
    show bgla at left
    
    b "It'd be regretful if I had to hurt you in front of someone I've just met."
    
    hide bgla
    
    hide d2an
    
    show d2n at right
     
    show bh at left
    
    b "So, then, Susan? You have a problem with a witch?"
    
    s sad "Yeah, she cursed me into a mongoose."
    
    hide bs
    
    show bp1 at left
    
    b "That's an odd animal choice."
    
    hide bp1
    
    show bn at left
    
    b "Do you mind it I use a spell on you to take a closer look?"
    
    s puzzled "Okay, I guess."
    
    hide bn
    
    show bh
    
    b "Lovely, this'll only take a moment."
    
    b "Derry, could you take a step over there?"
    
    hide d2n
    
    show d2vn at right
    
    d "Yeah, I'm moving."
        
    hide d2vn
   
    hide bh
    
    show bp1
   
    show bg bh with fade
     
    b "Oh, um..."
    
    b "Wow."
    
    s wat2 "I don't like that reaction."
    
    s puzzled "What? What is it?"
    
    hide bp1
    
    show bs
    
    b "I don't think I can undo this."
    
    s vsad "What?! B-but aren't you a professional witch?!"
    
    hide bay
    
    show bp1 
    
    b "'Mage', dear. 'Witch' is just for people that use magic to harm others."
    
    s sad "Oh, sorry!"
    
    s sad "But...why can't you fix it?"
    
    b "It's really complicated. The witch-"
    
    s sad "Candace."
    
    hide bp1
    
    show bh
    
    b "Candace. Right."
    
    hide bh
    
    show bp1
    
    b "I'm afraid Candace utterly messed up the spell."
    
    b "It's a confused mess, and it's totally tangled. The lines are everywhere."
    
    s puzzled "I don't...think I get it..."
    
    hide bp1
    
    hide bs
    
    show bp1 at left with dissolve
    
    show d2n at right with dissolve
    
    d "What REBECCA here is trying to say is that it's like a gigantic knot."
    
    hide d2n
    
    show dvn at right
    
    d "Even if she figured out where the spell began and ended, something of that magnitude would probably take years to undo."
    
    s puzzled "But what's so bad about that?"
    
    hide bp1
    
    show bp2 at left
    
    b "Derry, don't be obtuse."
    
    hide bp2
    
    show bp1 at left
    
    b "Derry-DEREK is right, but when he says it'll take years, it would be years only if I stayed there working on it, without pause, for years."
    
    s surprised "...!"
    
    s vsad "This is the worst week of my life."
    
    hide dvn
    
    show dp at right
    
    d "You never know, it could get worse."
    
    hide bp1
    
    show bgla at left
    
    b "DEREK!"
    
    hide dp
    
    show d2n at right
    
    d "What? It could. Things aren't as bad as they could be."
    
    hide d2n
    
    show d2vn at right
    
    d "She's a weremongoose, but she can control it, at least to some extent."
    
    hide d2vn
    
    show dp at right
    
    d "How's the rent situation?"
    
    s surprised "Oh!"
    
    s puzzled "My parents are going to help me, but-"
    
    hide dp
    
    show dvn at right
    
    d "There you go. It's not that bad."
    
    hide bgla
    
    show bp2 at left
    
    b "..."
    
    b "Derek, could you get something out my house for me?"
    
    hide dvn
    
    show d2p at right
    
    d "What?"
    
    b "You know where I keep my Artifacts, yes?"
    
    hide d2p
    
    show d2n at right
    
    d "Yeah."
    
    b "There's...a black medallion with swirly lines on it. Sort of like a hypnosis spiral."
    
    hide bp2
    
    hide bam
    
    hide bam2
    
    show bheh at left
    
    b "Could you get that for me, please?"
    
    hide d2n
    
    show d2vn at right
    
    d "Whatever."
    
    hide d2vn with dissolve
   
    hide bam2
    
    hide bheh
    
    show bam with dissolve
    
    b "..."
    
    s puzzled "......"
    
    b "........."
    
    s wat2 "WHAT?"
    
    hide bam2
    
    show bh
    
    b "It's just...Derry must like you."
    
    s puzzled "Well, I-Wait, why do you keep calling him 'Derry'?"
    
    b "It's just a nickname from when we were younger."
    
    s neutral "Oh. I guess you've known each other for a while, then?"
    
    hide bh
    
    show bam
    
    b "Mm-hm..."
    
    s puzzled "Uh...you said Derek must like me?"
    
    b "Mm-hm..."
    
    s puzzled "...Why? He's kind of...acerbic..."
    
    hide bam
    
    show bp1
    
    b "Oh, he's like that to nearly everyone."
    
    s puzzled "Then...why do you think he likes me?"
    
    hide bp1
    
    show bh
    
    b "He actually tried to make you feel better by saying that it's not that bad."
    
    s neutral "I would've thought you'd have said because he brought me to you."
    
    hide bs
    
    show bp1
    
    b "Not really. While I tend to charge highly, I don't do it to people who need my help but can't afford it."
    
    b "Even then, it helps to promote my services, so bringing you here benefits me more than you, I'd wager."
    
    s puzzled "I wouldn't think he'd get a crush on me that fast."
    
    hide bp1
    
    show bam
    
    b "I never said he had a crush on you."
    
    s puzzled "But, you just said..."
    
    b "Ah, what a world we live in when liking someone seems to automatically mean they must...LIKE you like you."
    
    s sad "Oh, I didn't mean-"
    
    b "That's it right there, I'm sure."
    
    s puzzled "...Uh?"
    
    b "You seem to be a genuinely apologetic and well-meaning person."
    
    hide bam
    
    show bs
    
    b "Unfortunately, Derek hasn't met very many people like that in his lifetime, human or otherwise."
    
    hide bs
    
    show bp1
    
    b "It probably doesn't help that he's...ah..."
    
    s puzzled "That he's...?"
    
    hide bp1
    
    show bn
    
    b "Well, he's an Empath."
    
    b "And...most of his life wasn't around, shall we say, the most pleasant of people."
    
    s surprised "Wow, that's...wow."
    
    s sad "He's not going to be angry you told me this?"
    
    hide bn
    
    show bam
    
    b "Even if he was, he usually doesn't stay angry for very long."
    
    hide bam
    
    show bs
    
    b "His emotions are...muted, nowadays."
    
    b "If he gets too emotional he risks-"
    
    d "I think I found it."
    
    hide bh
    
    hide bs
    
    show bn at left with dissolve
    
    show d2p at right with dissolve
    
    d "This is what you wanted, right?"
    
    hide bn
    
    show bh at left
    
    b "Yes, that's it."
    
    b "Susan, take this."
    
    b "I'll try to find an alternative way to undo your curse, but until then this should protect you from more."
    
    hide d2p
    
    show dn at right
    
    d "Barring the event Witch Girl suddenly becomes actually good at what she does and makes a curse stronger than the medallion."
    
    s happy "Thank you, Becky."
    
    hide dn
    
    show d2n at right
    
    b "It's nothing. Feel free to stop by any time, if you need anything before-"
    
    "*GRAAAR!!*"
    
    s surprised "The hell was that?!"
    
    hide bs
    
    show bay at left
    
    b "Ugh, did my shoggoth get loose again?"
    
    hide bay
    
    show bgla at left
    
    b "You weren't touching things you shouldn't be touching, were you Derry?"
    
    hide d2n
    
    show d2an at right
    
    d "Like I'd touch any of the creepy shit you keep lying around."
    
    s wat2 "...You have a shoggoth?"
    
    hide bgla
    
    show bh at left
    
    b "Yes; they're surprisingly good at chores."
    
    hide d2an
    
    show d2p at right
    
    "*CRASH!*"
    
    hide bh
    
    show bay at left
    
    b "Oh, my; I'm going to have go deal with this."
    
    hide bay 
    
    show bp1
    
    b "Very sorry I couldn't chat longer or show you both to the gate."
    
    hide bp1 with dissolve
    
    hide d2p
    
    hide dan
    
    show dvn with dissolve
    
    d "We should probably go."
    
    s sad "Probably."
    
    stop music fadeout 1.0
    
    play music "Music/MP.ogg"
    
    show bg lr with fade
    
    s sad "Well, this wasn't a complete bust, at least."
    
    d "Mm."
    
    s puzzled "(I wonder if what Becky said is true...I don't see why she'd lie, though...)"
    
    s puzzled "(He liked me? Really? And he was a-?)"
    
    hide dvn
    
    show dn
    
    d "Hey."
    
    s puzzled "Y-yeah?"
    
    hide dn
    
    show dvn
    
    d "You're zoning out."
    
    s annoyed "Ugh, I gotta stop doing that. People will begin to think I'm weird or something!"
    
    hide dvn
    
    show dp
    
    d "I've know you for like less than a day, and I can tell you that that ship has probably sailed."
    
    s angry "You're a terrible person."
    
    hide dp
    
    show dvn
    
    d "So I've heard."
    
    hide dvn
    
    show dn
    
    d "I'm ordering food. You can stay or leave; I don't care all that much either way."
    
    s puzzled "(Well...I don't get the feeling Becky would lie to me, so...)"
    
    s puzzled "If I stay, do I get food too?"
    
    d "You'd probably insult me if you didn't, so I guess."
    
    s happy "Then sure, I'll stay."
    
    hide dn with dissolve
    
    show bg dark with fade
    
    s df "So Derek and I sat down to eat lunch in the office, and it was surprising fun."
    
    s df "He ordered a pizza that was half pepperoni, half cheese. Also surprisingly, it turned out that he only ate fish (along with fruits, vegetables, that sort of thing)."
    
    s df "When I asked if it was because he had cat ears, he hit me in the face with a pillow."
       
    show cg dcg1 with fade
    
    d "-And that's when I realized sand worms don't make the best of pets."
    
    s puzzled "Large carniverous animals usually don't."
    
    show cg dcg3 with dissolve
    
    d "I blame Becky for leaving it there in it's cage."
    
    show cg dcg7 with dissolve
       
    d "Next to a teleportation spell."
    
    show cg dcg8 with dissolve
    
    d "It's like she was taunting me."
     
    show cg dcg9 with dissolve
    
    d "TAUNTING. ME."
    
    s puzzled "Dude, you gotta learn you some impulse control."
    
    show cg dcg4 with dissolve
    
    d "I have plenty impulse control."
    
    show cg dcg3 with dissolve
    
    d "For example, I didn't violently murder the complete stranger who walked up to me, grabbed my ears, and called me an 'adorable little kitty cat'."
    
    show cg dcg7 with dissolve
    
    d "And I wanted to."
    
    show cg dcg9 with dissolve
    
    d "Badly."
    
    show cg dcg1 with dissolve
    
    d "But I suppose at this point, it's just the way things are for me."
    
    s sad "That sounds...not very nice."
    
    show cg dcg2 with dissolve
    
    d "What, are you pitying me?"
    
    s surprised "N-no, I just-"
    
    show cg dcg4 with dissolve
    
    d "Relax. You're too high-strung."
    
    show cg dcg1 with dissolve
    
    d "As I said. It's the way things are. It happens."
    
    d "There's no point in getting upset anymore."
    
    s sad "..."
    
    show cg dcg2 with dissolve
    
    d "You know it's gotten kind of late right?"
    
    s surprised "Really?!"
    
    s annoyed "Crap, it is. It's not dark yet, but I should go on home."
    
    show cg dcg4 with dissolve
    
    d "Nah, just spend the night here."
    
    s surprised "Wha?!"
    
    show cg dcg1 with dissolve
    
    d "Mind you, there's only one bed, so I suppose we'll have to share."
    
    s wat2 "BUH-AH-WHA-!"
    
    d "..."
    
    show cg dcg3 with dissolve
    
    d "I'm joking."
    
    s sad "Oh, thank god."
    
    show cg dcg3 with dissolve
    
    d "I'll choose not to be insulted by that."
    
    show cg dcg1 with dissolve
    
    d "Also, that was a test."
    
    s puzzled "A test?"
    
    show cg dcg3 with dissolve
    
    d "Yeah."
    
    show cg dcg2 with dissolve
    
    d "We both know I look, what, eight? Nine? Ten at the most?"
    
    d "Not to mention we've known each other for less than two days?"
    
    show cg dcg9 with dissolve
    
    d "If you had said yes, I would have immediately kicked you out."
    
    show cg dcg1 with dissolve
    
    d "Congrats, you passed the test."
    
    show cg dcg3 with dissolve
    
    d "You're less creepy than about half of the people I deal with on a day to day basis."
    
    s puzzled "Uh...thanks...?"
    
    show cg dcg2 with dissolve
    
    d "Hm."
    
    show cg dcg1 with dissolve
    
    d "Well, 'bye, then."
    
    s annoyed "You're...something's wrong with you."
    
    show cg dcg3 with dissolve
    
    d "Yes, you've said that before. Don't be repetitive."
    
    s puzzled "*Sigh* Alright, alright."
    
    s happy "Thanks for introducing me to Becky."
    
    show cg dcg1 with dissolve
    
    d "Yeah."
    
    hide cg dcg1
   
    hide cg dcg2   
    
    hide cg dcg3
    
    hide cg dcg4
    
    hide cg dcg5
    
    hide cg dcg6
    
    hide cg dcg7
    
    hide cg dcg8
    
    hide cg dcg9
    
    show bg shack with fade
    
    s df "There was still plenty of daylight out. I considered going to the store to get a few things I was lacking, when-"
    
    s surprised "Oh!"
    
    s neutral "Huh. He actually said 'bye' to me."
    
    #Herp, new scene, if time permitting and god be willing
   
    stop music fadeout 5.0
    
    play music "Music/SF.ogg"
    
    show bg lr2 with fade
    
    s puzzled "I wonder if there's anything good on TV now..."
    
    "*RING RING*"
    
    s sad "(Man, nothing good seems to come out of me answering the phone. Maybe I should just ignore it.)"
    
    "*RING RING*"
    
    s sad "(Nope, not picking it up.)"
    
    "*RING RING*"
    
    s annoyed "(They'll just have to call back LATER.)"
    
    "*RING RING*"
    
    s angry "DAMN IT!"
    
    "*RI-*"
    
    s vangry "What?!"
    
    stop music fadeout 5.0
    
    play music "Music/OM.ogg"
    
    c "How rude of you, Susan."
    
    s annoyed "I am in no mood, Candace."
    
    c "Neither am I. You need someone else to solve your problems?"
    
    s vannoyed "I have no idea what you're on about."
    
    s annoyed "Get to the point or I hang up on you. Again."
    
    c "I'm talking about that MAGE you went to see."
    
    s df "I couldn't see her face, but I could just picture her face, pouting over the fact I may fix my 'condition'."
    
    s puzzled "Still stalking me, Candy Ass?"
    
    c "YOU ARE NEVER TO CALL ME THAT!"
    
    c "YOU KNOW HOW I FEEL ABOUT THAT NICKNAME!"
    
    s annoyed "You cursed me. I'll call you whatever I want."
    
    s puzzled "For example, I could call you a raging bi-."
    
    c "Don't you DARE!"
    
    s vannoyed "Uh, you called me, remember?"
    
    c "...Shut up, Susie."
    
    "*Click*"
    
    stop music fadeout 5.0
    
    play music "Music/SF.ogg"
    
    s happy "(Yeah, I figured you'd do that.)"
    
    s df "Candace never did tolerate bad language very well."
    
    s df "I flopped over on my sofa, using the TV as background noise as I read through help wanted ads."
    
    s sad "Bah, I'm either over qualified or under qualified."
    
    s df "Eventually, I just watched movies, played a few games, and went to bed."
    
    s df "Before going there, I remember wondering: when did my life become like this?"
    
    stop music fadeout 5.0
    
    show bg st2 with fade
    
    play music "Music/TV.ogg"
    
    s df "The next day, little after noon, I was walking down the street to get lunch when-"
    
    show dp with dissolve
    
    d "Going somewhere?"
    
    s surprised "AAH!"
    
    s vangry "Don't DO that?"
    
    stop music fadeout 5.0
    
    play music "Music/MP.ogg"
    
    hide dp
    
    show dn
    
    d "..."
    
    hide dn
    
    show dp
    
    d "Why do people ask if someone's going somewhere if they're clearly going somewhere?"
    
    hide dp
    
    show dn
    
    d "Better yet, why do people ask if someone's okay when they're obviously hurt?"
    
    s wat1 "Uh...?"
    
    d "So where are you going, then?"
    
    s puzzled "To go get something to eat."
    
    d "..."
    
    s neutral "......"
    
    hide dn
    
    show dvn
    
    d "........."
    
    s wat2 "WHAT?"
    
    hide dvn
    
    show dp
    
    d "I gave you dinner yesterday, and you can't even offer the same?"
    
    hide dp
    
    show dn
    
    d "You're parents must be ashamed over how terribly you turned out."
    
    s annoyed "Gee, thanks. I'm sure your parents feel the same."
    
    hide dn
    
    show dvn
    
    d "Shows how much you know; I don't have any."
    
    s df "ABORT! ABORT! BACK PEDAL!"
    
    s surprised "Er-!"
    
    d "Don't apologize, seriously."
    
    s wat2 "...I wasn't going to apologize."
    
    hide dvn
    
    show dp
    
    d "Yes, you were. Everyone does."
    
    hide dp
    
    show dn
    
    d "I was separated from my parents twenty years ago."
    
    hide dn
    
    show dvn
    
    d "Really, I'd have to be a bit unstable to never get over the loss my parents; I was a little kid when it happened."
    
    s happy "I guess that would be kind of...weird?"
    
    hide dvn
    
    show dn
    
    d "I know it may not seem like it, but I'm a bit more well-adjusted than that."
    
    hide dn
    
    show dp
    
    d "If you're going to get lunch, I know a cheap, half-way decent place we can go to."
    
    s puzzled "'We'?"
    
    hide dp
    
    show dan
    
    d "..."
    
    s surprised "Oh!"
    
    s happy "Of course; Derek, you should join me for lunch."
    
    hide dan
    
    show dn
    
    d "Well, if you insist."
    
    s happy "Sure. I INSIST."
    
    hide dn
    
    show dp
    
    d "Let's go, then; it's that-a-way."
    
    hide dp
    
    show bg rest with fade
    
    show dn with dissolve
    
    d "-Which is how I found out tooth paste in your eye burns like a mother."
    
    s puzzled "Even though you just told me what happened, I'm still confused as to how you accomplish something like that."
    
    hide dn
    
    show dvn
    
    d "Simple: first, you get a power drill."
    
    s puzzled "..."
    
    d "Next, you need a spork."
    
    s wat2 "How are those items even related?"
    
    d "Also, a step ladder is needed."
    
    s annoyed "Okay, you're yanking my chain."
    
    hide dvn
    
    show dp
    
    d "Then go home and try it."
    
    s neutral "...On second thought, I think I'll just take your word for it that that's how it happened."
    
    hide dp
    
    show dn
    
    d "You act like you think I'm weird or something."
    
    s annoyed "..."
    
    hide dn
    
    show dvn
    
    d "Right, well."
    
    d "Becky's just as bad."
    
    s puzzled "Somehow, I doubt that."
    
    d "Spend more time around her, you'll see."
    
    hide dvn
    
    show dp
    
    d "Her 'yes dear', 'thank you dear'?"
    
    hide dp
    
    show dn
    
    d "She doesn't really talk like that. At all."
    
    d "She's got a mouth that'd make a sailor blush."
    
    s puzzled "Really?"
    
    d "Really really."
    
    hide dn
    
    show dvn
    
    d "Here, I'll prove it right now."
    
    s df "Saying this, he took out a cell phone, and proceed to dial what I'm sure was Becky's number."
    
    s df "I heard a muffled 'hello?' from the other line, after which Derek immediatly hung up."
    
    s puzzled "Why-?"
    
    d "Just watch."
    
    s df "He proceeded to repeat what he did, calling, waiting for Becky to answer, then hanging up immediately."
    
    s df "After the third time, he sat the phone the table and waited."
    
    s sad "Derek, should you really be-?"
    
    "*~Da Da Da~*"
    
    s df "His phone rang. This time, he leaned over, hit speaker, and then answered."
    
    hide dvn
    
    show dp
    
    d "'Sup?"
    
    b "DON'T YOU 'SUP' ME, YOU ASSBITE!"
    
    b "STOP FUCKING CALLING ME AND HANGING UP WHEN I ANSWER!"
    
    d "Or what?"
    
    b "OR I'LL REACH THROUGH THIS DAMN PHONE AND STRANGLE YOU!"
    
    s surprised "Ah-!"
    
    b "...Did...you put me on speaker phone?"
    
    hide dp
    
    show dn
    
    d "Yep."
    
    b "...I hate you so much right now."
    
    b "Um, is that Susan?"
    
    s sad "Uh, yeah. It's me."
    
    b "...I'm sorry about my outburst. Please excuse my language."
    
    s puzzled "Er, right. No problem."
    
    b "Sorry for speaking to you at a time like this!"
    
    b "We'll have to talk again under better circumstances."
    
    s puzzled "Right. Okay."
    
    b "Great! I'm glad to here that. And, Derek?"
    
    hide dn
    
    show dp
    
    d "Mm?"
    
    b "We'll discuss this LATER."
    
    "*Click*"
    
    hide dp 
    
    show dn
    
    s df "She hung up. I stared at Derek, while he stared back with that same passive facial expression."
    
    s df "It was making me wonder if he did things like this to Becky often."
    
    s puzzled "You know if she punches you you kind of have it coming, right?"
       
    d "I can take a hit."
    
    hide dn
    
    show dvn
    
    d "And call it pay back for talking about my Empathy."
    
    s surprised "You know?!"
    
    d "I figured."
    
    d "I guess she thinks me being not a total asshole to someone is grounds for telling them about that."
    
    s sad "I'm sorry. I really don't want to be in your business or anything."
    
    hide dvn
    
    show dp
    
    d "Why not? Do you dislike me that much?"
    
    s surprised "No, I just-!"
    
    hide dp
    
    show dn
    
    d "I thought I told you you're too high-strung?"
    
    s puzzled "I..What?"
    
    d "NOW I'm yanking your chain."
    
    d "I'm not angry. Besides, I doubt Becky would have told you if she thought you'd freak and rat me out to Slavers or something."
    
    s surprised "What?! Why would I do that?!"
    
    hide dn
    
    show d2vn
    
    d "..."
    
    hide d2vn
    
    show dp
    
    d "There's a park near here. Want to go there?"
    
    s df "It dawned on me there might be more to his Empathy than he let on."
    
    s df "Sure, the cat ears could be a reason to kidnap him, but that usually doesn't happen nowadays."
    
    s df "Still. I wouldn't press the issue."
    
    s happy "Do you mean Laymen's Park? That's right behind my house!"
    
    hide dp
    
    show dn
    
    d "Convienent. Do you want to go?"
    
    s happy "Sure. Let me pay the bill first."
    
    s df "After paying, we headed towards to the park."
    
    hide dn
    
    stop music fadeout 5.0
       
    show bg park with fade
    
    play music "Music/TV.ogg"
    
    s happy "Isn't it funny how our part of the city is?"
      
    show dp with dissolve
    
    d "How so?"
    
    s neutral "Well, it's really small, for one."
    
    s neutral "Dog Town would take you about two hours to walk from one side to the other."
    
    s happy "But here, walking from one side to the other only takes, what, thirty minutes?"
    
    d "I imagine how fast you walk is a factor."
    
    s neutral "True."
    
    s happy "But I like how quiet it is here."
    
    hide dp
    
    show dn
    
    d "Mm."
    
    s neutral "Oh, yeah. That's my house, right over there."
    
    s happy "Your office is-"
    
    hide dp
    
    show dn
    
    d "Right around the corner, practically."
    
    hide dn
    
    show dp
    
    d "Have you always lived here?"
    
    s puzzled "No, I moved here about three years ago."
    
    s neutral "I would take the bus to my job, since it was about a twenty minute drive."
    
    s sad "Well, until I lost it, that is."
    
    hide dp
    
    show dn
    
    d "..."
    
    hide dn
    
    show dvn
    
    d "You never said why you got cursed, especially since you apparently know the witch that did it."
    
    s vsad "Oh. That. I didn't think it mattered."
    
    s sad "We both worked in the same place, but I got a job position she wanted."
    
    s sad "She didn't take the news well. She said I was a horrible friend for taking it, and cursed me."
    
    hide dvn
    
    show dp
    
    d "You used to be friends?"
    
    s vsad "'Used to be' is putting it mildly."
    
    s annoyed "I didn't even know she wanted that job."
    
    s annoyed "It's weird; thinking about it makes me sad and angry at the same time."
    
    hide dp
    
    show dn
    
    d "Well, if she runs around cursing people over things like that, it's probably best to not be friends with her."
    
    s annoyed "Probably. I just-"
    
    show bg park with fade
    
    stop music fadeout 5.0
    
    play music "Music/MP.ogg"
    
    s mssr "Wha-?"
    
    s msvan "ARGH!"
    
    hide dn
    
    show dp
    
    d "Back to being a weasel, huh?"
    
    hide dp
    
    show dn
    
    s msvan "Mon-!"
    
    s msay "You know what? Forget it."
    
    s mss "I should just go home. Can't do anything like this."
    
    hide dn
    
    show dp
    
    d "You want I should walk you over there?"
    
    s msn "Nah, it's just across the road, and I have the sense to watch for cars."
    
    hide dp
    
    show dn
    
    d "Mm. I'll probably stay here a bit; I don't feel like going home."
    
    s msh "Enjoy yourself; this is a rather nice park."
    
    s mssr "Crap!"
    
    s mss "I just realized I should've given Becky my number or gotten her's."
    
    hide dn
    
    show dvn
    
    d "Just give it to me, and I'll forward it."
    
    s msh "Oh, thanks!"
    
    show bg park with fade
    
    s "-Got that?"
    
    hide dvn
    
    show dn
    
    d "It's in my phone. I'll call you if something comes up with the money, though I doubt it."
    
    s msay "My luck is terrible, so I doubt it too."
    
    s msh "'Bye, Derek."
    
    hide dn
    
    show dvn
    
    d "'Later."
    
    hide dvn  
        
    #Derp, new scene ends here
    
    stop music fadeout 5.0
    
    show bg lr2 with fade
    
    play music "Music/SF.ogg"
    
    s msh "Man, good thing I never uninstalled that doggy door."
    
    q "Hee hee~ Poor Susan has to crawl through dog doors."
    
    q "That must be so EMBARRASSING~"
    
    s mssr "Who-?"
    
    #A while Candace appears! She uses Breaking and Entering! It's super effective!
    
    stop music fadeout 5.0
    
    play music "Music/OM.ogg"
    
    show cc with dissolve
    
    c "Hello, Suzanna."
    
    s msvsr "GAH!"
    
    s msvan "...Fucking A."
    
    hide cc
    
    show cp
    
    c "Now, now, Susan. Didn't your mom ever tell you young women shouldn't curse? It's unladylike."
    
    s msay "..."
    
    s msan "What are you doing in my house?"
    
    hide cp
    
    show cd
    
    c "I just wanted to say hi to my friend; nothing wrong with that."
    
    s msan "First of all, we aren't friends."
    
    s msvan "Second: GET OUT."
    
    hide cd
    
    show cay
    
    c "I don't think I like your tone, Susan."
    
    c "Maybe you should speak to me a bit more calmly."
    
    hide cay
    
    show bg dark with fade
    
    s df "Part of my brain said, 'Let it go, Susan; she'll get bored and wander off'."
    
    s df "But at that point...I really didn't care anymore."
    
    s df "She put a curse on me, because of a stupid job."
    
    s df "I knew she was ambitious, but this was too far, and under the circumstances, I'd been shockingly nice  about the whole thing."
    
    s df "I didn't want to be nice anymore."
    
    show bg lr2 with fade
    
    show cd
    
    s msay "You know what, Candace? You're a real asshole."
    
    hide cd
    
    show cay
    
    c "WHAT?!"
    
    s msan "You heard me: you're an asshole."
    
    stop music fadeout 5.0
    
    play music "Music/PK.ogg"
    
    s  msay "Maybe part of me thought if I'd just be patient and ignored you for the most part, it would..."
    
    s mss "I don't know, somehow FIX itself."
    
    s msvs "It being...us? We used to friends."
    
    s msay "And I apologized for the fact I got the job. I apologized when I didn't do anything wrong."
    
    s msn"I know that magic can...TAINT you, and change who you are if you misuse it, but I don't think that's the problem."
    
    s mss "Now, I think that you just have a flawed personality."
    
    s mss "And maybe you always did."
    
    hide cay
    
    show can
    
    c "...!"
    
    s msan "I don't care if you remove the curse. I don't care if I'm stuck as weremongoose."
    
    s msvan "I like you better when you're far away, so it'd be best if you stayed as far from me as possible."
    
    s df "And Candace stared at me in shock, as if she couldn't believe I had the adacity to tell her off."
    
    s df "Then her face twisted into something dark and malignant, looking the angriest I'd ever seen her."
    
    s df "But still. I had come this far and I refused to back down."
    
    hide can
    
    stop music fadeout 5.0
    
    play music "Music/WYW.ogg"
    
    show cr
    
    c "How DARE you talk to me that way, you-! You-!"
    
    c "ARGH!!"
    
    s msvsr "*HURK!*"
    
    hide cr
    
    hide cr
    
    show cg ss with fade
    
    s df "Can't...breathe...strangling..."
    
    c "Oh, I'm sorry? Does that hurt?"
    
    s df "*HACK!*"
    
    c "Oh, is THAT too tight? By all means, tell me if it is!"
    
    s df "*URGH*"
    
    c "It isn't? I suppose I can tighten it a bit more then~!"
    
    q "Don't make stab you in your creepy-ass eyes."
    
    c "Who-?!"
 
    hide cg ss
    
    show bg lr2 with fade
    
    "*THUD*"
    
    s msvsr "*GASP*!"
    
    s mss "(She..hah..dropped me. Whew.)"
    
    s msn "(Wait.)"
    
    s mssr "Derek?! What are you doing here?!"
    
    show cay at left with dissolve
    
    show dp at right with dissolve
    
    d "That's an ungrateful reaction."
    
    s msvan "She's going to kill you, you idiot!"
    
    hide dp
    
    show dn at right
    
    d "It's cool, I got this."
    
    c "You need a man to save you? What a loser."
    
    hide dn
    
    show d2vn at right
    
    d "Oh, I'm not going to fight you."
    
    hide cay
    
    show cp at left
    
    c "Really now?"
    
    d "Nope. My parents, rest in peace, raised me to never hurt a girl."
    
    d "That sort of thing sticks with you."
    
    s mssr "Oh my god, we're so screwed."
    
    hide cp 
    
    show cvd at left
    
    c "Yes, you are. His misplaced chivalry is going to get the both of you killed."
    
    hide d2vn
    
    show d2n at right
    
    d "Mm."
    
    d "No."
    
    hide cvd
    
    show cp at left
    
    c "No?"
    
    d "I said *I* wasn't going to hurt you; I didn't say no one else wouldn't."
    
    c "What are you talking about, you blue weirdo?"
    
    d "I have a Girl Hitter."
    
    c "A what?"
    
    s mss "(I think I can see where this is going...)"
    
    hide cp
    
    show cp
    
    show bgla at left with dissolve
       
    b "He said a 'Girl Hitter', witch."
    
    hide cp
    
    show cay
    
    c "Wha-"
    
    hide cay
    
    s df "I'm pretty sure she had no idea what hit her."
    
    s df "In that moment, the floor boards burst up and, like weird snakes, wrapped around Candace's body, knocking her to the floor."
    
    c "You BITCH! This isn't over!"
    
    b "No, dear, I'm afraid it is."
    
    c "Rrrggh!!"
    
    "*CRACK!*"
    
    hide d2n
    
    show d2p at right
    
    d "Damn, she can use her hair to slice the boards?"
    
    hide bgla
    
    show bp1 at left
    
    b "Apparently so."
    
    show cr with dissolve
    
    hide bp1
    
    show bs at left
    
    hide d2p
    
    show d2ay at right
              
    b "Candace, please stand down. No one here wants to hurt you."
    
    c "YOU'RE the one who's getting hurt!"
    
    hide bs
    
    show bay at left
    
    b "*Sigh* If you have to have it that way."
    
    b "Come at me, then."
    
    hide bay with fade
    
    hide cr with fade
    
    hide d2ay
    
    s msvsr "(Ack, what is she doing?!)"
    
    #Derek is in front of Susan here, alone
    
    show dp with dissolve
    
    d "Do you have anything flammable?"
    
    s mssr "What? Why?! And why aren't you helping Becky?!"
    
    hide dp
    
    show dn
        
    d "Becky'll be fine."
    
    s mssr "But-!"
    
    hide dn
    
    show dvn
    
    d "She'll be fine. She'll try not to tear up this house, though."
    
    d "Listen, get something flammable. We'll set her hair on fire; that should stop her."
    
    s mssr "But she sliced through boards with it!"
    
    hide dvn
    
    show dp
    
    d "It seems sharp; it might not be all that strong."
    
    d "She may have held you up in the air with it, but in your current body, you weigh, what? Five or ten pounds?"
    
    hide dp
    
    show dvn
    
    d "I'll help Becky to keep Witch Girl distracted. Get some hair spray or something, and matches."
    
    s mss "But, I...I can't hold anything."
    
    hide dvn
    
    show dn
    
    d "Sure you can. Just change back."
    
    s msvan "I CAN'T! I'm a bit too stressed to concentrate. Nearly being murdered kind of does that to you."
    
    hide dn
    
    show dp
    
    d "Do you want to help Becky end this quickly or not? Do you want to risk Becky getting injured?"
    
    s mss "No, but-"
    
    d "Do you want to risk Becky tearing the house up trying to stop her?"
    
    s mss "..."
    
    hide dp
    
    show bg dark with fade
    
    s df "I closed my eyes, trying hard to change myself back."
    
    s msay "(Mmm...okay, concentrate)"
    
    s df "I could hear the sound of Candace's hair whipping against the barrier Becky had up."
    
    s mssr "(Ugh, this isn't working. Okay, breathe.)"
    
    s df "I thought about Derek, who started acting a bit nicer."
    
    s df "And I thought about Becky doing her best to not go overboard or get hurt."
    
    s df "Finally, I thought about Candace, and how we used to be best friends."
    
    s df "And how, honestly, I wished we still were."
    
    show bg lr2 with fade
    
    s happy "WOO!"
    
    show dvn
    
    d "Great. Go get your flammable whatever, I'll help Becky."
    
    hide dvn with dissolve
    
    s surprised "W-wait-"
    
    s annoyed "(Dammit, he's gone.)"
    
    s surprised "(Oh! Right!)"
    
    show bg dine with fade
    
    s vsad "Come on, where is it?"
    
    s df "I looked frantically around the dining/kitchen area, for anything that would work."
    
    s vannoyed "UGH, where is my-?!"
    
    s happy "AHA!"
    
    s df "I grabbed a can of bug spray and a lighter, then sprinted back out."
    
    show bg lr2 with fade
    
    s surprised "(Crap!)"
    
    s df "Now both Becky and Derek were behind the shield."
    
    s df "Neither looked hurt; Becky looked severely annoyed, while Derek looked about the same."
    
    s df "I snuck closer to Candace from behind (making to sure to keep my items hidden), to get her attention."
    
    s happy "Hey, Candy~"
    
    show cr
    
    c "What?!"
    
    hide cr
    
    show cay
    
    c "Oh, right. It's you."
    
    s sad "Candace, why don't you just leave? Don't you think you're, well, overreacting?"
    
    s vsad "It might not end well if you don't calm down."
    
    hide cay
    
    show can
    
    c "Overreacting? OVERREACTING?!"
    
    hide can
    
    show cr
    
    c "AND DON'T TELL ME TO CALM DOWN!"
    
    s df "That was it. She whipped her hair towards me, when-"
    
    "*FWSH!*"
    
    hide cr with dissolve
    
    c "AAAHHH! My HAIR! My hair's on fire!"
    
    s sad "Warned you."
    
    s df "Candace fell the floor, swatting at her hair and screaming at the top of her lungs."
    
    s sad "Uh, Becky, could you...?"
    
    show bs with dissolve
    
    b "I'll put her out."
    
    stop music fadeout 5.0
    
    play music "Music/SF.ogg"
    
    hide bs with dissolve
    
    s df "Saying so, she did. Moments later, Candace was sitting tied up on the (partially ruined) floor, looking shocked."
    
    s sad "Are you okay, Candace?"
    
    c "You ask me that after setting me on fire?"
    
    s puzzled "Well, just your hair, and Becky put it out before it spread too far."
    
    s annoyed "And don't try to sound like the victim when you tried to strangle me."
    
    c "I wasn't going to kill you or anything; not really."
    
    s puzzled "I couldn't tell."
    
    c "I was...I was upset. Maybe I did overreact."
    
    c "Okay, I did. I freaked out."
    
    s neutral "At least you admit it."
    
    s puzzled "Wait, why are you admitting it?"
    
    show bp1 with dissolve
    
    b "Ah. I suspect her hair was the source of her power, and probably feeding on her anger, exascerbating the problem."
    
    hide bp1
    
    show bn
    
    b "Cutting it off seems to have mellowed her out."
    
    c "Do you have to call the Magic Cops, then? I mean, my hair..."
    
    hide bn
    
    show bay
    
    b "Dear, I said PROBABLY. Either way, it doesn't magically free you from taking responsibility from your actions."
    
    hide bay
    
    show bp1
    
    b "...No pun intended."
    
    s df "After that, Candace didn't say anything else, and just sat there scowling."
    
    hide bp1
    
    show bn at left with dissolve
    
    show dn at right with dissolve
    
    d "The cops should be here pretty soon."
    
    s neutral "Right. Thanks, Derek."
    
    s puzzled "By the way, how did you know I was in trouble?"
    
    d "Oh. That. You know I'm a..."
    
    hide dn
    
    show d2vn at right
    
    s df "I'm sure he was about to say 'Empath', but he slide his eyes toward Candace, then continued on."
    
    hide d2vn

    show dn at right
    
    d "A you-know-what."
    
    s puzzled "Yeah."
    
    d "I was still in the park when I felt you were in trouble."
    
    d "I called becky and she teleported over."
    
    s puzzled "She doesn't need to see where she's going?"
    
    hide bn
       
    show bam at left
    
    show d2n at right
    
    b "Well, I do and I don't."
    
    s puzzled "I still don't get it."
    
    hide d2n
    
    show dn at right
    
    d "We''ll explain it to you later."
    
    d "Once the cops get Psycho Chick-"
    
    c "CANDACE!"
    
    hide dn
    
    show dvn at right
    
    d "Whatever. After they come to get her, we can talk about it."
    
    s puzzled "Is that okay with you, Becky?"
    
    hide bam
    
    show bh at left
    
    hide dvn
    
    show d2n at right
    
    b "Of course!"
      
    b "Oh, isn't this great! We're all getting along swimmingly!"
    
    hide bh
    
    show bp1 at left
    
    b "Not really speaking of which, Susan. Would you like to work for me?"
    
    s surprised "Wha-? Really? But I don't use magic or anything!"
    
    b "No, but you did keep a relatively calm head during the situation."
    
    hide bp1
    
    show bn at left
    
    b "Besides, I need an assistant."
    
    hide d2n
    
    show dvn at right
    
    d "Don't listen to her, she'll make you do all the crap she doesn't want to do."
    
    hide bn
    
    show bgla at left
    
    b "Shut the hell up, Derek."
    
    hide bvn
    
    show d2ay at right
    
    hide bgla
    
    show bp1 at left
    
    b "*Ahem* So what do you think?"
    
    hide d2ay
    
    show dvn at right
    
    s puzzled "Well..."
    
    s happy "Yeah, I think I'd like that."
    
    s puzzled "I get paid, right?"
    
    hide bp1
    
    show bh at left
    
    hide dvn at right
    
    show d2n at right
    
    b "Of course. It should be enough to cover your rent."
    
    s happy "Then yeah, I'd love that."
    
    hide bh
    
    hide d2n
    
    show bg dark with fade
    
    s df "So that was then end of that."
    
    s df "It had been kind of chaotic series of events, and hard to believe they happened over only a couple of days."
    
    s df "I met Becky, a wi-no, MAGE, who was unfailingly polite (usually), and was very helpful."
      
    s df "And I met Derek, who was kind of a jerk, but did make the effort to be nicer."
    
    s df "While I may have lost one friend, at least I got two new ones."
    
    stop music fadeout 1.0
    
    return
