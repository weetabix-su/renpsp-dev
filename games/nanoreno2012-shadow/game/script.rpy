#BGS
image bridge1 = "Bg/bridge1.png"
image bridge1e = "BG/bridge1e.png"
image bridge1n = "BG/bridge1n.png"
image bridge2 = "BG/bridge2.png"
image bridge2e = "BG/bridge2e.png"
image bridge2n = "BG/bridge2n.png"
image bridge3 = "BG/bridge3.png"
image bridge3e = "BG/bridge3e.png"
image bridge3n = "BG/bridge3n.png"
image bridge4 = "BG/bridge4.png"
image bridge5 = "BG/bridge5.png"
image bridge5n = "BG/bridge5n.png"
image bridge6 = "BG/bridge6.png"
image water1 = "BG/water1.png"
image water1n = "BG/water1n.png"
image lot1 = "BG/lot1.png"
image lot2 = "BG/lot2.png"
image lot3 = "BG/lot3.png"
image lot4 = "BG/lot4.png"
image food1 = "BG/food1.png"
image store1 = "BG/store1.png"
image house1 = "BG/house1.png"
image house1e = "BG/house1e.png"
image house1n = "BG/house1n.png"
image house2 = "BG/house2.png"
image house2n = "BG/house2n.png"
image house_in1 = "BG/house_in1.png"
image house_in2 = "BG/house_in2.png"
image park1 = "BG/park1.png"
image park2 = "BG/park2.png"
image park3 = "BG/park3.png"
image park4 = "BG/park4.png"
image street1 = "BG/street1.png"
image street1n = "BG/street1n.png"
image end1 = "BG/end1.png"
image end2 = "BG/end2.png"
image end3 = "BG/end3.png"
image end4 = "BG/end3.png"

#Sprites
image eve 1 = "Eve/1/eve_1.png"
image eve 2 = "Eve/1/eve_2.png"
image eve 3 = "Eve/1/eve_3.png"
image eve 4 = "Eve/1/eve_4.png"
image eve 5 = "Eve/1/eve_5.png"
image eve 6 = "Eve/1/eve_6.png"
image eve 7 = "Eve/1/eve_7.png"
image eve 8 = "Eve/1/eve_8.png"
image eve 9 = "Eve/1/eve_9.png"
image eve 10 = "Eve/1/eve_10.png"
image eve 11 = "Eve/1/eve_11.png"
image eve 12 = "Eve/1/eve_12.png"
image eve 13 = "Eve/1/eve_13.png"
image eve 14 = "Eve/1/eve_14.png"
image eve 15 = "Eve/1/eve_15.png"
image eve 16 = "Eve/1/eve_16.png"
image eve 17 = "Eve/1/eve_17.png"
image eve 18 = "Eve/1/eve_18.png"
image eve 19 = "Eve/1/eve_19.png"
image eve d1 = "Eve/1/eve_d1.png"
image eve d2 = "Eve/1/eve_d2.png"
image eve d3 = "Eve/1/eve_d3.png"
image eve d4 = "Eve/1/eve_d4.png"
image eve d5 = "Eve/1/eve_d5.png"
image eve d6 = "Eve/1/eve_d6.png"
image eve d7 = "Eve/1/eve_d7.png"
image eve d8 = "Eve/1/eve_d8.png"

image eve 1b = "Eve/2/eve2_1.png"
image eve 2b = "Eve/2/eve2_2.png"
image eve 3b = "Eve/2/eve2_3.png"
image eve 4b = "Eve/2/eve2_4.png"
image eve 5b = "Eve/2/eve2_5.png"
image eve 6b = "Eve/2/eve2_6.png"
image eve 7b = "Eve/2/eve2_7.png"
image eve 8b = "Eve/2/eve2_8.png"
image eve 9b = "Eve/2/eve2_9.png"
image eve 10b = "Eve/2/eve2_10.png"
image eve 11b = "Eve/2/eve2_11.png"
image eve 12b = "Eve/2/eve2_12.png"
image eve 13b = "Eve/2/eve2_13.png"
image eve 14b = "Eve/2/eve2_14.png"
image eve 15b = "Eve/2/eve2_15.png"
image eve 16b = "Eve/2/eve2_16.png"
image eve 17b = "Eve/2/eve2_17.png"
image eve 18b = "Eve/2/eve2_18.png"
image eve 19b = "Eve/2/eve2_19.png"
image eve 20b = "Eve/2/eve2_20.png"
image eve 21b = "Eve/2/eve2_21.png"
image eve 22b = "Eve/2/eve2_22.png"
image eve 23b = "Eve/2/eve2_23.png"
image eve 24b = "Eve/2/eve2_24.png"
image eve d1b = "Eve/2/eve2_d1.png"
image eve d2b = "Eve/2/eve2_d2.png"
image eve d3b = "Eve/2/eve2_d3.png"
image eve d4b = "Eve/2/eve2_d4.png"
image eve d5b = "Eve/2/eve2_d5.png"
image eve d6b = "Eve/2/eve2_d6.png"
image eve d7b = "Eve/2/eve2_d7.png"
image eve d8b = "Eve/2/eve2_d8.png"
image eve d9b = "Eve/2/eve2_d9.png"
image eve d10b = "Eve/2/eve2_d10.png"

# Declare characters used by this game.
define e = Character('Eve')
define mom = Character('Ryo\'s Mom')
define dad = Character('Ryo\'s Dad')
define r = Character('Ryo')
define dad2 = Character('Eve\'s Dad')
define girlA = Character('Girl A')
define girlB = Character('Girl B')
define k1 = Character('Kid 1')
define k2 = Character('Kid 2')
define k3 = Character('Kid 3')
define k4 = Character('Kid 4')
define k5 = Character('Kids')
define Chika = Character('Chika')
define Jiro = Character('Jiro')
define Shigeru = Character('Shigeru')
define teacher = Character('Teacher')
define narrator = Character('')

label start:
    $love_points = 0     
    scene black
    $renpy.pause(0.5)
    play sound "clock.mp3"
    $renpy.pause(1)
    play music "Music/White Snow.ogg"
    $renpy.pause(3)
    mom "Ryo, you need to get up you are going to be late for school."
    r "Ugh... Just five, five more minutes."
    mom "Honestly what is the point of even setting an alarm if you ignore it all the time."
    mom "It is time to get up, young man. I will not allow you to be late for school."
    r "..........."
    mom "Ryo, you better be up and awake by the time I get back, or there will be consequences."
    r "Alright... alright, I'm getting up."
    mom "Good, now hurry down for breakfast."
    "With a groan Ryo crawled out of bed. Letting out a yawn he dressed himself in his uniform in a foggy haze. His body was still half asleep causing him to sway back and forth as he headed out of his room and to the kitchen."
    scene house_in1
    mom "Good morning, today I made a-"
    mom "You are not going to school looking like that are you?"
    "Ryo glanced up and down at what he was wearing a shrugged."
    r "Why not?"
    "He was wearing clothes, so he wasn't in his underwear, and he had his uniform on. He wondered what was wrong with what he was wearing."
    "Ryo's mom let out a sigh and shook her head. She reached into her pocket and magically pull out a comb."
    mom "You're hair is a mess. You can't go to school looking like that."
    "In a swift motion without waiting for her son's reply began to comb his hair. Combing it until it reached her approval, despite Ryo's protests."
    r "Mom, stop. I can do it myself. I'm not a little kid. It is embarrassing."
    "She smiled at her son and stopped fussing over him, allowing him control over his hair once again."
    mom "Oh, just look at you. You're still half asleep. You look like you are about to fall asleep again."
    play sound "sprayer.wav"
    r "Mom! What are you doing stop!?"
    mom "Sorry, I thought it would wake you up."
    "Ryo glared at his mother as he took the hand towel she held out to him."
    mom "Honestly sometimes you act just like a little child."
    r "I'm the child? It is pretty childlike in my eyes to spray someone with the sprayer."
    mom "Don't take everything so seriously. Have a little fun with life."
    play sound "toaster.wav"
    r "Toast for breakfast today?"
    mom "Ding. Ding. Ding. You've guessed correctly. Today I decided to make a western breakfast. But we had no eggs, so just toast."
    "Ryo shook his head at his mother's antics. He wondered just how in the world his mom and dad got together, they were complete opposites. His dad was always serious and hardly ever joked around, while his mother was almost never serious."
    mom "Here you go Ryo. I even cut the crust off so it would be easier for you to eat."
    "Ryo glared at the good being offered to him. It wasn't that he didn't like toast. No, in fact he actually liked toast. Nor was it the fact that his mother had made it."
    "He hated the extra attention that his mother had put into it. He was not a little kid and he did not want to be treated like one, ever."
    r "Thanks..."
    "He took the piece of toast and took one bite from the center of it before throwing the remainder away."
    "Ryo's mother quickly masked her slight disappointment and wished him a safe trip."
    "Ryo had only eating a tiny bit of the toast and had thrown away the majority of it. It was just a simple action, but it held deeper meaning to her. It reminded of of how whenever she tried to get closed to her son, he would throw her feelings away."
    r "Well, I'm off."
    mom "Have a safe trip."
    "Ryo bundled himself up in a winter coat and hat before heading out the door."
    scene house1
    "Currently there was no snow falling, but the cold march weather still caused a chill in the air."
    "A crisp breeze caused the trees to sway back and forth, and made the day feel much harsher than it was. It made the 0 C day feel more like -5 C" 
    "Ryo slung his bag over his shoulder and set out for school. The school was pretty far away over a thirty minute walk away."
    "On normal days Ryo didn't mind that his school was such a distance away, but on cold days like this one he hated it."
    scene black
    "School was hectic the students were all in excitement and it was noisy due to White Day being only a few days away."
    "Ryo settled into his chair and tried to ignore the noisy atmosphere. White Day meant nothing to him, so he had no reason to join in the chatter about it."
    "He had received nothing for any girl on Valentines Day, so he had no obligation to give any girl anything on White Day."
    "Ryo disregarded the nasty words spoken about him and his attitude. He was at the very top of the school in terms of grades."
    "When he first started at the school everyone was impressed with his grades and he was looked up to. But after a while when other students found out how little effort he put into getting those grades, he became despised by almost all the school."
    "Ryo was at the university level already, but his parents had thought it would be better to have him go through high school, like a normal teen. They thought it would be a good experience."
    "However so far the only real thing he had come to experience was how shallow and jealous teens can be, and how envy can change a person."
     
    teacher "Alright settle down. We are going to have a test today. Everyone try do their best."
     
    "Ryo finished filling in the test and then waiting for everyone else to finish."
    
    "The school day dragged on as usual until the sweet sound signaling freedom rang out. Ryo gathered together his stuff and threw it all in his bag before beginning the long journey home."

    scene bridge1
    with fade    
    play music "Music/Water's Surface.ogg" 
    "Ryo stopped when he came to the bridge. Cars zoomed by like normal, drowning out all sound when they passed. The busy street had cars going both ways at a frequent pace almost all hours of the day."
    
    "Something was different. Something was out of place."
    
    "The normally empty bridge had someone standing there. Draped in a black cloak the person seemed to be starring at the water down below."
    
    "Something felt off about this person. They seemed to have entranced them-self in their own little world. As if a bubble was around them, completely shutting out everything around them."
    
    "What was the reason behind their attire. It seemed to offer little to no protection from the wind and the cold. Ryo was curious, the person seemed to different and out of place. He felt that they had a unquiqe and interesting tale."
    
    "Ryo felt that something about this person was special. He wanted to know just why there were there lost in their own world."
    
    "They were a mystery, something different to shake up his boring day to day lifestyle, or at least that is what he hoped."
    
    
menu:
    "Call out to the person":
        $ love_points += 1
        jump choice4_girl
    
    "Ignore the person":
        jump choice4_ignore
        
label choice4_girl:
    
        $ meeting1_flag = True
        "After a brief amount of thought Ryo decided to call out to the person. No matter what happened he hoped that it would be interesting. Something to shake up his boring lifestyle."
        
        r "Hello there."
        
        "Ryo waited for a response but nothing came. The person had either not noticed his presence, or had decided to ignore him."
        
        "Ryo decided to take a more direct approach so he went and stood next to them. He noticed that he stood slightly taller than the person as he glanced down at them." 
        
        "As he tried to get a look at the figure's face, he could tell that the person under the cloak was a girl around his age. He could see a trail of sky blue hair streaking the girl's face."
        
        "The girl's face seemed weary and she appeared to be exhausted. Her skin was deathly pale, and she appeared grossly underweight."
        
        "What appeared to be pearls seemed stitched onto the lining of the hood and they hung down over her face. Ryo felt that she must be freezing for aside from her cloak the only thing she wore was a light green sundress," 
        
        "She stared down at the water with an expression that was not a frown nor a smile, but rather something in between."
        
        r "Hello there. Aren't you cold with what you are wearing."
        scene bridge2
        with Dissolve(.5)
        pause 2.0
        show eve 1b
        with Dissolve(.5)
        "The girl turned slightly and looked up at Ryo. Her cerulean eyes blinked as she stared at him with an indifferent expression."
        
        e "What is it? Are you talking to me?"
        
        "Her voice was soft and quiet. But under that was the tone akin to a sparrow, melodious and sweet."
        
        "Her hand she held in front of her chest shook with uncertainty and fright. She did not appear used to speaking to strangers."
        
        "Ryo hand a hand through his hair, messing it up even more than the wind had. Dealing with people was never one of his strong points, which stemmed out from many unfortunate previous encounters."
        
        r "Yes, I was. I was just curious how you managed to stay warm with what you are wearing."
        
        "She turned her head to the side with a slightly confused expression on her face."
        show eve 3
        with Dissolve(.5)
        e "You get used to it after a while."
        
        "Ryo raised his eyebrows wondering just what kind of answer was that."
        
        r "So you aren't cold?"
        show eve 5
        with Dissolve(.5)
        "The girl shook her head."
        
        e "No, I am very cold. Freezing in fact."
        
        r "Huh.."
        
        r "Why didn't you just say that in the first place?"
        show eve 1b
        with Dissolve(.5)
        e "You asked me how I managed it. Not if I was cold."
        
        "Ryo stripped himself of his coat and held it out to the girl."
        
        r "Here. You said you were freezing."
        show eve 2b
        with Dissolve(.5)
        e "Oh no, I couldn't. You will be cold then." 
        
        r "I'm lending it to you, since you are cold. I'm fine, I just came from a warm building. I don't need it."
        
        "It was a huge lie. With the distance he still had to walk, a coat would be a nice accessory, but still he wanted to give this girl it. She appeared to need it more than he did, or at least that is how it felt."
        scene bridge1
        with Dissolve(.5)
        pause 2.0
        show eve 4b
        with Dissolve(.5)
        e "Thank you, I'll cherish it."
        
        r "I'm not giving it to you! I'm... I'm just lending it to you. Actually... just forget it. You can have it." 
        
        "Ryo was about to enforce that he was just lending it to her, and not giving it away, but he stopped when he saw the light in her eyes as she stared at the coat."
        
        r "I'm Ryo. And you are?"
        show eve 4
        with Dissolve(.5)
        e "Eve."
        
        r "Nice to meet you Eve."
        
        "Ryo extended his head allowing for handshake."
        show eve 6
        with Dissolve(.5)
        "Eve stared at his hand with a confused expression on her face. After a few seconds her eyes grew wide in realization." 
        
        "She shoved the coat into Ryo's hand while bowing politely." 
        show eve 2b
        with Dissolve(.5)
        e "I'm sorry."
        
        "Eve cried out in a desperate voice before turning and making a break for the other side of the bridge."
        hide eve 2b
        with Dissolve(1.0)
        "Ryo stood dumbfounded as he watched her run away."
        
        r "That..." 
        
        r "That wasn't what I meant."
        
        "With a shrug Ryo continued heading home." 
        scene black
        with Dissolve(1.0)
        jump choice4_done
        
label choice4_ignore:
    
        $ meeting1_flag = False
        "Ryo shrugged and decided to just ignore the person. He figured they probably didn't have an interesting story anyway. It was just his imagination running away with him."
        scene black
        with Dissolve(.5)
        jump choice4_done
        
        
label choice4_done:
#night
       play music "Music/White Snow.ogg"
       "Ryo dropped his bag on the floor after arriving home." 
       mom "Ryo, you're home. What would you like for dinner?"
       "Without even turning and acknowledging his mother's existence he headed straight to his room, slamming the door behind him."
       "Hours passed by with the ticking from the clock keeping him company."
       mom "Ryo, it is time for dinner. Why don't you come and eat with us?"
       r "Not interested. Just leave it by the room. I'll eat it when I feel hungry."
       mom "Come on Ryo, why don't you come out. You can tell us all about your day. I'm sure something must have happened."
       r "Nothing happened. It was the same as always. Nothing to tell."
       "Even though it was a lie, Ryo didn't feel like talking. So he figured it would be better to just say nothing happened. He hoped that would make his mother leave him alone."
       mom "I see..."
       mom "Well I'm sure something was different, and if not you can just tell us what the normally happens."
       r "I said I didn't want!"
       r "Geez, just leave me alone."
       "No reply came back."
       r "Finally."
       "Now that no noise was present Ryo rested his head back and allowed himself to drift asleep."

       mom "Ryo, it is time to get up."
       "With grumble Ryo awoke and got ready for school."
       mom "Sit down Ryo I made a good breakfast for you."
       r "No thanks."
       "I'm heading to school."
       mom "But Ryo, you haven't had anything to eat since Lunch. I saw that you never ate dinner."
       r "I'll be fine. I just get something before work."
       "Ryo waved his mother off and headed out the door."
       r "All she does it nag. I'm not hungry."

