init:
	#Image Declarations
	#weetabix
	image weet cred = "img/portcred.jpg"
	image weet title = "img/title.jpg"
	image weet end = "img/credit.jpg"
	#chapters
	image chap on = "img/chapteron.jpg"
	image chap 1 = "img/chapter1.jpg"
	image chap 2 = "img/chapter2.jpg"
	image chap 3 = "img/chapter3.jpg"
	image chap 4 = "img/chapter4.jpg"
	image chap 5 = "img/chapter5.jpg"
	image chap 6 = "img/chapter6.jpg"
	image chap 7 = "img/chapter7.jpg"
	image chap 8 = "img/chapter8.jpg"
	image chap 9 = "img/chapter9.jpg"
	image chap 0 = "img/chapter0.jpg"
	image chap off = "img/chapteroff.jpg"
	#backgrounds
	image bg sky = "img/sky.jpg"
	image bg sky2 = "img/sky2.jpg"
	image bg sky3 = "img/sky3.jpg"
	image bg way = "img/way.jpg"
	image bg way2 = "img/way2.jpg"
	image bg way3 = "img/way3.jpg"
	image bg wayinv = "img/wayinv.jpg"
	image bg park = "img/park.jpg"
	image bg station = "img/station.jpg"
	#characters
	image phone minamo1 = "img/minamo1.png"
	image phone minamo2 = "img/minamo2.png"
	image phone minamo3 = "img/minamo3.png"
	image phone minamo4 = "img/minamo4.png"
	image phone minamo5 = "img/minamo5.png"
	image phone minamo6 = "img/minamo6.png"
	image phone minamo7 = "img/minamo7.png"
	image phone minamo8 = "img/minamo8.png"
	image phone ituki1 = "img/ituki1.png"
	image phone ituki2 = "img/ituki2.png"
	image phone ituki3 = "img/ituki3.png"
	image phone ituki4 = "img/ituki4.png"
	image phone ituki5 = "img/ituki5.png"
	image phone ituki6 = "img/ituki6.png"
	image phone ituki7 = "img/ituki7.png"
	image phone blank0 = "img/blank0.png"
	image phone blank1 = "img/blank1.png"
	#Character Declarations
	define ka = Character('Kasumi')
	define mi = Character('Minamo')
	define it = Character('Itsuki')
	define yu = Character('Yuuna')
label start:
	scene weet cred
	$renpy.pause(3)
	play music "snd/tasogare.ogg"
	scene bg sky2
	"'When we say that something is 'impossible', does that always have to mean that in reality the thing in question can't ever actually happen? I'm not sure I agree with that...'"
	"'See, I'd rather believe that the 'impossible' is merely something that others would never believe really happened, even if it did -- and even if you told them as much, right to their faces.'"
	"...is what she said to me as spoonful after dainty spoonful of black currant syrup-laced shaved ice disappeared neatly into her mouth."
	"In other words, that which I had experienced was just such a thing -- an 'impossibility'."
	scene weet title
	$renpy.pause(4)
label on:
	scene chap on
	$renpy.pause(2)
	scene bg sky3
	"What is the meaning of life?"
	"Why does the world exist?"
	"Why do people go on living? Just what is it that drives them to go on?"
	"All these mysteries..."
	"There's a part of me that keeps pondering and pondering about these things -- which is kinda weird, because I'd never so much as given them a second thought when I was a kid."
	"Maybe that's the so-called 'grown-up' in me. Or whatever."
	"But I haven't even once fallen in love, and I really don't *feel* like I'm becoming any more of a grown-up at all."
	"I'm not even filling out like a girl's supposed to...well, okay, let's be honest: I'm trying to say that I'm still flat as a board and *not* very happy about it."
	"In fact, ever since my first period -- the 'first (and only?) womanly thing about you', as my mom and my big sister so kindly put it -- this has all been nothing but trouble for me."
	"There's no way I can tell whether I'm gracefully becoming an adult or whether I'm still awfully childish for my age, either."
	"But I do know one thing: when I was a kid, I didn't have a single care about myself or about the world."
	"And lately, I've been thinking that maybe this is what becoming a grown-up is all about."
	"In other words, that becoming an adult..."
	"...is about not being able to accept..."
	"...the world that exists around me, or even the world that exists within me, just as it is anymore..."
	"I really don't think that I'm anywhere near to being all grown up yet, but I can feel myself becoming less and less of a child at an alarming pace."
	"So here I am, straddling the line in the sand."
	"[Name: Kasumi Kurasawa]"
	"[Sex: Female]"
	"[Birthday: 7/21]"
	"[Sign: Cancer]"
	"[Blood Type: O]"
	"[Saegasaki High School, 1st-year student]"
	"[15 years of age]"
	"...that was all there was to me."
	play music "snd/blank.ogg"
label 1:
	scene chap 1
	$renpy.pause(2)
	scene bg way
	play music "snd/natukaze.ogg"
	"*ka-click* *thump*"
	"This was definitely the high point of my mornings."
	"I always stopped by the vending machine next to the sweets shop, bought myself a Capri Sun, and slipped it into my backpack (which, of course, was in my bike's front basket)."
	"And then I'd drink it as I chatted with friends after I'd gotten to the classroom."
	"And of course, I had no plans on doing any differently today."
	"True, I was putting on a little more speed than usual because I was kind of on the late side, but otherwise, this was just the same old, same old morning routine. Nothing out of the ordinary at all."
	"But just as I rounded the last corner to school, a bike suddenly came speeding at me out of nowhere."
	"With incredible power, at that."
	"Eeeek!!"
	play music "snd/blank.ogg"
	"*WHAM!*"
	"The bike -- and the boy on it -- smashed into my bike's front wheel, sending us all flying."
	"The boy, our two bikes, and I all came crashing down to the ground..."
	"...and my backpack went tumbling across the street like a forlorn flat tire."
	"A glorious train wreck. Well, you know."
	ka "Owwwwww!"
	"By now the boy had crawled out from under his bike and gotten to his feet; now he stood brushing off his uniform."
	"???" "Ah...pardon me."
	"When he noticed me, the boy kind of shrugged in apology and then made as if to pick up my backpack."
	"I'd seen that uniform from somewhere."
	"So he went to the neighboring middle school."
#	play sound "snd/car.ogg"
	"*HONK*HONK*..."
	"...*CRUNCH*"
	ka "...oh..."
	"But the boy was nowhere near in time, and my backpack was ruthlessly run over by a small truck that was speeding by."
	ka "...oh."
	"Oh, as in: oh, my poor bag."
	"Oh, as in: oh, no, the stuff inside my bag."
	"Oh, as in: oh, this sucks."
	"I didn't have the strength or the heart to do anything but sit there dazedly and accept my busted backpack -- tire tracks and all -- when the boy finally handed it to me."
	"And then, I carefully opened it."
	"However..."
	scene bg wayinv
	ka "Augh!"
	scene bg way
	"Sure enough..."
	"The pack of Capri Sun had exploded from being run over, soaking my notebook and textbooks all over the place."
	ka "Gaaaaah!! My cellphone!!"
	"There were cracks all over the pink casing of my poor cellphone..."
	"...and I could tell that the Capri Sun had already soaked into the electronics through those cracks. It was such a pitiful sight."
	ka "Augh! My grandpa bought this to commemorate my entrance into high school!"
	ka "Just WHAT are you going to do about this, hmm?!"
	"But even as I looked up accusingly at the boy, he stepped back with a frightened expression on his face, righted his bike, and raced away as if he were being chased by a demon."
	ka "Hey! Wait, you...!"
	ka "......"
	ka "You STUPID LOSER!!"
#	play sound "snd/chaim.ogg"
	"*ding*dong*ding*dong*..."
	"I could hear our school's chime signaling the start of first period, ringing brightly like the punchline to a very, very bad joke."
	ka "Man, this sucks..."
	"Great, so now I was late on top of everything else."
	"This was turning out to be the worst morning of my life."
	play music "snd/blank.ogg"
	scene black
	$renpy.pause(2)
	play music "snd/city.ogg"
	scene bg sky
	"???" "Good morning, Kasumi...hey, wait, what happened to you?!"
	"It was now after homeroom...which, by the way, I'd walked in completely late for, all right..."
	"...and now my friend (?) Yuuna was staring at me -- and speaking to me -- with bewilderment."
	ka "Oh, man, let me tell you, Yuuna, something horrible happened to me just a little while ago..."
	"And, holding back tears, I filled her in on the disaster that had befallen me on the way to school."
	ka "Ahahaha! That just sucks!"
	yu "PLEASE don't look so delighted about that!"
	ka "Ugh, I guess this cellphone's no good anymore..."
	"Even though I'd wiped out the insides as well as I could and then masked all the cracks with scotch tape, the phone still wouldn't turn on or anything."
	yu "Well, given what it's been through, that's no surprise, is it now? And it smells kinda funny, too."
	ka "Waaaah! My poor phone's become a Capri Cell!!"
	yu "*sigh* c'mon, this all happened 'cause you drink that weird stuff every day. Divine punishment, see?"
	ka "Oh, don't be mean! Capri Sun is really tasty, and you know it!"
	yu "Yes, yes, only to YOU."
	"Just then, someone came to the classroom in search of Yuuna."
	"It was her boyfriend."
	"Jeez, he was such a flake. What was he doing, calling her out like this when class was going to begin in five minutes?"
	"And on top of that, in his presence Yuuna became so refined and ladylike, never displaying even an ounce of the venom that so eagerly dripped from her teeth when it was just her and me."
	"So unfair..."
	"It made me want to sigh in despair sometimes."
	"I mean, we'd gone to the same middle school, were attending the same high school, and were the same age, and yet we couldn't be more different."
	"She had a boyfriend, and she seemed to make the most of every day, even given the fact that she didn't participate in club activities after school."
	"Let's see. Compared to her...well...I enjoyed the various Capri Sun flavors but didn't really have anything I was passionate about, wasn't falling in love anytime soon, and didn't excel at any club activities either."
	"I was only average (or worse) at school and sports, didn't have any particularly interesting points, and wasn't really interested in any hobbies either."
	"And to top things off, my cellphone didn't even work anymore."
	ka "So I've got nothing..."
	"I looked out the window at a blue sky that obviously didn't care one whit about me."
	"And that was just as well -- I had nothing to my name but...well...nothing. I might as well have been walking around with a chunk of air inside me and nothing else."
	"Was there any value in my being alive?"
	"Did someone as pathetic as me have any hope for the future?"
	"Right now, even questions like THAT were floating around my head."
#	play sound "snd/noise.ogg"
	"*SHING*..."
	ka "Huh?"
	"For a moment, I could have sworn I saw a strange staticky discharge from my cellphone."
	ka "......"
	"(?)"
	"I stared at it cautiously for a while after that, but the phone was as dead as ever."
	"Was it just my imagination?"
