# BACKGROUNDS
image bg bgbonus = "bgbonus.png"
image bg room = "room.jpg"
image bg pond = "pond.jpg"
image bg field = "field.jpg"
image bg hallway = "hallway.png"
# MILICENT
image mi mi = "mi.png"
image mi pi = "mipi.png"
image mi pi2 = "mipi2.png"
image mi ma = "mima.png"
image mi ma2 = "mima2.png"
image mi wo = "miwo.png"
image mi pro = "mipro.png"
image mi sh = "mish.png"
image mi sh2 = "mish2.png"
image mi sho = "misho.png"
image mi sho2 = "misho2.png"
image mi wha = "miwha.png"
image mi sly = "misly.png"
image mi sad = "misad.png"
#MAE
image ma ma = "ma.png"
image ma oh = "maoh.png"
image ma sly = "masly.png"
image ma po = "mapo.png"
image ma po2 = "mapo2.png"
image ma shy = "mashy.png"
image ma sad = "masad.png"
image ma gl = "magl.png"
image ma se = "mase.png"
#CGs
image cg miwo1 = "miwo1.jpg"
image cg miwo2 = "miwo2.jpg"
image cg pond11 = "pond11.jpg"
image cg pond12 = "pond12.jpg"
image cg pond13 = "pond13.jpg"
image cg pond2-1 = "pond2-1.jpg"
image cg pond2-2 = "pond2-2.jpg"
image cg pond2-3 = "pond2-3.jpg"
image cg maeappearance = "maeappearance.jpg"
image cg miliceattacksmae = "miliceattacksmae.jpg" 
#using show miliceattacksmae:
#xpos 0 ypos -800 xanchor 0 yanchor 0
#linear 5.0 xpos -1140 ypos 0
image cg joisan = "joisan.jpg"
#
image cg maeflashback1 = "maeflashback1.jpg"
image cg maeflashback2 = "maeflashback2.jpg"
image cg maeflashback31 = "maeflashback31.jpg"
image cg maeflashback32 = "maeflashback32.jpg"
image cg maeflashback4 = "maeflashback4.jpg"
#
image cg memorychamber = "memorychamber.jpg"
#using show memorychamber:
#xpos 0 ypos -800 xanchor 0 yanchor 0
#linear 5.0 xpos -1025 ypos 0
image cg maememory = "maememory.jpg"
image cg mimamemory1 = "mimamemory1.jpg"
image cg mimamemory2 = "mimamemory2.jpg"
image cg mimamemory3 = "mimamemory3.jpg"
image cg mimamemory4 = "mimamemory4.jpg"
#
image epilogue11 = "epilogue11.jpg"
image epilogue12 = "epilogue12.jpg"
image epilogue21 = "epilogue21.jpg"
image epilogue22 = "epilogue22.jpg"
#SPLASHIIES
image sp splash1 = "splash1.png"
image sp splash2 = "splash2.png"
image sp splash3 = "splash3.png"
# Declare characters used by this game.
define mi = Character('Milice')
define vo = Character('??')
define m = Character('\"Mae\"')
define gi = Character('Girl')
define gh = Character('Daena')
define si = Character('Sirius')
#
define nvlx = Character(None, kind=nvl)
define nvlvo  = Character('Voice', kind=nvl)
define nvlmi  = Character('Milice', kind=nvl)
define nvlma = Character('Mae', kind=nvl)
define nvlm = Character('\"Mae\"', kind=nvl)
define nvlgi = Character('Girl', kind=nvl)
#transform mam:
#    xpos 0 ypos -800 xanchor 0 yanchor 0
#    linear 5.0 xpos -1140 ypos 0
label start:
    "This is a work of fiction. The similarities to real people, whether living or dead, real-life events, organizations and symbols are purely coincidental."
#    $renpy.pause(3)
    "It is not written to symbolize, to go against or support any existing political figure or military organization's opinion and beliefs. Any religious references mentioned are merely used as a simple plot device and not a preaching instrument."
    $renpy.pause(3)
    scene sp splash1
    $renpy.pause(3)
    scene splash2
    $renpy.pause(3)
    show splash3
    with dissolve
    hide splash2
    with Pause(3.0)    
    jump intro