if meeting1_flag:
       jump jacket_scene

else:
           
        label school1_scene:
        "School was same as always. Ryo found himself waiting for the bell to ring just like a delinquent. He counted the seconds until the bell finally rang."
        Chika "Ryo where are you going?"
        Jiro "Don't you remember Ryo has to work today."
        Shigeru "Aww man, I really wanted Ryo's help with the homework."
        Chika "It can't be helped."
        "Ryo found himself staying behind a little to talk to his friends. Of all the people in the school these three were the only ones to stay around and talk to him."
        r "I'll help you guys out some time. We'll cover over the latest lessons."
        Jiro "We are going to hold you to that Ryo."
        Chika "Yep, you promised, so you can't back out."
        "Ryo chuckled at his friends."
        r "Don't worry. I work break my promise."
        Chika "So right after we get the results back? Does that work for you Ryo?"
        r "Sounds good. I shouldn't have anything going on. But I might have to work, so I don't really know. I can't say for certain."
        Shigeru "Well if you have to work you have to work. Our studying can wait an extra day."
        Chika "But if you don't have to work you have to show up. No excuses."
        r "Don't worry. I'll be there."
        "Ryo waved goodbye to his friends before heading to work."
        jump meeting1_scene
        
label jacket_scene:        
        scene bridge1
        with Dissolve(.5)
        pause .5
        "Ryo stopped in the center of the bridge. The memory of the girl he talked to yesterday rose to the front of his mind."
        r "She looked so cold yesterday. I hope she is going okay."
        "He stared at the spot she stood just yesterday. His mouth fell and became a frown."
        "The wind was even worse than yesterday, making yesterday nothing compared to the chill of today."
        "Ryo scanned the area checking to see if anyone was around."
        "When he realized the coast was clear he took off his jacket and set down on the other side of the bridge. He made sure to hide it in the shadow of the bridge to more prevent people from finding it."
        "After he finished he wrote a small note in the snow."
        "He shrugged. He wasn't sure if Eve would get the riddle he placed. Also there was the chance that someone else could come and take his coat, or it would blow away."
        "Ryo shook of the negative thoughts. He would just have to hope for the best and hope that Eve would get it."
        scene black
        with Dissolve(.5)
        jump school2_scene

label school2_scene:
        "School was same as always. Ryo found himself waiting for the bell to ring just like a delinquent. He counted the seconds until the bell finally rang."
        Chika "Ryo where are you going?"
        Jiro "Don't you remember Ryo has to work today."
        Shigeru "Aww man, I really wanted Ryo's help with the homework."
        Chika "It can't be helped."
        "Ryo found himself staying behind a little to talk to his friends. Of all the people in the school these three were the only ones to stay around and talk to him."
        r "I'll help you guys out some time. We'll cover over the latest lessons."
        Jiro "We are going to hold you to that Ryo."
        Chika "Yep, you promised, so you can't back out."
        "Ryo chuckled at his friends."
        r "Don't worry. I work break my promise."
        Chika "So right after we get the results back? Does that work for you Ryo?"
        r "Sounds good. I shouldn't have anything going on. But I might have to work, so I don't really know. I can't say for certain."
        Shigeru "Well if you have to work you have to work. Our studying can wait an extra day."
        Chika "But if you don't have to work you have to show up. No excuses."
        r "Don't worry. I'll be there."
        "Ryo waved goodbye to his friends before heading to work."
        jump meeting2_scene
        
label meeting2_scene:   
        play music "Music/Water's Surface.ogg" 
        scene bridge1
        with Dissolve(.5)
        pause .5
        "Ryo halted to a stop when he came to the bridge."
        "Eve was standing there looking down at the water. She was wearing the jacket Ryo had left for her."
        "When she heard Ryo approach she turned toward him."
        show eve 2b
        with Dissolve(.5)
        e "Th-"
        e "Th-"
        e "Thanks for the jacket."
        "She burst out while politely bowing toward him." 
        r "You're welcome. I'm just glad you found it."
        show eve 4b
        with Dissolve(.5)
        e "Yes, it took a while, but I finally understood the message."
        r "It seems the coat did just what I wanted it to. You don't see as cold as yesterday."
        e "Yes I am. And it is all thanks to you. For giving me such a gift. I don't know what to say."
        r "Don't worry about it. It is a gift, all you have to do is say thank you and use it."
        show eve 6
        with Dissolve(.5)
        e "Thank you. I will. I won't ever take it off."
        "Ryo let out chuckle."
        r "You don't have to do that. Wearing it while inside your house would be silly."
        "And then a realization came to Ryo."
        r "What if Eve is homeless? What she has right now could be all she has. That coat could be something precious to her, that will allow her to live."
        "Ryo put a hand on her shoulder and gave her a bright smile."
        r "Don't worry. Things will get better. You just have to hold onto that hope, never letting it go."
        "Eve cocked her head to one side with a confused expression on her face. After a few seconds of silence she opened her mouth and spoke."
        show eve 7
        with Dissolve(.5)
        e "You're weird."
        r "I'm weird?"
        show eve 1b
        with Dissolve(.5)
        e "Yes."
        "Eve said it so plainly and in such a bland tone and Ryo couldn't help but burst out laughing."
        e "See. You just proved it. Laughing at a comment like that, is weird." 
        r "I guess so. But if I'm weird doesn't that mean that you are too."
        show eve 3b
        with Dissolve(.5)
        e "Yes."
        r "Eh?"
        "Eve answered instantly and in a plain tone, like there was nothing strange about it."
        "Ryo scratched the side of his hand, confused on how to reply."
        r "I didn't expect you to answer that way."
        show eve 5b
        with Dissolve(.5)
        e "I am weird. I don't act like the mass. I want to be myself, not a clone of society. There isn't anything wrong with doing that. Instead of going along with everyone else, I will choose what I do and what I like."
        e "Even if everyone else thinks it is weird, different, or strange to do such things. I will do what I want to do."
        r "That is..."
        r "An interesting outlook on life."
        show eve 6b
        with Dissolve(.5)
        e "Is it?"
        r "Yeah, it is really different. Not many people would say something like that."
        show eve 4
        with Dissolve(.5)
        e "I just made it up, just now."
        r "Eh?"
        e "Were you impressed?"
        r "Kind of."
        show eve 1
        with Dissolve(.5)
        e "You are still weird by the way."
        r "I'm weird?"
        show eve 5b
        with Dissolve(.5)
        e "Yes. You are. You are very weird."
        r "I think if either of is weird, it would be you."
        show eve 1b
        with Dissolve(.5)
        e "Deja vu."
        r "Huh?"
        e "We already went through this."
        e "I am weird. I don't act like the mass. I want to be myself, not a clone of society. There isn't anything wrong with doing that. Instead of going along with everyone else, I will choose what I do and what I like."
        e "Even if everyone else thinks it is weird, different, or strange to do such things. I will do what I want to do."
        r "Yeah... I know you just made that up."
        show eve 5
        with Dissolve(.5)
        e "Nope."
        r "Nope? What?!"
        show eve 4
        with Dissolve(.5)
        e "Nope. I made it up 2 minutes ago."
        r "...."
        r "Right..."
        show eve 6b
        with Dissolve(.5)
        e "You are fun to play with."
        r "What am I a toy for you to tease?"
        show eve 1b
        with Dissolve(.5)
        e "Yes."
        r "I didn't expect her to answer like that. She really is weird."
        r "Well. This has been interesting, but I have to go to work."
        r "See ya Eve."
        "Ryo called out as he walked past her heading towards the other side of the bridge."
        show eve 7
        with Dissolve(.5)
        e "Wait."
        "Ryo stopped and turned back to her when she called out."
        e "...."
        e "If you are free."
        "Eve stopped and turned back towards the water."
        r "What was that?"
        show eve 10b
        with Dissolve(.5)
        e "....."
        r "....."
        e "....."
        e "Could you visit me again?"
        r "Sure."
        show eve 8b
        with Dissolve(.5)
        e "Thank you."
        jump food_scene

label meeting1_scene:
        play music "Music/Water's Surface.ogg"
        scene bridge1
        with fade
        "Ryo halted to a stop when he came to the bridge."
        "The person from yesterday stood there, dressed in the same cloak from yesterday."
        "Ryo decided this time he was going to call out to the person."
        r "Hey. This is the second time I've seen you standing here. What are you doing?"
        "The figure turned towards Ryo and stared back him."
        show eve 1
        with Dissolve(.5)
        e "I'm just looking at the water."
        r "Why?"
        show eve 4
        with Dissolve(.5)
        e "Because I like it."
        r "That isn't really an answer."
        show eve 4b
        with Dissolve(.5)
        e "It isn't?"
        r "No, it isn't."
        show eve 6b
        with Dissolve(.5)
        e "Really?"
        r "Yes, really."
        show eve 7b
        with Dissolve(.5)
        e "Are you sure?"
        r "Yes, I'm sure."
        e "Why isn't it an answer?"
        r "Because it doesn't explain anything."
        show eve 2b
        with Dissolve(.5)
        e "Why doesn't it explain anything?"
        r "Because it is vague."
        show eve 6
        with Dissolve(.5)
        e "Really?"
        r "Yes."
        show eve 7
        with Dissolve(.5)
        e "Are you sure?"
        r "Yes."
        show eve 2b
        with Dissolve(.5)
        e "Why?"
        r "Because you still have no answered my question?"
        show eve 10b
        with Dissolve(.5)
        e "Are you sure?"
        r "Yes."
        show eve 6
        with Dissolve(.5)
        e "How haven't I answered your question?"
        r "Because you didn't explain anything?"
        show eve 2b
        with Dissolve(.5)
        e "How so?"
        r "Stop that. We are just going around in circles."
        show eve 6b
        with Dissolve(.5)
        e "Really?"
        r "Ye-"
        r "You are doing it again."
        show eve 5b
        with Dissolve(.5)
        pause 1.0
        show eve 4
        with Dissolve(.5)
        e "So you want me to answer your question?"
        r "Yes."
        e "Which question?"
        r "Uh..."
        r "The first one."
        e "I'm talking to you."
        r "Huh."
        show eve 3b
        with Dissolve(.5)
        e "You asked what I was doing. So I just told you what I am doing. Looking at you. Though why you asked that I'm not sure."
        "Ryo let out a sigh and shook his head at the whole mess. He wasn't sure if she was actually not sure what was going on, or if she was just messing with him. He guessed the latter."
        r "Alright the second question then."
        show eve 5b
        with Dissolve(.5)
        e "Because I like it."
        r "But why do you like it?"
        show eve 5
        with Dissolve(.5)
        "She shrugged."
        e "I just do."
        r "Surely you must have a deeper reason. Now go into more depth."
        show eve 4
        with Dissolve(.5)
        e "It makes me feel at ease."
        r "And?"
        e "Watching the water moving just makes me relaxed. It makes me think of life, how it is always moving. For everyone out there, life is always moving, things are always changing."
        e "We have no choice but to go along our path. No matter if we want it or not, we must travel on this path."
        e "But it isn't all that bad, for even if a change occurs that we don't like. Changes that we will like will eventually come along. It is all a part of life."
        e "Life is a series of ups and downs, it is never one or the other, even at our happiness a down will come."
        e "And even in the darkest hour, there will be a slight moment of happiness. Now these might not really change how far down or up the river is right now, but it does occur."
        e "There are good times and there are bad, and they will always mix. You can't have one without the other."
        e "It is the bad times that make the good times that much better. If nothing ever changed life would be boring. It would be like a dam in the river."
        e "Nothing would change, nothing would move, things would always be the same, and after a while, that would grow boring."
        e "The moving water is a sign that reminds us that even in the dark times things will get better, for changes will always keep happening around us."
        r "Where did that come from?"
        e "From my mind."
        r "And why didn't you just answer like that in the beginning?"
        show eve 4b
        with Dissolve(.5)
        e "I didn't feel like it."
        r "You didn't feel like it."
        e "Yep." 
        r "Wh-"
        r "Wait... I know where that will lead. Just forget it."
        show eve 1b
        with Dissolve(.5)
        e "I'm Eve. And you are?"
        r "Ryo."
        show eve 2b
        with Dissolve(.5)
        e "What am I supposed to forget Ryo?"
        r "What I just said."
        show eve 4b
        with Dissolve(.5)
        e "Hi I'm Eve, and you are?"
        r "Haha..."
        r "I walked into that one."
        show eve 1
        with Dissolve(.5)
        e "Yes, yes you did. You walk into a lot of them actually. Are you an idiot or something."
        r "Actually more along the lines of a genius."
        show eve 16b
        with Dissolve(.5)
        e "That is a good one."
        r "I'm serious."
        show eve 1b
        with Dissolve(.5)
        e "Well you are pretty stupid one then."
        e "You don't seem to have much common sense."
        show eve 4b
        with Dissolve(.5)
        e "But that makes you fun."
        r "Because you like to mess with people."
        e "Yep."
        r "You're really different."
        show eve 5b
        with Dissolve(.5)
        e "Hmm... how so?"
        r "Most people wouldn't admit to something like that."
        show eve 3b
        with Dissolve(.5)
        e "Well, I'm not most people."
        r "I can tell."
        show eve 7
        with Dissolve(.5)
        e "Boo.. and now you're just being a killjoy."
        e "Boring..." 
        e "Lame..."
        e "I'm out of here."
        e "......"
        r "......"
        show eve 20b
        with Dissolve(.5)
        e "What aren't you going to say anything?"
        r "Like what?"
        show eve 10b
        with Dissolve(.5)
        e "Please don't go Eve. I need you, you are so interesting to talk to. You lighten up my boring, dull, gray, drab, pathetic, worthless life."
        r "That is too many adjectives."
        show eve 21b
        with Dissolve(.5)
        e "That was the point, genius. Congrats you get a gold star."
        r "Like I need more of those. I have enough awards already." 
        e "Awards you made and gave yourself don't count."
        r "They weren't!"
        show eve 5b
        with Dissolve(.5)
        e "Whatever you say, genius."
        r "You're going to use that as a nickname now aren't you."
        show eve 4
        with Dissolve(.5)
        e "Yep."
        r "No matter what I say."
        e "Yep"
        r "Great..."
        show eve 2
        with Dissolve(.5)
        e "Why so glum, genius."
        r "Nothing you need to worry about."
        show eve 7
        with Dissolve(.5)
        e "Awww.. don't be that way. You don't have to be secretive with me."
        r "Yeah... no. I'm not going to start talking all about myself with someone I just met. I have that much common sense."
        r "What? Did you really think I was going to tell you?"
        show eve 10b
        with Dissolve(.5)
        e "No, of course not."
        r "Your expression says otherwise."
        show eve 7
        with Dissolve(.5)
        e "Hey..."
        e "It is okay for you to talk to me again. Got that."
        r "Like I need your permission."
        hide eve 7
        with Dissolve(.1)
        "Ryo had only looked away for a moment, and during that time Eve had vanished."
        r "Where did she go?"
        "And then he spotted her at the other side of the bridge."
        e "Remember it."
        jump work_scene
            