#	play sound "snd/chaim.ogg"
	"*ding*dong*ding*dong*..."
	"And then the next period began."
	play music "snd/blank.ogg"
label 2:
	scene chap 2
	$renpy.pause(2)
	scene bg way2
	play music "snd/tasogare.ogg"
#	play sound "snd/higurasi.ogg"
	"I made my way home slowly on a darkened country road, pushing along my bike and its newly-wobbly front wheel."
	"One disheartened trudge at a time."
	"(All right, so I can get my dad to fix my bike...)"
	"(But how am I going to tell him about my cell...?)"
	"The contours of the moutains, dyed yellow in the early evening light, marched out into the horizon."
	"Come to think of it, it had been getting hotter and hotter as of late..."
	"I sighed unhappily."
#	play sound "snd/noise.ogg"
	"*SHING*"
	"?"
	"I could have sworn that I heard some kind of staticky noise from somewhere."
	"And just as I started wondering about it..."
	play music "snd/blank.ogg"
	"*SHIIIING*"
	show phone minamo8
	"???" "Take that! And that!"
	"???" "You worthless piece of junk!"
	"??!!"
	play music "snd/natukaze.ogg"
	show phone minamo5
	"???" "......huh?"
	show phone minamo1
	"???" "...what the...?"
	"I almost fell over in shock."
	"...and for good reason, too."
	"I mean, it wasn't every day that a girl just appeared in front of me out of thin air like this."
	ka "Um...hmm...who are you?"
	"Okay, so apparently the girl in the middle of the air could see me, too."
	"And she had just spoken to me with a voice that sounded like it was being broadcast over a speakerphone."
	"???" "Uh...uh...ummm..."
	"What in the world? What in the world was this?"
	show phone minamo2
	mi "I'm Minamo..."
	mi "...Minamo Kawara, if you want my full name."
	ka "Uh, oh...okay."
	show phone minamo1
	mi "And what about you?"
	ka "My name is...Kasumi Kurasawa."
	"Was this some kind of hologram?"
	"Whatever it was, it was as hazy and as insubstantial as mist, like an illusion or a mirage."
	"And even when I stretched out an arm to try to touch it, my hand passed right through it."
	mi "So is that 'Kasumi-chan', then?"
	mi "Or 'Kasumii'?"
	mi "Or maybe 'Kasupyon'?"
	mi "How about 'Kaya'?"
	"Seemingly paying no heed to my bewilderment, the girl in the hologram started spouting a bunch of proposed nicknames at me."
	ka "......"
	"What the heck was going on?"
	mi "C'mon, c'mon, what do you want me to call you?"
	ka "You can call me whatever you like..."
	ka "But more importantly...how did, uh, this happen?"
	mi "...'this'?"
	ka "You know, THIS."
	ka "I'm talking about how you just appeared before my eyes, out of thin air like this."
	mi "Oh, well, yeah, you did the same thing on this end, too."
	mi "But no, your guess as to how this happened is as good as mine."
	show phone minamo2
	mi "Hey, maybe this is a trick our cellphones are playing on us!"
	"My cellphone?"
	"I reached into the front basket of my bike, opened my bag, and pulled my phone out of it."
	ka "......"
	"But the LCD was blank, and it looked as broken as it did this morning."
	"...and yet..."
	mi "Hey, I can see some of the area around you. So it's in the evening there, right, same as here? Lots of mountains?"
	"...that girl's voice was somehow coming out of my cellphone's speaker."
	"I jabbed the Call End button, just on a whim."
	play music "snd/blank.ogg"
	hide phone
	"*BLIP*"
	$renpy.pause(0.4)
	ka "......"
	"We got cut off."
	"That...was REALLY smart of me..."
	scene bg sky2
	"And after that, I couldn't get anything even remotely resembling that phenomenon to happen, no matter how much I fiddled around with my phone."
	scene bg sky3
	"Had that all been for real?"
	"It certainly looked as if my phone hadn't been suddenly fixed by all the jostling around, for one thing."
	"No, the fact that it was broken hadn't changed at all."
	"I tried doing all sorts of things to it for a while, but nothing ever happened, and for that matter I couldn't even make normal phone calls on it."
	"And obviously, no holograms appeared out of thin air, either..."
	ka "Hey, Oneechan..."
	"I told my big sister about everything that had happened this morning and this evening, just to see how she'd react."
	"And she told me: let me take a look at that cellphone of yours, then."
	"I brought the cracked, broken unit to her, but it just lay there stubbornly, doing nothing. Of course."
	"Oneechan" "Just what kind of wild goose chase are you trying to lead me on now? You know as well as I do that there's no way that phone can do ANYTHING in its current state, silly!"
	ka "Yeah, but couldn't it ever happen? You know, maybe the force of the shock and the soaking with Capri Sun made it, like, totally mutate somehow...?"
	"Oneechan" "Um, while I guess it WOULD be pretty awesome if such phones could exist..."
	"And she just smiled fondly at me."
	"As if she didn't believe me at all."
	ka "C'mon, maybe it's a one-in-a-million kind of thing...?"
	"Oneechan" "Look, even if you had said 'one-in-a-billion' or 'one-in-a-trillion', it still wouldn't change the fact that such a thing is impossible."
	"Oneechan" "So quit your daydreaming already, for crying out loud."
	ka "Ugh~~"
	"I begged and pleaded with her for a little bit longer, but it was no use."
	"I tried telling my mom and dad about it too, but they didn't believe me either."
	"Okay, okay, so I didn't have any proof or anything; there was no way I stood a chance of convincing them...I guess."
	"As a matter of fact, the only thing that came of telling them what happened was that I got scolded for having broken such a valuable gift from my grandfather."
	"But still...just what the heck happened to me...?"
	play music "snd/blank.ogg"
label 3:
	scene chap 3
	$renpy.pause(2)
	scene bg way
	"A few days later..."
	scene bg way2
	"I was heading home from school again."
	"Oh, and I was still carrying that broken cellphone around with me, having refused to get it repaired (which confused my parents to no end, I'm sure)."
	"After all, there was no telling whether I'd hear that noise again, and whether that girl would appear out of thin air again."
	"So I was acutely aware of the seconds ticking by -- maybe it was because I was really hoping it would happen."
# 	play sound "snd/noise.ogg"
	"*SHIIIIIIING*"
	$renpy.pause(0.4)
	"'!'"
	"(Yes!)"
	show phone ituki4
	play music "snd/natukaze.ogg"
	"???" "Oh...!"
	"???" "Oh my?"
	"A hologram had popped up right before me just as I had hoped, but the person inside it wasn't the girl I had seen the last time around."