label intro:
    scene black 
    $renpy.pause(1)
    play music "dream1.mp3"
    vo "Why are you crying, sister?"
    vo "Was it them who hurt you?"
    vo "Tell me. Was it them?"
    vo "I am not here to torment you sister. I'm here to help you."
    vo "Don't treat me as a burden. I'm not, that's for sure!"
    show mi pi
    mi "Can't you just leave me alone? Just leave me alone! I hate you!"
    vo "Why?"
    vo "Why do you hate me?"
    vo "And here, I thought you don't like feeling anything."
    vo "Now, sister. I don't want to burden you. I'll help you sister, I promise!"
    mi "And how can you? You're just a delusion! If you're real, then why don't you appear in front of me?"
    vo "No, unfortunately, I can't appear if you want me to."
    vo "I'll only appear if you need me."
    vo "Because that's what sisters are, right? They appear in times of need..."
    show mi ma
    mi "Leave me alone! Stop tormenting me!"
    mi "Why do you call me sister? We're not even related! Shut up! Get out!"
    mi "Don't come back! I never ever want you again!"
    vo "I want to do what my sister wants, but I can't."
    vo "I know you're hurt so I'll stay."
    vo "Isn't it it that white-haired girl was the reason of your hurt? What is her name?"
    show mi wo
    mi "She's... Sirius..."
    vo "Sirius, huh... Such a nice name. She's a star, right? I remember before a name was only used on people with high rank..."
    hide mi
    mi "Are you saying she'd be on a high rank soon? Hah! Impossible! She's a convict! Dirt of the nation!"
    vo "Do you believe in me?"
    mi "Not either!"
    vo "You know, I can see the future."
    vo "And I know... that Sirius girl will be the hindrance on whatever you are planning. Do you want that?"
    mi "Bah! Of course not!"
    vo "Then? What will you do?"
    mi "I'll come back to them! Extract my revenge! And I'll be sure they'll pay!"
    vo "You know that isn't enough! They shouldn't just pay... they should suffer!"
    vo "What do you do then? Oooh, you know, killing them will be nicer... Dragging them till they die, it will be really really nice.."
    vo "And I can just see their anguish, their pain, and their cries... My, it's just so fun to imagine!"
    show mi pi
    mi "I have to say.. you're quite brutal..."
    vo "I am your inner heart, your inner voice. I am you. Therefore, deep inside, you want such images too, am I correct?"
    mi "Maybe..."
    vo "Don't say such silly things like \"Maybe.\" It's one of the things that weak people has. Uncertainity. You should be sure of everything you say! You should contain confidence!"
    mi "..."
    show mi sh
    mi "... sister. I guess I should start calling you that."
    vo "Really? You will?"
    vo "I'd be so glad! Really!"
    vo "Sister~"
    mi "Yeah. Sister."
    hide mi
    stop music
    $renpy.pause(3)
    scene bg room
    $renpy.pause(3)
    scene cg miwo1
    "Ugh..."
    "What sort of thing did I imagine again..."
    "I shouldn't even get those stuff... sigh..."
    "I stood up, not quite feeling well. Ugh, what's with my head again..."
    "Snatching up the medicine bottle in the drawer of my side table, I grab a pill and swalowed it, even without water."
    scene black
    play music "usu.mp3"
    "Why do I keep on getting headaches recently..."
    "This isn't really nice. What am I thinking... all this things I am imagining..."
    "Hah... hah..."
    "I look down, and after a while, I realize I'm panting heavily."
    "After all, this is the last time I'll be sleeping here, in this bed..."    
    "I just can't really thing of what will happen next. Where will I be staying? On my cousin's probably."
    "There's the only place I can stay anyway. Without being taunted, at least..."
    "... at least I can find a little peace."
    vo "Hey."
    scene cg miwo2
    play music "dark.mp3"
    "Eeeh? Who was that?"
    vo "Don't pretend you're not hearing me."
    vo "Come, why don't you walk outside and air yourself up a bit?"
    "Agh, this voice again... Ugh..."    
    "They're just delusions..."
    scene black with dissolve
    "Ever since who-knows-when, I have been hearing voices in my head."
    "No, definitetly, I'm not crazy. I am not delusional and I will never be."
    "No, definitetly, I'm not crazy. I am not delusional and I will never be. And it's not an imaginary friend, I'm not a kid anymore."
    "But then... it feels like some real voice is talking in my head. It feels so real I don't even know where it comes from."
    "Yeah, like in that \"dream\" thing a while ago, she's fond of calling me sister."    
    scene cg miwo2
    "But still, it won't be bad to walk around much."
    "It sounds like a nice idea. It seems like a sunny day outside."
    "But still, I don't know where to stay... That wretched general told me not to brandish myself around the camp if I don't want to be talked about."
    "But where to stay... where to stay..."
    $renpy.pause(1)
    stop music
    play music "calypso.mp3"
    scene cg pond11
    "As I throw another rock at the pond, I see many people from afar glance my way, but I just shoot a dirty look back, even though they can't probably see it."
    "Even though it's quite public here, the place is pretty hard to reach. So even if people can glance my way, no one can go near or even see my face."
    "I just went down here because... well, I want to think."
    scene cg pond12
    "It is annoying, yes."
    "It is annoying, yes. Annoying,"
    "It is annoying, yes. Annoying, maddening,"
    "It is annoying, yes. Annoying, maddening, infuriating,"
    "It is annoying, yes. Annoying, maddening, infuriating, well, I can almost find a thousand words describing it."
    "All of my dreams... those are my dreams!"
    "All of my dreams... those are my dreams! Dreams that woman kicked away!"
    "I throw another rock in the water, and it plopped down, sinking to the bottom."
    "I can't really think well."
    scene cg pond13
    "I might have been very angry last... {w=0.5}last time. {w}Agggh, I was so mad I actually forgot what day is it today, or on what day it even happened."
    "But... it's unexplainable. Why do I feel so calm? It's like I want to get angry, but my chest tries holding it back..."
    "Suddenly...."
    scene cg pond2-1
    play music "dark.mp3"
    play sound "heartbeat.wav"
    "Ehhh..."
    "What the hell..."
    "The world suddenly comes to a spin and my vision blurred."
    "What is this?"
    "Aghhh... My head hurts..."
    play sound "heartbeat.wav"
    "I try to grab onto anything nearby, but nothing comes in contact as I reach out."
    "Suddenly...."
    "I felt a cold shift in the air."
    play sound "heartbeat.wav"
    "There was a cold touch in my skin..."
    mi "Who's there? Anyone?"
    "I can't see anything from my blurring, spinning vision. But there.. I can make out somebody."
    scene pond2-2 with dissolve
    vo "So, there you are."
    vo "I have been waiting, you know?"
    mi "Waiting? Waiting for me?"
    mi "Who are you? What do you want?"
    "I grab onto my waist to find my gun but I realized it was confiscated away from me..."
    "Suddenly, she giggled silently."
    scene pond2-3 with dissolve
    play sound "giggle.wav"
    "Her laughter was innocent, but at the situation at hand it sounds quite cruel to me."
    vo "You know what I want."
    vo "...and... for who am I?"
    vo "You know me."
    vo "You surely do."
    scene black with dissolve
    stop music fadeout 2    
    $renpy.pause(2)
    $ show_button_game_menu = False
    nvl show dissolve
    play music "darkambient.mp3" fadein 1 
    nvlvo "Hey."
    nvlvo "Hey, you! Wait for me!"
    nvlvo "Hey!"
    show mipi with dissolve
    nvlx "I still continued my walking."
    nvlx "I still can't see where am I. This is some delusion, right?"
    nvlx "Another delusion..."
    nvlx "As I walk, I try observing where I am, from what I can make out. There's.... nothing. Only black."
    nvlx "There doesn't seem to be any boundaries, because I keep on walking into any random direction I please and I don't bump into anything..."
    nvlx "Yes, this is a delusion. Impossible to be a dream. Dreams are myths."
    nvlmi "What do you want with me?"
    nvlx "I turn around to the source of the voice, but I can't see her face clearly."
    nvlmi "Have I done something to you?"
    nvlvo "Nope! Nothing!"
    nvl clear
    nvlvo "And what makes you think I have something I want from you?"
    nvlvo "You know, my only purpose in life is to give what you want..."
    nvlvo "...sister."
    nvlx "...."
    show mipi2 with dissolve
    hide mipi
    nvlmi "... sister?"
    nvlvo "Yes. We are sisters."
    nvlvo "We are more like twins though."
    nvlvo "You don't remember, huh... The time that Sirius girl attacked you."
    nvlvo "You can't say anything, so I went up and said it for you."
    nvlvo "I hear you saying in your head that you wanted to tell her the truth for the hell of it."
    nvlvo "But I didn't. I did something better than telling her the truth."
    nvl clear
    nvlvo "Why? What's that frown in your face? Can't you see what I am doing is for your sake?"
    nvlx "She sure is talkative."
    nvlx "And sure is observative."
    nvlmi "And why do you care?"
    nvlx "Suddenly, there was something that suddenly starts to materialize in front of me."
    show maeappearance with dissolve
    nvlx "The form became a person, a teen girl I don't know... {w}But seems familiar."
    nvlx "The grin on her face was almost ear-to-ear, and her moves seem as if to mock me."
    nvlgi "I have to, well, it's hard being a sister, but I have to."
    nvlx "..."
    nvlx "Twins..."
    nvlx "Such a silly girl. There's no such thing as blood relations. I will never be related to anybody. Ever!"
    play music "tension.ogg" fadein 1 
    nvlmi "Don't make me laugh."
    nvl clear
    nvlx "She pauses for a while, as if trying to process those words I just said."    
    scene black with dissolve
    show mipi at right with dissolve
    nvlmi "I'll never acknowledge someone as my sister. I'll never acknowledge you as anyone related to me!"
    nvlmi "Why do you think I walked out of the military? It's because I hated those thoughts they keep on slapping at each other's faces!"
    nvlmi "Don't make me laugh! You're like all those people! You're like the compilation of those three people, minus the sadistic laughing!"
    nvlx "She just kept quiet, with a simple smile in her face."
    nvlx "Suddenly, she walked around me, looking at me in the eye, as if she's examining a block of wood she's about to carve."
    show masly at left with dissolve
    nvlx "The grin on her face... it's telling me something..."
    nvlgi "Well, I do understand."
    nvlgi "But I think you don't."
    nvl clear
    nvlmi "What in the hell do you mean? I do understand everything you mean! What, can you just get away, get away!"    
    show mapo at left with dissolve
    hide masly
    nvlgi "I can't."
    nvlgi "Because you're the one that makes me stay here."
    nvlgi "When you die... that's the only time I can leave as well."
    show mima at right with dissolve
    hide mipi
    nvlx "I can't understand it, but my anger rose each second that pass."
    nvlx "It's just... it's just absurd!"
    show miwha at right with dissolve
    hide mima
    nvlx "Suddenly, I almost stepped onto an object near my feet."
    nvlx "I look down and it's a ... {w}knife?"
    nvlx "How in the--"
    show mashy at left with dissolve
    hide mapo
    nvlgi "Go. Kill me like you usually do to other people."
    show misly at right with dissolve
    hide miwha
    nvlmi "Heh, how brave of you to say something like that."
    nvlmi "Still, I might consider it."
    nvlmi "Killing you, I mean. It might not be worth my time."
    show mapo2 at left with dissolve
    hide mashy
    nvlgi "What stuff is worth your time?"
    nvl clear
    nvlgi "Trying to insult Sirius and Cetus but suddenly backfires?"    
    nvlgi "Trying to go cute with the head general only to get kicked out by his daughter?"
    nvlgi "Failing your dreams? Making yourself the laughingstock of the nation?"
    nvlgi "What is worth your time and effort, Miliceeeeent?"
    nvlgi "Failing all the time, everytime?"
    nvlgi "Always failing, is that where you are trying your best to succeed into?"
    show masly at left with dissolve
    hide mapo2
    nvlx "She laughed with a hysterical tone, and that's where she totally broke it."
    nvlx "I picked up the knife and charged towards her."
    show miliceattacksmae with dissolve:
        xpos 0 ypos -600 xanchor 0 yanchor 0
        linear 5.0 xpos 0 ypos 0
    nvlx "It wasn't in my own will. Something did it."
    nvlx "It's like some hidden force had clouded my judgement and started taking control of me."
    nvlx "I was mad, yes, but before, I know what I was doing. Now, i felt like someone's manipulating me..."
    nvl clear
    nvlx "But then, when I was near her, she didn't flinch. {w}She just smiled that crazy-looking grin she kept on brandishing."
    scene black with dissolve
    show masly with dissolve
    nvlgi "Heh."
    nvlgi "I win this time."
    nvlgi "I'm sorry, sister. It just have to happen."
    nvlgi "Condolences, Miliceeeent."
    scene black with dissolve
    stop music 
    
    nvl hide dissolve
    $ show_button_game_menu = True
    "What?"
    "... condolences?"
    "Suddenly, I felt something."
    "It's as if I was watching everything from third person view a while ago, and ..."
    "What the hell...."
    "What in the world is this sticky feeling? It's like I got this fluid all over me... "
    "It feels familiar, and the smell is sickly as well..."
    "I try opening my eyes, but it's no use. It feels sticky as well."
    "Reaching to my eyes, I rub the foreign substance away from my eyes."
    "And then..."
    scene joisan with dissolve
    play music "darkmystery.mp3" fadein 1 
    "What in the--"
    "Who's this person covered in blood? How did I get in here? Why am I holding this knife that's stabbed in his chest?"
    "Agh... What in the world..."
    "I don't know how I got in here, and I don't even know who's this guy..."
    "And most especially, I don't remember anything from a while ago..."
    "I look around me, and I realized I was in the camp. In the training field to be more specific."
    "Pretty much one of the most isolated places in the camp."
    "But why, why did this happen..."
    "Why was anybody -- or maybe I -- was so ... crazed to kill this guy?"
    scene field with dissolve
    show masly at left with dissolve
    vo "I was bored!"
    vo "I killed him because I was so bored!"
    "I can hear the same voice as a while ago on my head.{w=0.5} But now, it's as if I am also seeing{/i} a delusion, because that teenager girl from a while ago is right in front of me this time."
    "She walks around the corpse, and kicks on his head playfully."
    vo "So bored with the world! So bored with everything!"
    vo "I'm so tired of acting like someone else's puppy! I hate it!"
    vo "People might think I'm like an obedient dog, but I'm like a sly cat, staring at them evilly!"
    vo "This is the only way I can show how worthy I am! I will show them how will I treat anybody who crosses my way!"   
    "Someone else's puppy..."
    show mipi at right with dissolve
    hide miwo
    "Agh..."
    "I looked around, and it's nighttime. Judging from my surrounding, it may have been days after I lost consciuosness."
    "Firstly, this guy seems to be in the military circle, judging from the color of shirt he's wearing." 
    "Secondly, from his age, he seems to be the ones Daena appointed to fill one of the many blank positions, so..."
    "Right now, she's the one in place."
    "If I was the one who did this then..."
    "Then..."
    "This is all their fault! I will never be under them again! Damn it!"
    "If they just haven't made this system, then it wouldn't have happened!"
    "All of this wouldn't have happened!"
    "And if that system wasn't made... {w}Then this girl isn't in front of me now!" 
    show mashy at left with dissolve
    hide masly
    vo "Don't get mad at me! My boredom wasn't the only reason you know."
    vo "I promised, right?"
    vo "I told you before, when you were little, that I'd be a good girl and protect you!"
    vo "I am{/i} different, but I can still do it. I might be dead already, but I can still do what I didn't do."
    "What now? Before, a delusion. Now, someone who have risen from the dead?!"
    "Anger and fear both filled me to the brim, but her voice still went on. I don't understand what sort of feeling developed inside me, but..."
    vo "Miri-chan, I promised that."
    vo "Even if I die, I will protect you."
    vo "I will!"
    show misho at right with dissolve
    hide mipi
    "Mi-Miri-chan?"
    "That name sounds familiar...."
    "Almost instantly, I feel a rush of thought in my head."
    scene field with vpunch
    "As if they're just locked away in some hidden space in my head, thoughts and memories started to fill my mind."
    with vpunch
    "It felt like as if a mallet was pounding the insides of my head."
    with vpunch
    "Slowly...."
    with vpunch
    "Painfully..."
    with vpunch
    "After a couple of seconds, it was gone, but I felt dizzy."
    show mashy with dissolve
    "I looked up at her, but then, it's like..."
    "... that she's..."
    mi "Oneesan?"
    scene black with dissolve
    stop music 
    $renpy.pause(2)
    $ show_button_game_menu = False
    nvl clear
    nvl show dissolve
    $renpy.pause(2)    
    scene maeflashback1 with dissolve
    play music "memory.mp3" fadein 1
    nvlvo "Ne, she's really pretty, right, okaa-san?"
    nvlvo "Stop calling me by such an absurd name, Mae."
    nvlma "But, okaa-san--"
    nvlvo "Stop it."
    nvlma "... okay."
    nvlvo "And stop calling your sister such absurd names! You'd just influence Milicent!"
    nvlma "Yes, mom."
    nvlvo "Haah. Why did I have a daughter with this thing... Musica Syndrome..."
    scene black with dissolve
    nvl clear
    nvlx "Musica Syndrome. Since music is a symbol of cultures back at the old age, it means having knowledge about certain cultures and nationalities in the past."
    nvlx "It ain't genetic. It's an error in the mirochip that's implanted to her when she was born."
    nvlx "She likes speaking in some old Eastern country's \"form of respect\", but father and mother found it more of obnoxious and disrespectful."
    nvlx "They found her weird."
    scene maeflashback2 with dissolve
    nvlma "Hey, Milicent!"
    nvlmi "Sister Mae?"
    nvlma "Eh, stop calling me that. {w}I sound like an old woman! Call me oneesan!"
    nvlmi "Onee... san?"
    nvlma "Yep! It means sister!"
    nvlmi "Sister?"
    nvlma "Yep! That's why I'll call you sister too! I'll also call you oneesan!"
    nvl clear
    nvlmi "Mae... Mae-oneesan?"
    nvlma "Yep! {w}Hahaha, you do learn quickly!"
    scene black with dissolve
    nvlx "But I didn't find her weird at all."
    nvlx "She was a nice person."
    nvlx "She taught me a lot of things, taught me how do Eastern people eat, told me that people before \"bless their meals\" before they eat them."
    nvlx "When mom and dad were not at home, we even eat our food with our hands."
    nvl clear
    nvlx "Until one day, she got sick."
    nvlx "It wasn't a bad one, I think, since it didn't last long."
    nvlx "But after that, she totally changed."
    nvlx "I mean, she still eats with me, teaches me things, tells me stories."
    nvlx "But then, she suddenly had a darker view of the world, unlike before."
    nvl clear
    scene maeflashback31 with dissolve
    play music "darkmystery.mp3" fadein 1 
    nvlmi "O-o{w=0.5}-oneesan?!{w=0.5} W-{w=0.5}w-{w=0.5}what are y-{w=0.5}you doing?!"
    nvlmi "W-{w=0.5}what are you doing with the cat?!"
    scene maeflashback32 with dissolve
    nvlma "It stole my cookie."
    nvlmi "Well, I do understand that, but why do you have to crack the cat open? It looks hideous, mom and dad will get angry!"
    nvlma "The cookies he stole might still be in there! I'm looking for it..."
    nvlma "The cat ate it, so it still be in here somewhere..."
    nvlmi "Hey, hey! Stop it! The cat's dead already, and you're opening him up for just a cookie?"
    nvlma "Yep. Mirisento-san, it's... logic."
    nvlma "I can just return him back later on. You'll see."
    scene black with dissolve
    nvlx "I still didn't understand what happened that day. Why she mutilated the cat to find just a piece of cookie."
    nvlx "The next day, my parents found the cat's mutilated corpse, and they were too disgusted and horrified to even ask who of the two of us did it."
    nvl clear
    nvlx "Because of that, I was too scared to even go into her room, I might just find stuff written in blood there."    
    nvlx "It was... well, the time I still had fear."
    nvlx "We were the total opposites. I was afraid, sometimes she'd slap me for being a crybaby."
    nvlx "I loved one thing, she hated it or find it boring. But we still find each other good company...until now."
    nvlx "I was technically avoiding her, and I just watch from the terrace as she started carving weird symbols in the tree bark or as she kills another cat."
    scene maeflashback4 with dissolve
    play music "memory.mp3" fadein 2
    nvlx "But she died. Just like that."
    nvlx "But I didn't cry. I wasn't feeling anything."
    nvlx "We just found her dead, at the back of a large tree, unconcscious."
    nvlx "Not even the autopsy can tell what's the reason why she died. It's as if she just fainted and her life ended there."
    nvl clear
    nvlx "One side of me believed that she hated me because I won't join her demonic rituals. The other believed that before she died, she wanted to tell something to me but she wasn't able to reach it out because I was avoiding her."
    nvlx "I don't know what to believe."    
    nvlx "So, I tried continuing life, without... feeling anything."
    nvlx "Without feeling anything..."
    nvlx "That must be what I am now."
    nvl hide dissolve
    $renpy.pause(1)
    scene black with dissolve
    show field with dissolve
    $ show_button_game_menu = True
    show misho2 at right with dissolve
    play music "mystery.mp3" fadein 1 fadeout 2
    "No! She isn't that same Mae! She isn't!"
    "If she is sister Mae..."
    show mipi at right with dissolve
    "Then ... why does she keep on insulting me?"
    "Why does she keep on mocking me!"
    "She's crazy!"
    show magl at left with dissolve
    m "I am."
    "No, this voice... this voice doesn't exist!"
    "I better do something about this..."
    show mapo2 at left with dissolve
    m "You left me behind, Miri-chan."
    m "You can't deal with me."
    m "All you got to do is let me help you."
    m "Try to get rid of me and people will suffer."
    "Tsk. I can't differentiate whether she's a maniac or just a playful, mischievous kid..."
    show mipro at right with dissolve
    mi "Yeah, I may not be allowed to erase the memories, but I can modify them!"
    mi "I can just modify it in a way I won't be affected with whatever you do!"
    mi "I can do that!"
    "Ha, take that!"
    hide mapo2 with dissolve
    m "Pfft."
    m "I told you before. Getting rid of me will only harm other people."
    m "And didn't I tell you? Unless you die, I won't disappear."
    m "It isn't I who came to you. You're the one who called me here."
    m "I am neither spirit or a delusion. I am an existence made by your own imagination."
    m "You can classify me as a \"split personality\"."
    mi "Ahh, what..."
    show mima at right with dissolve
    hide mipro
    mi "What-- Just who are you?"
    mi "You--- you can't be Mae."
    mi "You just can't be Mae!"
    show masly at left with dissolve
    hide magl
    "She laughs maniacally."
    "Her laughter -- a scary, witch-like cackle -- seem more horrible than her laughter a while ago, but I guess it's just me."
    "She seems to be innocent, but her eyes were telling me something else..."
    m "Don't you worry..."
    m "I won't cause you any pain."
    m "Unlike them, who you trusted, who didn't give you anything at all."
    m "You know me Miri-chan, right?"
    m "I won't do anything."
    m "I won't."
    mi "..."
    show misad at right with dissolve
    hide mima
    "Gosh... what's this heavy feeling that developed?"
    "It feels like I'm neither angry or sad about her..."
    "Argh..."
    "Is it really Mae?"
    "If so, isn't she dead?"
    scene black with dissolve
    "Dead? Isn't she dead already?"
    "Mae, aren't you dead already?"
    "Just tell me you are dead already. Please."    
    play music "dream1.mp3" fadein 1 
    scene hallway with dissolve
    play sound "run.ogg"
    "I find myself running in the hallway of the military base."
    "There are a lot of twists and turns, but eventually, I found my way around them."
    show mipi with dissolve
    "Just show yourself, damn records room!"
    "Records room... where is it?!"
    "I've never been there to be honest, and I haven't even known what to expect when I get there."
    "But I know where it is, since the room is guarded day and night and ..."
    "She has been here before..."
    scene black with dissolve
    si "I have regretted everything I did that day."
    si "But I believed what I did was only right, to know who my parents are."
    si "The records room wasn't anything fancy. It's only a room filled with bookshelves and file cabinets dumped with lots of digital pads."
    si "Although, there are... several rooms there that I can't tell the purpose of..."
    scene hallway with dissolve
    show mi with dissolve
    hide mipi
    play sound "run.ogg"
    "I can still remember what that Sirius girl was thinking about the records room."
    "I still remember what she thought, dreamed, or whatever thing they call it, back at when she was captured."
    "I can still remember what the two of them thought."
    show misad with dissolve
    hide mi
    "It's a sad thing I can't read thoughts now. But I still remember what I've read."
    "After a couple of steps, I reach the records room."
    show miwha with dissolve
    hide misad
    "Surprisingly, no guards..."
    "I remember having a keycard for entry here somewhere in my pocket... {w}Ah, here it is!"
    show misly with dissolve
    hide miwha
    "Pfft, fools. They didn't take this away from me last time."
    "I insert the keycard and go in."
    scene black with dissolve
    nvl clear
    nvl show dissolve    
    play music "darkambient.mp3"
    $ show_button_game_menu = False
    nvlx "It's dark. So dark I can't even see where I was going."
    nvlx "It felt like that dream."
    nvlx "I try to stretch my hands out, so that I can feel in case I might be walking to a cabinet or a wall."
    nvlx "But then..."
    play sound "heartbeat.wav"
    nvlx "There's that cold touch again."
    nvlx "A cold touch over my eyes, and one on my arm."
    show masad at left with dissolve
    nvlm "I know you can't see anything."
    nvlm "I will be your eyes, Miri-chan."
    show mipi at right with dissolve
    nvlmi "Stop calling me with that name, please."
    nvlmi "You're not Mae. Only Mae can call me that."
    nvlm "Oh, is that so?"
    show mashy at left with dissolve
    nvlx "I hear her snicker."
    nvlm "Okay, Miliceeent."
    nvlm "I already warned you."
    nvl clear
    nvlm "Try to erase me, you'll harm other people."
    show mima at right with dissolve
    hide mipi
    nvlmi "Who the fuck cares about other people?"
    nvlmi "I just want you out of my life, that's all."
    nvlmi "And get your hands off me. It's so cold and you're dropping the degree-celsius meter to a ton."
    hide mashy with dissolve
    nvlx "She did let go off me. The cold feeling disappeared, but I can still feel somebody around." 
    nvlx "I tried fishing in my pocket for some source of light. and found a little flashlight."
    nvlx "With it, I tried finding my way to the back of the room covered with a screen."
    nvlx "Behind the screen, there was a metal door."
    nvlx "Beside the metal door, is a glass wall, where the room where the door leads can be seen. Since I haven't touched anything yet, there's nothing in the room."
    nvlx "I have never seen this thing in real life, only from a picture."
    nvlx "This chamber is called a \"memory retrieval chamber\", where any of us can get a memory from the archives."
    nvl clear
    nvlx "And this is now where the process starts..."
    nvl clear
    scene black with dissolve
    $renpy.pause(2)
    show memorychamber:
        xpos 0 ypos -425 xanchor 0 yanchor 0
        linear 8.0 xpos 0 ypos 0
    nvlx "I try to relax, to make my breathing feel normal."
    nvlx "It's quite hard to do, the glowing blue lights around me. {w=0.5}But then, I closed my eyes, and I felt a bit calmer."
    nvlx "I feel nervous because, well... I don't know how this works. I don't know how this memory chamber thingie works. I don't even know what to do."
    nvlx "The only thing I know is that I should stay in here, and try to remember everything about Mae. {w=0.5}About her."
    nvlx "Then the system will find those memories from their records, then when it appears, I can modify it. It's just like a search engine."
    nvlx "But then, modifying memories is a total crime. {w=0.5}If I get caught doing this, I'd not only get to jail, I'd be executed."
    nvlx "But I don't really care."
    nvlx "If it's for removing whatever memory Mae has left... {w=0.5}Yes, I'd rather die."
    nvlx "Oddly, I shouldn't even be remembering these things. {w=0.5}Every person forgets about his or her childhood, because of this system, and the drug that everyone's forced to take that makes us forget."
    nvlx "But since the Change has happened..."
    nvl clear
    nvlx "I did remember those memories again."
    play music "memory.mp3" fadein 1 fadeout 2
    scene black with dissolve
    $renpy.pause(1)
    nvl clear
    nvlx "Joi-san..."
    nvlx "I'm sorry I killed you..."
    nvlx "It's not Mae's mistake."
    nvlx "It's not the system's mistake."
    nvlx "It's me who bears the flaws that caused your death."
    nvlx "It's me that caused everything."
    nvlx "I finally remember."
    nvlx "How I felt that day... Because of my problems, I tried forgetting them."
    nvlx "But here on... I returned to them. To these feelings."
    nvlx "Mae... Even though you're dead, I'll always remember you."
    nvlx "I always will!"
    play sound "giggle.wav"
    nvlx "Suddenly, I hear a familiar laughter."
    nvlx "I hear her voice, but ...{w=0.5}she's nowhere to be seen."
    nvlma "I'm glad you have understood. Will you still continue?"
    nvlma "Will you still try to erase me?"
    nvl clear
    nvlma "I'm sorry, I know I was a nusiance."
    nvlma "I'll leave now."
    nvlmi "Wait."
    nvlx "I find myself calling her back, but then I feel like slapping myself for doing that."
    scene maememory with dissolve
    nvlx "She looks at me, but her stare wasn't of annoyance or trickery. It was of pure concern."
    nvlx "I remember back those days. The young version of me looking at her, wearing the same smile."
    nvlx "I guess I was just too harsh on everybody. Because of the pain I have felt."
    nvlx "I haven't sold my soul to the devil. I have just taken it away, locked it somewhere I can't find it, and pretended I can live without it."
    nvlma "Why? Do you want something, by any chance?"
    nvlx "Her memory seems to have been cleared, as if she doesn't remember she'd mocked me, or had insulted me."
    nvlmi "Please stay."
    nvl clear
    nvlmi "Here in this memory chamber, I'll recover our memories..."
    nvlmi "... and make them less painful."
    nvlmi "That way, you can finally rest in peace..."
    nvlmi "Sorry, Mae. I have to do this."
    nvlmi "It's both for your sake, and mine."
    nvlma "Do you not mind the casualties? The anger the people will set upon onto you?"
    nvlma "You know clearly that by doing this, lots of people will be affected."
    nvlma "Since all these memories are linked, one change will set upon a chain reaction."
    nvlx "I smile to her sweetly. I wish she have seen this before she died..."
    scene maeflashback4 with dissolve
    nvlx "That figure of her under that tree... dead... it doesn't feel at all as if she's dead. She looks like she's just sleeping."
    scene maememory with dissolve
    nvlmi "Don't get me wrong. I'm not mad at you, Mae."
    nvlmi "It's to get this guilty feeling off my chest."
    nvl clear
    nvlmi "You know, ever since you died, it was also a chain reaction."
    nvlmi "Your death, mom and dad's death, then now..."
    nvlmi "Joi is dead. I killed him."
    nvlma "No, don't say that. I killed him."
    nvlx "Her persistence, unlike a while ago, makes me laugh."
    nvlmi "Maybe so that we won't argue... We killed him."
    nvlma "Yep. We did."
    nvlx "She laughed sweetly, unlike a while ago."
    nvlx "Yet, there's still this mystery that resides in my mind, but who am I to care?"
    nvlx "I can see her right in front of me. She's dead, but I can see her."
    nvlx "She has revived. She was the sister I tried to forget."
    nvlx "And right now, I don't care if it's a delusion."
    nvl clear
    scene mimamemory1 with dissolve
    nvlma "Come, hold my hand. And can you remember, oneesan? What period of they year people repent in their sins to praise a dying Lord?"
    nvlmi "It was Lent."
    nvlma "It's Lent now. Try to remember your sins, and repent for them."
    nvlma "The action of remembering is already a sign of repentance."
    nvlma "It's the only way."
    scene mimamemory2 with dissolve
    nvlmi "It's ironic, you know. You were telling me to kill people a while ago and now you're asking me to pay for my sins."
    scene mimamemory3 with dissolve
    nvlma "Mood changes from one phase to another. It's normal."
    nvlma "And plus, isn't it that they should repent more?"
    nvlx "They should... repent more?"
    nvlx "Does she mean they are the ones that should ask more for... forgiveness?"
    nvl clear
    nvlma "The bigger the sin, the bigger the punishment."
    nvlma "So they made you a big sin, they should have a repentance and a punishment that's just as heavy as their faults."
    nvlma "Oh, I'm also sorry for butting in your conversations for the past few days."
    nvlmi "It's okay."
    nvlma "So what should we do now?"
    nvlx "She laughed again."
    scene mimamemory4 with dissolve
    nvlma "Well, clear everything, that is."
    nvlma "We still have lots of things to do."
    scene black with dissolve
    stop music fadeout 3    
    
    $renpy.pause(3)
    play music "darkmystery.mp3"
    centered "Thank you for finishing \"Twin Faces\"!"
    centered "Script, Story, Sprites, and almost everything else\nLumenAstrum"
    gi "Miss Hartnight, while I was on my way to the records room, I got a report coming from the security personnel of the records room."
    gh "Hmm? What is it?"
    show epilogue11 with dissolve
    gi "The records room were left open. Upon closer inspection and observation, we found out that former Calypso entered the records room."
    gh "Hmm? And?"
    show epilogue12 with dissolve
    gi "Well... how should I explain this..."
    gi "She was alone."
    gi "But this is the strange part..."
    scene black with dissolve
    centered "CG Help\nOhMhaiGosh\n(Go see her dA account! She's amazing!)"
    centered "That one odd hallway background\nmugenjohncel\n(I was sorta in a hurry to find another hallway BG...)"
    show epilogue12 with dissolve
    gh "Hmm. Another addition on the series of strange happenings lately."
    gi "She entered the memory chamber. But the footage was cut from there."
    show epilogue11 with dissolve
    gi "But we found somebody else in the memory chamber..."
    gh "Eh?"
    scene black with dissolve
    centered "Music\nJamendo, SENTIVE, Neosounds, wakaba-music, Rengoku Teien"
    centered "Filtered Photographs for BGs\nSamu-kun's photographs and some Japanese site I lost the link into\n(please tell in case you recognize the images ^^;)"
    show epilogue11 with dissolve
    gi "There was a woman in her teenage years who was lying in the memory chamber."
    gi "From her records, she was Mae, older sister of Milicent. But then, she died around ten years ago."
    gi "But from the autopsy results she died around only three hours ever since former Calypso entered the records room."
    gh "Hmm, it's more or less a technological phenomenon. We can also call the records room as a lab by it's own, considering the information we can get and utilize."
    gh "It is possible, but... it's quite unlikely."
    gh "Inspect where this Mae person's old body was placed, then tell me more."
    gh "Oh, I haven't seen Colonel Marshall a while ago in the meeting. Have you seen him?"
    scene black with dissolve
    centered "Acknowledgements\n\nazureXtwilight - For helping me in that one CG, helping me find music and for pre-reading my script! :D\n\nMy friend Kyle - For pointing out some grammar mistakes (even though there are still a lot right now)\n\nThe LemmaSoft community - For having NaNoReno and this project possible!"
    centered "Done with Ren'Py Visual Novel Engine"
    show epilogue11 with dissolve
    gi "Actually... {w}I also got another report, General. {w=0.5}He was found in the training fields with a knife stabbed in his chest."
    show epilogue12 with dissolve
    gi "But we're still trying to find out everything about this case."
    gh "Call in Team Spinos to deal with this matter. Dismissed."
    gi "Yes, General."
    gi "I'll inform you in case there will be updates about this case."
    play sound "door.wav"
    scene black with dissolve
    centered "I hope you enjoyed this short story I wrote!"
    centered "For anyone who does not get it, playing/reading my other KN \"Soul and Heart\" might help, although there'd be a bit of a spoiler now..."
    centered "Arigato gozaimasu from the Harmonica Vitrea team!"
    show epilogue21 with dissolve
    gh "So, it has happened now..."
    gh "I guess I can't really help it."
    show epilogue22 with dissolve
    gh "We have to prepare for the worst... if that split personality takes over... we're screwed."
    gh "But then, I have to pay for it. My family was the reason this entire personality ruckus even started...."    
    $ persistent.my_bonus = True
    return