label food_scene:
play music "Music/White Snow.ogg"
$ love_points += 1
"Ryo found himself in a daze until the end of school the next day. His mind wandered to Eve, she was so different, so unique. It made him want to talk to her again. To look forward to their next meeting."
scene bridge1
with Dissolve(.5)
pause .5
"Ryo stopped running when he reached the bridge. There she stood, however something was different. She wasn't looking down at the water but instead up at the clouds."
scene bridge2
with Dissolve(.5)
pause .5
r "Not looking at the water today?"
show eve 4
with Dissolve(.5)
e "Of course not. I don't come here daily and stare at the water for hours. That would be boring and get old."
"Ryo shrugged, he couldn't argue with that. It would get boring to just stare at water for hours on a daily basis."
r "So you are watching the clouds today?"
"Eve nodded, she still hadn't turned toward him. Rather the sky seemed more interesting to her, then he did."
r "You not even going to say 'hello'?"
e "Hello."
r "Very funny."
r "So you aren't even going to pay any attention to me, even though just yesterday you were crying out for me to come talk to you again."
e "That was then, this is now."
r "So the sky is more interesting then I am."
"Another nod."
show eve 4
with Dissolve(.5)
e "However, I'm not watching the sky. I am watching the clouds."
r "Same thing."
e "Not really."
r "So the sky is more interesting than me."
show eve 1b
with Dissolve(.5)
e "Dirt is more interesting than you."
r "That's..."
r "Really harsh."
e "Well to a pedologist, dirt is more interesting than you."
r "Are you one?"
e "One what?"
r "......."
r "Nope, not falling for it."
show eve 4b
with Dissolve(.5)
e "No, I do not study soil. Today I'm biologist."
r "Are you sure you're not a nepholologist."
show eve 9b
with Dissolve(.5)
e "Too many big words. It hurts."
e "If you agree to stop using big words, I'll pay attention to you, okay?"
r "But you were the one who started it."
r "Fine."
show eve 1
with Dissolve(.5)
e "Good."
r "....."
e "....."
r "....."
e "....."
r "...So why are you studying the clouds?"
show eve 6
with Dissolve(.5)
e "Who said I was studying the clouds?"
r "You did."
show eve 3
with Dissolve(.5)
e "I did not."
e "I'm not studying the clouds. I'm watching them."
r "Pretty much the same thing."
scene bridge1
with Dissolve(.5)
pause 2.0
show eve 5
with Dissolve(.5)
e "Nope."
r "Why are you watching the clouds then."
show eve 4b
with Dissolve(.5)
e "Because clouds are interesting. A lot of people don't like them, because they block out and ruin a 'sunny day.' But I enjoy them for they are different. If they didn't exist everything would be ruined."
e "Without clouds everyday would be sunny thus making it get old after a while, with clouds comes change, things are different. Without clouds we would have no rain or snow."
r "But there wouldn't be any bad storms without clouds."
e "Sure there are elements that we don't enjoy about them, but if we took away them, things would be worse off. Don't you think life is like that, everything has a purpose."
e "All the hardships you are going through and all the good times as well they have purpose."
e "Without them, you might be a completely different person, everything that happens to you shapes you."
e "How much will our meeting shape us, one can't say, but we can be sure that it will influence us. Even if we don't realize that it is, we are changing due to the stuff around us."
e "This won't stop happening until we die, we will constantly be changing due to our experiences."
r "How did we get from clouds to this?"
e "Clouds also reveals just how horrid life is. At any time a storm could get worse and could take someone's life. It is really unfair, that such a thing could happen."
e "Life is merciless and cruel, but it isn't without grace a beauty. For once the storm passes a wondrous rainbow will fill the sky."
"A loud grumble roared out, just before Eve put a hand to her stomach."
show eve 7b
with Dissolve(.5)
e "I'm hungry..."
r "That was a quick subject change."
e "What to do....."
e "So hungry..."
r "That's right. Eve might be homeless, she probably has to struggle just to get food most of the time."
r "Don't worry Eve, I'll treat you."
show eve 6b
with Dissolve(.5)
e "Really? Ryo, thank you."
r "It's no problem. We just need to stop by the work first and tell them I need the day off."
show eve 2
with Dissolve(.5)
e "Won't that get you in trouble?"
r "Don't worry about it. It will be fine. Seeing you worried over something is weird, stop that."
hide eve 2
with Dissolve(1.0)
pause 2.0
scene black
with Dissolve(1.0)
"The two of them made a quick stop at Ryo's workplace to request the day off. Despite it being such short notice, he recived the day off and the two of them heading to fast food place nearby."
scene food1
with fade
"Eve went to sit down at a booth while Ryo ordered the food. Ryo returned a few minutes later with 2 hamburgers. He gave one to Eve before sitting down across from her."
"He was about to take a bite of his own hamburger, when he looked over at Eve. His hands became frozen, and he slowly lowered the food."
"Eve was cutting her hamburger into little pieces with a knife and fork. She cut into the hamburger slicing it into tiny precise pieces before picking one up with her fork."
"After she finished swallowing she took her napkin and patted it against her lips."
show eve 4b
with Dissolve(.5)
e "What? What's wrong?"
r "Uhhh... What are you doing?"
e "Eating the food you gave to me."
r "No... I mean with the fork and knife."
show eve 5b
with Dissolve(.5)
e "I'm eating proper and politely. Is there something wrong with that?" 
r "No... But it looks weird. A hamburger normally isn't eaten that way."
r "......"
r "......"
r "I didn't mean for you to wolf down your food. You switched from being overly polite to overly messy and rude."
show eve 11
with Dissolve(.5)
e "Make up, your mind. You are so picky."
"After making that comment Eve started eating like a normal person."
r "You were just messing with me weren't you."
show eve 6b
with Dissolve(.5)
e "Me? I would never."
show eve 16b
with Dissolve(.5)
"The meal continued with light conversation throughout." 
show eve 6
with Dissolve(.5)
e "Ryo!"
hide eve 6
with Dissolve(.3)
"Eve jumped up from her seat and ran out the door, leaving Ryo behind with a confused expression."
r "...."
r "What was that about?"
r "Eve, what is going on? Why did you run out of the place?"
scene black
with Dissolve(.5)
pause 1.0
scene lot4
with fade
pause 2.0
show eve 17
with Dissolve(.5)
e "Ryo, look."
e "It is snowing!"
"Eve began to spin around as the snow swirled around her."
r "So?"
show eve 19
with Dissolve(.5)
e "So. Snow is great. It is so wondrous and beautiful."
e "It is so amazing. I love the snow."
"Eve laughed and giggled as she danced around in the snow like a little kid seeing snow for the first time."
r "What are you doing?"
show eve 18b
with Dissolve(.5)
e "Dancing. Come on Ryo join me. It will be fun."
r "Are you crazy, people could be watching."
show eve 16b
with Dissolve(.5)
e "So?"
r "Aren't you embarrassed to do something like that?"
show eve 18
with Dissolve(.5)
e "Nope."
"Eve ran over and snatched up Ryo's arm tugging on it pleadingly."
show eve 19
with Dissolve(.5)
e "Come on Ryo. Dance with me."
r "You're crazy."
show eve 16
with Dissolve(.5)
e "You never know when you are going to die. When your life will be unfairly ended, so why not do something you want to do, even if others would shake their heads and laugh at such things. If you enjoy it, isn't that the point." 
e "Who cares if people point and laugh, as long as you are laughing too."
"Ryo gave her a pointed look."
r "Didn't you just justify every thief and killer in the world?"
"Eve stopped tugging on Ryo's arm, and her smile left her face."
show eve 12
with Dissolve(.5)
e "No..."
e "I would never."
show eve 12b
with Dissolve(.5)
e "There is a difference between doing something that harms no one, and something that harms others. Even if you do it because 'I only have one life and I don't know when I'm going to die.' I can't accept it."
e "Just because you can do something doesn't mean it is right, or you should do it."
show eve 17
with Dissolve(.5)
e "Now enough of such a dark topic. Dance with me!"
hide eve 17
with Dissolve(1.0)
"Ryo let out a sigh and let Eve have her way. He stopped resisting, and the two of them began to waltz, among lots of other classical types of dance, in the snow."
scene black
with Dissolve(.5)
scene lot1
with fade
r "Why do you enjoy the snow so much Eve?"
"Eve stopped dancing and let go of Ryo's hand."
show eve 16b
with Dissolve(.5)
e "Because it feels like I've transcended. I've left the world I'm used to and entered a different wondrous world. Watching the snow fall is an amazing thing, it is something so delicate and pretty."
e "Rain feels heavy and dark. But snow feels light and airy, it is like I'm in a fairy tale."
r "You like that kind of feeling? Of being in an another world."
show eve 18b
with Dissolve(.5)
e "Yeah."
show eve 6
with Dissolve(.5)
e "Hey Ryo, do you think we could have a snowball fight?"
show eve 2
with Dissolve(.5)
e "Wait..."
e "There probably isn't enough snow yet."
show eve 8
with Dissolve(.5)
e "We'll just have to hope it keeps snowing so we can do it."  
show eve 19b
with Dissolve(.5)
e "I can't wait. It will be so much fun."
show eve 5b
with Dissolve(.5)
e "..."
show eve 16b
with Dissolve(.5)
e "Hey Ryo, you ever think about how lucky you are?"
r "I'm lucky?"
e "Seems that way to me. You are gifted with brains-"
r "Something I get harassed over."
e "People will always be jealous over something they don't have."
r "I suppose so."
e "Even if someone works so hard for something, and when they finally get it, even then will someone out there be envious. Even though the person earned it."
e "Do you believe you earned your brains?"
r "Not really."
show eve 6b
with Dissolve(.5)
e "Why?"
r "Because I've just breezed through life. Not really studying, everyone studies way harder, but I do better."
show eve 3
with Dissolve(.5)
e "Then why don't you actually go for it. Do just the same effort they did, show that you deserve your smarts."
r "I don't think that will change anyone's opinion."
e "Did I said it would?"
show eve 4
with Dissolve(.5)
e "It won't change others opinion, but it will change how you feel about it."
e "Be confident, show that you have earned your talents, and then use them to their fullest."
e "You are just wasting them if you don't do anything with them."
r "So I can use my talents to graduate early, big deal."
e "I'm sure you can use them for other things, also you probably have more talents than just that. You just haven't found them yet."
r "And what are your talents."
show eve 5b
with Dissolve(.5)
e "Hmm..."
show eve 2b
with Dissolve(.5)
e "Dunno. Haven't found them out yet."
r "Really?"
show eve 16b
with Dissolve(.5)
e "Or maybe I have, but they are secret."
"Eve put a finger to her lip and winked at Ryo."
e "See ya tomorrow Ryo."
"She waved to him as she called out."
show eve 19b
with Dissolve(.5)
e "And you better show up!"
hide eve 19b
with Dissolve(.3)
"She shouted before running off."
scene black
with Dissolve(.5)
$ money_flag = False
jump choice5_end

label work_scene:
$ love_points += 1
play music "Music/White Snow.ogg"
"Ryo found himself in a daze until the end of school the next day. His mind wandered to Eve, she was so different, so unique. It made him want to talk to her again. To look forward to their next meeting."
scene bridge1
with fade
"Ryo stopped running when he reached the bridge. There she stood, however something was different. She wasn't looking at the water, but instead she was staring at the street."
r "Not looking at the water today?"
show eve 4
with Dissolve(.5)
e "Of course not. I don't come here daily and stare at the water for hours. That would be boring and get old."
"Ryo shrugged, he couldn't argue with that. It would get boring to just stare at water for hours on a daily basis."
r "So what are you doing?"
scene bridge4
with Dissolve(.5)
pause 2.0
show eve 1
with Dissolve(.5)
e "People watching."
r "What for?"
e "Haven't you ever just watched the people pass by you and make up lives for them. Where they are going, what their life is like, their hopes and dreams?"
r "Can't say I have."
show eve 3b
with Dissolve(.5)
e "I figured so. You are very boring, it is to be expected."
e "Well, either way you should try it some time. It is interesting."
e "You use your imagination and everything you notice about the person to create a life for them."
r "That is... weird."
show eve 4
with Dissolve(.5)
e "Is it?"
pause 1.0
e "I'm hungry..."
r "Well, I have to get to work, so see ya."
e "Bye."
hide eve 4
with Dissolve(2.0)
scene black
with Dissolve(.5)
pause 1.0
scene store1
"Ryo tried to focus at work, but he founds his thoughts drifting back to Eve."
r "She said she was hungry."
"In the end he couldn't ignore it and he bought a cheap candy bar, and once his shift ended he headed off the find Eve."
scene lot2
with Dissolve(.5)
pause 1.0
"He didn't have to look long for he found her in the parking lot."
r "Eve?"
show eve 6
with Dissolve(.5)
e "Oh, hi Ryo."
r "What are you doing?"
show eve 4b
with Dissolve(.5)
e "Waiting for the snow."
r "Why?"
scene lot3
with Dissolve(.5)
pause 2.0
show eve 4
with Dissolve(.5)
e "I just feel like it is going to snow, and here is such a nice place to see it." 
"Ryo shook his head, he would never understand her."
r "Here, this is for you."
show eve 17
with Dissolve(.5)
e "Oo! Candy!"
"Eve snatched up the candy bar and scarfed it down."
show eve 18
with Dissolve(.5)
e "Thanks Ryo."
show eve 6
with Dissolve(.5)
e "Ryo, look."
show eve 17
with Dissolve(.5)
e "It is snowing!"
"Eve began to spin around as the snow swirled around her."
r "So?"
scene lot4
with Dissolve(.5)
pause 2.0
show eve 19
with Dissolve(.5)
e "So. Snow is great. It is so wondrous and beautiful."
e "It is so amazing. I love the snow."
"Eve laughed and giggled as she danced around in the snow like a little kid seeing snow for the first time."
r "What are you doing?"
show eve 18b
with Dissolve(.5)
e "Dancing. Come on Ryo join me. It will be fun."
r "Are you crazy, people could be watching."
show eve 16b
with Dissolve(.5)
e "So?"
r "Aren't you embarrassed to do something like that?"
show eve 18
with Dissolve(.5)
e "Nope."
"Eve ran over and snatched up Ryo's arm tugging on it pleadingly."
show eve 19
with Dissolve(.5)
e "Come on Ryo. Dance with me."
r "You're crazy."
show eve 16
with Dissolve(.5)
e "You never know when you are going to die. When your life will be unfairly ended, so why not do something you want to do, even if others would shake their heads and laugh at such things."
e "If you enjoy it, isn't that the point. Who cares if people point and laugh, as long as you are laughing too."
"Ryo gave her a pointed look."
r "Didn't you just justify every thief and killer in the world?"
"Eve stopped tugging on Ryo's arm, and her smile left her face."
show eve 12
with Dissolve(.5)
e "No..."
e "I would never."
show eve 12b
with Dissolve(.5)
e "There is a difference between doing something that harms no one, and something that harms others. Even if you do it because 'I only have one life and I don't know when I'm going to die.' I can't accept it." 
e "Just because you can do something doesn't mean it is right, or you should do it."
show eve 17
with Dissolve(.5)
e "Now enough of such a dark topic. Dance with me!"
hide eve 17
with Dissolve(1.0)
"Ryo let out a sigh and let Eve have her way. He stopped resisting, and the two of them began to waltz, among lots of other classical types of dance, in the snow."
scene black
with Dissolve(.5)
scene lot1
with fade
r "Why do you enjoy the snow so much Eve?"
"Eve stopped dancing and let go of Ryo's hand."
show eve 16b
with Dissolve(.5)
e "Because it feels like I've transcended. I've left the world I'm used to and entered a different wondrous world. Watching the snow fall is an amazing thing, it is something so delicate and pretty."
e "Rain feels heavy and dark. But snow feels light and airy, it is like I'm in a fairy tale."
r "You like that kind of feeling? Of being in an another world."
show eve 18b
with Dissolve(.5)
e "Yeah."
show eve 6
with Dissolve(.5)
e "Hey Ryo, do you think we could have a snowball fight?"
show eve 2
with Dissolve(.5)
e "Wait..."
e "There probably isn't enough snow yet."
show eve 8
with Dissolve(.5)
e "We'll just have to hope it keeps snowing so we can do it."  
show eve 19b
with Dissolve(.5)
e "I can't wait. It will be so much fun."
show eve 5b
with Dissolve(.5)
e "..."
show eve 16b
with Dissolve(.5)
e "Hey Ryo, you ever think about how lucky you are?"
r "I'm lucky?"
e "Seems that way to me. You are gifted with brains-"
r "Something I get harassed over."
e "People will always be jealous over something they don't have."
r "I suppose so."
e "Even if someone works so hard for something, and when they finally get it, even then will someone out there be envious. Even though the person earned it."
e "Do you believe you earned your brains?"
r "Not really."
show eve 6b
with Dissolve(.5)
e "Why?"
r "Because I've just breezed through life. Not really studying, everyone studies way harder, but I do better."
show eve 3
with Dissolve(.5)
e "Then why don't you actually go for it. Do just the same effort they did, show that you deserve your smarts."
r "I don't think that will change anyone's opinion."
e "Did I said it would?"
show eve 4
with Dissolve(.5)
e "It won't change others opinion, but it will change how you feel about it."
e "Be confident, show that you have earned your talents, and then use them to their fullest."
e "You are just wasting them if you don't do anything with them."
r "So I can use my talents to graduate early, big deal."
e "I'm sure you can use them for other things, also you probably have more talents than just that. You just haven't found them yet."
r "And what are your talents."
show eve 5b
with Dissolve(.5)
e "Hmm..."
show eve 2b
with Dissolve(.5)
e "Dunno. Haven't found them out yet."
r "Really?"
show eve 16b
with Dissolve(.5)
e "Or maybe I have, but they are secret."
"Eve put a finger to her lip and winked at Ryo."
e "See ya tomorrow Ryo."
"She waved to him as she called out."
show eve 19b
with Dissolve(.5)
e "And you better show up!"
hide eve 19b
with Dissolve(.3)
"She shouted before running off."
scene black
with Dissolve(.5)
$ money_flag = True
jump choice5_end

label choice5_end:
play music "Music/Firefly.ogg"
r "What I have?"
r "I should be working just as hard as everyone else? Would that really help?"
r "Compared to Eve, I have so much, and she has almost nothing."
r "I have a home to return to each night. That is something not everyone has. I have food that is always given to me, which I don't accept."
r "...."
r "I have been taking things for granted. I should be thankful for what I have."
r "I guess my smarts should be one of those too."
r "Work hard, and use my talents."
r "I guess that is what I should really be doing."



#(School)
play music "Music/Water's Surface.ogg"
Chika "Hey, Ryo. You're been acting different all day."
Jiro "I see, I wasn't the only one who noticed."
Shigeru "Yeah, what's up."
r "Nothing really, I've just decided to appreciate what I have, and use my talents, instead of do nothing."
Jiro "So does that mean you are going to do all our homework for us, from now on?"
r "No."
r "You wouldn't learn anything if I just did all your homework. I'm still only going to help you guys with studying."
Jiro "Rats."
Shigeru "Ryo, we could really use your help. How about a study session right now. You don't have to work today, right?"
Chika "Awesome, I was having trouble with the homework."
r "Sorry, I can't."
Shigeru "So you do have to work?"
r "No, I don't have to work, but I do have other plans." 
Chika "Oh. Okay, we will just have to do it some other time then."
Shigeru "Yeah, no big deal. See ya Ryo."