#	play sound "snd/higurasi.ogg"
	"???" "......"
	ka "......"
	"For a while, both of us were silent: she still looked like she was recovering from her initial shock, and I couldn't bring myself to say anything."
	"And so we stared at each other instead."
	"Unlike the energetic girl from last time, the person before me was a strikingly pretty -- no, utterly beautiful -- woman with a calm, refined air about her."
	ka "Uh, um...nice to meet you."
	"I stammered my way through a greeting, still completely stunned by her beauty."
	ka "My name is Kasumi Kurasawa. I'm 15 years old, and a freshman in high school. This kind of thing has happened to me once before, too."
	show phone ituki1
	"???" "Okay..."
	ka "And, um, ummmm..."
	"???" "So what Minamo said was true after all, then."
	ka "Huh?"
	"???" "Oh, my apologies."
	"???" "I am pleased to make your acquaintance as well."
	it "My name is Itsuki Mukai."
	it "I am two years older than Minamo, and I go to the same high school as her."
	"She said to me warmly and gently, as if she were talking to a child. Wow, she sounded so grown-up!"
	show phone ituki5
	it "I am glad to have met you, Kasumi-chan."
	"*tha-thump*"
	"How strange."
	"My heart was beating a little faster just in the presence of that woman's gentle smile."
	show phone minamo1
	mi "Hey! She's here!"
	"All the sudden..."
	ka "Whoa...!"
	mi "Hey, what's up, Kasumii?! It's been a while!"
	"The energetic girl from before rushed onscreen, crowding the woman out."
	"And she looked straight at me with a grin that would have split her face in two if it were any broader than it already was."
	ka "Ahaha...good to see you too, Minamo-chan."
	"I answered, likewise with a smile on my face."
	ka "I'm sorry about last time; I pressed the Call End button just to see what would happen, and we got disconnected because of it."
	mi "Oh, so that's what happened. In that case I'll be careful about that from now on too."
	"For some reason -- maybe it was because I'd so been looking forward to talking with her again -- it didn't feel like we were strangers at all anymore."
	show phone minamo3
	mi "See, Ii-nee? It's true, isn't it?"
	it "So it is. Pretty surprising!"
	"Minamo was pointing a finger at me and looking with vindicated pride at that woman named Itsuki."
	show phone minamo6
	mi "Hey, guess what, Kasumii? I told Ii-nee here about how we first met like this, and she didn't believe a word I said."
	ka "Yeah, I'm not surprised. I told my big sister and my mom about it too, and I couldn't get them to buy it either."
	show phone minamo1
	mi "Oh! So you have a big sister, then?"
	ka "Yeah. Just one; she's two years older than me."
	"Just then, I could see a finger poking Minamo-chan gently in the arm, as if to restrain her. Probably Itsuki-san."
	show phone minamo4
	mi "Huh, then it's kinda like me and Ii-nee. Well, although in this case we're just next-door neighbors and childhood friends."
	ka "Wha?! But my big sister isn't nearly as lovely as Itsuki-san is!"
	"I blurted out my true feelings right then and there."
	"And with a gentle jerk, Minamo-chan was pushed offscreen, and Itsuki-san cut in."
	show phone ituki5
	it "*giggle* thank you!"
	"She flashed me a smile that seemed truly happy, all the way down to the bottom of her heart, but soon enough Minamo-chan pushed her back."
	show phone minamo3
	mi "Aww, c'mon, stop that, Ii-nee!"
	ka "Ahaha!"
	"This was kinda fun."
	"The atmosphere of this long road -- which I'd always taken home, alone -- had completely changed."
	it "Anyway, Minamo. Come now, there are many more interesting questions to be asking at this time, are there not?"
	"Itsuki-san said from offscreen."
	show phone minamo1
	mi "Huh?"
	it "See...well, here, let's trade places for a second."
	show phone ituki1
	it "Good afternoon, Kasumi-chan."
	"She smiled sweetly at me again."
	show phone ituki4
	ka "Well, no, it's more like 'good evening', huh?"
	it "Yes, it'll be getting pretty dark soon."
	show phone ituki1
	ka "So it seems."
	it "Say, would you mind terribly if I asked you a bunch of questions? Of course, I'd be more than happy to answer any questions you have too, so how about it?"
	ka "Oh, of course..."
	it "Okay, well then, where shall we start?"
	it "Right now, we are in Ebisu. Where are you, Kasumi-chan?"
	"Ebisu...? So they were in Tokyo, then."
	ka "I'm in Hino City right now..."
	it "...oh, I see...well, not that I know where that is."
	ka "Umm...well, it takes about three hours to get here from Tokyo by train."
	it "Oh, my. Fairly far away, then."
	ka "Yeah, it kinda is."
	it "Okay, then, Kasumi-chan, how did your cellphone end up this way?"
	ka "Um...well, at school...no, on my way to school, my bike collided with someone else's, and things have been this way ever since."
	show phone ituki4
	it "Hmmm."
	ka "It was inside my bag at the time, but then that bag got run over by a car."
	ka "And then on top of that, a drink pack that was also in my bag exploded from being run over, and my phone got soaked as a result..."
	ka "...and that's about it."
	show phone ituki1
	it "Thank you. Yes, I think I see."
	show phone ituki2
	it "That must have been so awful for you, Kasumi-chan. It makes me feel sorry just listening to you..."
	ka "Ahaha..."
	"Sure enough, it had been a streak of luck so bad that even I felt sorry for myself when I thought about it."
	show phone ituki1
	it "But still, how fascinating. Generally speaking, there is no way that an accident like that could lead to this kind of thing."
	ka "Well, yeah, my big sister said as much as well."
	"What was even more fascinating was the fact that I was speaking so freely with Itsuki-san, regardless of the fact that I was usually shy to the point of pain. Her presence was so disarming..."
	ka "Perhaps, perhaps. In any case, the story on this end is pretty similar."
	it "A few days ago, Minamo..."
	show phone minamo4
	mi "What what? Did you call?"
	show phone ituki6
	it "You, Miss, may stay silent until you are told you may do otherwise, thank you very much."
	mi "Eek..."
	ka "...ahaha!"
	"It sounded like Minamo-chan wasn't, after all, following our conversation from offscreen, but was spacing out in her boredom instead."
	show phone ituki1
	it "Um, where was I? Oh, yes! A few days ago, Minamo was eating kimchee ramen at the cafeteria when she accidentally dropped her cellphone into it."
	"(Kimchee...)"
	it "And then it seems that she proceeded to use a washing machine to clean it, as well as several hand washings with laundry detergent afterwards."
	show phone minamo2
	mi "Hey! I cleaned it up all nice and proper!"
	show phone ituki2
	it "........."
	show phone ituki1
	it "Any cellphone that wasn't already broken before that 'cleaning' would certainly be completely broken after that, don't you think?"
	mi "Y-yes..."
	"Incredible."
	"In fact, this had to be at the very least two times more unlikely than what happened to me."
	"It made me feel kinda sorry for Minamo-chan's cellphone, at the very least."
	it "But, well, she's got just that kind of personality -- it seems that when she gets serious, she'll do anything and everything to get what she wants."
	show phone minamo2
	mi "And I was in the middle of doing just that when suddenly, a scene popped out of mid-air and there you were, Kasumii!"
	show phone ituki1
	it "And it seems...that that's how we've come to this."
	ka "That's incredible..."
	show phone ituki5
	it "Yes, she's pretty incorrigible, isn't she?"
	show phone minamo3
	mi "AHEM!"
	hide phone
	scene bg sky2
	"I spoke with the two of them for a bit longer after that."
	"They were both good girls, and we quickly became good friends."
	"Even though this probably wasn't much in the grand scheme of things, it was a very important incident indeed in my ordinary, ordinary life."
	"Little did I know that something even more important still was to come a matter of seconds later."
	scene bg way2
	show phone ituki1
	ka "I'm glad to have met both of you."
	"I said from the bottom of my heart."
	it "I feel the same way."
	"And then Itsuki-san stared at me for a while, as if she were deep in thought about something."
	ka "...um, is something the matter, Itsuki-san?"
	it "Hmm? Yes."
	it "Well, you see, I was just thinking to myself that it's so wonderful..."
	ka "Huh?"
	it "It's almost bewitching, really."
	it "You see, from here I can see what you cannot. I can see that you are surrounded by the lushness of nature, and that you are bathed in the last rays of the setting sun. I can see that you look incredibly beautiful..."
	show phone ituki5
	it "...as if you were a veritable princess of the forest."
	play music "snd/blank.ogg"
	"Itsuki-san spoke those incredible words with that selfsame warm smile on her face."
	"Casually, as if they were the most natural things in the world to say."
	ka "...n-no, not at all!"
	"Even I could tell that I was blushing all over."
	hide phone
	scene bg sky2
	"How did it come to this?"
	"That very instant..."
	"...I fell in love without a second thought."
label 4:
	scene chap 4
	$renpy.pause(2)
	scene bg sky3
#	play sound "snd/musi.ogg"
	$renpy.pause(0.1)
	"......"
	"Right after that, my cellphone died again and we got disconnected."
	"So it seemed that 'connection' and 'disconnection' both were completely up to chance."
	play music "snd/yoiduki.ogg"
	ka "...augh..."
	"But in any case..."
	"......"
	"What was I going to do...?"
	"Was this something akin to the fabled 'love at first sight'...?"
	"I didn't understand."
	"I didn't understand anything at all."
	"Only much, much later would I come to understand what those feelings that had been born within me that moment really *were*."
	"But even if I tried to think about it, puzzle it out, the only thing that came to mind was Itsuki-san's face."
	scene black
	$renpy.pause(2)
	scene bg sky2
	show phone ituki1
	it "You see, from here I can see what you cannot. I can see that you are surrounded by the lushness of nature, and that you are bathed in the last rays of the setting sun. I can see that you look incredibly beautiful..."
	show phone ituki5
	it "...as if you were a veritable princess of the forest."
	hide phone
	scene black
	$renpy.pause(2)
	scene bg sky2
	show phone ituki1
	it "Well, you see, I was just thinking to myself that it's so wonderful..."
	it "It's almost bewitching, really."
	it "You see, from here I can see what you cannot. I can see that you are surrounded by the lushness of nature, and that you are bathed in the last rays of the setting sun. I can see that you look incredibly beautiful..."
	show phone ituki5
	"...as if you were a veritable princess of the forest."
	hide phone
	scene black
	$renpy.pause(2)
	scene bg sky3
	"I could see her brilliant smile rising tenderly against the skies of sunset even with my eyes closed."
	"(...no, *you're* the wonderful one...Itsuki-san...)"
	"The depths of my heart whispered time and time again."
#	play sound "snd/musi.ogg"
	"It was only after I'd decided that I didn't have much appetite for dinner, went into the bath pretty much dazed, and was soaking in the tub listening idly to the buzzing of the insects outside..."
	"...when I finally got it."
	"I was in love."
	"......"
	"But the person I was attracted to was a girl..."
	"...and a girl I'd just met today, on top of that..."
	"...and a girl that lovely and sweet had to have a boyfriend anyway..."
	"...and she was pretty far away anyway..."
	"...and I had no idea whether my cellphone would allow me to talk to her again..."
	"...and so it was possible that I might never get to see her or talk to her ever again..."
	"......"
	"...but none of that mattered."
	"You see..."
	"My heart and my mind both were filled -- filled with feelings toward Itsuki-san. And there was nothing else within me."
label 5:
	scene chap 5
	$renpy.pause(2)
	scene bg sky
	"For a few days after that, my cellphone didn't so much as make a sound."
	"When would we be connected next?"
	"Or would we ever be reconnected ever again?"
	"And so it was that I started waiting with bated breath for that strange phenomenon to occur again."
	"I couldn't bear not to see her face again."
	"I wanted desperately to be able to meet her again, and to confirm my own feelings toward her."
	play music "snd/blank.ogg"
	scene black
	$renpy.pause(2)
	scene bg way
#	play sound "snd/noise.ogg"
	"*SHIIIIIING*"
	$renpy.pause(0.2)
	show phone blank0
	"The next time we were connected was four days later, during my commute to school."
	"It had already gotten so warm that you could work up a light sweat even in the morning; the sun was, of course, out in full force as well."
	"And sure enough, just when I thought I heard that strange noise, that viewscreen from before popped up before my eyes."
	"Getting all nervous for some reason, I got off my bike and stared hard at the image before me."
	"(What the?)"
	"But there wasn't even a trace of Minamo-chan or Itsuki-san anywhere."
	"Just a dark, seemingly empty room; nothing more."
	ka "Minamo-chan?"
	"......"
	ka "Itsuki-san?"
	"......"
	"I tried calling out their names."
	"*rustle*rustle*..."
	"I could see something moving in the darkness."
	mi "Hey, what the...?"
	play music "snd/city.ogg"
	mi "...I can hear Kasumii's voice...!"
	"This was unmistakably Minamo-chan's voice."
	"*FWIP*"
	show phone blank1
	"And then a noise like a curtain being thrown back."
	"At the same time, the viewscreen became flooded with light."
	"Okay, so apparently this was Minamo-chan's room that I was looking at."
	mi "Heeeey! Kasumii!!"
	"I still couldn't see Minamo-chan anywhere."
	"But it certainly seemed as if she could see me."
	mi "Eeek!! Look at the time!!"
	ka "......"
	"What, did I catch her sleeping in or something?"
	"After several moments filled only with the sounds of Minamo-chan scurrying to do whatever she did first thing in the morning, the screen suddenly shook -- as if someone had picked it up."
	show phone minamo2
	mi "Good morning, Kasumii!"
	ka "Good morning, Minamo-chan."
	"I admit that I felt kinda relieved when I finally saw Minamo-chan's face appear onscreen."
	mi "Mom, Dad, I'm heading off to school!!"
	mi "Oh, man, I'm gonna be late!"
	mi "What about you, Kasumii?!"
	ka "Well, I'm already almost to school, so I'll be fine."
	"Ever since that one disastrous incident, I had stopped my custom of buying Capri Sun on the way to school."
	"And maybe it was because of that, but I hadn't even been close to tardy anytime since."
	mi "Are you *really* going to be fine, though? It's already 8:00, you know?"
	ka "What?!"
	"...wait, if that were true, then even if I were *crawling* I should have reached school about five minutes ago..."
	"And in any case, I was so close that if it WAS 8:00 right now, I should have been hearing the chime of the bell tower by now."
	ka "But hey, it's been a while, hasn't it..."
	hide phone
	play music "snd/blank.ogg"
	"*BLIP*"
	ka "Oh..."
	"So we got disconnected again."
	ka "......oh, wow..."
	"That was just way too short this time around."
	"It ended without my even having caught a single glimpse of Itsuki-san..."
	"I wouldn't have cared about being late if I could just have seen her."
	"I'd been waiting all this time..."
#	play sound "snd/chaim.ogg"
	"*ding*dong*ding*dong*"
	"Minamo-chan probably set her watch a few minutes fast or something."
	"But then my musing was cut short by the sound of the chime, and I had to race off to school."
	scene black
	$renpy.pause(0.8)
	scene bg sky
#	play sound "snd/noise.ogg"
	"*SHIIIING*"
	"But the line abruptly went live again later that day, right after I'd finished eating my lunch up on the roof."
