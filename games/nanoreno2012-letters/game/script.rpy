init:
	image weet cred = "GUI/portcred.jpg"
	image weet title = "GUI/mm_ground.jpg"
	image bg kitchen = "BG/Kitchen.png"
	image bg door = "BG/Door 1.png"
	image bg door2 = "BG/Door 2.png"
	image bg forest = "BG/Forest.png"
	image bg livingroom = "BG/Living Room.png"
	image bg meadow = "BG/Meadow.png"
	image bg park = "BG/Park.png"
	image bg postoffice = "BG/Post Office.png"
	image bg postoffice2 = "BG/Post Office 2.png"
	image bg store = "BG/Store.png"
	image bg street = "BG/Street.png"
	image bg train = "BG/Train.png"
	image bg traintracks = "BG/Train Tracks.png"
	image sayaka livingroom = "BG/Living Room 2.png"
	image sayaka home = "BG/Sayaka home.png"
	image cg chase = "CGs/chase.jpg"
	image cg sayonara = "CGs/sayonara.jpg"
	image cg kite = "CGs/kite.jpg"
	image falling = "CGs/falling.jpg"
	image waiting = "CGs/waiting.jpg"
	image credits 1 = "GUI/[CREDITS] Proofreaders.jpg"
	image credits 2 = "GUI/[CREDITS] Music.jpg"
	image credits 3 = "GUI/[CREDITS] Sound Effects.jpg"
	image credits 4 = "GUI/[CREDITS] Art.jpg"
	image credits 5 = "GUI/[CREDITS] Testers.jpg"
	image credits 6 = "GUI/[CREDITS] Special thanks.jpg"
	image credits 7 = "GUI/[CREDITS] Special thanks 2.jpg"
	image fuyumi smile = "Sprites/Fuyumi/s mom_happy.png"
	image fuyumi idk = "Sprites/Fuyumi/s mom_idk.png"
	image fuyumi wondering = "Sprites/Fuyumi/s mom_wondering.png"
	image akane happy= "Sprites/Akane/t mom_happy.png"
	image akane smile = "Sprites/Akane/t mom_smile.png"
	image kyouhei smile = "Sprites/Kyouhei/s dad_happy.png"
	image kyouhei angry = "Sprites/Kyouhei/s dad_angry.png"
	image kyouhei suspicious = "Sprites/Kyouhei/s dad_suspicious.png"
	image tegami smile = "Sprites/Tegami/tegami_smile.png"
	image tegami neutral = "Sprites/Tegami/tegami_neutral.png"
	image tegami talking = "Sprites/Tegami/tegami_talking.png"
	image tegami supergrin = "Sprites/Tegami/tegami_supergrin.png"
	image tegami angry = "Sprites/Tegami/tegami_angry.png"
	image tegami close talking = "Sprites/Tegami/tegami_closedeyestalking.png"
	image tegami grin = "Sprites/Tegami/tegami_grin.png"
	image tegami neutral = "Sprites/Tegami/tegami_neutral.png"
	image tegami sad = "Sprites/Tegami/tegami_sad.png"
	image tegami tch = "Sprites/Tegami/tegami_tch.png"
	image tegami uh = "Sprites/Tegami/tegami_uh.png"
	image tegami content = "Sprites/Tegami/tegami_content.png"
	image tegami sweatdrop = "Sprites/Tegami/tegami_sweatdrop.png"
	image sayaka angry = "Sprites/Sayaka/sayaka_angry.png"
	image sayaka neutral = "Sprites/Sayaka/sayaka_neutral.png"
	image sayaka annoyed = "Sprites/Sayaka/sayaka_annoyed.png"
	image sayaka happy = "Sprites/Sayaka/sayaka_happy.png"
	image sayaka joking = "Sprites/Sayaka/sayaka_joking.png"
	image sayaka sad = "Sprites/Sayaka/sayaka_sad.png"
	image sayaka uh = "Sprites/Sayaka/sayaka_uh.png"
	image sayaka smile = "Sprites/Sayaka/sayaka_smile.png"
	image sayaka grr = "Sprites/Sayaka/sayaka_grr.png"

	define t = Character('Fujitaka Tegami')
	define s = Character('Narazaki Sayaka') 
	define m = Character('Boy')
	define f = Character('Girl')
	define ma = Character('Fujitaka Akane')
	define w = Character('Narazaki Fuyumi')
	define du = Character('Narazaki Kyouhei'")
	define mm = Character('Mailman')

label start:
	scene weet cred
	$renpy.pause(2)
	scene weet title
	$renpy.pause(3)
    play music "Music/Wallpaper.ogg"
    scene bg street
    show tegami tch
    m "(Ah, almost done with today's mail...)"
    "The boy's shoulders sagged in exhaustion, he massaged it using his hand and stretched a bit to loosen up his tense muscles."
    m "(Being a mailman is hard, being a special mailman is harder.)"
    m "(We special mailmen don't deliver just any ordinary letters.)"
    m "(We deliver invitations, doctor's reports, military stuff, confidential letters and letters to the soon-to-die.)"
    m "(The company has a strict policy for those letters. They're color coded for organizational purposes, and at least we couriers know what we're getting into.)"
    m "(I just hate how this job is unpredictable. I could be delivering just one letter today, and the next day twenty letters.)"
    m "(Tegami the Mailman... Sounds weird.)"
    show tegami supergrin
    t "(This is the fourteenth today. Walked a lot, good thing I'm young!)"
    scene bg door
    show tegami talking
    play sound "SFX/Knock knock.ogg"
    t "Excuse me! Doctor's Report for Narazaki Sayaka-san!"
    t "(After this, I'll head over to the next town...)"
    show tegami tch
    t "Excuse me? Anyone home?"
    t "(Maybe no one is home... I think I'll just leave it here in the mailbox...)"
    "Just as he was about to place it in the mailbox and leave, he was interrupted."
    f "Take the letter with you."
    t "Huh?"
    t "Are you Narazaki-san?"
    "A girl opened the door to the house and stepped out."
    show tegami tch at left
    show sayaka annoyed at right
    "She nodded without a word, and stood still at the door."
#make more tegami expressions
    show tegami uh at left
    t "I'm afraid I can't do that, Narazaki-san."
    s "Just keep the letter with you, you don't have to tell your boss you didn't deliver it."
    t "(I've never met someone who would so adamantly refuse receiving a letter...)"
    t "(Is that worry in her eyes? Why is she refusing so much?)"
    t "I can't do that. This's my job."
    t "And also, what's wrong with receiving this?"
    "The girl sighed in exasperation."
    show tegami tch at left
    show sayaka angry at right
    s "...Whatever, I'm still not receiving it. If you'll excuse me..."
    "The girl grasped the doorknob and turned on her heel to leave..."
    show tegami uh at center
    scene cg chase
    play music "Music/Merry Go.ogg"
#cg
    t "Hey!"
    "Then the girl suddenly changed course, and began to run in the opposite direction."
    t "Ack! Why're you running?!"
    "Tegami chased after her, the report still in his hand."
    s "WHY'RE YOU CHASING ME?!"
    t "CALM DOWN, DON'T RUN AWAY FROM ME!"
    s "I'm not an idiot! You'll do something once I stop running."
    t "What do you mean by 'something'?! I won't do anything, trust me."
    s "Liar! You wouldn't do this much just for a delivery."
    "Sayaka began to take longer strides, and sped up her pace."
    t "She's fast!"
    t "I just need to deliver this, why'd I get mistaken for a maniac?!"
    t "I just need to deliver the report to you! I'll go away afterwards!"
    s "I said I won't accept it!"
    t "Please accept i-"
    scene black
    play music "Music/blank.ogg"
    play sound "SFX/Thump.ogg"
    "BAM!"
    scene bg street
    t "Ow..."
    t "(Looks like I slipped... That hurt.)"
    show sayaka uh 
    s "..."
    s "Are you dead?"
    "Sayaka hesitantly tried to get closer to the boy. She was still cautious, although now she felt some worry." 
    show sayaka angry 
    s "Answer me! Stop playing dead..."
    show sayaka annoyed
    "Sayaka frowned, her worry clear on her face."
    s "Hey..."
    "She crept closer and poked him with a finger."
    show sayaka angry 
    s "He's not moving!"
    show sayaka angry at right
    show tegami supergrin at left
    t "Gah! I've alive!"
    scene black
    play sound "SFX/Punch.ogg"
	$renpy.pause(0.4)
    play music "Music/Merry Go.ogg"
    scene bg street
    show tegami supergrin at left
    t "Ouch! Hey, what was that for?"
    s "Don't scare me like that, I was about to bury you alive."
    show tegami uh at left
    t "You didn't even check if I was alive or not. I didn't look all that dead, did I?"
    "Sayaka sighed."
    show sayaka annoyed at right
    s "Going to all this trouble just to deliver a report... I guess I should accept it.."
    show tegami talking at left
    t "So... You feel guilty!"
    s "I don't."
    "Tegami handed her the letter he held in his hands. It was still in good shape, despite his earlier fall."
    t "Well, here it is."
    "He gave her a great, radiant grin as he finally delivered to her the report."
    show sayaka neutral at right
    s "..."
    t "I'll get going now, I have more letters to deliver today."
    show tegami supergrin at left
    t "My name's Tegami!"
    t "Bye, Narazaki-san!"
    "He ran to the opposite direction hurriedly."
    hide sayaka
    show tegami uh at center
    t "(I lost a bit of time back there! I gotta hurry, I have five more to deliver.)"
    hide tegami
    show sayaka uh at center
    s "What an odd man..."
    play music "Music/tamsp18.ogg"
    scene bg park
    show tegami supergrin
    t "(One more letter to go! I'm almost done with today.)"
    "Tegami smiled as he walked off to deliver one last letter. After that, he could go home."
    "His friend, a normal mailman, was supposed to be delivering this letter, but an urgent matter came up so he passed it over to Tegami."
    t "(I just can't refuse people, can I)?" 
    t "..."
    t "(Oh well! Time to deliver this, and get some rest after!)"
    t "(So this letter is addressed to...)"
    play music "Music/blank.ogg"
    show tegami uh
    t "(Narazaki Sayaka?)" 
    t "(She's the girl who didn't accept my delivery last time!)"
    show tegami tch
    t "(I have a bad feeling about this...)"
    show tegami smile
    t "(Still, I gotta deliver this. My friend asked me to, he believes in me!)"
    "Tegami unconsciously pumped his fists in determination."
    play music "Music/Wallpaper.ogg"
    scene bg street
    show tegami tch
    t "(This road really looks familiar, I can almost visualize the way I slipped and fell on the floor.)"
    t "(A few steps more...)"
    t "(And there's her house and mailbox.)"
    "He hesitated for a short moment, then opened his mouth and exclaimed loudly:"
    scene bg door
    show tegami talking
    t "Letter for Narazaki Sayaka-san!"
    t "(Her name kinda sounds familiar... Odd...)"
    show tegami tch
    t "(Besides her refusing the letter before...)"
    hide tegami
    s "I'm not accepting it."
    s "Tegami, right?"
    "Her voice could be heard through the door. She remained inside the house."
    s "Go home."
    show tegami uh
    t "You accepted the report last time!"
    s "That was then."
    t "But this isn't a report again! It's just an ordinary letter."
    "Sayaka didn't reply for a few seconds."
    s "No. Go home."
    t "(I can't give up!)"
    t "No, I'm staying here until you accept it."
    t "(If that's the way she wants to play, fine. I'll just stake out in front of her house! She can't stay in there forever!)"
    "Tegami sat down on the porch, and crossed his arms as he waited."
    "And waited...."
    "And waited."
    "Tegami grunted."
    t "I...I hate waiting."
    "He rapidly shook his head and leaned onto the door."
    t "(This won't take too long.)"
    "Time passed... Ten minutes turned into an hour."
    t "This is... taking a bit longer than expected."
    "By then, Tegami already relaxed his position. He was almost lying down."
    t "(Need to stay awake...)"
    t "(Need to...)"
    scene black
    play music "Music/Prelude in C - BWV 846.ogg"
    f "Why're you crying? There's no need to cry."
    m "I'm not crying!"
    "He hurriedly wiped away his tears."
    f "Hey, I don't see you here a lot."
    m "Why would you? I don't go out a lot."
    m "Hey, hey! Cheer up! Or else Bear-san will become sad."
    "She moved the teddy bear in her arms. Its head was inclined downwards, and its body hunched in sadness."
    f "See? Bear-san'll stay like that if you don't smile."
    m "..."
    "The boy clenched his teeth in a smile and gave the girl a forced grin."
    m "There, happy?"
    f "What, Bear-san?! I'm not bullying him or forcing him to laugh!"
    m "..."
    "The girl moved the bear up to ready for an action. Bear-san tackled the girl straight on the head, showing anger at his friend."
    f "Ouch! There's no need to hit me. I'm actually kind of jealous though. We've been friends for so long, and now you're choosing him over me!"
    m "... "
    m "Kuku...."
    "The boy had a small smile at first, but then he couldn't control it. He burst out laughing, amusement worming its way into his small young heart."
    f "!"
    f "You're laughing now!"
    "She grinned, dancing Bear-san around the air as well."
    f "What's your name?"
    m "Tegami."
    f "Cool, I'm Sayaka."
    f "But, call me Nara-chan since my last name's Narazaki."
    f "Starting from today, we're friends!"
    play music "Music/blank.ogg"
    $renpy.pause(2)
    play music "Music/tamsp18.ogg"
    scene bg door2
    show sayaka neutral
#cg
    s "Hey."
    show sayaka neutral at right
    show tegami uh at left
    t "Huh? Did I fall asleep for a sec?"
    show sayaka annoyed at right
    s "You idiot."
    "Sayaka stood in front of Tegami, looking down on him with some disdain."
    t "Ugh... What time is it?"
    s "Ten in the morning."
    t "Seriously?!"
    t "(I have to get to work! The Boss is gonna kill me!)"
    show sayaka joking at right
    s "Nah, just kidding. Look at the sky, it's sunset."
    show tegami tch at left
    t "...Oh."
    t "(I feel a bit stupid...)"
    t "(That's strange... Why don't I feel cold?)"
    "He squirmed a bit, and felt something soft on him."
    show tegami neutral at left
    t "(A blanket...)"
    show sayaka uh at right
    s "Go home."
    t "..."
    s "Staying out this late is gonna be impractical for both of us."
    s "You'll get sick, and I don't want to be responsible for it."
    s "Colds and fevers are in season."
    t "(Don't people get colds at any time of the year?)"
    show tegami uh at left
    t "You... You kinda sound like a mom..."
    t "Are you worried?"
    show sayaka angry at right
    s "What? Of course not."
    "She looked at him incredulously."
    show tegami talking at left
    t "Accept the letter, and I'll go home."
    t "It's that simple."
    show tegami supergrin at left
    "He beamed a grin at her, hoping that she'll eventually give in."
    show sayaka annoyed at right
    s "You're pretty sly sometimes, aren't you?"
    s "You know how to take advantage of others' guilt..."
    show tegami sad at left
    t "Please accept it?"
    t "(Giving my best puppy dog eyes here... Hope it works.)"
    show sayaka uh at right
    s "..."
    t "(It's working!)"
    show sayaka angry at right
    "She grit her teeth, annoyed with falling to Tegami's wiles."
    s "Fine! Give me the letter already."
    show tegami supergrin at left
    t "Yay!"
    show sayaka annoyed at right
    s "This is really gonna be the last time I'll accept a letter from you."
    t "Whatever you say..."
    s "Go home and rest."
    t "Yes, mommy..."
    "He fled before she could land a punch on him."
    play music "Music/Wallpaper.ogg"
    scene bg livingroom
    show tegami smile
    t "Finally, a day off..."
    t "(Feels nice to relax. The weather's clear and sunny today, too.)"
    t "I'm going out, Mom!"
    hide tegami
    show akane happy
    ma "Can you buy some things for me at the general goods store?"
    show akane happy at right
    show tegami talking at left
    t "Sure. What do you need?"
    ma "I have a list right..."
    ma "Here it is!"
    "She inserted a hand in her pocket, and took out a piece of paper."
    t "Got it."
    t "Is this urgent? I might get home in time for dinner."
    ma "No, I just need this for tomorrow."
    t "Okay. I'll be back for dinner. Bye~"
    ma "Take care..."
    hide tegami
    show akane smile at center
    "She waved and smiled as she watched him leave."
    "Tegami gently pushed the door shut, and leisurely walked towards the main part of town."
    scene bg park
    show tegami smile
    t "(I think I'll do Mom's errand first, I don't wanna rush it in case I run out of time.)"
    t "(After that, I think I'll go to the bookstore...)"
    "Tegami passed by several running kids. Some bumped into him as they played their game."
    t "(Well, the kids are really lively today...)"
    "Lively's an understatement."
    show tegami neutral
    t "(Better than a dead town.)"
    t "(Take a turn to the left...)"
    show tegami talking
    t "(And there's the general store!)"    
    "He stopped in front of the small store, its walls were a bit ragged and a shade of dirty white."
    show tegami supergrin
    t "(This store is pretty old, but still standing.)"
    t "(Gotta admire the owner.)"
    "He entered the shop, and looked around for the things he needed."
    scene bg store
    show tegami smile
    t "(Soy sauce, flour, and gelatin.)"
    t "(First off is the sauce section at the right.)"
    hide tegami
    "He walked over to the right shelf, and scanned the different brands displayed."
    "Grabbing one of the bottles, he read the brand and its label."
    "Afterwards, he returned it on the shelf."
    show tegami tch
    t "(Not this brand...)"
    "He continued scanning the display before he set his eyes on one bottle."
    show tegami grin
    t "(This one! This is the one at home.)"
    t "(Cheap and good!)"
    "He grinned in satisfaction, and took the bottle before proceeding to another shelf."
    show tegami smile
    t "(Flour...)"
    "He picked up a red bag of flour..."
    show tegami tch
    t "(Hm... Not this...)"
    "And returned it."
    "He looked for a bit, and got a brown bag."
    show tegami talking
    t "(Ah, this one's the one mom uses!)"
    "He held it with his left hand."
    t "(Only soy sauce left!)"
    "With the bottle of soy sauce held using his right hand and a bag of flour held in the other, he made his way to the desserts aisle."
    "He politely gave way for an old lady buying some vegetables, keeping to his right."
    "When he reached the desserts aisle, he saw a familiar person looking at something."
    show tegami supergrin
    t "What a small world, haha."
    show tegami supergrin at left
    show sayaka annoyed at right
    s "You don't say?"
    "Narazaki Sayaka had a basket with her containing about ten items."
    show tegami talking at left
    t "So you're running errands too?"
    show sayaka uh at right
    s "I guess."
    show tegami uh at left
    t "Hey! That's pretty expensive." 
    "He pointed at the gelatin mixture Sayaka held." #a CG would be better here, showing the object
    s "Yeah, it is."
    "Tegami pulled out a small box labelled “Plain gelatin” from the shelf."
    show tegami supergrin at left
    t "This brand is cheaper, and it's just as good!"
    s "Really?"
    t "There are also flavoured ones like grape, orange, strawberry, and green apple."
    t "It's really good, believe me!"
    s "Why should I?"
    show sayaka joking at right
    "Sayaka's tone was teasing as she stuck her tongue out like a kid."
    show tegami talking at left
    t "I like food, so I guess I have good taste. And I wouldn't try to poison you."
    show tegami supergrin at left
    "Tegami shrugged his shoulders and dopily grinned at her."
    show sayaka smile at right
    "Sayaka paused for a moment before chuckling."
    s "Ah, fine. That's considerably cheaper anyway."
    "She put the product back on the shelf, and selected another one."
    show tegami smile at left
    t "So... thanks?"
    s "I haven't tried it yet, so I hold my thanks for now. This could be worse than the one I buy."
    t "(You're just too shy to say thanks.)"
    "The boy laughed, and walked to the counter. He took out a few bills from his pocket and handed it to the cashier."
    "He glanced at the girl, and pointed at her stuff."
    show tegami uh at left
    t "You're buying a lot."
    show sayaka uh at right
    s "That's called grocery shopping. You, of all people, should know."
    show tegami tch at left
    t "(That's odd... She didn't say that insultingly.)"
    t "(She sounded a bit... friendly?)"
    show tegami smile at left
    t "(Ah! Maybe she thinks of me as a friend now!)"
    show sayaka smile at right
    s "So... Wanna help me carry this stuff home?"
    "She shyly smiled as she took a paper bag full of things."
    show tegami uh at left
    "Tegami was taken aback for a second, before getting what she meant."
    show tegami smile at left
    t "I'll take the other bag, then."
    "He got the last paper bag and carried it using his right arm."
    "They took the left path, heading to Sayaka's house."
    scene bg street
    show tegami tch at left
    t "(It's a really quiet walk...)"
    t "(But really... I feel like I've heard her name before...)"
    play music "Music/blank.ogg"
    scene black
    play music "Music/Prelude in C - BWV 846.ogg"
    f "Hey, what's your name? Bear-san beat me up and now wants to get to know you..."
    m "...Tegami."
    f "Tegami... as in ‘letter'? That's a really odd name!"
    f "Ow! You hit me again, Bear-san!"
    f "Anyway, I'm Narazaki Sayaka-chan. You can call me Sayaka, or Nara-chan!"
    m "..."
    f "Repeat after me!"
    f "NARA-CHAN!"
    m "..."
    f "Or else..."
    "She jabbed him in the side, tickling him."
    m "H-hey!"
    f "Now, say it. Nara-chan..."
    m "Nara-chan..."
    play music "Music/blank.ogg"
    scene bg street
    play music "Music/tamsp18.ogg"
    show tegami tch 
    t "Nara-chan..."
    show tegami tch at left
    show sayaka smile at right
    s "Did you say anything?"
    t "(Did I say it out loud?)"
    show tegami uh at left
    play music "Music/blank.ogg"
    t "You're probably gonna think I'm crazy, if you haven't already, but are you Nara-chan?"
    t "I have this friend from childhood who had your name... and she asked me to call her Nara-chan..."
    t "I swear I'm not making this up..."
    t "(Please don't punch me.)"
    "..."
    "While Tegami was squirming, Sayaka broke into a giggling fit."
    play music "Music/Merry Go.ogg" 
    show sayaka joking at right 
    s "Took you long enough to remember."
    t "..."
    show tegami uh at left
    t "What?!"
    "Shock rendered him near speechlessness."
    s "Welcome back, Captain Obvious..."
	play music "Music/blank.ogg"
    $renpy.pause(2)
    play music "Music/tamsp18.ogg"
    show sayaka happy at right
    s "I recognized you right away, Tegami."
    t "How?"
    s "You didn't change much."
    s "And you were pretty quiet when we were kids."
    s "You're much more lively now. I like it."
    show tegami tch at left
    t "But why were you so hostile to me when we first met again?"
    s "I didn't recognize you that time, sorry."
    show sayaka smile at right
    s "I only realized you were my friend the day you stayed outside my house for an hour and a half."
    t "And that was when I fell asleep and stuff..."
    show tegami supergrin at left
    t "So that's why you were worried about me."
    t "(That's nice to hear!)"
    "She hesitantly admitted that, crossing her arms and huffing."
    show sayaka uh at right
    s "I guess... I guess you could say that."
    t "(She's a bit... feistier now?)"
    t "(I don't know. She was very kind before.)"
    "(She's still kind now, but a bit more sarcastic?)"
    show tegami talking at left
    t "Why'd you come to this town?"
    show sayaka smile at right
    s "I certainly didn't follow you here, if that's what you're thinking."
    t "(Shoot.)"
    s "I have many reasons, educational, convenience, and opportunities and the like."
    s "..."
    show sayaka joking at right
    s "I did miss you, though."
    show sayaka happy at right
    s "I felt like a big sister when I was with you!"
    show tegami uh at left
    t "(Big sister?!)"
    s "You were so quiet at first, but when I finally won you over you got much more energenic."
    "She laughed at the thought, memories getting the best of her."
    show sayaka joking at right
    s "You're still dense, too, as evidenced by how long it took to remember me."
    s "It shouldn't have been that hard."
    s "I don't think I changed that much."
    show tegami tch at left
    t "(Wow, I am pretty slow...)"
    t "(But this is a new record.)"
    show tegami uh at left
    t "Ouch, that hurt. I didn't recognize you immediately because..."
    t "...because you're taller!"
    show sayaka smile at right
    s "Isn't that expected? I find it hard to believe that I'd still be 148 centimetres today."
    t "(She's still notorious in teasing me, up to this day.)"
    show tegami smile at left
    t "(Oh well, it's good to have that friendship back.)"
    s "So, enough about that. It's summer now, but I'm curious about school."
    show sayaka uh at right
    s "Where are you studying right now? I don't see you around at school..."
    show tegami tch at left
    t "Uh..."
    show tegami uh at left
    t "I'm not studying anymore..."
    s "..."
    s "Can I ask why?"
    "She made a strange facial expression, and looked a bit conflicted on whether to probe further."
    show tegami tch at left
    t "Sure."
    s "Why aren't you in school, then?"
    t "I'm working as a special mailman now, if you haven't already noticed."
    s "At first I thought it was just a summer job, sorry about that."
    s "I was wondering where you were studying. There's only one school near here, and I don't remember seeing you on campus."
    s "Why're you working instead of studying?"
    t "I need to earn money, I can't be burden."
    "Sayaka nodded in understanding."
    t "I can't be a burden... Not like before."
    show sayaka neutral at right
    s "You weren't, aren't, and will never be one."
    "..."
    t "(Time to change the subject... Quick, before she asks more.)"
    show tegami uh at left
    "Tegami made a surprised expression."
    t "Ah, we're almost at your house, right?"
    show tegami supergrin at left
    t "We spent a lot of time catching up!"
    t "..."
    show sayaka annoyed at right
    "Sayaka glared for a second, before going with what he was trying to do."
    show sayaka uh at right
    s "There it is."
    "She pointed at a small house beside a few others of its kind."
    t "The cursed mailbox!"
    "He cackled as he saw the mailbox near her home."
    show sayaka smile at right
    s "I still remember how you slipped and fell while chasing me."
    show sayaka joking at right
    s "Should've recorded that!"
    show tegami uh at left
    t "Mean."
    s "Just kidding."
    "Laughing, she went to the house's door, and inserted a key into the keyhole."
    "The door was unlocked with a small click, and she turned the knob and motioned for Tegami to go inside."
    scene sayaka livingroom
    show tegami talking
    t "This is the first time I've been inside your house..."
    "He glanced at the walls, furniture, and decorations."
    "After noting how homely it felt inside, he turned back to her."
    show tegami talking at left
    show sayaka smile at right
    s "Just place it there beside the bag, above the table."
    "Tegami did as directed, placing the brown paper bag on the wooden table."
    s "Thanks for helping me."
    s "That would've been heavy and hard to carry home."
    "She smiled in a mixture of appreciation and amusement."
    s "You have pretty good timing, you know?"
    show tegami supergrin at left
    t "Of course! I was there for you when you needed help."
    s "Not just now. Even before, your timing is great."
    show tegami sweatdrop at left
    t "How?"
    t "(How could my timing be great? I have pretty bad luck...)"
    s "That's a secret!"
    show sayaka joking at right
    s "That's for me to know, and you to find out."
    t "(Um... okay...)"
    t "(Hm... It's almost four...)"
    show tegami uh at left
    t "(Ah, I still have to go to the bookstore!)"
    t "Sorry, I gotta go now. Have some more things I need to do in town."
    show tegami smile at left
    t "It was nice, catching up!"
    s "Bye bye, Tega-chan~"
    show tegami uh at left
    t "(Where'd that nickname come from?!)"
    t "Tega-chan...?"
    "Sayaka shrugged lazily."
    s "It works."
    t "No, it doesn't!"
    t "Anyway, I'm going now, hope to see you again."
    s "Yeah..."
    scene bg livingroom
    show tegami smile
    t "Mom, I'm home."
    t "(The bookstore didn't have much new stuff today...)"
    show tegami supergrin
    t "I got the things you wanted!"
    show tegami supergrin at left
    show akane smile at right
    ma "Thank you!"
    show akane happy at right
    ma "You chose well. Of course, you're an expert on what we use at home."
    t "Of course!"
    ma "Let's have a nice dinner!"
    ma "You're going to work tomorrow, so we should probably relax tonight."
    "..."
    scene bg postoffice
    play music "Music/Wallpaper.ogg"
    "Five days later..."
    show tegami uh 
    t "(Whoa, I have twenty-eight deliveries today?)"
    t "(Seriously?)"
    t "(Well, some of these places are near each other, like the library and town hall...)"
    t "(But there are also places on the other side of those...)"
    t "(This's why I don't like being a special mailman...)"
    "He sighed, feeling his sling bag's contents."
    t "My first destination is the library."
    scene black
    "Tegami ran around town the whole day, passing by like a blur to other people."
    "Some yelled at him for bumping into them, exclaiming how rude he was."
    t "(Fifteen more to go...)"
    t "(It's lunchtime...)"
    t "His stomach grumbled promptly, as if it heard his thoughts."
    t "(No time for lunch. I delivered thirteen letters in four hours, I need four more hours for fifteen.)"
    t "(I'm sorry, tummy...)"
    "He sighed, and scurried off to his next destination."
    scene bg street
    show tegami talking
    t "An invitation for Kazuki-san!"
    show tegami uh
    t "Kazuki-san?"
    show tegami tch
    t "(Looks like he's not home... I'll just leave this in the mailbox and go. I need to deliver a few more letters....)"
    "He inserted the envelope in the mailbox, and was about to leave when..."
    play music "Music/blank.ogg"
    show tegami uh
    t "(H-hey...)"
    play sound "SFX/Dog Growling.ogg"
    play music "Music/Merry Go.ogg"
    "...A large Doberman to his right glowered at him."
    t "I'm not a thief, I swear. Don't attack me!"
    "The Doberman tensed up and bared its fangs."
    t "(This is bad...)"
    t "(Should I run? I might anger the dog more...)"
    "Well, the dog apparently had enough waiting. He leaped, ready to pounce on Tegami"
    t "(On second thought...)"
    t "(RUN!!!)"
    "He took off without hesitation. The only things that energized him were adrenaline and fear."
    t "(How'd this happen?)"
    t "(Now I'm farther from my next destination...)"
    t "(Why am I so unlucky...)"
    scene bg park
    show tegami uh
    "Tegami snuck a glance behind, and saw that the Doberman was still hot on his heels."
    t "(I gotta lose him! But how?!)"
    "He continued running, navigating around a bunch of trees in a confusing pattern swiftly."
    play music "Music/blank.ogg"
	$renpy.pause(2)
    play sound "SFX/Dog crash.ogg"
    "!"
    "He heard a ‘thud' from behind."
    t "...What was that?"
    "He mustered the courage to look back..."
    "And saw that the dog collided with one of the trees." #use a CG here
    t "(Whew, he's outta commission for a while...)"
    t "(Time to get outta here fast!)"
    scene bg street
    t "(In the end, I managed to deliver them all...)"
    t "(It's not yet night time. I think I did a good job.)"
    t "(People at the office laughed at me when they see how tired I am.)"
    t "(Oh well...)"
    "He was practically dragging his feet on the pavement. Fatigue was taking over him faster than Sayaka's rebuttals."
    t "(I can't wait to get home...)"
    t "(This road looks familiar...)"
    t "..."
    t "(Hey, why's that house moving?)"
    t "(Why's the sky moving?)"
    t "(Why...)"
    scene black
    play music "Music/Prelude in C - BWV 846.ogg"
    f "Come over to my home sometime!"
    m "Why?"
    f "I'm bored, I wanna play with someone!"
    m "Find someone else. There's lots of people."
    f "As if you're doing a lot at home."
    m "..."
    f "Anyway, it'll be super fun!"
    f "We can play, and have cookies after!"
    m "Play?"
    m "You don't mean play house, do you?"
    f "You like playing house?"
    "The girl gasped, startled at what she thought."
    m "What?!"
    m "No, I don't!"
    "He blushed furiously, and denied the statement."
    f "Oh, really?"
    "She smirked and playfully nudged him with an elbow."
    m "I don't! Really!"
    f "Prove it! Go to my house and play."
    m "Fine!"
    "..."
    "And that was how they had their first playdate."
    play music "Music/blank.ogg"
    scene bg street
    t "(Wha-?)"
    t "(What's with this... pain?!)"
    t "(I feel like my butt's on fire!)"
    "He jolted awake, eyes bursting open."
    show tegami uh
    t "What's happening..."
    play music "Music/Merry Go.ogg"
    t "IT'S YOU!!!"
    "He yelled at seeing the face of his ‘attacker'."
    t "Why are you dragging me on the floor, Nara-chan?"
    show tegami uh at left
    show sayaka uh at right
    s "You passed out on the road."
    show tegami sweatdrop at left
    t "(Really?!)"
    t "I was? Are you sure you're not tricking me?"
    s "Of course not. If I left you there, you'd just get run over or something."
    show sayaka grr at right
    s "Anyway, what're you eating?!"
    s "Why're you so heavy?!"
    show tegami uh at left
    t "Hey, I'm not heavy!"
    s "Yes, you are. Try lifting yourself and see."
    show tegami tch at left
    t "(...)"
    t "(I wonder if I'd have a hard time lifting myself, I might really be heavy...)"
    t "(Wait a minute..)"
    show tegami uh at left
    t "... I can't do that... That's impossible!"
    show sayaka smile at right
    s "You don't say?"
    show tegami sweatdrop at left
    t "Can you please stop dragging me on the road?"
    t "It hurts! Friction sucks."
    play sound "SFX/Thump.ogg"
    "Sayaka immediately let go of his hand, causing Tegami's upper body to land on the ground with a soft thump."
    show tegami uh at left
    t "OW!"
    s "Sorry..."
    show sayaka joking at right
    s "Want me to try it again?"
    show tegami tch at left
    t "NO."
    show tegami sweatdrop at left
    t "I'll stand and walk on my own..."
    "He slowly got up, using his right hand to support him on the ground, and right foot to push him up."
    "Sayaka patiently waited for him to get up."
    show tegami talking at left
    t "Okay, I'm good."
    t "Are we near your house?"
    show sayaka happy at right
    s "Yep, two minutes away."
    s "Don't collapse on me again."
    "She laughed and started to walk again."
    t "This road does look familiar..."
    show sayaka joking at right
    s "Maybe it's the –"
    show tegami uh at left
    t "No, definitely not the chasing incident."
    t "Geez, you'll never let go of that."
    s "It was priceless, you have to admit."
    show tegami smile at left
    t "I think I pass by here a lot when I'm delivering letters."
    s "But we never see each other much."
    show tegami sweatdrop at left
    t "What a coincidence."
    show sayaka smile at right
    s "Maybe I'm just in the main part of town whenever you're here?"
    t "That kinda sounds like fate doesn't want us to meet again or something."
    t "Haha..."
    play music "Music/blank.ogg"
    "..."
    s "..."
    show tegami tch at left
    show sayaka uh at right
    s "What're you thinking?"
    t "..."
    play music "Music/Merry Go.ogg"
    show sayaka joking at right
    s "I need to see you again. I haven't annoyed you enough yet!"
    show tegami uh at left
    t "Um... what?!"
    s "Before was just the start."
    show sayaka smile at right
    s "..."
    s "Hopefully, this isn't the end."
    t "..."
    show tegami smile at left
    t "I'm sure it isn't."
    s "..."
    play music "Music/blank.ogg"
    scene black
    $renpy.pause(2)
    play music "Music/tamsp18.ogg"
    scene bg door
    "They soon arrived at Sayaka's house." 
    scene sayaka livingroom
    show sayaka smile 
    s "I'll go get some water for you, and some food. You probably haven't eaten anything, either."
    hide sayaka
    show tegami content
    t "Thanks..."
    "She headed to the kitchen. Tegami could hear the clattering of things in the kitchen as she looked for things."
    "After a few seconds, Sayaka returned."
    hide tegami
    show sayaka uh
    "She handed him a glass of water, and a piece of bread."
    "She looked a bit embarrased with what she had to serve."
    s "Uh, sorry, this all I have on hand right now. I don't like to cook-"
    "She turned to see Tegami wolfing down the piece of bread and downing the water in one gulp."
    show sayaka smile
    "She rolled her eyes and snickered."
    s "Okaaay..."
    show sayaka smile at right
    show tegami supergrin at left
    t "Ah! Even plain bread can taste good when you're hungry!"
    show sayaka angry at right
    s "Do you even have a right to be picky with food right now?"
    t "Thanks for the meal!"
    show sayaka smile at right
    s "You've gotten food here..."
    show sayaka happy at right
    s "So give something in return!"
    show tegami grin at left
    t "Wow, you're such a great friend!"
    "His words dripped with sarcasm."
    s "I know."
    show tegami sweatdrop at left
    t "So... What do you want in return?"
    show sayaka uh at right
    s "Hm..."
    "She paused for a while to think."
    show sayaka happy at right
    s "Tell me about your job."
    t "(That's...)"
    t "(That's a surprisingly simple request.)"
    t "(What's a good story that'll be entertaining?)"
    show tegami content at left
    t "(Ah! Maybe some really funny stories.)"
    "He drank some water, laid back on the couch, and began to tell a story."
    show tegami talking at left 
    show sayaka smile at right
    t "Before, when I was delivering mail..."
    t "It rained the day before, so the road was a little slippery."
    t "I had a lot of mail to deliver... I think somewhere around thirty."
    t "I was running from the main square to the clock tower."
    show sayaka joking at right
    s "I think I know where this is going..."
    show sayaka smile at right
    t "I bumped into a woman carrying a bag of oranges."
    t "Of course, I said sorry real quick and kept running..."
    show tegami uh at left
    t "But then I slipped on one of the oranges!"
    s "Here I thought you slipped because of the wet floor..."
    t "Nah, I can get by wet floor..."
    t "The worst part was when I slipped..."
    "Tegami grimaced at the memory."
    t "My boss was going out for lunch and saw me."
    show sayaka joking at right
    s "Pft... What was his reaction?"
    t "He kinda laughed at me, but excused me for not mailing everything that day because of that ‘accident'."
    s "Hey! At least you got something out of it."
    "She laughed at imagining her friend's experience."
    t "Why're you laughing?!"
    s "It's so you!"
    s "I mean, you're a master at balancing on wet floor, but you tripped on a fruit instead."
    s "And your boss is funny."
    show tegami sweatdrop at left
    t "You mean like you?"
    s "Touche."
    t "Well, that's my story."
    show sayaka smile at right
    s "This is nice."
    s "Catching up, telling funny stories..."
    show tegami talking at left
    t "Next time!"
    s "Huh?"
    "Sayaka looked genuinely puzzled at Tegami's sudden outburst."
    show tegami supergrin at left
    t "Next time, you'll be the one telling a story!"
    s "..."
    show sayaka joking at right
    s "Yeah, although my stories aren't as hilarious as yours!"
    show tegami sweatdrop at left
    t "I wasn't trying too hard to be funny."
    t "Anyway... I think I should go now."
    t "It's almost time for dinner, and I should get home."
    show sayaka smile at right
    s "Your mom's waiting for you."
    t "Yeah. Today was fun despite the stress."
    show tegami smile at left
    t "Thanks for taking care of me."
    show sayaka angry at right
    s "Who said I took care of you?"
    show sayaka smile at right
    s "If you're feeling that well to make those kinds of remarks, then go home already."
    show tegami supergrin at left
    t "Got it. Take care!"
    "He stood up and walked towards the door."
    hide tegami
    show sayaka smile at center
    s "Shouldn't you say that to yourself?"
    s "..."
    s "Take care too."
    scene black
    t "(That was unexpected.)"
    t "(This day turned out better than I thought...)"
    t "(I missed having a good friend. It's kinda hard to find one at work.)"
    t "(Even if she's sarcastic, she's still a good friend...)"
    t "(But I can't forget...)"
    t "(Her shaking hands as she dragged me along.)"
    t "(Why were they shaking?)"
    play music "Music/Prelude in C - BWV 846.ogg"
    f "Hey, let's play."
    m "Again?"
    f "This is different! We'll use this!"
    "In her hands was a red kite with a simple yellow tail."
    m "What's that?"
    f "Eh?! You don't know?"
    m "No."
    f "Play with me, and I'll tell you what is it after!"
    m "You're not gonna fool me again."
    f "Don't you wanna know what this is?"
    "She teasingly lifted the kite towards him."
    m "Why would I want to know what that is?"
    "He crossed his arms and pouted."
    f "Are you sure you don't wanna know?"
    f "This can fly up in the sky!"
    "To emphasize her point, she waved the kite in the air, mimicking a helicopter."
    m "That's not a bird... How can it fly?"
    f "Well, it's definitely not a bird. If you wanna know what it is, then play with me!"
    m "..."
    f "Let's just play!"
    play music "Music/blank.ogg"
    scene black
    t "(Ugh... Is I already morning?)"
    t "(I feel...groggy. Five more minutes...)"
    "Plopping back down, he shut his eyes and went back to sleep..."
    "Only he couldn't."
    t "Ugh... Stupid mattress..."
    "He rolled on his side and curled up."
    "He tried to go back to sleep, but just couldn't."
    "He slowly sat up, deep in thought."
    t "Why am I remembering all of this now?"
    "..."
    "I gotta get up, I still have work..."
    play music "Music/Wallpaper.ogg"
    scene bg postoffice
    show tegami smile 
    t "Only eight letters today..."
    t "That was a nice surprise."
    t "And it's only just after lunch."
    t "..."
    show tegami tch
    t "Actually, this is a bit boring..."
    t "(I can't go fishing, don't have equipment...)"
    t "(I don't wanna go to the library and read...)"
    t "(Hm...)"
    show tegami talking
    t "(Oh! I'll go visit Nara-chan.)"
    show tegami tch 
    t "(But wait...)"
    t "(That dream...)"
    show tegami talking
    t "(Hey, that gives me an idea! We can fly a kite again sometime.)"
    t "(I think I have a kite at home...)"
    t "(Maybe I should go home now, and look for it again.)"
    t "(I can file for an off day, and drop by Nara-chan's place.)"
    show tegami supergrin
    t "(That's a good plan! We'll also be able to bond more.)"
    t "(She's a lot more sarcastic now, but she's still the same from before...)"
    t "(I'll get going to the post office first, and then home...)"
    hide tegami
    "He continued his plans while skipping through town with a  bright sunny look."
    scene black
	play music "Music/blank.ogg"
	$renpy.pause(2)
    play music "Music/Wallpaper.ogg"
    scene bg door
    s "Yes? Who is it?"
    "Sayaka raised her voice so that it could be heard by the person outside."
    show tegami supergrin
    t "It's me! Wow, you're not trying to chase away people at your door now!"
    s "Oh, it's you."
    show tegami supergrin at left
    show sayaka smile at right
    "She opened the door and stepped out."
    "She shifted to a friendly and laid back expression."
    s "I thought you were working today?"
    show tegami smile at left
    t "I'm not skipping, I have an off day today."
    show tegami supergrin at left
    t "Ha! You thought I was skipping work, didn't you?"
    s "Yes."
    show sayaka joking at right
    s "Nah, just kidding, I know you wouldn't skip work."
    s "So, any reason why you're here?"
    t "I brought this!"
    "He took out a blue kite from his bag."
    show sayaka uh at right
    s "You want to fly a kite?"
    show tegami tch at left
    t "Yeah, but I don't know where we can fly it."
    t "And I don't know if it's gonna be windy today."
    s "I think I know a good place for that."
    s "There's a meadow part of some sort nearby. Kids go there and play after school."
    s "There'll be a bunch of kids there since it's summer, but I think they wouldn't bother us."
    s "Let's go!"
    "She sprinted towards the meadow park."
    t  "Hey, wait for me!"  
    play music "Music/blank.ogg"
    scene black
    scene bg meadow
    play music "Music/Piano 2.ogg"
    show tegami uh 
    t "Wow, we ran a lot..."
    show tegami uh at left
    s "Doesn't your job involve a lot of walking? You should be used to this..."
    show sayaka smile at right
    show tegami smile at left
    t "Says the person who's tired too."
    show sayaka joking at right
    s "I didn't say I wasn't tired."
    show sayaka smile at right
    s "Hey, there's a bunch of kids here."
    show tegami supergrin at left
    t "It's nice to see kids getting some exercise."
    s "Some city kids don't go out a lot, but our town is old and rustic – according to them."
    show tegami smile at left
    t "Who cares if it's old or rustic? This place is still home."
    s "..."
    show sayaka joking at right
    s "That's a lot like you, always caring about home."
    show sayaka smile at right
    s "It's very important to you."
    show tegami tch at left
    t "Yeah..."
    "He paused to glance at the kids, before turning his attention back to Sayaka."
    show tegami supergrin at left
    s "Hey, it's moderately windy today. I think this is a good day to fly a kite."
    t "Heheh, I have good timing!"
    show sayaka happy at right
    s "So, let's fly that kite already!" 
    "They set up the string. Sayaka held onto the kite, while Tegami held the handle with the string."
    show tegami grin at left
    t "Throw the kite up in the air when I count to one."
    show sayaka smile at right
    s "Okay."
    show tegami talking at left
    t "Three..."
    show sayaka neutral at right
    "She readied her arms."
    t "Two..."
    t "One!"
    "With all the strength she could muster, she threw the kite high up into the air."
    show sayaka uh at right
    s "Hey-"
    s "..."
    scene cg kite
    "Tegami was running, soaring the kite high in the sky."
    s "Like he's the one flying in the sky instead..."
    "She was shocked and amazed at that fleeting moment."
    t "Hey, Nara-chan! Can you see how high it's flying?"
    s "Yeah, it's amazing!"
    t "This feels great! I love the wind!" 
    "He halted, and tugged at the string to control the kite as it floated in the air."
    scene bg meadow
    show tegami supergrin
    t "Hey, Nara-chan!"
    show tegami supergrin at left
    show sayaka smile at right
    s "Yes, it looks nice."
    t "Nara-chan, try flying the kite yourself!"
    t "You did that a lot before."
    show sayaka uh at right
    s "Eh? But..."
    show tegami talking at left
    t "Come on! And don't give me that ‘only kids do that'."
    show tegami supergrin at left
    t "I flew a kite, and I'm not a kid."
    show sayaka neutral at right
    s "..."
    show sayaka smile at right
    s "Fine, give me the handle."
    "Tegami gave the string to Sayaka, making sure it didn't bring the kite down."
    show sayaka happy at right
    s "Hey, it's flying!"
    s "It's going high, this is amazing!"
    show tegami smile at left
    t "(And she's a kid again.)"
    t "(This makes me sorta miss my childhood...)"
    t "(...)"
    show tegami tch at left
    t "(Wait a minute, the kite's dropping...)"
    t "Oi, the kite's going down!"
    show sayaka uh at right
    s "Ah! It's gonna get stuck in one of the trees!"
    t "Hold the string, let's so get it back from where it went."
    t "We can follow its trail, the string."
    scene bg forest
    show tegami smile
    "They looked over at the trees, and spotted the kite stuck in its leaves and branches."
    t "I'll go and get it."
    "He climbed the tree, and untangled the kite from its branches."
    show tegami supergrin
    t "Got it!"
    "He grinned satisfactorily, showing the now free kite."
    hide tegami
    show sayaka smile at center
    s "Okay, so now let's go back and fly it again."
    scene bg meadow
    show tegami talking at left
    t "Why don't we do it the other way around this time?"
    show sayaka uh at right
    s "Huh?"
    t "I'll throw the kite, and you'll fly it."
    "He said in an as-a-matter-of-fact like tone, as if it was the most obvious thing in the world."
    s "I don't know..."
    "Strangely, she looked hesitant. That's unusual for the ever-sarcastic girl."
    show tegami supergrin at left
    t "You loved flying kites before! I bet you miss flying one."
    show tegami smile at left
    t "Unless... You're scared of not knowing how to fly one anymore?"
    show sayaka uh at right
    "At that statement, Sayaka was startled."
    s "What?! I didn't say anything about that..."
    show tegami supergrin at left
    t "So...?"
    "He awaited a response, doing his best to look persuasive."
    "Finally; she replied."
    show sayaka joking at right
    s "Challenge accepted."
    show tegami talking at left
    t "Great! So... I got the kite now." 
    "Sayaka backed away a little from Tegami."
    show sayaka smile at right
    s "There, I'm standing farther from you now."
    t "Great. Got the string?"
    s "Yeah."
    t "Alright..."
    t "Do the counting this time!"
    show sayaka uh at right
    "Sayaka sighed."
    s "Three..."
    "She furrowed her brow."
    s "Two..."
    "She clenched her teeth."
    show sayaka grr at right
    s "One..."
    "She released the breath she didn't know she was holding."
    hide tegami
    show sayaka grr at center
    s "Go!"
    "Immediately, Tegami shot the kite high up into the air." 
    "Sayaka ran, propelling the kite upwards."
    hide sayaka
    show tegami supergrin at center
    t "See, you're doing it!"
    t "You haven't forgotten how to fly a kite!"
    play music "Music/blank.ogg"
    show tegami tch at center
    t "(Hey, what?!)"
    play sound "SFX/Thump.ogg"
    "The next thing he knew, Narazaki Sayaka's knees gave way, and she dropped to the ground."
    hide tegami
    t "NARA-CHAN!!!"
    "He rushed over to her, running as if his own life was at risk."
    t "Are you okay?!"
    scene falling
    play music "Music/Haze of Sense.ogg"
    "He faced a distraught Sayaka who was lost in thought."
    "Her hands lost grip of the handle, and they were shaking."
    t "What happened?"
    t "(Are you okay? Did I do something wrong? Maybe I shouldn't have taken you out to fly a kite.)"
    t "(I'msorryI'msorryI'msorryI'msorry-"
    s "I'm fine!"
    "Narazaki Sayaka resiliently yelled at the panicking Tegami."
    "She resolutely looked at him straight in the eye."
    t "You're not okay!"
    s "Yes, I am!"
    s "I'm just tired. Give me a few secs and I'll get up."
    t "Bu-"
    s "I SAID I'M OKAY."
    "At that, Tegami shut up, not wanting to infuriate her further."
    t "..."
    scene bg meadow
    "She slowly, gently got up... Her hands were still shaking a bit, and her posture unsteady..."
    "But she was okay."
    "She was okay, and that was all that mattered to Tegami."
    show sayaka uh at right
    s "I'm sorry for ruining the day, but can we go home now?"
    show tegami tch at left
    t "...Sure."
    "Tegami picked up the forgotten kite, and he and the girl slowly walked back home."
    "She was dragging her feet a bit, but Tegami repeated a silent mantra in his mind."
    hide sayaka
    show tegami tch at center
    t "(She's gonna be okay..)"
    scene black
    t "(It's been four days since ‘that incident'.)"
    t "(I can't forget about how she fell... How lifeless she suddenly looked...)"
    t "(I can't forget how it could've been my fault.)"
    t "(Maybe she was tired that day, and I was bothering her...)"
    t "(Maybe I forced her to come with me. Maybe she really didn't want to go.)"
    t "(I can't stop thinking like this.)"
    t "(I hate how a lot of stuff is my fault. Not just now...)"
    t "(But...)"
    t "(I gotta try, even if it seems like she doesn't want me around.)"
    t "(She might be lonely...)"
    t "(I know! I'll try to go visit her when I can.)"
    scene bg postoffice
    show tegami tch
    t "(So today I have ten letters to deliver...)"
    "He scanned the deliveries he needed to make for the day."
    "One caught his eye."
    show tegami talking
    t "(Another doctor's report for Narazaki Sayaka!)"
    t "(This could be my chance to see how she's doing!)"
    t "(I'll deliver this last, so I gotta make a quick delivery for the others.)"
    scene bg door2
    show tegami tch
    t "(...And here I am.)"
    "Tegami stood in front of the door to Sayaka's house."
    "The once homely looking door now looked like a fearsome gate to him."
    t "(This is actually making me a bit nervous...)"
    "He gulped, and knocked on the door."
    show tegami talking
    t "Doctor's Report for Narazaki Sayaka!"
    t "(...)"
    show tegami tch 
    t "(Is she out? There's no response...)"
    "He waited for a few seconds, until there was finally a reply from the other side."
    s "I'm not accepting it."
    t "Eh?! Why? We're friends, right?"
    s "This isn't about whether we're friends or not."
    "Tegami's breath stopped, his eyes widened in shock."
    t "Please... Hear me out here."
    t "I'm not going until you accept it."
    s "Why?"
    t "..."
    t "(Why?)"
    "He pondered on that question"
    t "Because..."
    "He paused and collected his thoughts."
    t "Because..."
    t "Because it's important."
    s "Huh? Important?"
    t "I... I have a bit of a guess on why you don't want to accept the deliveries."
    t "But even so, this is important, not just for my job."
    s "..."
    s "Why?"
    "Tegami could hear her fist on the other side of the door."
    scene waiting
    t "This isn't about my job anymore..."
    t "It's about you."
    "To him, everything went silent in that instant."
    "In a flash, the background sound of the birds chirping, and the sound of noise in town faded away."
    t "(When did I start caring this much?)"
    t "(When did she begin to feel less like a nuisance when we were kids, to such a close friend?)"
    "He closed his eyes and took a deep breath."
    t "This is about you now."
    t "I don't know why you don't want to accept this..."
    t "But I'm just concerned for you now."
    t "If there's any reason why, you can...you can talk to me."
    t "I might be a bit stupid at times, or too loud..."
    t "But I'll listen to you, so don't keep everything to yourself, alright?"
    "Sayaka remained silent."
    "Tegami's heart felt heavy and ragged, like stone."
    "He sat and leant on the door, waiting and waiting."
    "They stayed like this for a long time."
    scene black
    play music "Music/blank.ogg"
    "Ever since that instance, Tegami and Sayaka's situation had still not improved."
    "Tegami's work schedule was loaded. He often had to deliver more than twenty letters for this week."
    "It was almost the half of the second month of summer."
    "Tegami needed to talk to Sayaka, and mend things before they worsened."
    "When he finally got a day off, he headed straight for the girl's house."
    t "(I can't believe these roads and houses that once looked so friendly and welcoming... are now so scary.)"
    t "(I wonder if I'll be shunned again?)"
    t "(When I think about these things, my mind gets all muddled up...)"
    t "(I'm not myself anymore.)"
    t "(I'm becoming the me from before.)"
    t "(But I can't let Nara-chan...)"
    t "(...turn into someone like the old me.)"
    scene bg door
    play music "Music/Piano 2.ogg"
    "As if by deja vu, he was once again in front of the simple wooden door."
    show tegami tch
    t "(It feels like the porch is gonna give, and I'm gonna fall into the ground.)"
    t "(But I can't chicken out now.)"
    "He knocked on the door, feeling as if he was knocking on Sayaka's heart."
    t "(Please open the door...)"
    play music "Music/blank.ogg"
    "The last person Tegami expected to be there opened the door and greeted him."
    hide tegami
    show fuyumi idk
    w "How can I help you?"
    "She paused, and scrutinized Tegami."
    show fuyumi idk at right
    show tegami sweatdrop at left
    t "(Does she think I'm a robber?)"
    show fuyumi wondering at right
    w "You..."
    show fuyumi smile at right
    w "You've grown so tall!"
    "She exclaimed, hugging him."
    t "..."
    "The woman noticed how confused Tegami was with the situation."
    w "Oh, I'm sorry about that!"
    w "I think you're a bit confused..."
    w "I'm Saya-chan's mom!"
    t "..."
    show tegami uh at left
    play music "Music/Merry Go.ogg"
    t "(Eh?! Aren't Nara-chan's parents in the other town?)"
    w "You've grown so tall and handsome, Tegami-kun!"
    "She admired the boy's appearance unabashedly."
    show tegami supergrin at left
    "Tegami blushed in flattery. He scratched his head and made a dopey grin."
    t "Thanks, ma'am..."
    w "Are you here to see Saya-chan? Please do come in."
    show tegami sweatdrop at left
    t "(Eh?! This would be a nice chance to see Nara-chan...)"
    t "Is that okay?"
    w "Of course! It's also rude for me to keep you out for so long."
    w "It's cozier inside, and we have some food."
    w "Please come in!"
    scene sayaka livingroom
    "She led him inside."
    show tegami sweatdrop
    t "Thank you, ma'am..."
    hide tegami
    "Tegami was still recovering from the shock of what happened earlier, particularly from how Sayaka's mother gushed all over him."
    "They went to the living room, and Tegami was once again surprised."
    "This time, there was a man seated on the couch."
    show kyouhei angry
    du "Who's that?"
    "He leered at Tegami."
    hide kyouhei
    show tegami sweatdrop at center
    t "(He's scary...)"
    show tegami sweatdrop at left
    show fuyumi idk at right
    w "Honey, don't scare him!"
    t "(...Was it that obvious?)"
    hide tegami
    show kyouhei suspicious at left
    du "Who's he? I don't think you'd let in random strangers..."
    show fuyumi smile at right
    w "Silly, he's Tegami-kun, Saya-chan's friend when she was small!"
    du "..."
    "He raised an eyebrow and analysed things in his head."
    du "Now that you mention it, he looks like that kid, only taller and older."
    t "..."
    w "See! He's so handsome now!"
    du "Well - "
    hide kyouhei
    hide fuyumi
    show sayaka uh at center
    play music "Music/blank.ogg"
    $renpy.pause(2)
    play music "Music/tamsp18.ogg"
    s "What's with all the noise?"
    "Sayaka emerged from the kitchen with a plate of cookies."
    "She spotted Tegami, and a vein slightly popped out."
    show sayaka angry
    s "Mom, what's he doing here?"
    hide sayaka
    show fuyumi smile at center
    w "I let him in! He was gonna visit you."
    "Sayaka stared at Tegami."
    hide fuyumi
    show sayaka annoyed at right
    s "Really?"
    show tegami sweatdrop at left
    t "Yep!"
    t "(Eep, she looks a bit annoyed...)"
    "He  winced internally, but kept his radiant smile in place."
    hide tegami
    show sayaka uh at center
    "Sayaka once again sighed, and set the plate of cookies down the coffee table."
    s "I'm not sure if that's enough for everyone though."
    hide sayaka
    show fuyumi wondering at center
    w "Can you please get us some water, Saya-chan?"
    hide fuyumi
    show sayaka uh at center
    s "Okay. "
    hide sayaka
    "She turned around, and went to head back to the kitchen."
    "Tegami stood up on reflex."
    show tegami talking
    t "I'll help you."
    "He headed for the kitchen as well, while Sayaka's parents talked to each other as they sat on the couch."
    scene bg kitchen
    show tegami talking at left
    t "How many cups do you need?"
    "Sayaka turned from getting the cups, shocked at his sudden arrival."
    show sayaka angry at right
    s "You scared me! What're you doing here?"
    t "I said I'd help with getting the cups. Didn't you hear me?"
    show sayaka annoyed at right
    s "...No."
    t "So, what can I carry?"
    s "I don't need your help, I can manage three glasses on my own."
    play music "Music/blank.ogg"
	$renpy.pause(2)
    play music "Music/Haze of Sense.ogg"
    "Saying those words, she felt her grip on the glass loosen."
    "She tried to grip it back again,"
    "But to no avail, it fell to the ground and shattered to small bits."
    w "What happened? Are you two alright?"
    "Sayaka's mother's voice could be heard from the living room."
    s "..."
    "Sayaka had a conflicted look on her face. She glared and bit her lip."
    scene bg kitchen
    show tegami tch
    t "(Need to think of something quick...)"
    show tegami talking
    t "Ah! Sorry, ma'am, I'm a bit clumsy and I accidentally dropped one of your glasses."
    show tegami supergrin
    t "Don't worry, nobody got hurt, and I'll pay for what I broke!"
    show tegami supergrin at left
    show sayaka uh at right
    s "Why're you saying that? I dropped it..."
    "Her voice was soft and almost unheard."
    show tegami smile at left
    t "Let's go clean that mess up."
    "He swept up the broken shards, and put them in a paper bag."
    "He filled three glasses with water, placed them on a tray and carried it out."
    show sayaka grr at right
    s "I can do that!"
    show tegami talking at left
    t "It's okay. I wanna help."
    show tegami supergrin at left
    "He beamed at her, and walked back to the living room."
    hide tegami
    show sayaka uh at center
    s "..."
    "She could hear their voices from the living room."
    t "Here's your water! I'm sorry about earlier, I'll pay for the cup I broke."
    w "It's alright, Tegami-kun, you don't have to."
    "She took the glass of water the boy put down on the table."
    du "Were you this clumsy when you were a kid?"
    t "Yes, there's even a time where..."
    "He sat down and began to tell the couple stories about his misadventures."
    s "..."
    "Sayaka was speechless at the boy's sudden attitude."
    "How did the lonely, aloof boy from before change so much?"
    show sayaka sad
    s "What am I doing..."
    play music "Music/blank.ogg"
    scene black
    $renpy.pause(2)
    play music "Music/tamsp18.ogg"
    scene sayaka livingroom
    "The rest of the day turned over quite well."
    "They ate snacks, and Tegami and Sayaka's parents chatted with each other."
    show fuyumi smile at right
    w "So are you studying at the school here too?"
    show tegami talking at left
    t "No, ma'am. I'm working as a special mail courier here."
    hide tegami
    show kyouhei smile at left
    du "I heard about that job."
    du "It has a good salary."
    hide kyouhei
    show tegami sweatdrop at left
    t "But the schedule is a bit crazy at times."
    show fuyumi wondering at right
    w "Why aren't you studying now? "
    show tegami tch at left
    t "I'm not studying now because of financial reasons."
    w "That's unfortunate... You could have excelled in school."
    show tegami sweatdrop at left
    "He chuckled, not knowing how to respond properly."
    t "Eheh... Somehow, I highly doubt that, ma'am."
    w "Hm... I just remembered..."
    show fuyumi smile at right
    w "Can you please go with Saya-chan and pick up some potatoes from the store?"
    w "It's a bit heavy, and she can't carry it all by herself."
    show tegami smile at left
    t "It's alright. Did you need it for dinner?"
    w "I'm making mashed potatoes. You two loved that when you were kids."
    t "I remember going to your house a lot to eat."
    "The woman turned to Sayaka."
    w "Saya-chan, can you go buy a bag of potatoes?"
    hide tegami
    show sayaka uh at left
    s "Sure, mom."
    hide fuyumi
    show sayaka uh at center
    "Sayaka redirected her attention to Tegami."
    s "Let's go. Mom still needs to boil these so they'll be easier to mash, so we need to get them now."
    hide sayaka
    scene bg street
    "Their walk was silent for a while."
    "The background noise seem amplified, and the silence felt so loud."
    show tegami tch
    t "(What can I say?)"
    t "(I have to break the ice... This tension is just...)"
    "Before he could speak, he was intercepted."
    hide tegami
    show sayaka smile at right
    s "I was shocked at you a while ago."
    show tegami uh at left
    t "Why?"
    s "You're a smooth talker."
    s "You've managed to win my parents over."
    s "And you sound so formal when talking to them."
    s "I don't know, it's different."
    show tegami close talking at left
    t "I guess I change around different people."
    show tegami neutral at left
    show sayaka neutral at right
    "Silence once more."
    "It was a long, long while before the tension was cut."
    show sayaka grr at right
    play music "Music/blank.ogg"
    $renpy.pause(2)
    play music "Music/Haze of Sense.ogg"
    s "Why did you do that earlier?"
    show tegami tch at left
    t "Huh?"
    s "Covering it up. I was the one who broke the glass."
    show tegami content at left
    t "I figured you didn't want your parents to know."
    show sayaka uh at right
    "Her eyes widened a fraction in shock."
    s "Why wouldn't I-"
    show tegami tch at left
    t "(This is it.)"
    t "You're sick, aren't you?"
    "For once, she didn't have a retort or rebuttal."
    s "How do you know?"
    t "From before..."
    t "When we flew that kite."
    show sayaka grr at right
    s "I told you I was just tired back then."
    t "No, not just that."
    show sayaka uh at right
    s "..."
    t "On our first meeting, you didn't want to accept what I was delivering to you..."
    t "A doctor's report."
    show sayaka grr at right
    s "You could have been a robber!"
    show tegami close talking at left
    t "We special mailmen have a generally good reputation, and we're the only ones who deliver special letters."
    show sayaka neutral
    t "I think I specifically said I was delivering you a doctor's report."
    "He delivered that statement with a strange smile, perhaps it was one not out of joy."
    "Sayaka remained silent."
    t "Why didn't you want to accept the doctor's report? You even ran away from me..."
    t "I'm not sure why..."
    "He paused, and the entire world seemed to go silent."
    show tegami tch at left
    t "But I think you were afraid of what was inside it."
    "It felt like forever before Sayaka finally spoke."
    show sayaka uh at right
    s "I didn't think you'd figure that out."
    t "Huh?"
    t "(I didn't expect that...)"
    show sayaka sad at right
    s "You're right, I was afraid of that report."
    t "Why?"
    s "Because, just like you said, I'm sick."
    show tegami uh at left
    t "You..."
    "Sayaka took a deep breath."
    s "I'm going to die."
    s "One day, I'll just lose control over my entire body."
    t "..."
    t "I won't let that happen!"
    s "Once it begins, it can't stop."
    t "There's gotta be a way to cure you!"
    t "Find out what you're sick of, then get medicine for it!"
    s "...T-Tegami..."
    t "See, let's just put that stuff aside... We can't give up!"
    s "..."
    s "No."
    s "I'm scared, but I've accepted it."
    show tegami tch at left
    t "(What should I say?)"
    t "(Should I comfort her, reassure her?)"
    "What Tegami thought and what he actually said were different, though."
    t "What are you going to do?"
    show sayaka uh at right
    "Sayaka closed her eyes, steadied herself, and reopened them."
    s "My parents want me to go back home for the meantime..."
    s "Our hometown."
    show tegami uh at left
    t "Won't the travel be hard for you?!"
    "He couldn't stop himself. He found himself losing his own composure by the second."
    t "What if you... during the trip..."
    s "If it acts up, I'll be forced to tell them."
    s "If it doesn't, I'll tell them at home."
    show tegami tch at left
    t "..."
    t "When are you leaving?"
    s "On Thursday."
    t "..."
    s "I've decided."
    s "I have to spend as much time as I can with them now."
    s "I can't close off everything."
    s "I can't let myself have regrets."
    t "(I don't know how I feel about this.)"
    t "(Am I happy for her decision, or sad about her situation...?)"
    "Tegami slowly lifted his head and looked at Sayaka."
    t "!"
    hide tegami
    show sayaka smile at center
    "She had a peaceful, resolute expression. Despite the situation, she stood firm."
    s "Thank you. I'm sorry for the other day. Thanks to that, I realized what I had to do."
    hide sayaka smile
    show tegami content at center
    t "(For now...)"
    t "(I guess this is okay.)"
    scene black
    play music "Music/blank.ogg"
	$renpy.pause(2)
    play music "Music/tamsp18.ogg"
    "The next day, after delivering the letters for the day, Tegami immediately rushed towards Sayaka's house."
    scene bg door
    "The Narazaki household was busy packing for their trip."
    "Sayaka's mother was sorting out her clothes, and keeping the clutter in the house."
    "Sayaka was the once to answer the door, and the one to usher Tegami in."
    scene sayaka livingroom
    show sayaka smile at right
    s "Hi, what brings you here?"
    show tegami supergrin at left
    t "Just visiting."
    show sayaka joking at right
    s "What timing, visiting when the house's so messy!"
    show sayaka grr at right
    s "Mom, I'm gonna go out for a bit, I need a break from this!"
    w "Alright! Come back soon, okay? You're not escaping from this."
    show sayaka smile at right
    "Sayaka rolled her eyes and laughed."
    s "Okay, okay."
    "She turned to Tegami."
    s "Let's go walk for a bit. The mess here is a bit overwhelming."
    show tegami sweatdrop at left
    "Tegami just sweatdropped at the situation, and went along with it."
    scene bg street
    "Once they went out of the house and on the road, Sayaka spoke."
    show sayaka smile at right
    s "So, you really didn't come here for any reason?"
    show tegami supergrin at left
    t "Nope, believe me."
    show sayaka joking at right
    s "I find it a bit hard to believe."
    t "Nah, you're just paranoid."
    s "Now THAT I can believe."
    show tegami sweatdrop at left
    t "So, I can see packing is hectic."
    show sayaka smile at right
    s "Absolutely."
    s "Mom's a bit of a neat-freak. She wants everything to be nice and orderly before we leave."
    s "And she has a ton of clothes. She brought five suitcases!"
    s "I don't know why she brought so much!"
    s "I mean, we're going back to our house anyway."
    show sayaka grr at right
    s "It's almost like she brought her entire wardrobe here!"
    show tegami supergrin at left
    $renpy.pause(0.3)
    show sayaka smile at right
    $renpy.pause(0.3)
    show tegami talking at left
    t "That's so like moms!"
    t "Mine is also kinda like that."
    show tegami sweatdrop at left
    t "She cleans a lot, and the furniture is moved around almost every week!"
    t "Sometimes it's hard to move in the middle of the night."
    show tegami supergrin at left
    t "You keep bumping into furnitures while getting a midnight snack."
    show sayaka happy at right
    "Sayaka joined in his laughing, and both had tears coming out of their eyes."
    "Slowly, the two stopped and relaxed."
    show sayaka smile at right
    s "That was a good laugh!"
    show tegami smile at left
    t "Feels nice to laugh about these kinds of things."
    s "Thanks for cheering me up, even if you weren't trying."
    show tegami tch at left
    t "..."
    t "(How did I cheer her up?)"
    s "It feels great to have a friend like you, always happy and energetic."
    t "(Me, always happy?)"
    t "(Now, I'm the one finding that hard to believe.)"
#img flash
    t "(I can't really say I'm always happy...)"
    show tegami content at left
    t "(Forget that. I helped her, and that's what counts.)"
    s "Let's go back to my house. I think mom would have a fit if I'm gone for too long."
    show tegami supergrin at left
    t "Ha, I can imagine that. She'd be fuming."
    show sayaka joking at right
    s "With smoke coming out of her ears, and fire behind her."
    hide tegami
    hide sayaka
    scene bg door
    $renpy.pause(1)
    scene black
    t "(I guess it's a bit funny how much I talk to myself while all of this is happening.)"
    t "(Maybe I'm starting to go crazy.)"
    play music "Music/blank.ogg"
    $renpy.pause(2)
    scene bg postoffice
    show tegami tch 
    t "(Tomorrow...)"
    t "(She's leaving tomorrow.)"
    t "(I really need to visit her today.)"
    "He looked at how much he needed to deliver for the day."
    t "(Thirteen letters... Most of these are for places near each other.)"
    t "(I gotta deliver this quick.)"
    "He ran as if his life was at stake."
    scene bg street
    play music "Music/Piano 2.ogg"
    "The trees and houses passed by like blurs as he ran for Sayaka's house."
    "The scorching heat of the sun only served to make him go faster."
    scene bg door
    "He took a sharp turn, and stopped at the porch."
    "He stopped his panting before knocking on the door three times."
    "This time, it was the father who answered the door."
    show kyouhei smile at right
    du "Hey, kid. Perfect timing."
    show tegami smile at left
    t "Hello, sir. Wha-"
    scene sayaka livingroom
    "Tegami was dragged inside."
    show kyouhei smile at right
    du "Could you help them with bringing down their things?"
    du "I would, but I gotta fix this ceiling. Looks like it'll cause a leak when it rains."
    show tegami smile at left
    t "Uh, sure, no problem."
    scene sayaka home
    "He went up the stairs, his strides big enough to cover two steps at a time."
    "Tegami saw Sayaka's mother with two suitcases."
    show tegami sweatdrop at left
    t "(Wow, Nara-chan wasn't kidding when she said her mom overpacked.)"
    show tegami talking at left
    t "Do you want some help?"
    show fuyumi smile at right
    w "Oh, it's you, Tegami-kun!"
    w "You can get one of the suitcases there, I'lll take the other one."
    w "Let's bring this down to the living room."
    "Tegami took the heavier suitcases. He waited for the woman to lift the others, and then they went down the stairs."
    scene sayaka livingroom
    "He placed the suitcase near the door, in a place that it won't obstruct anyone."
    show fuyumi idk at right
    w "Can you go and check up on Saya-chan? I think her bag's still upstairs."
    show tegami smile at left
    t "Alright."
    scene sayaka home
    show tegami talking at left
    t "Nara-chan! You there?"
    show tegami uh at left
    show sayaka joking at right
    s "Hey, it's you again!"
    show tegami sweatdrop at left
    t "Ouch, it's like you don't want me here."
    "She playfully punched him on the arm."
    s "Shut up and carry this."
    scene sayaka livingroom
    "Tegami picked up her luggage, and brought it down to the same location he did for the suitcases."
    show sayaka smile at right
    s "Thanks. "
    show sayaka joking at right
    s "And it's not like I don't want you here, I was just kidding."
    show tegami content at left
    t "I know."
    show sayaka uh at right
    s "Tomorrow, we're leaving at eight in the morning at the train station."
    t "So... You're telling me to see you off?"
    show sayaka joking at right
    s "Oh... What made you think that?"
    show tegami content at left
    t "(Something tells me she just did.)"
    t "I'll go help out your family. I'll see what's needed."
    scene black
    t "(Yesterday was a bit tiring...)"
    t "(I feel like an old man. My shoulders kinda ache.)"
    t "(Good thing I went to the office early and got my deliveries.)"
    t "(I'll go see Nara-chan and her parents off before delivering today's job.)"
    scene bg park
    play music "Music/tamsp14.ogg"
    t "(Ah, I gotta hurry!)"
    t "(It's almost eight!)"
    scene bg train
    show tegami uh 
    t "(I can see the trains!)"
    t "(Where are they?)"
    "He frantically craned his head in search of the Narazaki family."
    hide tegami
    show sayaka happy at center
    s "We're here!"
    "Sayaka's voice rang through the train station."
    hide sayaka
    t "Nara-chan!"
    "Sayaka waved to Tegami as he ran over to them."
    "The Narazaki family was standing in the waiting area."
    show fuyumi smile at right
    w "Tegami-kun, good to see you here!"
    w "Seeing us off?"
    show tegami grin at left
    t "Yep! I'm glad I made it in time."
    hide tegami
    show kyouhei smile at left
    du "Didn't expect ya to run over here, kid."
    du "Don't ya have work?"
    hide fuyumi
    hide kyouhei
    show tegami content at left
    t "I can deliver the letters later, there aren't that many today."
    t "Besides, this is more important."
    show sayaka smile at right
    s "So... Anything you're gonna say before we go?"
    t "..."
    show tegami tch at left
    t "(What did I want to say?)"
	play sound "SFX/Train.ogg"
    hide sayaka
    hide tegami
    show fuyumi smile at center
    w "There's the train."
    $renpy.pause(5.0)
    hide fuyumi
    "Sayaka's parents picked up their bags, and headed to the train."
    "Sayaka picked up her own bag, and turned to look at Tegami for the last time."
    show sayaka smile at right
    s "So, this's goodbye."
    show tegami smile at left
    t "Silly, you're coming back here, right?"
    show sayaka uh at right
    s "..."
    show tegami supergrin at left
    t "Get going, your train's gonna leave you behind!"
    t "Take care of yourself, okay?"
    show sayaka smile at right
    s "Got it."
    show tegami content at left
    t "And we'll be friends, even after this."
    s "..."
    scene cg cg sayonara
    s "You take care too, Tegami."
    "She turned and followed her parents to the train."
    t "(I guess this is it.)"
    "The two's paths separated, diverged from each other."
    t "(Take care, too, Nara-chan.)"
    scene bg traintracks
    play music "Music/blank.ogg"
    $renpy.pause(5)
    scene black
    $renpy.pause(2)
    scene bg postoffice
    mm "Hey, Tegami."
    t "Hey, what's up?"
    mm "I got a letter for you."
    t "Thanks, man."
    t "Strange, the envelope's black..."
    t "...From Narazaki Fuyumi."
    play music "Music/tamsp14.ogg"
    show credits 1
    $renpy.pause(3)
    show credits 2
    $renpy.pause(3)
    show credits 3
    $renpy.pause(3)
    show credits 4
    $renpy.pause(3)
    show credits 5
    $renpy.pause(3)
    show credits 6
    $renpy.pause(3)
    show credits 7
    $renpy.pause(5)
    play music "Music/blank.ogg"
    scene black    
    centered "To be continued?" 
    $renpy.quit()