#(Meeting)[snowball fight]
play music "Music/Peaceful Days.ogg"
scene bridge1
with fade
"Ryo found himself running to get to the bridge. He was looking forward to spending time with Eve again."
r "She isn't here."
"Ryo frowned as he looked around for Eve."
r "And she was the one who ordered me to be here."
e "Alright troops. Fire! Annihilate the target!"
"A small army of little kids along with Eve suddenly ran out from under the shadow of the bridge. And in seconds Ryo was pelted with snowballs."
show eve 21b
with Dissolve(.5)
e "Keep going! Don't let up until the enemy surrenders!"
"Ryo had no time to react as snowballs flew at him with the rapid pace akin to that of a machine gun."
r "I surrender. I surrender"
e "Alright troops you heard him. Stop firing."
"Once the bombardment had stopped Ryo stood and addressed Eve."
r "What was that about?"
show eve 16b
with Dissolve(.5)
e "I told you I wanted to have a snowball fight, didn't I?"
r "You did, but what is with the little kids."
e "I thought it would be funner if we had our own little armies, and they didn't seem to be doing anything. Plus they thought it sounded fun, and agreed to play."
"Ryo looked down at the kids, they all appeared to be as Eve had said, really excited to play."
"Letting out a sigh, Ryo didn't protest."
r "Alright. They seem to really want to play, so I won't say anything."
show eve 19b
with Dissolve(.5)
e "Great. Okay, these three are on your team. They are you army, and you are the commander."
show eve 16
with Dissolve(.5)
e "If your solders get hit twice they are out of the game. But we only have to be hit once."
e "No making rocks in your snowballs, and so on. You can only use snowballs on each other."
r "I would be worried if that wasn't the case."
e "Your base will be the park. Mine will be the parking lot."
e "And will begin the game in 5 minutes, so be ready."
show eve 18
with Dissolve(.5)
e "Alright troops, march with me as we discuss strategy."
show eve 19
with Dissolve(.5)
e "Everyone sing with me."
e "I don't know what you've been told."
k5 "I don't know what you've been told."
hide eve 19
with Dissolve(1.0)
e "But Ryo's heart is ice cold."
k5 "But Ryo's heart is ice cold."
e "Second verse."
e "I don't know what you've been told."
k5 "I don't know what you've been told."
e "But his arm is as strong as mold."
"Ryo burst out laughing at Eve antics until she was out of sight."
r "Alright. Here is the plan. We are just going to be on the defensive. I doubt Eve will play defensively, so she will probably charge us as soon as the game starts."
scene black
with Dissolve(.5)
pause 2.0
scene park2
with Dissolve(.5)
"Ryo's group stayed huddled up in the arbor, waiting for the enemy to strike back."
"Minutes passed by, but still they hadn't seen any sign of the enemy. Ryo was about to say he was wrong about Eve, when he assumptions were proven correctly."
scene park1
with Dissolve(.5)
"Eve put down the trumpet and lifted a wooden sword into the air." 
show eve 21b
with Dissolve(.5)
e "Charge! Take no prisoners!"
hide eve 21b
with Dissolve(.2)
r "Get ready. Here they come."
"Three little kids rushed out from behind a large mound of snow. In their hands they held trash can lids. They used their make shift shields to block all incoming snowballs"
r "They have shields. Eve that is cheating, you said only snowballs."
e "I said you can only use snowballs on each other, I never said you couldn't use shields."
r "You had this planned. That's cheating."
e "Is not. War is all about being prepared. The one who uses the most strategy and cunning wins."
k1 "Fear not captain I will get them."
"The kid ran by Ryo and burst out of the arbor and rushed toward the incoming army."
k2 "Man down! Man down!"
"Ryo shook his head at the whole event."
r "Well that was pointless."
e "Keep advancing, they are already down to 3. We shall not fall. The unstoppable army from the kingdom of Evenia shall prevail."
r "We can't give up. So what if we are out numbered now and they have shields. We can still win right?!"
k4 "Yeah!"   
r "Just keep firing, they can't block everything. Eventually we will hit."
k2 "No, Takashi."
r "Mika, don't give out on me now. It is just you and me now. I need all the help I can get."
k2 "Yes, Sir."
e "You are finished Ryo. You are trapped."
scene park2
with Dissolve(.5)
pause 1.0
scene park3
with Dissolve(.5)
"Ryo had already noticed it. There was only 2 ways to leave the arbor, and Eve had dispatched at least one child to each side."
r "Mika, I have a plan. We will both rush the exit that only has 1 child. I will draw his attention, and then you run by him, and head for Eve. It is up to you, you have to take her out."
k2 "I'm sorry. I've been hit."
r "Mika! Noooo!"
show eve 21b
with Dissolve(.5)
e "This is the end Ryo. You are the only one left alive. It won't be long, before we capture you, and torture you until you reveal the secrets on to take down the kingdom of Ryoddela."
r "Never! I will spill nothing!"
"Ryo climbed over the railing of the arbor and made a break for the the large snow pile Eve stood in front of."
r "This is between me and you now general of Evenia"
"Eve smirked."
show eve 21b
with Dissolve(.5)
e "That is what you think general. Rule 2 of war, always have a trap set."
"Another child, a fourth solider of Evenia rushed out from behind the snow pile."
e "Fire. Take him down. But don't hit any vital points. We still need him to talk!"
e "Yes! We won! We are the top kingdom. Evenia will never fall!"
r "You cheated you had 1 extra unit."
show eve 20b
with Dissolve(.5)
e "I never said we had the same amount of kids. If fact I even gave you a clue. You were 'Ryoddela,' which contains the word 'odd', and my country was 'Evenia' which has the word 'even' in it."
r "Still was unfair."
show eve 21b
with Dissolve(.5)
e "All is fair in war, General."
scene black
with Dissolve(.5)

#(Parents)

"They played a few more times switching up the teams, and even doing a game where it was Ryo and Eve verses the children, before saying goodbye to the war front."
scene bridge1
with fade
pause 2.0
show eve 18
with Dissolve(.5)
e "Well that was tons of fun."
r "It actually was."
show eve 2
with Dissolve(.5)
e "We should do it again. Actually on second thought, we shouldn't. It won't be as good as this time, so it would be better to just preserve our memories of this time."
r "Eve, what is wrong, you're shaking."
"Ryo wanted to slap himself for not noticing it until now. With what she was wearing of course she would be cold after being outside for sure long."
r "Come on, my house isn't too far. You should warm up."
show eve 1
with Dissolve(.5)
e "That's okay Ryo, I'm fine."
r "No. I insist."
show eve 2b
with Dissolve(.5)
e "Are you sure your parent's won't mind?"
r "Yeah, it will be fine."
show eve 4
with Dissolve(.5)
e "Alright."
hide eve 4
with Dissolve(1.0)
scene black
with Dissolve(.5)
pause 1.0
scene house1e
with fade
pause 1.0
scene house_in1
with Dissolve(.5)
show eve 4
with Dissolve(.5)
e "You have a very nice house, Ryo."
r "Yeah, I guess so."
mom "Ryo, who is this?"
show eve 16b
with Dissolve(.5)
e "I'm please to meet you. I am Eve. Your son invited me to come over and warm up. I thank you for your hospitality."
mom "Oh wow, you're really polite. Maybe you can rub some of that off on Ryo."
e "I'll try."
mom "Eve, why don't you stay for dinner."
show eve 2b
with Dissolve(.5)
e "I couldn't impose."
mom "Nonsense, it is in return for enduring my son."
hide eve 2b
with Dissolve (1.0)
scene black
with Dissolve(1.0)
"Ryo could do nothing but watch as his mother and Eve began talking to each other at a mile a minute."
"Dinner went very awkwardly. Ryo answered with one word responses when addressed. He remained silent otherwise, no matter how hard his parents tried to get him to talk."
"After dinner Eve waved goodbye to Ryo's parents before heading out the door with Ryo."
scene house1e
with fade
play music "Music/Water's Surface.ogg"
show eve 16
with Dissolve(.5)
e "That was fun. You have nice parents Ryo. You're really lucky."
r "You think so?"
show eve 16
with Dissolve(.5)
e "Yep, you should really appreciate them more. Either that, or give them to me."
r "Appreciate them.."
show eve 3
with Dissolve(.5)
e "Yeah, you only have them for so long. You should really enjoy them."
e "Even if they bug you a lot or push you into doing something. They are just doing it because they love you, and care about you."
e "But that doesn't make all their actions right. Even parents can be wrong to, but you should still love them no matter what."
r "Not everyone wants that, nor is is possible sometimes."
show eve 4b
with Dissolve(.5)
e "That's true, there is always exceptions to things. That is why people need to try their best to get along, so that there isn't very many exceptions."
scene black
with Dissolve(.5)
pause 1.0
scene bridge1e
with fade
pause 1.0
show eve 6b
with Dissolve(.5)
e "Oh, this is fine Ryo. I can go the rest of the way by myself."
menu:
    "Bid Eve goodnight.":
        jump choice6_night

    "Refuse and take her the rest of the way.":
        jump choice6_home
 
label choice6_night:
show eve 4
with Dissolve(.5)
$ house_flag = False
e "Goodnight Ryo."
e "Thanks for walking me back. See you tomorrow."

jump choice7_end

label choice6_home:
$ love_points += 1
scene bridge2e
with Dissolve(.5)
pause 3.0
show eve 7
with Dissolve(.5)
e "Really it is fine. I can get home by myself."
r "No, I insist. I'm going to make sure you get back safety."
e "Ryo, I appreciate the gesture, but really, I can get back by myself."

menu:
    "Bid Eve goodnight.":
        jump choice7_night

    "Refuse.":
        jump choice7_home

label choice7_night:
show eve 4b
with Dissolve(.5)
$ house_flag = False
e "Goodnight Ryo."
e "Thanks for walking me back. See you tomorrow."
scene black
with Dissolve(.5)
jump choice7_end

label choice7_home:
$ love_points -= 1
show eve 12b
with Dissolve(.5)
$ house_flag = True
e "You really aren't going to take no for an answer are you."
show eve 12
with Dissolve(.5)
e "Fine. Let's go."
scene black
with Dissolve(.5)
scene street1n
with fade
pause 3.0
scene house2n
with Dissolve(.5)
pause 2.0
show eve 1b
with Dissolve(.5)
e "Here this is where I live."
r "Wait, you live in a house?"
show eve 20b
with Dissolve(.5)
e "Of course. What did you think I lived in dumpster or a box?"
r "Not...exactly."
e "Alright, you've seen, where I live, now go."
r "That's awfully rude."
e "Go."
r "What is with you?"
e "I turn into a rude monster called Eve2 when the sun goes down."
r "Geez, alright. I'm leaving."
hide eve 20b
with Dissolve(1.0)
e "Thanks for walking me back."
r "Huh?"
r "I thought I heard Eve."
r "It must have been in my head."
scene black
with Dissolve(.5)

jump choice7_end

#(Morning Meeting)

label choice7_end:
play music "Music/White Snow.ogg"
mom "Ryo time to get up."
"With groan Ryo turned off his alarm and got ready for school."
scene house_in1
with fade
mom "You will eat breakfast today. So sit down."
r "No th-"
r "Appreciate them.."
"The memories of what Eve said flooded into Ryo's mind."
r "I guess it wouldn't hurt to make an effort."
r "Okay."
"Ryo Mom's mouth fell open as she watched her son sit down, ready to eat breakfast." 
"After some light conversation while eating breakfast Ryo finished getting ready for school."
mom "I wonder who that could be. Ryo could you get the door?"
r "Yeah sure."
scene house1
with Dissolve(.5)
pause 2.0
show eve 17
with Dissolve(.5)
e "Good morning Ryo!"
r "Eve. What are you doing here? I have school today."
e "I know. I just figured I would walk with you to school, so you have some company. It is the least I can do after yesterday."
show eve 16b
with Dissolve(.5)
e "Thanks again for allowing me to stay for dinner. Thank your parents for me later okay."
scene black
with Dissolve(.5)

#(Talking)
 
Chika "Ryo, is today a good day to study?"
r "Sorry guys, but I have plans already."
Shigeru "Alright, but remember we are your friends too, make some room for us."
r "I will."
play music "Music/Water's Surface.ogg"
scene bridge1
with fade
pause 2.0
r "Hi Eve."
show eve 16
with Dissolve(.5)
e "Hello Ryo."
r "Watching the water again?"
e "Yep, I decided to watch the water while waiting for you."
r "You know, I've been wondering this, what is with the outfit you are always wearing? Why don't you ever change clothes, and why are you wearing something like that at this time of year?"
show eve 16b
with Dissolve(.5)
e "Those are good questions."
r "......."
r "......."
r "Are you going to answer them?"
show eve 6b
with Dissolve(.5)
e "Did you want me to?"
"Ryo gave Eve a pointed look."
show eve 4b
with Dissolve(.5)
e "What if I don't want to answer?"
r "Are they some kind of secret?"
e "Come closer."
"Eve whispered gesturing Ryo closer with her hand."
show eve 1b
with Dissolve(.5)
e "Closer."
e "Closer."
r "It is impossible to get closer without us being on top of each other."
show eve 3b
with Dissolve(.5)
e "I'm here on a secret mission. I'm a spy."
r "Wearing clothes that make you stand out?"
show eve 4
with Dissolve(.5)
e "Haven't you ever heard the most inconspicuous is the one who stands out the most."
r "No."
e "Neither had I, I was hoping you had."
r "So, are you going to answer the questions."
show eve 10
with Dissolve(.5)
e "You're still on that? Geez, move on already. You shouldn't be held up by one thing for so long, you will start to brood over it and then after a while it will control your whole life."
r "I don't care. Answer the question."
show eve 8b
with Dissolve(.5)
e "Look at the time. I have to get home. See you tomorrow Ryo."
r "Nice try, but you were waiting for me remember, so that means you have to have some free time."
show eve 2b
with Dissolve(.5)
e "Rats."
r "If you really don't want to answer the questions just tell me so."
show eve 6b
with Dissolve(.5)
e "I really don't want to answer the questions."
r "Too bad, answer them."
show eve 15b
with Dissolve(.5)
e "Why are you so mean Ryo? You're such a nasty person."
r "Good, answer."
show eve 7b
with Dissolve(.5)
e "There is no getting out of this is there.."
r "Nope, I'm not falling for any tricks."
show eve 5b
with Dissolve(.5)
pause 1.0
show eve 3b
with Dissolve(.5)
e "Fine, you win. I'll tell you."
pause 2.0
show eve 1b
with Dissolve(.5)
e "I'm from another world."
show eve 9b
with Dissolve(.5)
e "Ow."
"Ryo lightly smacked Eve on the head."
r "Stop joking around. I really want to know."
show eve 2b
with Dissolve(.5)
e "Fine. Fine. Meanie."
e "....."
r "....."
r "....."
r "Stop stalling."
show eve 3
with Dissolve(.5)
e "I'm not stalling. I'm trying to think of an answer."
r "You don't have one?"
show eve 6b
with Dissolve(.5)
e "I do, but I don't want to tell you, so I'm thinking of another one."
r "I see."
pause 1.0
e "Okay, I've got it. I like to dress up."
r "I want the real reason."
show eve 5b
with Dissolve(.5)
pause 1.0
e "Alright."
e "This outfit has a special meaning to it. My mom used to wear an outfit just like this all the time."
r "So why do you wear it."
show eve 7b
with Dissolve(.5)
e "...."
e "Forget it. You will think it is silly."
r "Tell me. I'll decided that."
e "I wear it in memory of my mother, so I won't ever forget her."
r "That isn't silly."
e "I wasn't finished."
e "I also wear it in hopes that it will make things better."
r "Better? What do you mean?"
show eve 3b
with Dissolve(.5)
e "It is nothing. Forget it."
r "And the pearls and cloak with hood?"
show eve 6b
with Dissolve(.5)
e "Oh this. I just like dressing up."
r "Uh-huh."
show eve 4b
with Dissolve(.5)
e "What don't you believe me?"
r "Knowing you there has to be more."
show eve 1b
with Dissolve(.5)
e "Have you ever wanted a different life. To be someone completely different."
r "And what does this have to do with my question?"
show eve 1
with Dissolve(.5)
e "Shh.. I'm getting to that. So just listen."
show eve 7b
with Dissolve(.5)
e "Looking down at the water. The ripples and the rushing sounds I've wished for a different life. Many times have a wished that the water I was looking at was just a dream, and I would wake up to my real life."
show eve 14b
with Dissolve(.5)
e "So many times that I've lost count even. I've convinced myself that maybe if I dress differently one of these times I will wake up somewhere else. This dream will vanish and I will be back."
show eve 15b
with Dissolve(.5)
e "Don't you just wish, your life was just a dream sometimes. So that you can wake up from this cruel reality."
show eve 22b
with Dissolve(.5)
e "Look at me, spouting out all this stuff."
r "Dark times won't last forever. Have faith." 
show eve 6b
with Dissolve(.5)
e "Why are you giving me that weepy teary look?"
show eve 8b
with Dissolve(.5)
e "Don't tell me you actually fell for that sob story."
r "It was just another trick?"
show eve 18b
with Dissolve(.5)
e "Really you're pathetic, you still fall for the simplest tricks. You shouldn't believe every word spoken to you."
r "It was a trick?"
show eve 19b
with Dissolve(.5)
e "Oh course dummy. Why would I wish for something so silly? Why would I believe in such a silly hope? It is a just foolish thought, why would anyone believe in it?"
e "I'm going to head home now. I'm not feeling all that well today. I think the cold might be getting to me."
r "Are you really okay Eve."
show eve 17b
with Dissolve(.5)
e "Stop believe stupid tricks, dummy. You are making me feel bad for tricking you. See, I'm crying because I feel such pity for a fool like you."
hide eve 17b
with Dissolve(.5)
r "...."
r "Is that really true."
e "You've changed Ryo."
r "Huh? What? Wait, Eve. What did you mean?"
r "And she is gone..."
scene black
with Dissolve(.5)