#	play sound "snd/noise.ogg"
	show phone minamo1
	play music "snd/natukaze.ogg"
	mi "Huh?"
	mi "Hey, awesome! It's Kasumii again!!"
	ka "Hey, good afternoon, Minamo-chan!"
	show phone minamo4
	mi "Kasumii~"
	"Minamo-chan waved her hands at me excitedly."
	ka "Hey, it's wonderful that we didn't have to wait nearly so long to see each other again this time, huh?"
	show phone minamo2
	ka "Ehehe, yeah~!"
	"Minamo-chan smiled widely at me even as she kept chomping on something or other."
	"While I hadn't been entirely happy about having to eat up here alone every day because Yuuna now went off to eat lunch alone with her boyfriend, right now it was the most incredible blessing."
	"Because obviously, it would be pretty difficult to explain this to anyone who might be watching."
	ka "Where are you right now, Minamo-chan?"
	show phone minamo1
	mi "Well, I'm in my school's courtyard right now, eating bread with Ii-nee."
	"*THA-THUMP!*"
	ka "...o-oh, is Itsuki-san there as well?"
	"Minamo-chan was about to answer when..."
	show phone ituki5
	it "Good afternoon, Kasumi-chan!"
	"Itsuki-san made her appearance onscreen, waving at me with a gentle smile."
	ka "Y-yes, it's a wonderful afternoon, and I hope you're having a good day too, Itsuki-san!!"
	"But -- whether it was because I was caught off-guard or because I was really scared -- my reply came as a blurted squeak. I regretted it immediately."
	show phone ituki1
	it "Ahaha, what's the matter?"
	it "Are you that surprised to see me?"
	ka "Th-that's not it at all. Uh...um...well, it's just that I was kind of disappointed to not have been able to talk to you this morning...and, um..."
	"And I thought to myself: oh no. Now I've gone and said it."
	"I broke out into a cold sweat when I realized that I'd just declared to Itsuki-san how much I'd been pining after her."
	it "Thank you. When Minamo told me about what had happened this morning, I was disappointed too."
	show phone ituki5
	it "But see? We're talking to each other at last."
	"*THA-THUMP!*"
	"Any more of this and my heart was going to explode."
	"I couldn't take this after all."
	"Just one look at her smiling face was enough to render my brain into scrambled eggs."
	"So the fact that she was smiling at me so sweetly right now meant that my life was in mortal danger."
	show phone ituki1
	it "So I understand that you woke Minamo up today?"
	mi "That's right! She's the legendary 'Kasumin the Alarm Clock', ya know!"
	show phone ituki2
	it "That's quite enough out of you, Minamo."
	it "Did you at least thank her properly?"
	show phone minamo5
	mi "Oh, that's right, I haven't yet..."
	show phone minamo4
	mi "Ehehe, thank you, Kasumii!"
	ka "Oh, no, it wasn't anything that I did, anyway..."
	"I replied absentmindedly."
	hide phone
	scene bg sky
	"After that, I kept a tight rein on my pounding heart and proceeded to make small talk..."
	"...and by the time we got down to saying stuff like 'thank God it's Friday' and 'I'm looking forward to this weekend', Minamo-chan suddenly exclaimed:"
	show phone minamo2
	mi "Wait, I just had a good idea!"
	"Her eyes were glittering with excitement."
	play music "snd/blank.ogg"
	show phone minamo1
	"Let's meet up the next time around!"
	ka "......"
	"Whoa. That WAS a good idea."
	play music "snd/natukaze.ogg"
	show phone ituki1
	it "Yes, I completely agree."
	it "After all, it is completely within our reach."
	it "Certainly, we're kind of far away, but it's not as if we're on opposite sides of the country, and besides, I'd love to meet you in person, Kasumi-chan."
	ka "Y-yes, m-me too! I'd love it as well, Itsuki-san!"
	"I wanted absolutely sure confirmation that we'd meet in person, especially given the fact that we could have gotten disconnected any second now."
	show phone minamo4
	mi "Yeah, yeah, let's do it!"
	show phone ituki4
	it "Then shall we make a date?"
	it "You did say that it takes 3 hours by train between where we are and where you are, right, Kasumi-chan?"
	ka "That's right."
	it "Now, would there happen to be some place in the middle that we could meet up at?"
	ka "Um, let's see..."
	ka "I don't know much about train stations..."
	ka "Well, I have relatives in Tachikawa, so I know that area okay, but..."
	show phone minamo6
	mi "Where's that?"
	show phone ituki1
	it "Hmm. I have only been Tachikawa once myself, but I should be able to find my way around."
	it "But is that okay with you? Hopefully that is not too far away from your place, Kasumi-chan?"
	ka "It's perfectly okay with me!"
	ka "Well, it's better than heading all the way to Tokyo, but it is a tiny bit far, yes."
	"But I'd have been happy to WALK there through snow if it meant being able to see Itsuki-san in person."
	it "You don't have to transfer trains or anything to get there, right?"
	ka "Yes, that's right."
	it "Very well, sounds good. When shall we do this?"
	it "Wait, do you happen to have tests soon as well, Kasumi-chan?"
	ka "Oh!"
	ka "Yes...next week."
	"Eek, I really didn't want to think about that."
	"But sure enough -- it was true."
	"There was no way we could justify meeting and having fun when the exams were this close."
	it "...ours are next week too."
	show phone minamo7
	mi "Augh! Tests! Augh!"
	ka "Ahaha!"
	ka "You must really hate tests, Minamo-chan."
	show phone ituki1
	it "Ahaha, that's Minamo for you..."
	ka "Um, Itsuki-san, I hate tests too."
	it "Yes, as do I."
	it "...but still, one can't help but feel a little sorry for poor Test-chan. Everyone seems to hate her..."
	ka "Ahaha..."
	"I was stunned. This was the first time I'd ever heard of someone addressing TESTS so affectionately and compassionately."
	"But it also made me think: that's so like Itsuki-san."
	"It was so very warm, and in and of itself filled me with a kind of wonder."
	it "Hmm. Well then, I guess...next week?"
	ka "I'd love it!"
	show phone minamo3
	mi "Yaaaay! We finally get to meet!"
	show phone ituki5
	it "Ahaha. You'd better study hard for your tests, then."
	show phone minamo4
	mi "Of course!"
	show phone minamo2
	mi "Awesome, aweso--"
	hide phone
	play music "snd/blank.ogg"
	"*BLIP*"
	ka "Uh..."
	"......"
	"(Darn it...)"
	"We got cut off, as abruptly as ever."
	"But..."
	play music "snd/natukaze.ogg"
	ka "......"
	"I could only look up at the sky, the smile on my face more radiant than even the sun itself."
	"Now my life wouldn't depend on this cell and its intermittent connections."
	"That was right. I would finally get to meet Itsuki-san once tests were over."
	"That made me happier than anything."
	"In fact, I doubted that I'd feel this happy even if I'd won a trillion yen in the lottery or something."
	scene bg sky3
	"I found it hard to go to sleep that evening."
	"I still could scarcely believe..."
	"...that a girl as dead ordinary as I was could have something so out-of-this-world happen to her..."
	"...and be able to participate in a meeting that was equally out-of-this-world..."
	"...and fall in love just like this. I mean, what were the chances?"
	"It made me think that this world sure was wondrous."
	"And that human life was equally wondrous."
	"And that I'd take as many of these wondrous miracles as I could get."
	"It was as if I'd become the main character of a beautiful story."
	"Yes, the main character of, say, a science fiction love story epic."
	"Obviously, I was in no state to be able to concentrate hard enough to study for exams."
label 6:
	scene chap 6
	$renpy.pause(2)
	scene bg sky
	"A week later, my heaven had turned into purgatory."
	"Why did my connections with those girls have to be so infrequent and so out-of-the-blue?"
#	play sound "snd/noise.ogg"
	"I mean, the next time it happened it was a few minutes before one of my final exams."
	"It wouldn't be good at all if other people saw this, and in any case I was already in the classroom and the exam was about to start, I unhappily pressed the Call End button."
	"Funny how that was the only button on my phone that actually worked."
	"But after I'd disconnected like that, we didn't get reconnected for a long time afterwards."
	"It made me think...that fate was cruel and that reality sucked."
	scene bg sky3
	"And on top of that, my cell chose to connect at the most random times."
	show phone minamo1
	mi "Yo! Hey there, Kasumii~!"
	ka "Eek! Give me a moment here--!"
	hide phone
	"It even happened one time when I was in the bathroom."
	"Well, yeah, I probably shouldn't have carried it with me into the bathroom in the first place, but I couldn't part with it for even a second; after all, I never knew when we'd be connected again."
	scene black
	$renpy.pause(2)
	scene bg way
	"But there was one thing that kinda concerned me."
	"There were some times when our conversations took a turn for the strange."
	"And when I say 'strange', I mean 'so strange and so out-of-place that we came to a screeching halt'."
	show phone minamo1
	ka "Minamo-chan, it's been hot these days, hasn't it?"
	mi "Hmm, well, it's about normal, I guess."
	ka "Don't you think it might be nice if it got cooler soon?"
	ka "After all, I'd like to go skiing and stuff...how about you, Minamo-chan?"
	mi "Skiing?"
	ka "Yeah, but then again, I'm sure that once it becomes winter, I'll start complaining that it's gotten TOO cold, you know?"
	mi "...win...ter?"
	ka "Yeah. Hey, Minamo-chan, do you like summer better?"
	"That's the impression that I got just from looking at her, at the very least."
	mi "Summer...?"
	hide phone
	play music "snd/blank.ogg"
	"*BLIP*"
	ka "......"
	"......"
	"...we got cut off."
	"......"
	"This was what I meant by 'strange'."
	"Why was it?"
	"There were times when Itsuki-san reacted in this incongruous manner as well."
	"...why could it be? Was I missing something?"
	"But I always just shoved the question into the back of my mind. After all, I never knew when we were going to be disconnected, so I wasn't going to waste our precious time."
	scene black
	$renpy.pause(2)
	scene bg sky
#	play sound "snd/noise.ogg"
	"*SHIIIIING*"
	play music "snd/natukaze.ogg"
	"We seemed to be able to connect with each other most easily in the late afternoon."
	"And so it was that I often walked home from school chatting gaily with the two of them the entire time."
	scene bg way2
	show phone minamo5
#	play sound "snd/higurasi.ogg"
	mi "Hey, Kasumii, are you smart?"
	"Finals week was now about half over."
	"And as usual, Minamo was continuing to rant on about how much she hated tests. Of course, by now it would have worried me if she WEREN'T complaining, so..."
	ka "Oh, not at all. I'm about average."
	show phone minamo8
	mi "Oh? I'm envious!"
	show phone ituki5
	it "Ahaha! You see, Minamo has always been at the bottom of her class."
	"There was no doubt in my mind that Itsuki-san, on the other hand, was incredibly smart."
	"According to what Minamo-chan was saying now, Itsuki-san was one of those people who didn't study much at all, yet always got the highest scores."
	show phone ituki1
	it "Oh, but I actually listen and take notes during lecture, you know."
	it "You might try doing the same, Minamo."
	mi "I *do* listen...well, at least at first..."
	show phone ituki6
	it "You can't just leave it at that!"
	"It intrigued me to no end that Itsuki-san, who was so very kind and gentle, could actually get mad and reprimand Minamo-chan like this."
	ka "Ahaha! You two really ARE like sisters, aren't you?"
	show phone ituki7
	it "Well, Minamo needs all the help she can get..."
	show phone minamo4
	mi "Sisters, huh?"
	mi "Ehehe! Then maybe that means that I'll have boobs as big as Ii-nee's someday?"
	show phone ituki6
	it "S-stop that, Minamo!"
	mi "Oh, c'mon~"
	"The two really seemed so comfortable with each other."
	"They really WERE close. It had to be."
	"For my part, I was envious of Minamo-chan."
	"That she could always have such a wonderful "big sister" at her side."
	hide phone
	scene bg sky2
	"But when we spoke of our studies, I was even more shocked."
	"See, it's impossible to get by on tests just by going to class and listening -- generally, you have to study like crazy outside of class too."
	"And on top of that, Itsuki-san was a senior, so she should have been going craziest of all with test preparations given how heavy her courseload was."
	"But instead of looking flustered, she always seemed so calm and collected, going about her days as if they were nothing at all."
	"It made me think that she wasn't the type to push herself to her limits at all."
	"I'd never say this with Minamo-chan around, but the very fact that Itsuki-san was attending the same high school..."
	"...had to be just another manifestation of the fact that Itsuki-san really didn't choose to push herself at all."
	scene bg way2
	show phone ituki1
	ka "Oh, Itsuki-san, I'd love it if I could take everything in life so calmly, the way that you do."
	show phone ituki5
	it "Huh? Oh, but that's not the case at all. The upcoming tests make every day a struggle for me, too."
	"She said gently, not sounding as if she were struggling at all."
	"Okay, fine, maybe in reality she MIGHT have been struggling with some things. Maybe not. I don't know."
	"But still, I was so envious that she had the kind of personality that allowed her not to show even a tiny bit of that struggle to anyone else."
	"That's what made her such a wonderful woman -- who only got more wonderful the more you got to know her."
	show phone ituki1
	it "Oh, and--"
	hide phone
	play music "snd/blank.ogg"
	"*BLIP*"
	"(Oh no!)"
	"......"
	ka "*sigh*"
	"Even when I was expecting it, these moments were always such shocks."
#	play sound "snd/higurasi.ogg"
	""
	$renpy.pause(2)
	"Yes, the moments when we were disconnected from each other without a single warning."
	"My connection with the girls was over, and their images had vanished from before me, and the scenery that surrounded me came crashing down upon me with all the weight of reality."
	"Almost as if I were waking from a dream."
	"Almost as if reality itself were telling me 'wake up; these fun times cannot last for all eternity'. I *hated* these moments."
label 7:
	scene chap 7
	$renpy.pause(2)
	scene bg way
	play music "snd/city.ogg"
	"...and then."
	ka "Mmmmmm!!!!!"
	"I stretched out fully as I walked past the school gates."
	"My finals were over at last."
	"And yet I was all on pins and needles."
	"And the reason was obvious."
	"Well, no, it wasn't Itsuki-san's fault at all. If there was anyone to blame, it was me and my total one-sided obsession with Itsuki-san."
	"After all, there was no point in thinking about the tests anymore."
	"That's right."
	"They were over and there was nothing I could do about them now."
	"And since they were over, the next thing to worry about was this Sunday."
	"That's when I'd be meeting them."
	"I wanted to let out a yell that would burst my throat; I wanted to pedal so hard that my bike would fly in the air."
	ka "YES!!!"
	"I felt as free and as high-flying as the sky overhead."
	"Because even as the sun scorched me, even as the shadows cast long stains on the evening soil, that day that I was waiting for was approaching, hour by hour."
	scene black
	$renpy.pause(1)
	scene bg sky3
#	play sound "snd/musi.ogg"
	"That night, I had finished dinner and gone to my room when the connection happened again."
	show phone blank0
	"And my broken cellphone cast that unreliable, static-filled image of another world in the air before my eyes."
	"I found myself looking at Minamo-chan's darkened, empty room."
	"After five minutes, the door opened, and I heard a very familiar voice."
	mi "Hey!! It's Kasumii!!"
	"But Minamo-chan was nowhere to be seen."
	"Instead, I heard the sound of a curtain being drawn, then a window being opened, and then Minamo-chan shouting something to the outside."
	mi "Ii-nee!!!!!"
	mi "I've got Kasumii on the line now!!"
	"A little while later, I heard the window being closed again. And then:"
	show phone minamo4
	mi "Hey, Kasumii! Isn't it awesome that tests are over?!"
	"Minamo-chan made her entrance onstage, looking incredibly happy."
	mi "I've called over Ii-nee as well, so she should be here any moment now."
	ka "O-okay."
	"I felt jittery all at once when I heard that."
	ka "Oh, so you and Itsuki-san really ARE next-door neighbors after all."
	show phone minamo1
	mi "That's right! In fact, her room and mine face each other. We're not even a stone's throw away!"
	mi "Well, rather, we're not even an ERASER'S throw away. Sometimes, when I don't have one, I ask her to throw me one, and she does."
	"Whoa..."
	show phone minamo4
	mi "Isn't that neat?"
	ka "Yeah, that's pretty nice..."
	"It seemed to me that she was carrying on a life that I could only DREAM of."
	"If Minamo-chan weren't as pure and innocent as she was, why, I'd probably be incredibly jealous of her."
	hide phone
	play music "snd/blank.ogg"
	scene black
	$renpy.pause(1)
	ka "......"
	"...and then."
	scene bg sky3
	show phone ituki1
	it "Ahaha, so she's fallen asleep."
	ka "S-so she has..."
	play music "snd/natukaze.ogg"
	"It was well and good that Itsuki-san had come over, but..."
	"So Minamo-chan, who had apparently been off having fun like crazy right after exams had ended (in celebration, no doubt...), had by now crawled into bed and was dozing away."
	"...all right, now what?"
	"I was getting incredibly nervous."
	"I felt like I couldn't breathe."
	"See, it was just Itsuki-san and me now..."
	ka "I-it's...the first time that it's just been the two of us ever since we first met, huh...?"
	"Oh, great, what was I saying?!"
	"For crying out loud, now I was so nervous that I was just blurting out whatever was coming to mind..."
	show phone ituki5
	it "Yes, so it is. It brings back some memories..."
	show phone ituki1
	it "I remember being so very surprised..."
	ka "Y-yeah, I was shocked too..."
	ka "Because I'd never seen someone as pretty as you..."
	"I had no idea where the thread of this conversation was taking me anymore."
	show phone ituki5
	it "Ehehe, thank you!"
	it "You certainly know how to flatter people, Kasumi-chan."
	ka "N-no, that's not true! I really think that you're the prettiest woman I've ever met!"
	it "Oh, please, stop it, or else I'm going to start blushing."
	"That moment, when I saw her get a little bashful, was so dear to me."
	ka "Oh...uh...um, I'm sorry..."
	show phone ituki7
	it "Ehehe, it's quite all right. But I think that you're really cute yourself, Kasumi-chan."
	"*THA-THUMP!*"
	"Oh, no, my heart was going to give out for real! I was going to die!"
	ka "Th-th-th-th-th-th-th-th-that's not true at all...!"
	"I had so little control over my articulation that even *I* found it pitiful."
	show phone ituki1
	it "I'm sure you're getting lots of attention from the boys?"
	ka "Wha?! N-no...that could never happen..."
	"If this were a manga, my eyes would probably have gone all swirly by now."
	ka "H-h-h-how about you, Itsuki-san? Y-y-y-you have a boyfriend...right?"
	"Oh, goodness. In my own confusion, I'd asked about the very thing that I most wanted to know."
	"But if she told me that she had one, I was going to be completely depressed."
	"I'd really bet everything I had on her saying that she didn't have one when I asked."
	"But now that I thought about it, she had to have one..."
	"Please, let her say no!"
	it "Hmmm..."
	it "Well, unfortunately, I don't have one at the moment."
	"'At the moment'."
	ka "I-is that so? A-and...h-here I was thinking that you'd...d-definitely have one..."
	"'At the moment'."
	"'At the moment'..."
	"In other words...she had one before."
	"...well..."
	"...obviously."
	"A weird feeling that was half depression, half relief -- and that I had no idea what to do with -- slammed into me..."
	"...and I had even LESS of an idea what to do with myself."
	it "Say, Kasumi-chan, is there a guy that you like?"
	ka "Huh?"
	"Oh no, now this conversation was taking a strange turn."
	"Obviously, there's no guy that I like."
	"Because I like you."
	show phone ituki5
	it "Ahaha!"
	it "Come, Minamo is asleep, and it's the evening, and it's just the two of us, so why don't we have some just-us-girls talk?"
	"Whoa, when I thought about it, Itsuki-san had just said something incredibly mean..."
	"So apparently even SHE thought of Minamo-chan as little more than an elementary schooler."
	ka "...um, but Minamo-chan is a girl too?"
	it "Well, you see...she still doesn't know anything about love."
	it "She may look like a high schooler, but she's pretty much an elementary schooler at heart still."
	ka "A-ahaha..."
	"Bullseye."
	show phone ituki1
	it "But there has to be someone YOU like, yes, Kasumi-chan?"
	show phone ituki5
	it "What kind of person could it be?"
	it "I'd very much like to know..."
	"Oh, oh no..."
	"What was I supposed to do now? It looked like Itsuki-san enjoyed this kind of conversation."
	ka "Um, well, there's nobody right now..."
	show phone ituki4
	it "What? No kidding?"
	ka "That's right..."
	it "...hmm...that's odd..."
	ka "?"
	ka "Um, Itsuki-san? Is something wrong?"
	show phone ituki1
	it "...well, see, these days you've been looking a lot like a young lady in love..."
	"*THA-THUMP!*"
	"No, wait, this was bad!!"
	ka "Um, um, no, that's not true at all!"
	"Itsuki-san, you're sharp."
	"But you only got half of it."
	"...you didn't figure out that the person I'm in love with is YOU, did you...?"
	"I was relieved and I was disappointed and I was relieved and..."
	"NOW what was I going to do?"
	"I was getting more and more panicked."
	ka "Um, I just thought about this, but could it be that, uh, you get lots of attention from the girls as well?"
	"I might have asked this question way too abruptly, as I was still really failing to grasp the thread of this conversation. But I had to ask."
	show phone ituki4
	it "Huh?"
	ka "......"
	show phone ituki5
	it "Ahaha, Kasumi-chan, you're amazing."
	"But Itsuki-san just replied to me with a smile."
	it "My shot missed, but it looks like your shot hit its mark."
	"...I'd expected as much."
	"She had to be in pretty high demand even with the lesbians..."
	show phone ituki2
	it "I wonder why that is? Every so often, I get confessed to by some of the more junior girls. It's so odd."
	play music "snd/blank.ogg"
	ka "........."
	"My abrupt question had boomeranged, and was now like the edge of a sword being held against my neck."
	show phone ituki3
	it "Say, Kasumi-chan. Do I really look like a lesbian to you?"
	ka "Huh?"
	play music "snd/yoiduki.ogg"
	".........how the heck was I supposed to answer this?"
	ka "I...don't...think so..."
	show phone ituki2
	it "That's right..."
	it "Then why is it that so many girls assume that I am one?"
	ka "Um, well...uh, what do you always say to the girls who come to confess to you, then?"
	show phone ituki1
	it "Huh?"
	show phone ituki7
	it "That's a tricky one. I mean, I have to tell them that I'm sorry but I'm not interested."
	show phone ituki3
	it "But it's painful, because no matter what, I'm hurting the other person's feelings..."
	show phone ituki5
	it "Ahaha, in any case, this is one of my many worries."
	it "I guess it's kind of strange, huh?"
	ka "......"
	hide phone
	scene black
	"We got disconnected shortly after that."
	"I went out into the evening streets to cool myself off."
	scene bg way3
	"I understood."
	"I understood."
	"I understood..."
	"That's why it was fine; after all, this was normal."
	"It was blindingly obvious."
	"Yeah..."
	"So I..."
	"There was no helping it."
	"I'd fallen in love with Itsuki-san."
	"Fallen in love..."
	ka "......"
	"And, for the first time, I understood."
	"All those words, all those songs, all those stories written about the wonder and the pain and the pleasure of love -- I'd never really grasped any of that."
	"But now I understood everything."
	"I understood why people said that love was wonderful, and why love was painful."
	"I understood why...falling in love was such an agony."
	"The joy and the sadness as well were so amplified."
	"...the sadness as well."
	scene black
	"That evening, I wandered about aimlessly, lost within my anguish and my thoughts."
	$renpy.pause(2)
	play music "snd/blank.ogg"
	scene bg way2