#(Night)
play music "Music/Firefly.ogg"
r "I've changed?"
"Ryo's mind became stuck on that one line. It bothered Ryo so much that he couldn't sleep. Frustrated at his lack of sleep he dressed himself and stepped outside hoping the night air would clear his mind."
r "I don't feel like I've changed."
r "Nothing really feels that different."
r "What did Eve mean?"
"Ryo let out a frustrated groan as he ran a hand through his hair."
r "I don't get it. What did she mean? Have I really made a noticeable change? When did I change? What changed about me?"
r "Have I really changed?"
r "....."
r "I will just have to ask Eve what she meant tomorrow."


#(Friends)
play music "Music/Harmony.ogg"
mom "Ryo wake up, you have visitors."
r "Is it Eve?"
scene house_in1
with fade
"Ryo got ready in a flash and headed out to greet his guest."
Chika "Good morning Ryo."
Jiro "Ready to study?"
r "Oh its you guys."
Shigeru "Were you expecting someone else?"
Chika "Oooh was Ryo waiting for someone?"
Jiro "How interesting."
r "Alright, alright, let's go study."
Shigeru "Okay group move out."
Chika "Thanks for the snacks, Ryo's mother."
Jiro "Yeah, they were great."
scene black
with Dissolve(.5)
pause 1.0
scene food1
with fade
pause 2.0
r "Alright, so you take this, and then do this, then this, and then keep following it down. You should be able to do the rest of it."
Jiro "Ryo what about this section of the homework."
"Let out a sigh and began to explain yet another part of the homework."
"Ryo stopped in the middle of his explanation as he spotted Eve outside of the building."
Shigeru "Ryo? Is everything alright?"
r "Uh.. yeah. I just saw someone I know."
Chika "Is it the person Ryo was expecting? We should go and introduce ourselves."
Jiro "Excellent idea, that means break time."
r "Come on guys, we shouldn't stop now."
Chika "You read my mind, 'I want a break' was what was on it."
Shigeru "Alright then, I declare it, break time."
scene black 
with Dissolve(.5)
pause 1.0
"Ryo gave up and let his friends have their way. He had studied with all of them enough to know it was pointless to fight it, when a break was decided upon, their was no stopping it at that point."
scene lot3
with fade
Chika "Who is it Ryo? Where is your friend?"
"Ryo let out a sigh and pointed to Eve."
"Chika excitedly bounced over to Eve and snatched up her hand." 
scene lot4
with Dissolve(.5)
Chika "Nice to meet you. I'm Chika, I'm a friend of Ryo's as well."
show eve 4
with Dissolve(.5)
e "Umm.... hello. I'm Eve."
show eve 5
with Dissolve(.5)
e "Um..."
show eve 7
with Dissolve(.5)
show eve 9
with Dissolve(.5)
show eve 10
with Dissolve(.5)
e "Could you stop shaking my hand. My arm is starting to hurt."
"Eve winced as she pleaded for Chika to stop."
Chika "Oh, sorry about that. Sometimes I just space out and don't realize what I'm doing."
show eve 9
with Dissolve(.5)
e "You are still doing it."
Chika "Opps, like I said, I sometimes act the like spas."
"Chika released Eve, laughing at her own stupidity."
show eve 4b
with Dissolve(.5)
Shigeru "Hello Eve, I'm Shigeru. It is pleasure to meet you."
Jiro "Name's Jiro. And any friend of Ryo's is a friend of ours."
e "It is nice to meet both of you."
"Chika leaned in close to Eve almost as if studying her."
Chika "Hmmmm... You approve."
show eve 6b
with Dissolve(.5)
e "I approve? For what?"
Chika "For the requirements for me to want to get to know you."
"Chika snatched up Eve's arm again and started pulling her inside."
Chika "Come on, we need to get to know each other better."
show eve 2b
with Dissolve(.5)
e "I really don't."
show eve 7b
with Dissolve(.5)
e "Please stop."
show eve 10b
with Dissolve(.5)
e "It is really starting to hurt."
show eve 9b
with Dissolve(.5)
e "Don't pull so hard."
Chika "Oh come on, don't be such a baby. A little chat won't hurt."
"Ryo chuckled walking up next to Eve and whispering to her."
r "How does it feel for a change? Normally you are the one always pulling me along."
"Eve stuck her tongue out at Ryo."
show eve 17b
with Dissolve(.5)
e "Alright, let's get to know each other."
hide eve 17b
with Dissolve(.5)
scene black
with Dissolve(.5)
"She no longer fought against Chika and instead starting walking with her."
"The two girls began chatting while sitting in one of the booths."
scene food1
with fade
play music "Music/Dreamland.ogg"
pause 2.0
show eve 7b
with Dissolve(.5)
e "...."
e "I think I'm going to head home."
Chika "Awww, why? We barely got a chance to talk even."
e "I'm not feeling too well, sorry."
Chika "Oh, okay."
Shigeru "It was nice meeting you."
Chika "Yeah, let's talk again, okay."
r "Alright then, see-"
show eve 3b
with Dissolve(.5)
e "Goodbye."
hide eve 3b
with Dissolve(.1)
menu:
    "Go after Eve":
        jump choice10_Eve

    "Stay and help your friends study.":
        jump choice10_friends

label choice10_friends:
$ friend_flag = True
r "I'm sure Eve is fine. I'm probably just imagining things."
Chika "Alright let's get back to studying then."
Shigeru "Right the homework is due tomorrow, so today is the last day."
Jiro "It is good thing we have Ryo to help us."
r "Alright enough stalling. Time to get to work."

jump choice10_end

label choice10_Eve:
$ love_points += 1
$ friend_flag = False
r "Eve, wait!"
Jiro "Ryo where are you going?"
Shigeru "What about studying."
r "I'm sorry guys, we'll have to continue some other time."
Jiro "But the homework is due tomorrow."
r "I'm really sorry, but I have to go."
Chika "Ryo!"
r "I'll make it up to you guys."
scene black
with Dissolve(.5)

#(Tears)
scene bridge1n
with fade
"Eve stood on the bridge staring down at the water."
r "Eve, are you okay?"
scene bridge2n
with Dissolve(.5)
pause 2.0
show eve 4b
with Dissolve(.5)
e "Yeah I'm fine. Just a little tired."
r "Is there something wrong?"
show eve 5b
with Dissolve(.5)
e "No, nothing is wrong. Why would think something is wrong?"
"Ryo shrugged as his glance changed from Eve to the water."
r "Just a feeling I have."
show eve 3b
with Dissolve(.5)
e "You shouldn't trust something as silly as that. Taking it as a fact will only get you in trouble someday."
r "You aren't acting like yourself."
show eve 3b
with Dissolve(.5)
play music "Music/Cold Mind.ogg"
e "......"
hide eve 5b
with Dissolve(.5)
scene bridge3n
with Dissolve(.5)
"Eve turned from Ryo and stared back at the water instead."
show eve 4b
with Dissolve(.5)
e "Ryo, can you tell what is in the water?"
r "Huh? What?"
show eve 11b
with Dissolve(.5)
e "Just answer."
r "What is in the water? As in underwater?"
e "Yes, what is underwater?"
r "Nothing."
show eve 7b
with Dissolve(.5)
e "...."
scene bridge2n
with Dissolve(.5)
r "Was that wrong?"
e "...."
r "Eve?"
show eve 3b
with Dissolve(.5)
e "Just stop okay."
r "Eve?"
show eve 12
with Dissolve(.5)
e "Yes." 
e "Yes it was wrong."
show eve 20b
with Dissolve(.5)
e "The answer is that their is a huge shark underwater, and so if you go in the water it will eat you."
r "In this river? Impossible."
"Eve's hand's clenched around the railing."
e "How do you know?"
r "Logically speaking it is silly."
show eve 3b
with Dissolve(.5)
e "Then why does no one swim in this river. Why is there never anyone near the water's edge?"
r "The current is too fast."
show eve 8b
with Dissolve(.5)
e "Is that really the case, maybe it is because of the shark. It is possible that only adults know of its existence, a horrible creature that lives under the surface."
r "With how deep this river is? Are you messing with me?"
show eve 11b
with Dissolve(.5)
e "Ryo, stop. You aren't getting it. Stop taking it literally. Open your eyes!"
"Ryo stepped back, surprised by Eve's harsh tone."
r "Well, I suppose I can't say for 100 percent certain that something like that is impossible I guess."
show eve 12
with Dissolve(.5)
e "And why can't we know for certain the answer? Why is it we can't be sure if my shark does, or doesn't not exist?"
r "Because we can't see under the surface of the water, so it is impossible to tell what is really under it. Is the answer you are looking for, but that isn't fully true."
show eve 20b
with Dissolve(.5)
e "Alright, and since you still aren't getting it. I'll finish it up for you. I'll spell it out. I'm just like that example."
e "You only have been seeing what is on the surface. You know nothing about me. So don't go making statements like you know me. You don't. You are just a stupid person who thinks they know everything when they know nothing."
e "You don't know me. You don't understand anything at all, so just shut up!"
r "What do you mean I don't know you? I know we've just been hanging out this week, but we have spent hours spending time with each other and talking. How can you say I don't know you?"
e "Ryo, not everyone is simple like you are. Not everyone leaves themselves bare. You do it either because you don't care, or are too stupid to understand."
r "What is that supposed to mean?!"
show eve 11b
with Dissolve(.5)
e "Take it however you want. It matters not to me."
r "What is going on? Why are you acting like this?"
play music "Music/Toy's Dance.ogg"
show eve 12b
with Dissolve(.5)
e "Why don't you understand? For a genius you are so stupid. How do you not get it!?"
show eve 20b
with Dissolve(.5)
e "Or maybe you understand, but you just don't want to accept it. That really is the answer most of the time isn't it." 
e "When people say they don't understand and want you to explain that is the case a lot isn't it. They actually know the answer but they just don't want to believe it."
e "So they want you to explain in a naive hope that they were thinking wrong."
e "So since you want me to explain, I will."
show eve 12
with Dissolve(.5)
e "You wear nothing. You don't hide yourself. You act the same inside as you do on the outside. There is no lie being reflected from your eyes."
show eve 11
with Dissolve(.5)
e "However for most people this is not the case. People mask themselves behind layers of lies and hide everything about their true feelings behind all those closed doors. They seal them away with a key and refuse to never open them."
e "They do this to prevent themselves from getting hurt, for they feel if people knew their real self they would not be excepted, or that things would change."
e "They fear both change and getting hurt, so in a hope to avoid this they lock their heart and mind up. Concealing it behind a curtain of lies and masks."
show eve 20b
with Dissolve(.5)
e "I'm sure you understand. In fact I'm sure you understood from my water example, you just don't want to except it."
e "I'm one of those people Ryo. I'm not like you, I cover myself up. I have cages around myself and layers of masks. So what you've seen is only just a mask. You know nothing about my true self. You don't understand. You can't understand."
r "You've been saying that 'I don't know you' and 'You can't understand.' But I don't see where that is coming from."
r "Are you going to say that all this time, I've been hanging out with an mask, almost another personality that you use to hide away with."
show eve 7b
with Dissolve(.5)
e "That is the truth. It is up to you, if you are going to face it or not. They say the truth will set you free, but I don't see it. I feel like the truth causes farewells."
r "If there wasn't a lie or deception in the first place, then such pain would not occur."
show eve 10b
with Dissolve(.5)
e "Not everyone is strong enough to go through life like that. We hide behind masks and cover up our feelings so that drama will not occur. Simply because people can not accept the truth. So all it brings is heartache."
r "I don't think there is anything wrong with that. Covering up your feelings so that arguments won't happen."
show eve 7b
with Dissolve(.5)
e "So you don't mind lies, in fact you approve of them?"
r "I didn't say that."
show eve 3
with Dissolve(.5)
e "Yes you did. When you are covering up your feelings you are lying, maybe not to someone else, but to yourself. Nonetheless I agree with you, harmless white lies are not something to be ashamed up."
r "So there is nothing wrong with you covering yourself up."
show eve 11b
with Dissolve(.5)
e "You aren't understanding at all. I'm not asking for your approval. I'm telling you I've just been using you and watching from the sidelines like a 3rd person. I've been deceiving you and just playing with you."
r "That..."
show eve 20b
with Dissolve(.5)
e "Don't say it. It is true. I might not have any ill intent, but does that still make it right? The me you were hanging out with was just a fictional character, a made up persona."
r "You keep saying that, but I don't believe you. All that time, I don't believe the person I was talking to was just a persona. Maybe you're right, not everything you told me was the truth, maybe you tricked me and lied to me at times."
r "Maybe you acting differently then you really felt."
r "However, not everything about that girl, 'you', was fake. If you really want me to believe that everything was lie, then look me in the eye and tell me everything, every emotion, every thought, every action you did while hanging out with me is a lie."
"Eve let out a sigh and stared straight at Ryo's face, her eyes cold and filled with conviction."
show eve d4b
with Dissolve(.5)
e "Everything that I did, said, and felt was a lie." 
show eve d8b
with Dissolve(.5)
e "That is the cold truth Ryo. Everything was just a lie. It was simply a game a pretend. I'm sorry, the person you hung around with doesn't exist. She was a lie, a made up being."
e "So forget about her. I don't want to play with you like this, not anymore. It isn't fair to you."
r "What is wrong with playing pretend?"
show eve d9b
with Dissolve(.5)
e "Ryo don't you get it. This isn't real. Make believe is something that should stay with kids. Something like this is better left to die."
r "That isn't true, it was real."
e "I just told you-"
r "You are deceiving yourself. You are lying to yourself to keep yourself from possibly getting hurt."
r "I don't know why, but for some reason you feel you will go through pain if we stay friends, so you are cutting ties. You are holding the scissors and the thread of our friendship and trying to cut it in two."
r "You may say everything was just a lie, but I don't believe that is the truth, and I don't think you do either."
r "Maybe it is true you weren't being truthfully all the time, maybe you held up a mask and hid your real feelings at times, but everyone does that. It is nothing to be ashamed of."
r "But you can't tell me that everything was just a big act. At some point your real self and this Eve intermixed, but you don't want to admit it."
show eve d6b
with Dissolve(.5)
e "Not everyone is so simple minded as to let their real self come out. No, they hid it in the deepest darkest depths. They swallow it whole and drown it in an endless sea."
r "I'll believe. I'll believe that all that time we spent together wasn't meaningless for you. That some of the 'fun' you had shown was real."
show eve 3b
with Dissolve(.5)
show eve 5b
with Dissolve(.5)
e "...."
show eve 15
with Dissolve(.5)
e "Why.."
show eve 15b
with Dissolve(.5)
e "Why do you care so much?"
menu:
        "Because I love you.":
            jump choice11_love

        "Because we are friends.": 
            jump choice11_friend


label choice11_love:
play music "Music/Approaching Shadows.ogg"
scene bridge1n
with Dissolve(.5)
pause 2.0
show eve d8
with Dissolve(.5)
e "I see."
show eve d3
with Dissolve(.5)
e "So it is something like that."
r "Eve?"
show eve d1
with Dissolve(.5)
e "Ryo, let me tell you something."
show eve d4b
with Dissolve(.5)
e "Love is a lie. It is just a fake illusion. It is a fleeting thing that is their one minute and then gone the next."
r "You can't be serious, love is-"
show eve d9b
with Dissolve(.5)
e "Fake! There is so much thing, not the way you are thinking of it at least. It is a just a passing affection, that one day will vanish. Love is just another word for 'interest' and like with all interests, it will vanish."
r "That isn't-"
show eve d6b
with Dissolve(.5)
e "It is true. You want to know how I know this. Because I've seen it. Love is fleeting, love is passing, it will fade it time, so it is pointless to do long term or big actions based on it."
r "I don't believe that."
show eve d10b
with Dissolve(.5)
e "Well I do. You say you hold this kind of interest in me, but the fact is that it will fade. Your care and affection is only temporary." 
show eve d9b
with Dissolve(.5)
e "I don't need passing pity!"
r "That isn't-"
e "Goodbye Ryo! This is the end. I'm cutting the string now. Don't talk to me again."
r "Eve wait."
"Ryo grasp Eve's arm and held it tight."
show eve d5
with Dissolve(.5)
e "You're hurting me."
r "Eve listen to me."
show eve d10b
with Dissolve(.5)
e "No. I will not be used and then throw away!"
"Eve broke away from Ryo and ran off into the night."
hide eve d10b
with Dissolve(.3)
r "Eve..."
r "It doesn't look like Eve is going to show up."
r "Eve..."
r "Are you really okay with letting things end this way."
r "...."
r "I'll try again tomorrow."
r "...."
r "It looks like you really meant it."
r "So that really was goodbye."
"A tear slid down Ryo's face."
r "Goodbye...Eve."
jump bad_end

label choice11_friend:
play music "Music/Firefly.ogg"
scene bridge1n
with Dissolve(.5)
pause 2.0
show eve 6
with Dissolve(.5)
e "Yeah, that's right."
show eve 6b
with Dissolve(.5)
e "I'm just surprised. I didn't know such things happened. I've experienced this type of thing before."
show eve 8b
with Dissolve(.5)
e "So this is what a real friend is like. It is interesting. So much different then what I have had before."
r "Eve, it is okay. You don't have to hold up your masks anymore. I'll accept you for who you are. Like any real friend would."
show eve 4b
with Dissolve(.5)
e "Ryo..."
"Eve turned and walked away."
show eve 16
with Dissolve(.5)
e "See you tomorrow."
hide eve 16
with Dissolve(.5)
pause 2.0
scene black
with Dissolve(.5)
jump choice10_end 

#(White Day)

label choice10_end:
pause 3.0
play music "Music/Harmony.ogg"
scene bridge1
with fade
pause 2.0
show eve 19
with Dissolve(.5)
e "Good morning Ryo!"
"Ryo stared at the chipper girl. He stifled a yawn before addressing her."
r "You're awfully excited today. Much better than you being gloomy like yesterday."
show eve 16
with Dissolve(.5)
e "Yeah... that. I was just being silly okay. So never bring that up again."
r "Alright."
show eve 18b
with Dissolve(.5)
e "I mean it. Never bring it up. Or else you will suffer the rather of the world champion tickler."
e "But I must say it surprised me to see you have friends, other than me that is."
r "Really? Why?"
show eve 16b
with Dissolve(.5)
e "Because of how socially awkward and boring you are."
r "That is the normal Eve right there."
e "No, You just seem like a lone wolf type."
r "Really?"
show eve 17
with Dissolve(.5)
e "Yep. So I was surprised to learn you have a pack. It is like I just watched you grow up. From a little pup to a full fledged wolf."
"Eve ruffled Ryo's hair like a child."
r "Stop that."
show eve 19b
with Dissolve(.5)
e "Aww~ Little Ryo is getting grumpy."
r "You're really in a playful mood."
r "I'm glad."
show eve 2
with Dissolve(.5)
e "Hmm?"
r "It is weird seeing you not like this."
e "It was?"
r "Yeah, you are the type of person who always acts goofy and energetic."
show eve 6
with Dissolve(.5)
e "I am?"
r "I've learned my lesson, I'm not falling for it."
show eve 16
with Dissolve(.5)
e "You really are getting better. I can't fool you anymore."
show eve 5
with Dissolve(.5)
e "Ummm... Ryo."
r "Yeah?"
"Eve stared at the ground before glancing back up a Ryo. She pulled out a small box hidden behind her back."
show eve 4
with Dissolve(.5)
e "Here, this is for you."
r "Huh? What is this for?"
e "Just open it."
"Ryo opened the small box and found a set of neatly wrapped chocolates inside."
r "Did you make these yourself?"
"Eve responded with a nod."
show eve 18b
with Dissolve(.5)
e "Yeah... It is a thank you gift for the dinner, walking me home, the food, and of course your jacket."
r "Today is white today, the opposite is supposed to happen. Guys give gifts to the girls who gave you chocolate on Valentine's day."
e "I know how the holiday works."
show eve 17b
with Dissolve(.5)
e "I just figured you probably weren't going to do anything for it, and that is no fun. So you have to give me something in return for white day."
r "That is only if the chocolate was on Valentines day."
e "Just pretend you got it on valentines day then."
show eve 21b
with Dissolve(.5)
e "So make sure you get me a gift okay. It doesn't have to be anything special. Have fun picking it out."
hide eve 21b
with Dissolve(.5)
r "...."
"Ryo let out a sigh before containing on to school."
r "'Have fun' she says. This is going to be a big pain. Ugh.."
scene black
with Dissolve(.5)

#(Gift)
if money_flag:
        jump store_ver2
                
else:
        jump store_ver1
                
label store_ver1:
    "Ryo glanced down the aisles, trying to find a good gift for Eve."
r "What should I buy? Oh wait, I better make sure I have enough money first."
r "Of the money I have a good choice might be."
r "They seem to have a few types of flowers for cheap"
r "Hmmm.... What should I buy?"

menu:

    "Yellow and Purple Carnations":
        $ f1_flag = True
        $ book_flag = False
        jump choice13_flowergift_end

    "Mauve Carnations":
        $ f2_flag = True
        $ f1_flag = False
        $ book_flag = False
        jump choice13_flowergift_end

    "Peonies":
        $ f3_flag = True
        $ f1_flag = False
        $ f2_flag = False
        $ book_flag = False
        jump choice13_flowergift_end
                
label store_ver2:
"Ryo glanced down the aisles, trying to find a good gift for Eve."
r "What should I buy? Oh wait, I better make sure I have enough money first."
r "Of the money I have a good choice might be."
r "They seem to have a few types of flowers for cheap, There is also the possibility of a fantasy book."
r "Hmmm.... What should I buy?"
menu:
    "Flowers":
        jump choice13_flowers

    "A book":
        $ book_flag = True
        jump choice13_book

label choice13_flowers:
r "Okay I'll buy some flowers, now the question is what kind of flower. They have striped yellow and purple carnations, solid mauve carnations, and peonies."
menu:

    "Yellow and Purple Carnations":
        $ f1_flag = True
        $ book_flag = False
        jump choice13_flowergift_end

    "Mauve Carnations":
        $ f2_flag = True
        $ f1_flag = False
        $ book_flag = False
        jump choice13_flowergift_end

    "Peonies":
        $ f3_flag = True
        $ f1_flag = False
        $ f2_flag = False
        $ book_flag = False
        jump choice13_flowergift_end

label choice13_flowergift_end:
"Ryo scooped up a few of the flowers and paid for them before heading back to the bridge to meet."
jump choice13_end

label choice13_book:
"Ryo looked at the back of many books before he gave up and just grabbed the next book that seemed interesting." 
jump choice13_end


label choice13_end:
scene bridge2e
with fade
r "Hopefully this turns out alright."
show eve 1
with Dissolve(.5)
e "You're late."
r "Sorry about that, it took me a while to decide on what to buy you."
show eve 6
with Dissolve(.5)
pause .5
show eve 2
with Dissolve(.5)
e "Um...."
show eve d10b
with Dissolve(.5)
e "I wasn't actually serious about you having to get me a gift."
show eve 19
with Dissolve(.5)
e "Oh well, it you bought me one I'll take it anyway."
label gift_check:
if book_flag:
        jump gift_version1
else: 
    if f1_flag:
        jump gift_version2
    else:
        if f2_flag:
                jump gift_version4
        else:
            if f3_flag:
                jump gift_version3
            else:
                jump gift_check
#label flower_check1
#if yp_carnations go to gift_version2
#if mauve_carnations go to gift_version4
#if peony go to go to gift_version3

label gift_version1:
$ love_points += 1
r "Here you go Eve."
show eve 6
with Dissolve(.5)
e "A book. When you said you got a me a gift I did not expect something like this."
r "Don't you like it?"
e "A fantasy story about an another world."
r "..."
e "..."
r "..."
e "..."
r "Do you not like it."
show eve 17
with Dissolve(.5)
e "Nope, I love it silly. This kind of books are something I enjoy."
r "I figured that would be the case. She you said you liked thinking about other worlds."
e "Oh, so you have been listening to me. I'm shocked."
r "I do sometimes manage to remember things people say."
show eve 16b
with Dissolve(.5)
e "Don't worry we all have our faults. You just are unlucky and have way more than the average person."
r "Even when I know you are just joking around comments like that still sting a little."
show eve 6b
with Dissolve(.5)
e "Ooh wow this book follows the principle of belief."
r "Principle of what?"
show eve 16
with Dissolve(.5)
e "It is just a thing you find in some novels and stuff. Basically it is a theory where if you believe and wish for something with all your heart you can create a cause and effect."
r "That is kind of silly."
show eve 11b
with Dissolve(.5)
e "Says you."
r "It isn't logical at all."
show eve 3b
with Dissolve(.5)
e "That is why I said it was in books. It basically means if you believe you can make something happen, but you have to suspend your belief of what you know is true."
r "Like I said it is silly."
show eve 16b
with Dissolve(.5)
e "That it might be, but wouldn't it be cool if that was the case."
r "No."
show eve 2b
with Dissolve(.5)
e "Why not?"
r "Because then we would have all these mythological stuff running around the streets, dragons, fairies. Need I go on?"
show eve 3b
with Dissolve(.5)
e "It isn't that simple dummy. You have a create a mass, basically you have to convince more people of your truth. You have to make the mass question what is the truth."
r "I still think it is silly. Wait a minute. You actually believe it don't you?"
show eve 6b
with Dissolve(.5)
e "What? I told you I thought it was silly too."
r "Oh no, before you told me you believed that you could maybe change things wake up in another world and such."
show eve 7b
with Dissolve(.5)
e "..."
show eve 10b
with Dissolve(.5)
e "So what... So what if I believe in it. You going to make fun of me for it?"
r "No, it just is interesting."
show eve 1
with Dissolve(.5)
e "What is?"
r "For you the believe in that, means you have something you really want to change."
e "Yeah so, doesn't everyone have things they wish they could change."
r "Not to that level."
show eve 20b
with Dissolve(.5)
e "Haha."
e "Yeah I got it. Not to the level where you would become a nut-job and believe in fantasies."
r "I didn't say that."
e "You didn't have to."
show eve 18b
with Dissolve(.5)
e "Anyway don't worry about it. I know what you meant. I just like the idea of it being possible to change something if you made enough people think that certain way."
r "That is kind of creepy, forcing everyone to believe one way."
scene bridge1e
with Dissolve(.5)
pause 2.0
show eve 20b
with Dissolve(.5)
e "That wasn't what I meant. And just for that I'm done talking to you for the day."
r "Huh?"
show eve 5b
with Dissolve(.5)
e "..."
r "..."
show eve 5
with Dissolve(.5)
e "..."
r "Are you really actually not going to talk?"
e "..."
show eve 3
with Dissolve(.5)
e "Loan me a piece of paper and a pen."
r "I don't have either of those things."
show eve 5
with Dissolve(.5)
e "Fine."
"Eve shook her head and walked away."
r "Where are you going?"
show eve 3b
with Dissolve(.5)
e "If you would have had a pen and some paper, you would find out."
hide eve 3b
with Dissolve(.5)
"Ryo chuckled and shook his head."
r "Why couldn't you just tell me, instead of saying that."
scene black
with Dissolve(.5)
$ dream_flag = False
jump gift_end

label gift_version2:
r "Here you go Eve."
show eve 6
with Dissolve(.5)
e "Flowers."
e "..."
show eve 3b
with Dissolve(.5)
e "Yellow and purple striped carnations? Umm.. Ryo do you know what these flowers mean?"
r "No, what do they mean?"
show eve 19b
with Dissolve(.5)
"Eve shook her head back and forth while laughing."
e "Don't worry about it. It isn't important."
r "Now you have to tell me. I'm curious now."
show eve 18
with Dissolve(.5)
e "Alright. Alright I'll tell you."
e "The yellow means rejection. The purple park means unreliability. And because they are stripped it means a refusal."
r "I didn't know they meant that. I wasn't trying to insult or hurt your feelings."
e "Don't worry, I know that."
show eve 6
with Dissolve(.5)
show eve 16
with Dissolve(.5)
e "Oh man. I just remembered something I have to take care of. I'll see you tomorrow Ryo."
hide eve 16
with Dissolve(.5)
pause 2.0
scene black
with Dissolve(.5)
$ dream_flag = False
jump gift_end

label gift_version3:
$ love_points += 2
r "Here you go Eve."
show eve 6b
with Dissolve(.5)
pause 1.0
show eve 19b
with Dissolve(.5)
e "Hahaha!"
e "That flower."
e "Heheheh, hahaha! My sides they hurt."
r "What?"
show eve 18b
with Dissolve(.5)
e "This flower. Heheheh."
e "That was a good one. I didn't except you to get me back in such a way."
r "I don't understand."
show eve 17b
with Dissolve(.5)
e "Haha then this is even funnier. This flower means masculinity."
e "You are lucky I'm not a more sensitive person otherwise they might get upset at getting a flower like this."
r "I didn't know what it meant; honest."
show eve 18
with Dissolve(.5)
e "I believe you. Interestingly enough in other parts of the world this flower means 'shame' instead."
show eve 6
with Dissolve(.5)
e "Oh man. I just remembered something I have to take care of. I'll see you tomorrow Ryo."
pause 2.0
scene black
with Dissolve(.5)
$ dream_flag = False
jump gift_end

#(Dreams)
label gift_version4:
play music "Music/Dreamland.ogg"
$ dream_flag = True
r "Here you go Eve."
show eve 6
with Dissolve(.5)
e "This... this flower."
r "Do you not like it."
"Eve shook her head."
show eve 5
with Dissolve(.5)
e "No, its not that."
r "The what is it?"
show eve 5b
with Dissolve(.5)
e "Its nothing."
show eve 4b
with Dissolve(.5)
e "Ryo what do you think of dreams?"
r "Dreams, as in fantasies or dreams you have at night?"
e "Hmm... both."
r "Well, taking them one at a time. I would say that dreams as a fantasy are good things to have, as long don't need them to come true."
r "You would like it to come true, but you don't need it. And most likely if it does come true it won't be the same as your fantasy."
e "And dreams?"
r "Well, it is hard to say if they have any real value. A lot of dreams you have you don't even want." 
show eve 1b
with Dissolve(.5)
e "I like dreams. Windows into the soul they say, I said windows into other worlds."
e "Wouldn't it be funny if this world was just a dream. It would be an interesting twist wouldn't it."
r "Not really."
show eve 12b
with Dissolve(.5)
e "You are boring sometimes you know that. You want things to stay the same, with no twist."
show eve 4b
with Dissolve(.5)
e "Haven't you ever wish you could wake up. That this is just a dream and you can stop and wake up at any time."
r "I suppose so. There have been times I've wished for change. For something like that, to wake up from this life and being in a different one."
show eve 6b
with Dissolve(.5)
e "It is funny. Dreams are something I have want to end, but I always wanted this to end. But if it is a dream, I don't want to wake up now."
show eve 7b
with Dissolve(.5)
e "Oh no, it is already this late."
e "I forgot I have something really important to do. I'll see you tomorrow Ryo."
pause 2.0
scene black
with Dissolve(.5)
jump gift_end

#(Missing)
label gift_end:
play music "Music/Life.ogg"
scene bridge1
with fade
pause 3.0
scene bridge1e
with Dissolve(3.0)
"Ryo rubbed his hands together trying to keep them warm."
r "It doesn't look like she is coming."
r "She said she was going to come though."
r "I wonder what happened to her."
scene bridge1n
with Dissolve(3.0)
"As the sky started blacken Ryo decided to give up and head home."
scene black
with Dissolve(.5)

#(Priority)

"Ryo's mind played with him all night long. His thoughts were plagued with thoughts about Eve and why she didn't show up. With none of them being good things."
"Even at school his mind continued to haunt him. He began to count down the seconds until he felt the bell freed him from the school day."
r "I have to check on Eve."
Chika "Ryo, where are you going?"
r "I have to do something."
Shigeru "Ryo can it wait? We need your help. The paper that is due today, we need your help with it."
Chika "Please Ryo, this paper is said to be 25 percent of our grade. If we fail it, we're dead."
Jiro "Come on Ryo, don't let us down."
Chika "We really need you."
r "I'm sorry. I have something I need to do. I'm really sorry."
"Ryo walked away from his friends before he heard their response. He was afraid that he might change his mind and help them, but then he would be worried about Eve the whole time. He needed to find about what happened to her."

#(Abuse; What you have)
play music "Music/Water's Surface.ogg"
scene bridge1
with fade
"Ryo let out a sigh of relief when he stopped Eve standing the on bridge."
r "Oh good you are here."
"Eve didn't turn around she kept her back towards Ryo."
e "Yeah sorry, yesterday I had some things I needed to take care of."
r "Are you alright."
e "Yes, I'm perfectly fine."
r "Then why aren't you turning around."
e "I like facing this way. I like looking at the other end the bridge. It makes me think of life or something. How we always have a long road ahead of us."
r "Sure..."
e "So how was school?"
r "Fine."
r "You could at least look at me while you are talking."
e "But I like this view."
r "Alright what is really going on?"
e "Nothing."
"Ryo frown and walked around Eve, but when he did she spun around she so was facing the other way."
e "I like this view too."
r "What are you hiding?"
r "Are you mad at me?"
e "No."
r "Then what is it?"
e "I don't you I just like looking at this view."
r "I don't believe you."
"Ryo snatched up Eve's hand and spun her around."
play music "Music/Toy's Dance.ogg"
scene bridge2
with Dissolve(.5)
r "..."
"Ryo's mouth fell open in shock. Around Eve's eye was swelled up purple mark. She had a black eye."
r "How?"
show eve d8
with Dissolve(.5)
e "It is nothing. Don't worry about it."  
r "If you don't want to tell me how you got it, then it is not nothing. If it was an accidental thing, then you would laugh it off and tell me. The fact that you are hiding it shows something is up."
show eve d4b
with Dissolve(.5)
e "I told you it is nothing, so just drop it."
r "Eve... you aren't being abused are you?"
show eve d2b
with Dissolve(.5)
e "Where did you come up with that?"
r "It is something people hide, and it would explain a few other things."
show eve d7b
with Dissolve(.5)
e "I am not abused, so let those thoughts leave your mind."
show eve d2
with Dissolve(.5)
e "I was just in the way, it was totally my fault. It was just a punishment don't worry about it."
r "That!"
r "That is not something to just laugh off. If you are being abused Eve you shouldn't make excuses. Your parents are just being demons."
show eve d9b
with Dissolve(.5)
e "You know Ryo, sometimes you should just die."
r "Huh.."
show eve d4b
with Dissolve(.5)
e "Sometimes you are so annoying. Geez, there is nothing strange about my situation, so stop making a big deal out of it. I'm used to it so just stop, it doesn't even bother me anymore."
r "You should get help. The one who is abusing you should pay."
show eve d4
with Dissolve(.5)
e "Geez stop playing the goodie-goodie, it is annoying."
r "I'm trying to help-"
show eve d9b
with Dissolve(.5)
e "Well don't!"
e "I don't need your pity, nor your help. So just shut up and drop it. And if you can't just leave me alone!"
e "Not everyone has a nice home and family like yours! Some people have to endure things too. Most people don't get to be that lucky."
e "So instead of griping over what I don't have, why don't you try and look at what you have for once. You want me to have it, yet you are calling it annoying and frustrating. You are nothing but a hypocrite."
hide eve d9b
with Dissolve(.5)
"Ryo stood there stunned. He didn't know what to say. He didn't know what to think."
r "Have I really been a hypocrite?"
scene black
with Dissolve(.5)
#(Exam Results)
pause 2.0
play music "Music/Dreamland.ogg"
mom "Ryo, time to wake up."
"Ryo's mother was greeted with a surprise as the door opened and Ryo stepped out all ready for school already."
r "Thanks mom."
mom "Huh? What?"
r "For always waking me up and making breakfast."
mom "Huh?"
mom "What?"
mom "..."
mom "You're welcome."
"Ryo ate breakfast with his mom before heading off to school."
girlA "Look there is he is again. Look at him always acting like he is better than the rest of us."
girlB "Can you believe it."
r "We must have gotten our exams posted today."
"Ryo didn't even bother to look at the results. He didn't care."