#	play sound "snd/higurasi.ogg"
	"......"
	"...but."
	"Apparently, a girl in love is a strong girl indeed."
#	play sound "snd/noise.ogg"
	"*SHIIIING*"
	"Even given what had happened..."
	show phone ituki1
	play music "snd/natukaze.ogg"
	it "All right then, this Sunday we'll meet at noon at Tachikawa Station, right in front of the ticket stands."
	ka "Okay!"
	"I was going to go through with this meeting with Itsuki-san."
	"Because just with that, my depression had lifted, and my spirits were soaring once again even before I knew it."
	"...and if I thought about it, the reason why was obvious."
	show phone minamo1
	mi "You'd better come!"
	ka "Of course I'll be there."
	mi "And you'd better not be late!"
	show phone ituki2
	it "YOU'RE the one who's most likely to be late, Minamo."
	mi "Ehehe~"
	show phone ituki1
	it "Don't worry, Kasumi-chan. I'll drag Minamo out in her pajamas if need be."
	ka "Okay."
	hide phone
	scene bg sky2
	$renpy.pause(2)
	"After all, the pain wasn't the only thing that was amplified."
	play music "snd/blank.ogg"
label 8:
	scene chap 8
	$renpy.pause(2)
	gosub *BGM_city
	show bg sky
	"Tachikawa Station, 10:00."
	"There was one girl there who was darting about merrily and with great anticipation."
	"Of course, that was me."
	"I'd undone my braids, and I was wearing the best clothes I had; I didn't want to look the part of the country bumpkin if I could help it."
	"I'd come way ahead of time, but then again, if I thought about it, this gave me time to calm my nerves."
	"It was nice and sunny out today."
	"It was your stereotypical gorgeous summer day, and there was no shade anywhere to be found. But did I care about any of that? No, of course not."
	"(I hope they'll come soon...)"
	"Itsuki-san."
	"Minamo-chan."
	"How would they make their appearance onstage?"
	"Now that I thought about it, I had no idea how tall they were or anything."
	"And today would be the first time that I'd be hearing their voices for real."
	"(~~~!)"
	"I was looking forward to this so much that it almost hurt. I couldn't help it!"
	"So I walked back and forth around the vicinity,"
	"But then I stopped because I didn't want to sweat,"
	"And in any case I kept waiting impatiently for the promised time to come."
	scene black
	$renpy.pause(2)
	scene bg station
	ka "Oh!"
	"At 10:50, I saw the boy who had rammed me with his bicycle that one day making his exit from the station."
	"It was an incredible coincidence to be bumping into him here."
	"And so before I knew it, I'd called out to him."
	ka "Hey, you!"
	"???" "...yes?"
	"It looked like he'd forgotten me."
	"I took the time to explain to him that I was the girl he'd crashed into with his bicycle that one day, and he apologized and made to run for it."
	"But I grabbed him by the arm."
	ka "No, really, it's fine. Actually, because of what you did, something really lucky happened to me."
	"???" "...what?"
	ka "So you can be at ease."
	ka "No, for that matter, I should be grateful to you."
	"I took that bewildered middle schooler's hand and then shook it up and down with exaggerated vigor."
	ka "Thank you very much!!"
	"???" "???"
	ka "Oh, sorry to have kept you. You can go now. I'll be meeting with my friends soon."
	"???" "O-okay..."
	"The boy then started walking away from me, an expression of 'what the heck was that?!' on his face."
	"And I waved at him happily whenever he looked over his shoulder (probably to make sure that I wasn't following him or anything)."
	"After all, it was all because of him that I got to meet Itsuki-san."
	scene black
	$renpy.pause(2)
	scene bg station
	"11:50!"
	ka "......"
	"Soon, soon!"
	scene black
	$renpy.pause(2)
	scene bg station
	"11:55!"
	ka "......"
	scene black
	$renpy.pause(2)
	scene bg station
	"11:58!"
	"(*tha-thump*tha-thump*)"
	scene black
	$renpy.pause(2)
	scene bg station
	"12:00!!"
	"(*THA-THUMP*THA-THUMP*)"
	scene black
	$renpy.pause(2)
	scene bg station
	"12:05!"
	ka "......"
	"(*tha-thump*tha-thump*)"
	scene black
	$renpy.pause(2)
	scene bg station
	"12:10!"
	ka "........."
	"(I wonder where they are...)"
	scene black
	$renpy.pause(2)
	scene bg station
	"12:20."
	ka "............"
	scene black
	$renpy.pause(2)
	scene bg station
	"12:30."
	ka "..............."
	scene black
	$renpy.pause(2)
	scene bg station
	"1:00..."
	ka "..................*sigh*"
	"It was at times like these when having a functional cellphone would have been very nice."
	"I started searching around the vicinity, but I couldn't see anyone even remotely resembling them anywhere."
	scene black
	$renpy.pause(2)
	scene bg station
	"1:24..."
#	play sound "snd/noise.ogg"
	"*SHIIIIING*"
	$renpy.pause(0.2)
	ka "!!"
	"(Oh, thank God!)"
	show phone minamo1
	mi "Oh, thank goodness~! Hey, Ii-nee! I got Kasumii on the line!"
	mi "Oh, hey, Kasumii, you've got your braids undone!"
	ka "Ahaha, so I do."
	ka "But, uh, what happened today, Minamo-chan?"
	show phone minamo6
	mi "That's OUR line!! We waited and waited and waited!"
	ka "Huh?"
	"I continued speaking even as I turned toward a wall to hide the holographic image from any passersby."
	ka "What are you talking about? I'm at Tachikawa Station right now, and I've been here for hours."
	mi "Huh? Where?!"
	show phone ituki1
	it "Hi there, Kasumi-chan."
	"*THA-THUMP!*"
	"Just when I thought my tension had been broken, Itsuki-san came up onscreen."
	"(Oh, Itsuki-san, you know this is bad for my heart...)"
	it "Oh, so it's true! Kasumi-chan, you really did undo your braids!"
	ka "Oh...uh...um...yes, I did."
	it "Ahaha! It's got a beautiful wave to it! You look very much the part of the elegant princess!"
	"Oh, no..."
	"She had such a way with words..."
	"Such a way, in fact, that it was almost making me forget something even more important."
	it "I'm so sorry, though. You went through all this trouble to dress up nicely."
	it "But see, Minamo here declared that she was too tired to pick out which clothes she wanted to wear, so we came in our ordinary clothes."
	show phone minamo5
	mi "But I also figured that it would make it easier for you to pick us out of a crowd, Kasumii..."
	ka "Oh, please don't worry about it. After all, both of you look very good in them."
	show phone minamo4
	mi "Really?! I look cute?!"
	ka "Yes, you look cute."
	show phone minamo3
	mi "Yaaaaaaay!"
	show phone ituki5
	it "Ahaha, how nice for you, Minamo."
	show phone ituki4
	it "Oh, more importantly..."
	it "Tell me, Kasumi-chan: where are you right now?"
	"See what I mean? I had completely forgotten about this thanks to Itsuki-san's initial onslaught of gentle words."
	ka "I'm directly in front of the ticket stands."
	it "......"
	"Itsuki-san looked around herself."
	show phone ituki1
	it "Directly in front of the ticket stands where?"
	ka "If you turn toward the exit, I should be on the right side."
	it "...so you should be pretty close to the guide map of the area, then."
	ka "The one on the right, yes."
	it "All right, the guide map..."
	show phone ituki4
	it "What the...?"
	"Itsuki-san looked around herself again."
	it "I'm next to the map that you describe, but I don't see you anywhere."
	ka "Wha?! Maybe we're in different ticketing areas...?"
	"...wait a second. This station had only one ticketing area."
	show phone ituki1
	it "Say, Kasumi-chan, could you show me some of the scenery behind you?"
	ka "Of course."
	"I turned my body in order to conceal the holographic image from passersby as best I could and to give Itsuki-san a good view of my surroundings."
	show phone ituki6
	"Like this, she should have been able to see the automatic ticket machines and the analog clock that hung from the ceiling above them."
	"Itsuki-san stared intently in my direction."
	it "We're in the same place, all right..."
	it "......"
	show phone ituki1
	it "Kasumi-chan, here, why don't you take a look at this?"
	ka "Of course!"
	show phone blank1
	"Itsuki-san blinked out, and now I could see the scenery behind her."
	show phone minamo4
	"Or at least, I should have been able to. Instead, I got a faceful of Minamo grinning broadly at me."
#	play sound "snd/puni.ogg"
	show phone blank1
	ka "Come now, don't interfere!"
	mi "Ahaha..."
	"After I'd collected myself again, I took another look."
	"I could see a stand of automated ticketing machines, and an analog clock hanging from the ceiling above them..."
	ka "?"
	"This was weird."
	show phone ituki4
	it "Kasumi-chan, this is Tachikawa Station, yes?"
	kka "Yes, it is."
	"My surroundings and theirs were absolutely identical...there was not a single difference, no matter where I looked."
	play music "snd/blank.ogg"
	show phone ituki3
	it "Kasumi-chan..."
	"Itsuki-san's voice shook anxiously."
	it "Isn't there something strange about this?"
	ka "...yes, there is."
	"That was a mild way of putting it."
	play music "snd/yoduki.ogg"
	"Itsuki-san, Minamo-chan, and I were all standing in the same place in the same station in the same country."
	"But we hadn't met."
	"There was no way we couldn't have met."
	ka "This is kind of frightening..."
	it "Yes, Kasumi-chan, so it is..."
	"(Wait a second...)"
	"I'd just noticed something."
	ka "Um, what time is it right now on that clock over there?"
	"I couldn't see all that clearly through the staticky haze, but I did think I saw something very strange indeed."
	mi "It's 1:38!"
	"Minamo-chan replied cheerfully."
	ka "......"
	show phone ituki4
	it "What's wrong, Kasumi-chan?"
	ka "So it's 1:38 over there..."
	ka "...but, um, over here, that very same clock reads 1:31."
	it "What?"
	"And then we checked back and forth, several times."
	"And the result was invariably the same."
	"No mistake about it, we were all in the same place."
	"But we were not there *together*."
	"And we were not there at the same *time*, either. Well, that is, the same clock in the same place was reading different times on my side and on theirs."
	ka "How could this be...?"
	"Even though the rainy season had ended a long time ago..."
	"...even though the air was this hot and toasty..."
	"...cold shivers were running down my spine."
	show phone minamo2
	mi "I got it!! We're on barrel worlds!!"
	"Minamo-chan sounded as cheerful as ever despite all of this."
	show phone ituki2
	it "Um, you mean 'parallel worlds', do you not?"
	show phone minamo3
	mi "That's right, that's right! I learned about it from reading manga!"
	show phone ituki2
	it "Look, I told you, that was manga. In reality, that kind of thing..."
	ka "......th-that's right, isn't it? There has to be some mistake..."
	"Wait. 'Reality'?"
	"...but in 'reality', both my cellphone and Minamo-chan's were connecting with each other through a phenomenon that could not exist."
	"...'real'."
	"...what was 'real'?"
	"Were the things that happened in manga 100% *not* real? "
	show phone ituki1
	it "...say, Kasumi-chan. Mind if we confirm a few things here?"
	ka "Of course. Um, what would you like to know?"
	it "Well, let's start with the time, as that seems to be the most obvious thing that presents itself. Perhaps we are living in completely different times, and that is why we are unable to meet each other."
	"...while that, too, was something totally out of a manga, I didn't have any better explanation for this phenomenon."
	ka "Certainly. Well, over here, it's 1:34PM on Sunday, July 14, 2002 AD."
	it "Thank you. And here, it is also the year 2002 AD, Sunday, July 14."
	show phone ituki3
	it "...so it seems that only the time of day is different, and only a little bit at that. Right now, the station clock here reads 1:41PM."
	hide phone
	scene black
	"The names of famous singers."
	"The names of famous artists and movies."
	"The name of the latest Prime Minister, even."
	"Every single thing we could think to ask about, every single thing we could think to compare -- all the same."
	scene bg station
	show phone ituki2
	it "So our eras and our worlds, even, are identical...the only difference being a seven minute time differential..."
	"And then I remembered that one morning when Minamo-chan and I were both walking to school."
	"At that time, I'd thought that she'd just set her watch ahead, but apparently that was not the case at all."
	"In fact, it was looking like it was just the time differential that existed between my world and theirs..."
	it "...Hmmm...why, just why? Why is it that we can't meet you, Kasumi-chan?"
	"Me too. I didn't want to just give up and go home."
	"Itsuki-san sounded really anxious to meet me, and for that matter not so long ago I'd been sure that we *would* meet..."
	hide phone
	scene black
	"After that, we asked questions back and forth so many times, confirming over and over what we already knew."
	"...and I started to grow terrified."
	"It was as if I was watching a nightmare unfold, and I couldn't do anything about it."
	"I could feel myself clutching weakly at my cellphone, and my legs started trembling all the sudden."
	scene bg station
	show phone minamo1
	mi "I'm tellin' ya, we've gotta be on barrel worlds!"
	ka "Uh, Minamo-chan, that's 'parallel worlds'."
	"Sure enough, I couldn't think of any other way to explain this."
	"There just wasn't any other possible thing it could be."
	"I'd read about this somewhere before."
	"Parallel worlds."
	"Worlds that existed alongside each other, never touching, never colliding."
	"A favorite plot device for bad science fiction writers everywhere."
	"So the reason that we were unable to meet even though we were in the same place at about the same time was the fact that we existed in different universes entirely."
	"I knew this to be true because Itsuki-san and Minamo-chan weren't here with me in the Tachikawa Station of my universe..."
	"...and in the same manner, I wasn't there with them in the Tachikawa Station of their universe."
	"Even worse -- since the word "universe" encompassed the Earth, the Milky Way, and all the galaxies in the sky, if we lived in different ones that surely meant..."
	show phone ituki3
	it "But if that's really true, then that means that we all can never meet..."
	play music "snd/blank.ogg"
	"*THA-THUMP!*"
	"My heart started beating wildly with fear."
	"This is what I had been most afraid of."
	"If we lived on different worlds altogether, then no train or rocket or span of a million lifetimes..."
	"...would ever allow me to meet those two girls in person."
	"And just as our worlds existed in parallel...those girls and I would continue to exist in parallel...our lines never once crossing..."
	"...not even once, not in all eternity."
	"...the world was filled with mysteries."
	"I'd come to realize that not too long ago."
	"After all, not so long ago, a certain phenomenon that couldn't be explained by any of the logic or the science in the world actually *happened* to me."
	"...but the kind of mystery I was facing right here, right now?"
	"I didn't want anything to do with it!"
	play music "snd/tears.ogg"
	ka "I can't accept this!!"
	hide phone
	scene black
	"I yelled, on the verge of tears."
	"The passersby were probably staring at me by now."
	"I took off running, clasping my cellphone and the hologram it projected to my chest."
	it "Hey, wait, Kasumi-chan!"
	"Because I wasn't on the VERGE of tears."
	it "Oh dear, there there, Kasumi-chan...it's all right, so please pull yourself together."
	it "Dry your tears, okay?"
	"That's right. I was IN tears already."
	$renpy.pause(2)
	"And before I knew it, I found myself in a big public park."
	play music "snd/blank.ogg"
	scene bg sky
	"I just crouched there at a corner of the adjacent parking lot, unable to stop the tears that were flooding from my eyes."
	show phone minamo5
	mi "Kasumii, why are you crying?"
	mi "After all, barrel worlds are something out of a manga, right? So they've gotta be fun, right?"
	"Was there no end to Minamo-chan's cheer?"
	"I didn't want a reality like this."
	"I mean, I'd fallen in love for the first time! And now to be told that I could never, ever meet the person that I was in love with..."
	"I...I just..."
	"Look, I knew that this love would never amount to anything."
	"But I couldn't just let it go if we couldn't even meet in person once."
	"Not if we couldn't even meet..."
	ka "But...but I..."
	"I tried desperately to control the chaotic feelings bubbling up inside me, even as I dabbed ineffectually at my tear-stained face with a handkerchief."
	ka "But...but..."
	"I didn't think that there was any way I could stop my tears from falling."
	ka "You see...I...well, you see...these days, my best friend got a boyfriend...and now I don't see her much...and so I'm lonely..."
	ka "And...and...just when I thought...that I'd found wonderful friends through this..."
	"This wasn't entirely the truth, but it wasn't...entirely a lie, either. Right?"
	ka "To tell me...that now we can't ever meet...that's just..."
	it "......Kasumi-chan..."
	show phone minamo7
	mi "C'mon~, Kasumii~, don't cry now...if you keep this up I'm going to start too..."
	show phone ituki1
	play music "snd/nukumori.ogg"
	it "Kasumi-chan."
	ka "Itsuki-san..."
	ka "It makes me very glad to know that you think of us so highly. I'm...very very happy."
	show phone ituki5
	it "Thank you, Kasumi-chan. We think very highly of you, too."
	ka "...*sob*..."
	"When I looked closely, I could see that the two had also run all the way over to the same park that I was in, and were now squatting in the exact same place in the exact same parking lot."
	"They'd come to this place in the other world, chasing after me even though they knew full well that I would not be there."
	"When I thought of that, I wondered just where I'd run to..."
	"...and with that, I stopped crying."
	"That was right."
	"Itsuki-san and Minamo-chan were always so warm and nice to me...even now, even when we knew where we all stood (or didn't stand)."
	"And even if we weren't in the same physical location, it was a rare and wonderful thing in and of itself that these two were showering me with their affection."
	ka "I'm sorry, Itsuki-san...I, I kind of lost myself there..."
	show phone ituki7
	it "Oh, that's okay, Kasumi-chan. We're already best friends, after all."
	"...best friends?"
	ka "Even if we can't ever meet?"
	show phone ituki5
	it "But we are meeting right now, are we not?"
	ka "Oh..."
	ka "...okay."
	"Yes."
	"Even if we could never become more than friends, even if we could never meet...we still had this. We could still talk with each other."
	"And if I could have just that, I was happy..."
	"...because Itsuki-san was right here..."
	show phone ituki1
	it "Hmm, interesting, we're still connected..."
	"As she said this, I looked down at my watch and noticed that sure enough, it was 3:00."
	"She was right. If this were as usual, we'd have been disconnected hours ago."
	show phone minamo1
	mi "Hey, Kasumii, let's play!"
	ka "......how?"
	mi "Let's go somewhere together!"
	show phone ituki1
	it "Yes, that could be fun indeed."
	it "After all, I don't know about you, but I'm kind of interested in seeing just where and how our worlds differ. How about it?"
	show phone minamo1
	mi "Whoa! Yeah, that's awesome!!"
	ka "...yeah, seems interesting."
	"I finally pulled myself together and stood up."
	"That was right, wasn't it?"
	"We'd agreed to come together today to have fun. So we were going to have fun."
	hide phone
	play music "snd/blank.ogg"