#(Betrayal)

"The day was filled with the constant whispers of his classmates. He was like normal the talk of the school."
r "Hey, guys."
"Ryo called out to his friends, however they just ignored him and left school."
r "They must be mad about yesterday."
"Ryo let out a sigh, he knew he would have no choice but to wait for his friends to calm down."
r "Eve isn't coming.."
r "..."
r "Have I messed everything up? Did I lose both my friends and Eve?"
r "I'm such an idiot."
if friend_flag:
        jump envy_end
        
else:
        jump choice14_end
        
label envy_end:
menu:
     "Answer the phone":
         jump choice14_study

     "Let it ring":
         jump choice14_water

#(Water)
label choice14_water:
"Ryo decided to just ignore the phone. He didn't feel like talking to anyone."

if dream_flag:
        jump dream_end 
else:
        jump choice14_end
#(Enternal Dream)
label dream_end:
play music "Music/Life.ogg"
"After a while Ryo got fed up with being in his room, and he decided to take a walk."
scene bridge1n
with fade
r "Someone is on the bridge."
r "Eve, what are you doing out here?"
show eve d1b
with Dissolve(.5)
e "Oh... Ryo... It is you."
r "Eve... what happened."
show eve d3
with Dissolve(.5)
e "It is nothing, I just got in the way again."
e "I'm always in the way."
r "Eve you should be treated this way."
show eve 4b
with Dissolve(.5)
e "...."
show eve d5b
with Dissolve(.5)
e "Ryo, don't start that again."
r "No, I will. I understand I didn't accept my parents before. I didn't realize how good I had things."
scene bridge3n
with Dissolve(.5)
e "Ryo, do you remember what I said about dreams."
r "Yeah?"
show eve d3b
with Dissolve(.5)
e "I want this dream to end now."
r "What?!"
show eve d10b
with Dissolve(.5)
e "You heard me. I want this dream to end. I want to move onto the next one."
r "What is their isn't one?"
show eve d5b
with Dissolve(.5)
e "Then I guess that is it."
e "But... I'm scared."
scene bridge1n
with Dissolve(.5)
"Ryo's eyes went wide as Eve dove into him. Unsure he closed his arms around Eve and tried to comfort her."
r "Come on, I'll take you home."
pause 3.0
scene bridge6
with Dissolve(.5)
pause 2.0
show eve d6b
with Dissolve(.5)
e "I'm... sorry."
e "I'm taking the cowards way out, and I still can't even do it by themselves."
r "What?"
show eve d10b
with Dissolve(.5)
e "I'm sorry."
e "Let's go to an eternal dream."
hide eve d10b
with Dissolve(.5)
pause 2.0
scene black
with Dissolve(2.0)
"Ryo had no time to react, by the time he knew what was going on it was too late. With one strong shove Eve had used her weight to push both of them back and down the hill toward the water below."
scene water1n
with Dissolve(1.0)
e "I'm sorry, Ryo...."
e "Please.."
e "Don't hate me..." 
jump bad_end

#(Study Session)
label choice14_study:

r "Hello?"
Shigeru "Hey Ryo, we are having a study session tonight, and we were wondering if you can come."
r "I should make it up to them. I bailed on them before."
r "Yeah, I can make it."
Shigeru "Great we are meeting in the park, in 2 hours."
r "Okay, I'll be there."
pause 3.0
scene park4
with Dissolve(3.0)
pause 3.0
play music "Music/Approaching Shadows.ogg"
r "I'm the first one here?"
"Ryo glanced down at his watch, making sure he had the correct time."
r "Did I misunderstand something?"
r "They are really running late."
"A sharp pain ran through Ryo's head as the sound of metal rang out."
scene black
with fade
"Ryo's vision instantly faded to black as he was struck again."
r "What."
r "What is going on..."
Chika "Hurry up, or someone might see us."
r "Chika?"
Jiro "He is still awake!"
Shigeru "That doesn't matter idiot."
r "What... I don't-"
Chika "We hate you. Simple as that."
Shigeru "Always getting good grades and looking down at us like you are on some pedestal. It sickens us."
Jiro "But we figured we could get stuff out of you."
Chika "But then you had to betray us. So you really think that highly of yourself. Like you are so big shot who doesn't need to look down at the little people. You disgust me!"
r "....All this time. You guys were the same. Looking at me with contempt. Those envious eyes of yours only see what you want to see."
Shigeru "Shut up. You think you are so smart, so much better then us. Well if you are so smart, figure out a way to live through this."
scene bridge6
with Dissolve(.5)
"Ryo felt his body get picked up and dragged over to the side of the hill."
Chika "Enjoy your swim Ryo."
"And they tossed him down the hill toward the rushing river below."
scene water1n
with Dissolve(1.0)
r "I was a fool. To think that anyone would look at me differently..."
r "Everyone is the same, they only look at things with malice and envy."
r "Life is cruel, it is without beauty."
jump bad_end

#(Friendship)
label choice14_end:
play music "Music/Dreamland.ogg"
Chika "Ryo."
r "Hmm?"
Shigeru "We want to apologize."
Chika "We shouldn't have forced you into helping us. We should have been understanding, and just dropped it when you said you were busy."
Jiro "Yeah, we're sorry."
r "Don't worry about it."
Shigeru "To make it up you, we want to give you this."
Chika "It is a ticket to join us on a cruise. It is sailing on October 4th, so make sure you show up."
Jiro "Yeah, we all pooled our money in for this."
Shigeru "If you really want, we can also get a ticket for Eve."
Chika "Yeah, you should bring Eve too. I'll play for Eve's ticket."
r "Thanks guys, this is really nice. I'm looking forward to it already."
Chika "Geez it is months away don't get too excited."
Shigeru "No go on, go hang out with Eve, like you always do."
r "What about studying?"
Jiro "We'll manage."
Chika "Yeah, go on. We've already got everything worked out. You don't have to worry about helping us anymore."
r "Okay, but if you guys need extra help, just ask."


#(Missing)
scene bridge1
with Dissolve(2.0)
pause 4.0
play music "Music/Approaching Shadows.ogg"
scene bridge1e
with Dissolve(3.0)
pause 4.0
scene bridge1n
with Dissolve(4.0)
"Ryo waited for hours and hours but Eve didn't show up again."

if house_flag:
        jump ver2
else:
        jump choice15_nothing

label ver2:
"Ryo clenched his fists. He couldn't sit back and do nothing while this was happening to Eve."
r "I don't care what happens. I'm going to save her."
jump choice15_save

#(Do nothing)
label choice15_nothing:
"Ryo clenched his fists, before letting out a sigh. There was nothing he could do."
jump choice15_end

label choice15_save:
scene black
with Dissolve(.5)
pause 1.0
scene street1
with Dissolve(1.0)
pause 2.0
scene house2
with Dissolve(2.0)
"Ryo huffed as he stood in front of Eve's house. He had just ran all the way there, but despite being out of breath he didn't feel tired. Instead he felt like he could do anything he was finding energy he didn't know he even had."
r "Eve hang on. I'll save you."
scene black
with Dissolve(.5)
"After a few slams the door burst open allowing Ryo to enter inside."
r "Eve! Eve! Answer me Eve! Are you here!?"
"He took a gulp, before his eyes narrowed with conviction. No matter what he found inside he would be ready and do whatever it takes to save Eve."
"Taking a step into the house, Ryo began to scan the room he found himself in."
"Right away his eye was snatched up by the end table. Garbage and mail cluttered it, overshadowing the furniture in a sea of trash."
"A tall glass cabinet caught Ryo's attention. There was only one thing inside the see-through amoure. An old photograph coated in a layer of dust."
"It was a photo of a woman wearing the same outfit Eve always wore playing with a little girl."
e "No, father please stop."
"Eve's outcry snagged Ryo's attention, causing his legs to move to her location without a second thought."
scene house_in2
with Dissolve(.5)
"Bursting through the door, he spotted Eve laying on the floor, her father standing over her."
"Ryo's vision flooded with red as he stared at Eve lying motionless on the floor."
r "Eve..."
r "How... how could you?"
"Ryo's fist shook from rage and he rushed at Eve's dad without a second thought."
"Ryo quickly realized that he was outmatched. He wasn't all that athletic and tough, but compared to this tall muscular man he felt akin to an ant."
"A punch to the gut caused Ryo to gasp for breath as he fell to his knees."  
r "I need to think of something. At this rate, I'm not going to be able to save Eve. I can't do this by myself, I need some kind of help."
"He noticed the father picking up an empty glass beer bottle. Ryo scanned the room in an instant trying to locate something he could use for a weapon, but to his regret nothing seemed to be of use."
r "Something of use could be in the living room. I could try making a break for there and hope I can find something there."
menu:
        "Make a break for the living room.":
            jump choice18_livingroom

        "Stay in the room and continuing fighting.":
            jump choice18_bathroom
 
label choice18_livingroom:
  "Ryo let out a huff before making a sprint to the door."
  "However right as his body pass through the door he felt a horrid pain swell up on his arm and the echoing sound of shattering glass."
  "Ryo's arm dropped limply to his side as all feeling left it. That one strike had shattered the nerves in his arm and caused it to go numb."
  scene black
  with Dissolve(.5)
  "Holding his arm Ryo rushed into the living room."
  "Before he even had any time to react to he felt his body be thrown into the end table. His head clipped the corner of the table."
  "Ryo was grabbed by the collar of his shirt and held up by it. A stream of blood ran down his forehead from the cut, creating a red line on his face."
  dad2 "You brat, just where do you think you are going? Huh?!"
  "His breath reeked of alcohol. His speech slurred from the thickness of his induced state."
  r "Sir you need to calm down you are hurting Eve. What you are doing is wrong, and you don't deserve to have a daughter if you do things like this."
  "Ryo tried to punch the man in the gut."
  "The man staggered slightly, but his grip on Ryo only tightened."
  "With the force of a rhino Ryo felt his body get thrown backward." 
  "A shock wave of pain wracked his body as he crashed into the glass cabinet. With the sound level of a train the cabinet fell forward and smashed into Ryo's back."
  "Glass shattered everywhere like a rain of blades. They sliced into Ryo like with the ease of a scissor cutting into paper."
  "Ryo laid motionless around the sea of glass as blood poured of the many cuts on his body."
  r "Eve..."
  r "I'm sorry."
  r "I couldn't save you."
  "Tears formed in his eyes as his vision became hazy, just before he blacked out."
  jump bad_end
  
label choice18_bathroom:
  r "No, I can't run away and leave Eve. I have to stay here and protect her."
  "Ryo rushed at the man and delivered a punch to his stomach."
  "The man barely flinched at Ryo's punch. He lifted the bottle up into the air and prepared to hammer it into Ryo's skull."
  
menu:
    "Block with left arm.":
        jump choice19_left

    "Block with right arm.":  
        jump choice19_right

label choice19_left:
$ righthand_flag = False
"A loud 'thunk' rang out as the glass connected with Ryo's arm."
"Ryo could feel the bones in his wrist shatter, and his skin begin to swell up."
"This is my chance, I have to go on the attack now."
jump battle

label choice19_right:
$ righthand_flag = True
"A loud 'thunk' rang out as the glass connected with Ryo's arm."
"Ryo could feel the bones in his wrist shatter, and his skin begin to swell up."
"This is my chance, I have to go on the attack now."
jump battle
label battle:
"Ryo launched himself with all the strength he could muster into the chest of Eve's dad. Ramming into him with the strength of a bull." 
"The man lost his balanced and was pushed backward. His head slammed into the side of the bathtub which caused the bottle to fall from his hand and rolled along the tile."
dad2 "You're dead."
"The man grabbed Ryo and delivered a strong punch to his face, sending him backward into the wall."
"A trickle of blood ran down the side of Ryo's face as he tried to regain his focus. That last punch had knocked the wind out of him, causing the world around him to spin."
dad2 "You're dead brat."
"Ryo stared up at the man towering over him like an executioner."
if righthand_flag:
        jump die
else:
        jump win
  
label win:       
  "Ryo spotted the bottle out of the corner of his eye and in a split second descion he snatched it up."
  r "I won't let you hurt Eve."
  "Ryo rushed at the man and drove the bottle into the side of the man's skull. The bottle shattered to pieces as the man fell to the floor."
  "Ryo let out deep breath and fell to his knees."
  "He just remained their like a statue. The only sound in the room was Ryo's huffing."
  show eve 9b
  with Dissolve(.5)
  e "AWHHHH!"
  "Eve's scream caused Ryo's eyes to fly open. She sat in the corner hugging her knees. Her body shook and rattled like she was experiencing an earthquake. Tears streamed down her face as she stared at her father."
  r "Eve? Are you okay?"
  "Eve did not respond to Ryo's voice instead she continued streaming and crying."
  show eve 10b
  with Dissolve(.5)
  e "No... No... This can't be happening."
  r "Eve, calm down."
  show eve 15b
  with Dissolve(.5)
  e "No."
  e "No."
  e "Noooooooo!"
  show eve 24b
  with Dissolve(.5)
  e "No! No! No! No!"
  "Eve seemed to be emotionally unstable. She snatched up one of the shards of glass and cut herself with it."
  r "Eve stop!"
  "Ryo rushed over to her and yanked the glass from her hand."
  show eve 9b
  with Dissolve(.5)
  e "No! Stop! Let me go! Don't stop me. I want to do this!"
  r "Eve, don't do this."
  show eve 9
  with Dissolve(.5)
  e "Let me go Ryo! I want to do this! I don't want to stay here anymore. I-I don't want this!"
  e "I don't want a life like this! No!"
  show eve 15b
  with Dissolve(.5)
  e "Please, Ryo... let me do this."
  r "I need to say something to calm her down."
menu:    
    "Don't worry. I'm here for you. I'll help you.":
        jump choice21_unstable


    "Fine, kill yourself. Take the cowards way out.":
        jump choice21_caretaker

label choice21_unstable:
  "Ryo held Eve close and whispered in her ear."
  show eve 24b
  with Dissolve(.5)
  e "But... but I don't want this."
  e "I want my father..."
  e "I want my mother..."
  e "I want to be with them..."
  e "I don't want this."
  r "It will be okay. I won't leave you."
  "Ryo's eyes flew open as he felt something wet on his hand. Blood was gushing out of new cut."
  show eve 15b
  with Dissolve(.5)
  e "I'm sorry, Ryo. I want to go."
  e "I want to be with them."
  "Ryo stared down at Eve. He refused to allow himself to cry and tried to remain as strong as he could."
  show eve 5b
  with Dissolve(3.5)
  r "I understand."
  r "Good-"
  r "Goodbye."
  r "Eve."
  hide eve 5b
  with Dissolve(3.5)
  pause 3.0
  scene black
  with Dissolve(3.0)
  pause 3.0
  scene bridge3
  with Dissolve(5.0)
  "The cold breeze roared causing Ryo's hair to become horrid looking."
  "He gazed over the side of the bridge at the water below."
  "He was dressed in a fancy suit, but rather than going to something happy, he had just come from a funeral."
  "Eve and her father had no relatives and no friends showed up, so in the end only he and his family attended."
  "It was overall just very sad event. Almost as if no one cared about these people. They only had each other."
  r "Eve was such a nice girl. Why does no one care? No one noticed her. She was just a shadow, being passed by and ignored."
  r "And she was always alone. She felt completely alone. Like no one saw her. Her whole world revolved around her family, the people she felt could see her."
  r "But I saw her. The lone shadow standing there on the bridge."
  "Ryo threw the flowers he was holding over the side of the bridge."
  r "And I'll miss her."   
  jump bad_end
  
label choice21_caretaker:
  show eve 20b
  with Dissolve(.5)
  e "Fine I will!"
  "Eve stabbed the glass in her stomach."
  r "You're just a coward! Go on quit! See if I care!"
  show eve 15b
  with Dissolve(.5)
  e "What? What?"
  "Shock shown on her face as she stared mouth agape at Ryo."
  r "You are taking the easy way out. And instead hurting everyone around you."
  show eve 10b
  with Dissolve(.5)
  e "What do you mean..."
  "Eve seemed to calm down as confusion took over her hysterics."
  r "You wonder how you are hurting people? Well you are hurting me. Because I have to go on without you. You know who will be in the most pain then?"
  r "Me. You'll hurt me."
  r "I don't want to go on without you."
  "Ryo scooped up another piece of glass and held it at his throat."
  r "If you go. I'm going with you."
  "Ryo stabbed the glass into his neck, allowing a trickle of blood to run down."
  show eve 24b
  with Dissolve(.5)
  e "No, stop!"
  "Eve cried out and dove at Ryo knocking the glass out of his hand."
  e "Don't do it Ryo."
  e "You have your whole life ahead of you."
  r "Then stay with me."
  show eve 6b
  with Dissolve(.5)
  r "Stay with me."
  show eve 15b
  with Dissolve(.5)
  show eve 24b
  with Dissolve(.5)
  e "I'll stay with you. So don't throw your life away."
  r "Then don't throw your life away either."
  r "Stay with me."
  show eve 23b
  with Dissolve(.5)
  e "I'll stay."
  e "Ryo."
  jump good_end
  