label 9:
	scene chap 9
	$renpy.pause(2)
	play music "snd/dream.ogg"
	scene bg sky2
	"The most astonishing thing was that, on this day, we continued to be connected for hours and hours on end."
	"And so we enjoyed this strange Sunday as much as we could, as long as we could."
	"I chatted gaily with my two friends, looking over at them as they walked through their world, imagining them walking by my side in my world."
	"...an almost miraculous, somehow poetic, but in the end somewhat lonely kind of fun."
	"While my world and their world were at a glance identical, there were lots of little -- and not so little -- differences."
	"For instance, the first thing that surprised me was the fact that the number of prefectures of Japan were very different."
	"There were only 41 in their world."
	"But in my world, there were 49. That was a big difference!"
	"For that matter, Kashii Prefecture, which was where I lived, didn't even exist in their world."
	"We'd even stopped by at the 'same' bookstore and taken out maps there to compare and contrast, and I was stunned."
	"I mean, in their world, Yamanashi Prefecture was right next to the Tokyo Metropolitan Area -- and Saitama Prefecture didn't even exist."
	"And no matter where I looked, I couldn't find Hino City anywhere."
	scene black
	$renpy.pause(2)
	scene bg park
	"We eventually came back to that park that we'd started at, and went inside."
	"There, we dropped by a shaved ice vendor and ordered some."
	"The shop was in the same place in both worlds, but there seemed to be a lot more flavors of syrup in their world."
	"It looked like Itsuki-san was fond of black currant, for instance."
	"I felt kind of let down."
	"See, the shop in my world didn't have black currant syrup in stock."
	"And I wanted to try having what Itsuki-san liked, obviously."
	show phone minamo1
	mi "Mmmm, tasty!"
	"Minamo-chan had chosen melon syrup."
	show phone ituki5
	it "It really is delicious."
	"And of course, Itsuki-san had chosen black currant syrup."
	ka "Mine tastes good too."
	"And finally, I'd gone with apricot."
	ka "Shaved ice is so great in the summer!"
	"But as I said this, both of the other girls stopped eating altogether."
	show phone minamo6
	mi "What? Shaved ice is great in some air?"
	ka "Ahaha, no, no, 'summer'."
	mi "Sum...mer?"
	ka "Yeah."
	show phone minamo4
	mi "What's a summer?"
	ka "Huh?"
	"Now it was my turn to imitate a deer in headlights."
	show phone ituki1
	it "Um, Kasumi-chan, what does 'summer' mean? We don't have that word here in our world, so why don't you tell us about it?"
	"I was completely taken aback."
	ka "Well, summer is summer...you know, the season of summer."
	show phone ituki4
	it "...'season'?"
	hide phone
	scene bg sky2
	"Okay, so this made the prefecture thing look pretty trivial."
	"I was shocked out of my mind."
	"Because now they were telling me that in their world, seasons themselves did not exist."
	"That they had the same climate all year round, without it getting particularly hotter or colder at any point."
	"That difference was all too huge."
	"I mean, wouldn't something like that have had a huge impact on the way that humankind developed?"
	ka "I find it hard to believe that your world -- which seems so similar to mine in so many ways -- doesn't have any seasons..."
	scene bg park
	show phone ituki5
	it "I suppose so."
	it "But you know, I think that's quite all right."
	it "My head is already spinning after all these strange miracles we've had, so what's one more?"
	"She giggled."
	ka "But...but...that's impossible...for our worlds to be so similar and yet for yours to have no seasons..."
	show phone ituki7
	it "Hmm?"
	"For a while, Itsuki-san thought on this, daintily eating her shaved ice, and then she spoke."
	show phone ituki1
	it "You know, I've been thinking about this..."
	it "When we say that something is 'impossible', does that always have to mean that in reality the thing in question can't ever actually happen? I'm not sure I agree with that..."
	it "See, I'd rather believe that the 'impossible' is merely something that others would never believe really happened, even if it did -- and even if you told them as much, right to their faces."
	show phone ituki5
	it "I mean, you can't even believe it yourself, can you?"
	"She smiled gently at me as she said this."
	"I couldn't help but blush deeply in response."
	"And somehow, I could feel acceptance of this entire situation taking hold. Somehow."
	hide phone
	scene bg sky2
	"A small time later, we were finally disconnected."
	scene black
	"Having finished this day well, I went home with a smile on my face."
	scene bg sky3
	"As if these wonderful, miraculous days would stretch on from now into eternity."
	"That was my prayer as the train taking me home jolted me ever so slightly in its familiar rhythmic cadence."
	scene black
	"But those girls and I were never connected again."
	play music "snd/blank.ogg"
	$renpy.pause(2)
label 0:
	scene chap 0
	$renpy.pause(2)
	play music "snd/tasogare.ogg"
	scene bg sky3
	"I kept waiting."
	"Waiting every day, like an idiot."
	"As if I had nothing else to do, as if nothing else in the world was of any importance."
	"Just waiting for that by-now-familiar sound to announce that those girls had connected with me once again."
	"I waited for so long, and I had my share of tears, but nothing but empty space greeted me."
	"And as I just stared at that jury-rigged cellphone wrapped in scotch tape, my summer vacation began...and ended."
	"Why?"
	"How?"
	"This was too cruel."
	"I'd fallen so in love..."
	"...we'd become such great friends...I'd never be able to forget them...as if these memories and feelings were part of my flesh..."
	"...and now we couldn't even talk to each other ever again. Why? How?"
	"I'd never be able to meet them again; I'd never be able to see their faces again; I'd never hear their voices again; I'd never be called 'Kasumi-chan' by Itsuki-san ever again."
	"This was..."
	"This was as if my arms and legs had been ripped off of me. And I felt just as paralyzed."
	scene black
	$renpy.pause(2)
	scene bg way3
	"...how many hours, how many days, how many weeks did it take for my feelings to finally be put to rest?"
	"Yeah...in truth..........I'd known from the very beginning."
	"After all, this had all been started by something that could only be called an incredible coincidence."
	"And even then, our connections were very unstable, and ended so quickly and abruptly."
	"Somewhere, somewhere deep inside my heart, I knew from the very beginning that it would be hard to continue to speak with those girls the way things were."
	"I knew."
	"And yet..."
	"And yet."
	"......"
	"I was so happy..."
	"...in those days, my every moment was illuminated with a radiance that I had never known could exist within me..."
	"...and I never wanted it to end."
	"I wanted to be enveloped in that light for ever and ever and ever..."
	"......"
	"Just what were those days, then?"
	"Just what *were* those days that came upon me like a dream?"
	"They certainly had disappeared from me as if they had been dreams and nothing more."
	"For instance, soon enough it was my birthday."
	"I so longed for Itsuki-san to be there to tell me 'happy birthday'."
	"My little, little dreams, now all scattered about, had fallen down to earth like so much shaved ice and had melted away...just like shaved ice."
	scene black
	$renpy.pause(2)
	"It makes me think that those days -- those feelings -- were something not unlike that one word that I'd had to learn in English class, not so long ago."
	"And that word has remained in my heart, imprinted there as if by some gigantic hand."
	scene bg sky3
	"RESONANCE - (n) an echo, a reverberation, an evocation."
	scene black
	"This summer, in some place and some time still, my love resonated...and then vanished into nothing."
label off:
	scene chap off
	$renpy.pause(2)
	scene bg sky2
	"And that was how my summer ended."
	"I wasn't any closer to understanding anything about life or the world."
	"After all, this world existed, and that was that."
	"This world in which a chance meeting like that was possible -- this was my world. There was no way I was going to understand it."
	"That's right. Understanding was not required of me. Yet."
	"One evening, I asked a question to my big sister as she watched TV."
	ka "Hey, question for you."
	"Oneechan" "Hmm?"
	ka "If -- just if -- you were handed a test where every single question was absolutely unanswerable...what would you do?"
	"Oneechan" "...I would flip it over and start drawing on the back."
	"She replied, not taking her eyes off the TV."
	"And I thought to myself: that's gotta be the right answer."
	scene black
	"My life hasn't changed that much since then."
	"I've gone back to my habit of buying Capri Sun, for one."
	"If anything's changed at all, it's that I just drink it on the way to school now instead of throwing it into my backpack."
	"Oh, right, now I'm a little more careful about that last turn on the way to school, of course..."
	"...and finally, there's the matter of how one day, that middle schooler who had started all of this by crashing into me was waiting for me by that turn, and handed me a love letter with a huge blush on his face."
	"Since then, I've never owned -- or had reason to own -- a cellphone ever again."
	play music "snd/blank.ogg"
	scene bg sky2
	$renpy.pause(1)
	"[Name: Kasumi Kurasawa]"
	"[Sex: Female]"
	"[Birthday: 7/21]"
	"[Sign: Cancer]"
	"[Blood Type: O]"
	"[Saegasaki High School, 1st-year student]"
	"[16 years of age]"
	""
	"This summer, I..."
	"...took one more step away from being a child."
scene weet end
$GAME_print('        Afterword')
$GAME_print('')
$GAME_print('')
$GAME_print('All the themes seemed to come together all at once, and thus did production on this work begin.')
$GAME_print('')
$GAME_print('Summer.')
$GAME_print('')
$GAME_print('Youth.')
$GAME_print('')
$GAME_print('Adolescent girls.')
$GAME_print('')
$GAME_print('Lesbian yearnings.')
$GAME_print('')
$GAME_print('An unattainable first love.')
$GAME_print('')
$GAME_print('A wondrous correspondence.')
$GAME_print('')
$GAME_print('All these themes -- each one a special favorite ingredient of this chef -- were mixed together in a shiny new bowl called "online distribution", and then before I knew it the fires of creativity were burning bright.')
$GAME_print('')
$GAME_print('Since I had all my favorite ingredients lined up before me like that, I couldn't exactly stop myself, or so it seems.
$GAME_print('')
$GAME_print('I was between jobs at the time, and so after three weeks of intense preparation, I am proud to present this story as a finished dish -- plated and ready to be judged -- to all of you.')
$GAME_print('')
$GAME_print('But as a matter of fact, I think the person who tasted this dish most profoundly was none other but me. I keep feeling that I want to create something more.')
$GAME_print('')
$GAME_print('Well, certainly, the act of taking the world that exists within you and printing it out for all to see can be very embarrassing, and right now I don't write nearly as well as I'd like to, so I ended up with something that fell well, well short of what I'd originally imagined, but the joy of creating something and nurturing it from conception to birth cannot be stayed. Furthermore, I am struck by the fact that there are so many different paths, so many different ways to create things.')
$GAME_print('')
$GAME_print('For instance, when you've given it your all, and expressed yourself to your limits without once involving money or payment or anything like that ... you stand satisfied, ready for any judgment, because you know you've done what you must.')
$GAME_print('')
$GAME_print('So let's meet each other again on different pages someday.')
$GAME_print('')
$GAME_print('I don't know if I'll be able to write a story that is all that different from the one I've presented here, but I do know that whatever it is, I'll write it the way I please. And that will not change, no matter what.')
$GAME_print('')
$GAME_print('Thank you all for nurturing my ever-so-clumsy, ever-so-childish efforts.')
$GAME_print('')
$GAME_print('')
$GAME_print('1 July 2002')
$GAME_print('Kagura Saitoh')
$renpy.quit()