label die:
  "Ryo spotted the bottle out of the corner of his eye. He reached for it, but when he tried to grab it, he found he could not hold it. The bones in his right hand's wrist had been shattered, so he couldn't hold the bottle."
  "Ryo was frozen as his body was picked up and held in the air."
  "Everyone faded to black as he was thrown backwards and he felt his skull crash into the sink. A pool of blood poured out of his skull as stared at Eve."
  r "Eve...."
  r "I'm sorry."
  jump bad_end
  
label choice15_end:
play music "Music/Toy's Dance.ogg"
"All night long, and all the next day Ryo thought about Eve. Concerns for her safety ran through his mind constantly."
scene bridge1
with Dissolve(2.0)
pause 4.0
scene bridge1e
with Dissolve(3.0)
pause 4.0
scene bridge1n
with Dissolve(4.0)
r "Please show up today."
"Ryo waited and waited until soon he could barely see anything."
"He let out a sigh and was about to head home when he heard Eve's voice."
show eve d1
with Dissolve(.5)
e "Ryo?"
r "Eve, good you came. I was worried something happened to you."
show eve d3
with Dissolve(.5)
e "..."
r "Eve are you okay?"
show eve d3b
with Dissolve(.5)
e "..."
r "Eve?"
show eve d5b
with Dissolve(.5)
e "I don't know."
e "I'm really not sure Ryo."
show eve d10b
with Dissolve(.5)
e "I don't know if I can handle this anymore."
r "Eve, is there anything I can do?"
show eve 5b
with Dissolve(.5)
e "..."
show eve d3b
with Dissolve(.5)
e "Ryo..."
show eve d5b
with Dissolve(.5)
e "Will you come with me?"
menu:
      "Yes, I'll come with you.":
          jump choice20_come

      "I'm sorry, but I can't come with you.":
          jump choice20_sorry

label choice20_come:
show eve d7b
with Dissolve(.5)
e "Thank you, Ryo."
scene bridge5n
with Dissolve(.5)
"Eve climbed over the railing and stood on the edge."
r "Wait... what are you doing?"
show eve d8b
with Dissolve(.5)
e "You said you would come with me."
r "Eve, don't do this. It isn't worth it. Remember what you said, that bad times only last so long."
e "...."
show eve d3b
with Dissolve(.5)
e "So I'm guessing this means you aren't coming with me after all."
r "Eve don't throw your life away."
show eve d6b
with Dissolve(.5)
e "I'm not surprised. In the end, I'm always abandoned and left alone."
hide eve d6b
with Dissolve(.5)
r "Eve stop!"
"Ryo tried to grab a hold of her. But he was too late, the fabric slipped just through his fingers."
scene bridge3n
with Dissolve(.5)
r "No!"
r "Eve!"
"He angrily pounded the railing, until his fists started to bleed."
r "I couldn’t.... I couldn't do anything to help you."
r "I'm sorry Eve. I hope the pain is gone now."
r "...."
r "I won't forget you."
r "You've taught me the value of life."
r "Thank you, Eve."
jump bad_end

label choice20_sorry:
show eve d3b
with Dissolve(.5)
e "..."
show eve d5
with Dissolve(.5)
e "I figured you'd say that. I always end up alone. I'm the one who gets tossed away and abandoned."
r "You're not alone. I'm not tossing you aside. This just isn't the answer. Running away from the problem won't help you all that much. Just like ignoring it."
show eve d6
with Dissolve(.5)
e "So what should I do?"
r "Get help."
show eve d3
with Dissolve(.5)
e "Help?"
r "Yeah, try to get you and your dad consoling, so you can work through this. You love your dad, and if your dad loves you he will agree to it as well."
show eve d5
with Dissolve(.5)
e "I don't know Ryo... I'm scared."
r "Have faith Eve. Believe that he cares for you."
show eve d1
with Dissolve(.5)
e "I think I have a lot to think about, so I'm going to go home now."
r "Alright. Remember you aren't all alone."
e "I will."
hide eve d1
with Dissolve(.5)
scene black
with Dissolve(2.0)
pause 3.0

#(Help)
play music "Music/Firefly.ogg"
label choice20_end:
scene bridge1
with Dissolve(2.0)
pause 2.0
show eve 4
with Dissolve(.5)
e "Ryo."
r "That's rare. You greeting me, and you didn't even let me get all that close."
show eve 3
with Dissolve(.5)
e "Stop. This is important. I have something I need to tell you."
r "Hmm?"
show eve 1b
with Dissolve(.5)
e "We won't be seeing each other for a while."
r "Why? What is going on?"
show eve 17b
with Dissolve(.5)
e "I took your advice, my father and I are going to be getting consoling. Though it means I don't have time to greet you here anymore."
show eve 7b
with Dissolve(.5)
e "I don't know when I will be able to greet you here anymore."
show eve 2b
with Dissolve(.5)
e "However, can you wait for me?"
show eve 10b
with Dissolve(.5)
e "I know it is a selfish request. To ask you to wait for me here after school every day, for an unknown amount of time. So I don't want you to wait long, just 10 minutes will suffice."
show eve 8b
with Dissolve(.5)
e "So can you wait for me Ryo?"
e "I don't want to lose our friendship."
r "Don't be silly Eve."
r "Oh course I will wait for you. We're friends. That is just a silly thing to ask, for I would do it anyway."
show eve 16
with Dissolve(.5)
e "Thank you Ryo!"
show eve 18
with Dissolve(.5)
e "Till we meet again."
hide eve 18
with Dissolve(.5)
"Ryo smiled until Eve disappeared from sight. He was happy for Eve, but he still couldn't manage anymore than a fake smile."
r "Yeah... till we meet again."
pause 2.0
scene black
with Dissolve(.5)
pause 2.0

#(Not there)
queue music "Music/Firefly.ogg"
scene bridge1
with Dissolve(1.0)
"Even though he knew Eve wouldn't be showing up, he still found himself standing on the bridge."
scene bridge2
with Dissolve(1.0)
r "It is really quiet without Eve."
scene bridge3
with Dissolve(1.0)
r "This isn't like the other times. I didn't know what to think at those times. But now I know she is fine right now."
scene bridge3e
with Dissolve(2.0)
r "It is really peaceful."
scene bridge5
with Dissolve(3.0)
pause 2.0
r "I think I understand why Eve looks at the water so much now."
r "It is calming."
r "Till we meet again Eve."
pause 3.0
scene black 
with Dissolve(.5)
pause 5.0

#(Family)
Shigeru "Ryo, headed home?"
r "Yeah, but first I'm going to stop by the bridge."
Chika "Aww, Ryo is so dedicated. It is cute."
Jiro "But it has been 6 months now. It is almost October."
"Ryo shrugged."
r "Habits are hard to break."
Chika "I hope she shows up one of these days."
scene bridge1
with Dissolve(2.0)
pause 3.0
scene bridge1e
with Dissolve(3.0)
pause 3.0    
play music "Music/Harmony.ogg"
show eve 19
with Dissolve(.5)
e "Ryo!"
"Ryo felt weight crash into his back. Small arms wrapped around him as he was forced into a hug."
e "You waited just like I asked."
show eve 18b
with Dissolve(.5)
e "I'm so happy."
r "Don’t worry about it."
r "Something seems different about you."
show eve 16b
with Dissolve(.5)
e "I am different. In fact I’m thinking about losing this look all together now."
r "No more gypsy look?"
show eve 18
with Dissolve(.5)
e "Yep."
r "What is it going to be now? A princess? An amazon?"
e "No."
show eve 16
with Dissolve(.5)
e "I figured I would maybe go for a more normal style."
r "What about the different style, and costume jewelry for pretend."
show eve 17b
with Dissolve(.5)
e "Does not matter anymore. In fact I do not normally wear this anymore at all."
e "I just wanted to wear it again while we met again for the memories and such."
r "Is that so?"
show eve 18b
with Dissolve(.5)
e "Yeah, I do not need them anymore."
e "I wore the cloak because I wanted to be ignored and forget about like a shadow. I did not want anymore to notice me, or call out to me. I just wanted to stay in my little bubble."
show eve 16b
with Dissolve(.5)
e "But I am glad you invaded it."
r "That is kind of funny, since it was your cloak that made me call out to you." 
e "Life is funny like that."
r "Anyway, continue."
show eve 17b
with Dissolve(.5)
e "Well I do not need the jewelry or outfit anymore. I no longer want the reason I wore them. I would not trade my life for a fantasy or another life anymore."
r "So I am guessing things went good with the consoling."
show eve 18b
with Dissolve(.5)
e "Yeah, it took a long while, but things finally are good again. And I am even over my mom leaving us."
r "Wait; what?"
show eve 16b
with Dissolve(.5)
e "It is nothing, do not worry about it. It is not a weight holding me down anymore. I have freed myself from my problems and worries."
e "And even if I do not have a perfect life. I would not trade my life for anything. I love my life."
if love_points > 4:
        jump choice_final
else:
        if love_points == 4:
                jump choice_final
        else:
                jump choice21_friend

label choice_final:
show eve 6b
with Dissolve(.5)
e "Hey, Ryo."
r "Hmm?"
show eve 16b
with Dissolve(.5)
e "How do you feel about me?"
menu:
      "You are my friend":
          show eve 18b
          with Dissolve(.5)
          e "That is what I thought. And I would be mad if you said you didn't see me as a friend. After all the time we've spent together."
          jump choice21_friend

      "I think I like you more than a friend.":
          jump choice21_love


#(Road to happiness)
label choice21_love:
show eve 6b
with Dissolve(.5)
e "What?"
e "I must have heard that wrong. Can you repeat that."
r "I like you more than just a friend."
show eve 6
with Dissolve(.5)
e "Yeah..."
e "That is what I thought you said."
r "..."
r "..."
r "No reaction."
show eve 3b
with Dissolve(.5)
e "It is called being speechless, and it is a reaction, Genius."
show eve 2b
with Dissolve(.5)
e "I honestly do not know what to say."
show eve 16
with Dissolve(.5)
e "But I can feel my heart beating, so I wonder if I happy about it."
r "I thought you did not believe in love."
show eve 4b
with Dissolve(.5)
e "I do not know what to believe. My mom ruined both my dad, and mine life when she left us."
r "I will just have to prove it to you then. Will you give me the chance?"
show eve 2b
with Dissolve(.5)
e "I doubt I have a choice in the matter. You are the one making the choices right now from my perspective."
r "You have got that right."
"Ryo leaned down and brought his lips close to Eve’s" 
r "You can pull away if you want."
show eve 19b
with Dissolve(.5)
e "I know, Genius."
"Ryo's eyes flew open and Eve closed the space between them and made the first move."
"The kiss only last for a few short moments, before Eve pulled away."
show eve 18b
with Dissolve(.5)
e "You'll have to work hard to prove to me the existence of love if you want a longer kiss or anything more."
r "Don't worry, I won't give up. I didn't stop coming each and everyday. I will give this even more effort. I will make you believe in love."
show eve 19b
with Dissolve(.5)
e "Geez, stop being so corny."
e "I can't stop laughing now."
r "Eve."
show eve 4b
with Dissolve(.5)
e "Hmm?"
r "I love you."
"Ryo planted a soft kiss on Eve's forehead."
show eve 2b
with Dissolve(.5)
e "We'll have to work on that..."
e "If you keep up all this corny stuff we won't last long."
r "Sorry."
show eve 18b
with Dissolve(.5)
e "Well... I guess it can't hurt, once in a while."
show eve 16b
with Dissolve(.5)
e "Ryo, I think I might be falling for you as well."
e "Just maybe, we could reach a happy ending."
r "Now, who is being corny."
show eve 21b
with Dissolve(.5)
e "Shut up, I was trying to be sweet!"
r "And I love that about you."
show eve 2b
with Dissolve(.5)
e "Geez, you keep throwing curve balls at me, it is like I'm a baseball player."
r "A baseball player in the game of love."
show eve 9b
with Dissolve(.5)
e "Grr stop already."
"Eve stormed away grumbling to herself. Ryo could not help but smile as he followed behind her."
r "I love you Eve."
show eve 10
with Dissolve(.5)
e "UG! Stop that!"
jump good_end

#(Smile)
label choice21_friend:
show eve 16
with Dissolve(.5)
e "Without you Ryo, I wouldn't have lowered my mask. I would still be hiding in the shadows. And even if someone spoke to me, I would just have a plastic smile."
show eve 5
with Dissolve(.5)
e "Most of the time my emotion was plastic. Even during the time we spent together, I never really got it deep down."
show eve 4b
with Dissolve(.5)
e "I was just playing the happy part, hoping my inner-self would change to match it. I was lying to myself trying to force myself to say that I was happy."
show eve 3b
with Dissolve(.5)
e "But not anymore. It has been such a long time since my smile had any light in it."
r "I don't see anything different about it."
r "You are still the same Eve to me. The Eve I've been having fun with since day 1."
show eve 6b
with Dissolve(.5)
e "You're right, I still am pretty much the same. Maybe I was wrong actually. Maybe all that time I did show some of my real self. The mask was cracked I guess."
show eve 21b
with Dissolve(.5)
e "Are all my metaphors flying over your head genius."
r "What? Of course not."
show eve 19b
with Dissolve(.5)
e "Haha, I'm just kidding."
show eve 16b
with Dissolve(.5)
e "But really Ryo. If I wasn't for you. I wouldn't know how to smile."
show eve 18b
with Dissolve(.5)
e "Thank you."
r "Your-"
show eve 21b
with Dissolve(.5)
e "Alright that is enough of that! Ryo, I challenge you to a race. Whoever reaches the park first wins. The loser has to buy food for the winner, whatever the winner wants."
r "What? Wait-"
show eve 19b
with Dissolve(.5)
e "And I want lobster, or maybe steak, steak and lobster?"
r "I can't really-"
show eve 21b
with Dissolve(.5)
e "Go!"
r "Wait Eve!"
e "Slowpoke! And you call yourself a guy. A girl is beating you. You better have your savings account ready!"
scene black
with Dissolve(.5)
"Ryo shook his head, but nonetheless joined in anyway."
r "That's it is on!"
pause 2.0
scene park4
with Dissolve(1.0)
pause 2.0
show eve 19
with Dissolve(.5)
e "I win! I win!"
r "My wallet is so screwed..."
show eve 16
with Dissolve(.5)
e "Let's go some place cheap."
r "What happened to steak and lobster?"
show eve 6
with Dissolve(.5)
e "Do you want to buy me that?"
r "No."
show eve 18
with Dissolve(.5)
e "Then just consider it your reward for waiting all the time for me."
r "My wallet is-"
show eve 19b
with Dissolve(.5)
e "But that doesn't mean I won't order one of everything~"
r "...Screwed."
if book_flag:
        if friend_flag:
                jump secret_end
        else:
                jump good_end
else:
    jump good_end
    
#(Regret)
label secret_end:
queue music "Music/Life.ogg"
scene bridge3
with fade
"Eve stood on the bridge. The wind blew through her hair as she stared down at the water. A bouquet of flowers was in her hand."
show eve 13
with Dissolve(.5)
e "Ryo..."
"Her eyes started to fill with tears."
show eve 14b
with Dissolve(.5)
e "I never thought, that something like this would happen."
e "That when you went on a cruise with your friends you would go missing."
show eve 15b
with Dissolve(.5)
e "I-I...I should have gone with too."
e "You might not have gone missing if I had gone with."
show eve 14
with Dissolve(.5)
e "I refuse to believe you are dead."
e "Even if everyone says you died, and there is no chance of you living after falling off the boat."
show eve 22b
with Dissolve(.5)
e "I'll believe."
e "Even if it just a silly thing. I'll believe, and I'll make others believe as well."
show eve 23b
with Dissolve(.5)
e "I'll rewrite it. Even if it has no meaning, I'll make everyone think that you happened to drift to a nearby island."
show eve 22b
with Dissolve(.5)
e "I'll believe that you survived."
e "And someday we will meet again."
e "Ryo."
e "Till we meet again."
jump true_end

label bad_end:
play music "Music/Eternal Dream.ogg"
scene black
with Dissolve(1.0)
pause 2.0
scene end1
with Dissolve(2.0)
scene end3 
with Dissolve(2.0)
pause 6.0
scene black
with Dissolve(1.0)
pause 2.0
return
    
label good_end:
scene black
with Dissolve(1.0)
pause 2.0
scene end1
with Dissolve(2.0)
scene end2 
with Dissolve(2.0)
pause 6.0
scene black
with Dissolve(1.0)
pause 2.0
return

label true_end:
play music "Music/Cold Mind.ogg"
scene black
with Dissolve(1.0)
pause 2.0
scene end1
with Dissolve(2.0)
scene end4 
with Dissolve(2.0)
pause 6.0
scene black
with Dissolve(1.0)
pause 2.0
return
