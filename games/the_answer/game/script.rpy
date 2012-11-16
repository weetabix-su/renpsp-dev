init:
	image weet warn = "img/legalwarning.jpg"
	image weet cred = "img/portcred.jpg"
	image weet logo = "img/4lslogo.jpg"
	image weet title = "img/title.png"
    image sophie blush = "img/sophie_blush.png"
    image sophie confused = "img/sophie_confused.png"
    image sophie frown = "img/sophie_frown.png"
    image sophie happy = "img/sophie_happy.png"
    image sophie neutral = "img/sophie_neutral.png"
    image bg coffee = "img/bg_coffee.png"
    image bg room = "img/bg_room.png"
    image bg cakehappy = "img/bg_cakehappy.png"
    define narrator = Character(' ')
    define bhk_ = Character('Girl')
    define bhk = Character('Sophie')
    define mc = Character('Arthur')
label start:
    $ end_points = 0
	scene weet warn
	$renpy.pause(4)
	scene weet cred
	$renpy.pause(2)
	scene weet logo
	$renpy.pause(2)
	scene weet title
	$renpy.pause(3)
label pt1:
    scene bg room 
	"A large part of writing is about striking a balance between your personal ambitions as a writer, and the responsibilities you undertake when you choose to pursue becoming a storyteller."
	"Cater too much to the audience, and you're pandering. Likewise, if you start thinking that you can disregard their opinions and chase only what you want out of your writing,"
	"Then it's just a wank."
    play music "snd/LOLDRAMA.ogg"
	"First rule: Don't insult your audience's intelligence. A writer is only as good as how enjoyable their last book was. Nothing more, nothing less. Fuck your messages and intent; save it for later."
	"The minute you decide what is better for your readers for them, that is when you lose the point of writing. An especially egregious example: Putting the intent of characters in brackets after each line of dialogue."
	"Are you serious? Stop fucking around! What arrogance! If you can't trust your readers to be able to interpret your writing on their own, or give them the freedom to form their own opinions, this isn't for you! You have the audacity to charge for that shit?"
	"I don't even know why I'm wasting my time with this genre. Like I'll find a good game here."
	"Of course, I'm talking about Original English Visual Novels. It's shit. For how most of the makers talk about their writing in comparison to real literature, like Tolstoy, it's like staring into a sea of garbage."
	"Second rule of writing: Know your medium! A visual novel isn't a book, where do you get the bollocks to compare your hour long game to real literature! Fuck you!"
	"Next you're going to tell me that visual novels can be compared to movies, TV shows, or legitimate video games that aren't just clicking through screens! They can't, because even though all of these things involve writing, the mediums are different."
	"And don't you dare to compare your games to anything if you're going to put so little effort into them. I haven't seen a single OELVN that manages to break the 2 hour playtime mark."
	"That is the third rule of writing: If you're going to aim so low, don't hand out advice like someone who is aiming high, especially to people who are aiming high. It's like a McDonald's grill cook trying to give pointers to budding restauranteurs."
	"Even when the tips are technically sound, they're unimaginative and bland. A person like you has no right to give advice to people with higher ambitions. Clean your own house first."
	"You know, the more I browse the OELVN community, the more I wonder if any of these games even has a theme. "
	"A plot, sure. It's easy to shit out a plot. But where are the themes? Where is the development? A story can't stand without these things."
	"Without development, there is no point to reading a story, because there is no growth within the story. Without change, all a reader takes out of it is the memory of having read the story with the absence of having gained anything from it."
	"Without themes, you're screwing yourself out of your one opportunity to deliver your feelings and thoughts to the reader without coming off as a jackass. Not to mention, without themes, what is your story even about? What's the point?"
	"I can't take it anymore. Fuck it, even I could do better than this. When I try to give advice, I get shouted down. A burning thirst for vengeance arises within me."
	"Fuck you all! I'll make my own VN! ...Well, I don't know. It seems like a waste of time."
    menu:
		"Make an OELVN":
            jump pt2
        "Why bother?":
            jump fail_end
label fail_end:
	$renpy.block_rollback()
    play music "snd/blank.ogg"
    scene black 
    play sound "snd/crash.ogg"
	"THE GREATEST FAILURE IS WHEN YOU DON'T TRY AT ALL"
	play sound "snd/crash.ogg"
	"UNLESS YOU ARE REALLY SHITTY, THEN YOU SHOULDN'T TRY AT ALL"
	jump quit
label pt2:
	$renpy.block_rollback()
	play music "snd/blank.ogg"
    scene bg coffee 
	play music "snd/calm.ogg"
	"It's been three days and I'm sitting in a grungy bookstore cafe, trying to make the most of a stolen stack of 2-for-1 coffee coupons."
	"A fly buzzes overhead, stopping to land on the lightbulb on a string that passes for lighting swinging over my head. It's been swinging since I walked through the door; a sinister pendulum of Damocles."
	"This game is driving me crazy. I can write it, and already have started doing so. I can compose music for it, although shittily. I may be able to code it, because I have a knack for somehow pulling off things I do not understand. But..."
	"I can't draw to save my life. It'd be an improvement if I did the sprites and CGs in MS Paint."
	"As I am brooding, someone taps me on the shoulder. I turn my chair around to face whoever it is."
	show sophie neutral 
	"It seems to be a somewhat cute girl. But, I have no time for girls, this is about vengeance. Also, she looks kind of poor."
	bhk_ "Excuse me... you only drank one coffee, right? And, if you're going to use a coupon to get two for the price of one, I was wondering if I could, um, have the second one, please? I'm really thirsty and I don't have the money."
	"She must be poor. Only someone really down and out would go up to random strangers and ask them for coffee. No wonder she looks slightly depressed and worn out."
	"I'm about to tell her to get a job and look at her disdainfully as I let out a bourgeoisie laugh,"
	"But then I notice she is holding a sketchbook. I can feel my heart beating quickly and my blood pounding in my temples, like when they do drugs in Fear and Loathing in Las Vegas."
	mc "Are you an artist?"
	show sophie blush 
	bhk_ "Um... A little. I mean, I draw things sometimes, but I'm not like a professional, or anything."
	"Leaping to my feet, I almost slip on a napkin but manage to right myself at the last second and stare into her cold, dull, lifeless eyes."
	mc "This must be fate! How would you like to be the artist for a visual novel I'm working on?"
	"As soon as I say it I put my hand in front of my face to guard myself from the possibility of being sprayed with mace, but it never comes."
	show sophie confused 
	bhk_ "What's a visual novel?"
	mc "A visual novel is a game that consists mainly of reading text and looking at images, occasionally making a choice between multiple options that may or may not contribute towards changing the plot of the game somehow."
	mc "The object of the gameplay is to experience the story told within, or all stories if there are multiple plot threads. Either that, or to enable viewings of hentai scenes depicting the protagonist having sexual intercourse with one of the girls."
	mc "Basically, they are about getting laid through an anime surrogate. That is why the main character never has eyes."
	show sophie neutral 
    bhk_ "Okay. I guess I'll do it, because I am really thirsty."
	"I grab her by her hands and almost jump up in the air."
	mc "Yes! Damn, what ambition! I can feel the flames of passion burning in me like a lingering ulcer. I'm impressed with your drive. That hunger, that is what young people today lack; that will to excel, that thirst for greatness."
	show sophie confused 
	bhk_ "No, I'm thirsty. I just want some coffee."
	"I see she is eyeing the stack of coupons even now, interrupting my melodrama, and put them in my pocket."
	show sophie frown 
    bhk_ "Noooo...."
	mc "Shut up, this has long passed the point of coffee. Anyway, I am very happy about this. This is awesome."
	mc "My name is Arthur. Arthur Proxy."
	show sophie neutral 
    bhk_ "Okay. I'm Sophie Butthurtko."
	mc "Sophie? That is a nice name. It is like a delicate flower standing alone and out of place in the contrast of the vast, burning fields of hatred and petty vengeance that rage through my soul like brush fires in California."
	mc "The hatred upon which this game was found. The monster born when the torch of my justice was extinguished, the flame of truth expunged by the blind darkness of ignorance and faggotry."
	show sophie happy 
    bhk "Uh... okay? Ahaha~?"
	play music "snd/blank.ogg"
	"Her laugh reminds me of Kanon. I projectile vomit onto her shoes."
	show sophie confused 
    "It's okay to employ gimmicks like idiosyncratic speech patterns if you can pull it off, but it's just disgusting when they're almost the only thing defining the character."
	mc "Damn, how awkward."
	mc "I hope this doesn't change anything."
	show sophie frown 
    "She looks at her shoes and makes the same face my mom did when I told her I wanted to be an air conditioner repairman."
	bhk "Not... really..."
	mc "Okay. Ballin'."
	jump pt3
label pt3:
	scene bg room 
    play music "snd/calm.ogg"
	mc "Goddammit, Sophie, I require updates. How am I supposed to know how much progress the game is making if I have no idea what the hell you are doing?"
	"I leave out the fact that I have no idea what I'm doing either."
	mc "Ughhh... this is like the blind leading the blind... one hand not knowing what the other is doing... or... some other analogy..."
	show sophie frown 
    bhk "I don't understand why you're so upset about this. I'm sorry."
	mc "First rule of making a VN: If you don't have good synergy between all your departments, you're going to fucking fail."
	mc "Visual novels are called that for a reason. The art is always going to be the bigger draw than the writing, unless your writing is so good it gets word of mouth going. But, basically, your art is going to be the hook for 90%% of people."
	mc "I stopped playing The Question as soon as the first sprite appeared onscreen. Even though they updated the sprites recently, the memory of the horror that was those sprites still burns in my mind's eye..."
	mc "That's why I'm depending on you. I need you."
	show sophie blush 
    "Sophie blushes and starts fidgeting, tapping her toes together nervously."
	bhk "Um..."
	mc "Shut up!"
	play music "snd/blank.ogg"
	menu:
        "Structure of visual novels":
            $ end_points = end_points+1
			jump structure
        "Nature of visual novels":
            $ end_points = end_points+2
            jump nature
label structure:
	$renpy.block_rollback()
	"Well, at least progress on the art front is happening. Still, I dread the directing phase."
	show sophie neutral 
    bhk "Um... how done is the game right now?"
	mc "Hard to say. I can tell you that writing is almost complete. I guess you're halfway done with the art. Backgrounds aren't done, neither is music. And directing..."
	mc "Basically, no fucking clue."
	mc "I'm afraid of the technical side of the VN."
	show sophie confused 
    bhk "Huh?"
	play music "snd/LOLDRAMA.ogg"
	mc "Structure! The presentation! The presentation is one of the things that makes a VN what it is! The choices!"
    mc "There are kinetic VNs which don't offer the player any say in the direction of the plot; those primarily exist solely to tell the story. But, I have always considered that cheap, unless you have a great story to tell!"
	mc "Narcissu, for instance, was a kinetic novel, but it worked very well. The music fit the mood, the game was short, and the story it aimed to tell was simple and from the heart. No preaching, but a solid theme of life."
	mc "Life and death! In a kinetic VN, you have to truly capture your reader's emotions, because you're denying them a choice; what they want. Therefore, you can't afford to fuck around, and you likewise have to throw away what you want and pursue only the plot!"
	mc "Your narrative must be tight, because there is nothing stopping you from making it so. When you offer the reader choices, you have to account for each individual choice. Is it relevant? How will you work it into the gameplay? What will it contribute to?"
	"I make some exaggerated hand gestures to get my point across better in the way only exaggerated hand gestures can."
	mc "That shit isn't easy! Don't fuck around!"
	show sophie frown 
	bhk "Okay."
	mc "Of course, all this won't play a factor until you FINISH THE ART."
	show sophie confused 
    bhk "The other stuff... um... it sounds important, too..."
	mc "Yes, but this is a visual novel. Visual. Everything rides on it. Everything. The point is your art is great. It fits the mood of the game perfectly. And I need art. And you work for food."
	show sophie frown 
    bhk "I'm hungry."
	mc "I know. I too am hungry. Hungry for the glory of vengeance, even though I know glory fades. Hungry for a higher standard, even though I know I walk a dark path, making a game about making a game about making a game about... fuck this."
	"Sophie opens her mouth as if to say something, but instead just looks away. I think she clearly does not understand anything."
	mc "Basically, art has to be good. And by good, I mean not just in artistic quality, proportions, and style, but it has to be eye-catchingly interesting and distinct. Gotta think carefully about design, even in eroge, not just about tits and asses."
	show sophie confused 
    bhk "Uh... okay."
	mc "And although the style of all the art in this game must be consistent, don't copy it for future works. Sticking with one style too long makes an artist's skills degrade, as they're not getting practice with a variety of subjects."
	mc "Same shitty moe moe teenage girls with similar body types being drawn in the same poses, same positions... no wonder their talent goes to hell and becomes bland and generic. They lose the fire of new experiences!"
	show sophie neutral 
    bhk "Is it like, in VNs, the art has to get the emotions of the characters and their personalities across, but at the same time, it has to fit the mood of the writing right? And... the setting?"
	mc "Yes, that's exactly right."
	play music "snd/blank.ogg"
	bhk "Okay. Does that mean I should stop making everyone wear pink?"
	mc "No, it's fine. It's fine! Pink is close to red, which fits the character perfectly."
	bhk "What is this character about? Like, what does he feel and stuff?"
	mc "Revenge."
	show sophie confused 
    bhk "Um... what about him?"
	mc "Revenge."
	"..."
	show sophie frown 
    bhk "Okay..."
	jump pt4
label nature:
	$renpy.block_rollback()
	"Visual novels are actually kind of interesting."
	show sophie neutral
	bhk "Really?"
	play music "snd/LOLDRAMA.ogg"
	mc "Yes. Visual novels use a combination of writing with music and art to give life to otherwise lackluster plots or unexceptional writing."
	mc "Think about it. Tsukihime at times reads like bad fanfiction, if it were a real book, the standards would be higher. Tsukihime is able to make up for shortcomings with visuals and sound."
	mc "That's why it's foolishness to compare visual novels to things outside of the visual novel medium! Do you know of any books that have branches outside of Choose Your Own Adventure?!"
	mc "What books have a full soundtrack and character sprites? Can a VN be compared the dynamic energy and full motion of movies? The paneling of comics? Animation? Nigga please!"
	mc "A VN's presentation is totally different from everything else! Don't fuck around! Admit the strengths and weaknesses of visual novels, or you're just being delusional!"
	mc "Phantom of Inferno had great cinematic style in its storytelling, but in what movie would you be able to get away with a 20 minute long scene about learning to drive? In a movie, 20 minutes is an eternity!"
	mc "Ever17 was great because it used the presentation of the narrative and the design of visual novels to great effect. Some of the twists were made for VNs."
	mc "Don't be a dumbass! VN music is rarely anything special. VN art is rarely anything more than generic. VN writing by itself is usually shit compared to writing in any other medium. Alone these things are worthless!"
	"I make some exaggerated hand gestures to get my point across better in the way only exaggerated hand gestures can."
	mc "It's only through combining that they can become something more. You must never forget that. That is why it's important to know the medium, and to ensure all aspects of the game work well together."
	show sophie confused 
    bhk "Oh... I see. Every part is so equally important..."
	mc "Yes!"
	show sophie blush 
    bhk "I don't really know much about writing."
	mc "Well, first off, you have to keep a tight narrative. A good example of this is Crescendo. The entire game takes place over five days, and still manages to tell a story. Best part... no timeskips."
	mc "The shittiest thing you can do, the biggest hack trick of all hack tricks, is using a timeskip to cover for real character development."
	mc "If the game is too short to allow for anything else, why go for that ending at all? If you can't pull off the ending you want, do the ending that will do justice to your story, justice to your reader. Better to do something simply and well than shitty."
	mc "Having an outline of what you want to do is important, and will save you a lot of heartbreak and regret. Post-production is to shine what could be better, and you can't forget that it's impossible to get everything right the first time."
	mc "Oh yeah, style. Style is important, because if the style is incongruent with the events, character, and emotions going on in the story, it will come off as incredibly shitty."
	mc "A good exercise is to attempt to write from the perspectives of many different people, like an old man, a young girl, a retard, a blind man, a poor person, a rich person, a prisoner, whatever..."
	mc "Otherwise, the first thing you write is just going to be what you know, and that is always less than you think!"
	bhk "Oh..."
	mc "Another thing! Don't ever bring up something once if you don't plan to follow up! And don't realize this in hindsight, Hindsight is gay! Get it right the first time!"
	mc "Of course, I'm guilty of a lot of this myself, but the point is you should get called out on whether or not your shit sucks. Then you go through the usual bawwwing, but then there's catharsis. You acknowledge your shit sucks. Then, you grow."
	bhk "...But, wait, you said that there is always more to edit... but, hindsight is---"
	mc "Shut up! I know, but just because there is always more to edit doesn't mean you can half ass it and clean up your mess in PP. If you aren't good enough to be careful the first time, you will be in post-production forever."
	show sophie neutral 
    bhk "That sounds like a good thing. Um... It's creepy if people concern themselves more with being nice than improving...?"
	mc "Depends. It's a hard call to make. Do you stick with shit and stagnate to keep up a happy appearance, or do you offer constructive criticism and let those who will learn from it... learn from it? ...Come on!"
	mc "Look, let's say it's you. Would you rather be shit, but have a bunch of yes men tell you you're the shit, so that when you go outside of your hugbox community you get, rightfully, fucking wrecked,"
	mc "Or would you rather have honesty so you can improve and have something that is, in the end, worthy of your prick pride? The choice is obvious."
	mc "Anyway, I can't forget the cardinal rule of writing: Entertaining the reader over choosing to indulge your whims and wishes as the writer. Once you lose that, you've lost the plot, you lose everything. That is the lonely road I follow."
	mc "Just like the bitter jerks before me, like James Joyce or Franz Kafka; great men who wrote for the sake of mocking author hubris and laughed at any and all presumptions of greater depth. That is me, only I'm not as talented."
	show sophie confused 
    "Sophie's shoulders sag slightly."
	bhk "You're not?"
	mc "No."
	show sophie frown 
    bhk "Awww..."
	mc "I can't eschew themes to troll lit. professors decades after my death like they did. I have themes. Themes of vengeance."
	bhk "Revenge is... not a good thing."
	mc "Yes, it is. Remember 'The Cat In The Hat?' That cat was an asshole. How would you feel if a bipedal cat with a striped hat came into your house and started breaking things, fucking everything up, and all that?"
	show sophie neutral 
    bhk "I think I would be scared."
	mc "Maybe you would... I would desire revenge. Revenge against the bipedal cat that is destroying my life."
	mc "Sure, after I got my revenge I would ask questions. Who created this superintelligent cat with opposable thumbs? How many more of them are there? What was his goal? Is he merely an agent of chaos, or was it something more sinister?"
	mc "How did the cat have so many resources? What were Thing 1 and Thing 2? Slaves? Were they human, or also artificial lifeforms like the cat? Was the cat an artificial lifeform or some sort of mutant?"
	mc "Could it have even been some elder god of cats, poking a slimy tentacle into our dimension, perceived as a striped hat-wearing cat only because the fragile prepubescent human mind could not comprehend the terror of it's true visage?"
	"H.P. Lovecraft was a decent author who fell into the trap of becoming formulaic. Once you fall into that routine, it's over, and that holds true across all mediums. Aoi Nishimata was a great artist; years of eroge have reduced her to a stale one."
	play music "snd/blank.ogg"
	"That is another cardinal rule: It's always more important to think about what people before you have done wrong rather than to dream about what you plan to do right. Learning from the mistakes of the past is one of the oldest lessons in the book."
	show sophie confused 
    bhk "Uh..."
	mc "Are you still here? Go home!"
	jump pt4
label pt4:
	$renpy.block_rollback()
	scene bg room 
    play music "snd/calm.ogg"
	"Directing phase has begun."
	"Unfortunately, I don't really understand how to direct."
	show sophie neutral 
    bhk "So, what is directing?"
	mc "Leave me alone. I'll answer your question when I'm not brooding on my failure."
	"A silence fills the room, lit up only by the vaguely sickening glow of the computer monitor. Cold and desolate, like the surface of that pudding I found in the fridge the other night. Remembering this, I take two digestive meds just in case."
	show sophie frown 
    bhk "...Okay. When will you be not-brooding?"
	"She chews the end of a pencil thoughtfully and I briefly wonder if it's one of mine, because if so it's contaminated now and I'll have to charge her about fourteen cents so I can replace it."
	mc "I guess now."
	mc "Directing is when you take everything; your art, my writing, and then music, backgrounds, all that other shit, and then combine it through the power of coding into the actual game. It's when you bring it to life."
	mc "It's a pretty important job. You can be really creative with it unless you're a stupid, boring plonker."
	mc "I guess it's like, making a game is like... buying crap from Ikea. You buy something and those bastard ass Swedes just give you the parts. The parts are elements of the game. The director is the allen wrench you need to put everything together."
	show sophie neutral 
    bhk "Huh... I like Ikea, their furniture is futuristic and efficient at the same time."
	"Seems like she understands the analogy."
	"Inspiration! Like a flash of lightning. Talking about directing has gotten me fired up about it."
	mc "I got it,"
	mc "Lines like 'she smiles' or 'I notice she looks sad' shouldn't be used unless they also add something key to that scene. Why be redundant? If you want to show what a character is feeling, isn't that what sprites are for?"
	mc "The effect is more polished; more subtle. It will even bring the reader closer into the story, because the feel is more intimate. In fact, to not do it would be almost disregarding the hard work of your artists!"
	show sophie blush 
    bhk "Um..."
	bhk "I'm.... really happy you think about what I do like that. I mean... I think it's nice. I didn't know that you---"
	mc "Shut up! You're distracting me!"
	show sophie frown 
    play music "snd/clackclack.ogg"
	"Clackclackclackclackclackclackclackclack" "Clackclackclackclackclackclackclackclack" "Clackclackclackclackclackclackclackclack"
	play music "snd/calm.ogg"
	"I'm almost proud of myself until I try to play through what I've just directed and the game immediately freezes a couple of lines in."
	mc "What the hell?"
	mc "Fffffffffffffffffffffffffffffffffffffffffff..."
	"Rule No. 1: Don't be a ponce. Play through what you have directed or what was directed so that you don't end up creating a bug. Work doesn't end at completion, you have to stand back and look at it again to make sure what you did makes sense."
	show sophie confused 
    bhk "Ah... Are you okay?"
	mc "No. Can't you see I'm brooding?"
	show sophie frown 
    bhk "Um..."
	mc "What do you want?"
	"I can't really see her properly with my head on the desk like this. She tries to stand in front of me and tilts her body to the side so that she looks upright in my eyes."
	show sophie blush 
    bhk "Can I try directing?"
	play music "snd/blank.ogg"
	menu:
        "Let Sophie do it":
            $ end_points = end_points+2
            jump direct_sophie
        "lol no":
            jump direct_alone
label direct_sophie:
	$renpy.block_rollback()
    "I'm surprised."
    mc "What? Why? You want to direct?"
    play music "snd/TOUHOU.ogg"
    show sophie neutral 
	bhk "Yup."
    mc "Okay. Why?"
    bhk "I just want to try it."
    mc "Okay..."
    "I get out of the chair and hold it for her."
    "She pokes around the engine, but once she gets started directing, I have to admit she has a knack for it. Kind of disturbing. Her fingers fly across the keyboard. It is almost like she knows what she is doing. ...Does she?"
    mc "Wow, you're actually pretty good at this..."
    show sophie happy 
	bhk "Um... thank you. This is the first time you have said I was good at---"
    mc "Yeah, whatever. Have you done this before?"
    show sophie frown 
	bhk "No."
	mc "Well, you are good at it."
    mc "In an ideal world, all writers would be able to direct their own shit. Unfortunately, this is not always the case. In that case, you have to know what you want, and all of that has to be communicated to the director if you want your intent to come across clearly."
    show sophie neutral 
	bhk "Uh huh... Okay, so what do you want me to do?"
    mc "I don't really care."
	play music "snd/blank.ogg"
	show sophie confused 
    bhk "Huh?"
    show sophie frown 
    bhk "Okay. I guess you want... revenge. So... I will make everyone angry all the time."
    bhk "Um, why did I draw all those sprites if I'm just going to use... the angry sprite?"
    mc "We can discuss this later."
    jump ending
label direct_alone:
	$renpy.block_rollback()
    "Get real!"
    show sophie blush 
	bhk "Can I...?"
    "I pat her on the back in a casual and reassuring but still distant and semi-professional manner. It's a gesture I've perfected through years of fearing a sexual harassment lawsuit."
    mc "Hahaha..."
    mc "NO!"
    show sophie frown 
    play music "snd/clackclack.ogg"
	"clackclackclackclackclackclackclackclackclackclack" "clackclackclackclackclackclackclackclackclackclack"
	play music "snd/blank.ogg"
    jump ending
label ending:
    scene bg room 
    if end_points > 3:
        jump ending_good
    else:
        jump ending_bad
label ending_good:
	$renpy.block_rollback()
    "The game is finally done."
    play music "snd/TOUHOU.ogg"
    show sophie happy 
    bhk "Yay!"
    mc "Ugh..."
    show sophie confused 
    bhk "Huh? What's wrong? Aren't you happy?"
    mc "Well, I guess I am... slightly less angry."
    show sophie happy 
    bhk "Yay!"
    "I try to grimace as hard as possible without pulling a muscle in my face or something, but she doesn't get the message."
    mc "Just because it's done means nothing. Other than that it's done."
    bhk "But that's still a very good thing... We should do something to celebrate."
    "Celebrate? What are you talking about? It's not like we put a man on the moon. Don't be a retard! There is no cause for celebration; you made a VN, and that doesn't mean shit to anyone but you! ...But I guess it's alright, if it's just between us."
    show sophie neutral 
    mc "Well, I guess we can bake a cake to celebrate. You are going to have to help me, though"
    show sophie happy 
    bhk "I like cakes."
    "Sophie claps her hands together."
    mc "Get a grip! Just for that, we're going to make a cake you don't enjoy. I'm going to assume since you're an artist and not wearing a beret, you do not like the French. Therefore we are going to make a napoleon."
    show sophie confused 
    bhk "I like Napoleon..."
    mc "Fine, then we are making a black forest cake."
    show sophie frown 
    bhk "But it'll make me fat."
    mc "Shut up!"
    "I put on my tall Chef Boyardee hat and grab a big wooden spoon."
    scene bg cakehappy 
    mc "Where's the salt? You need to add a little salt into your cake ingredients. Salt enhances our ability to taste through stimulation of more taste buds. You need that subtle contrast to make the sweetness really come out."
    mc "Try to bake a cake without salt. Shit sucks! Gotta use iodized salt; the miniscule amounts of salt needed for a cake mean that any higher quality salt is wasted on it, and you might as well get some iodine, as cakes have little nutritional value."
    bhk "Here you go. Um, I was thinking... I kind of like... how you tell people how to do things all the time, and I think that maybe you really do care, and---"
    mc "We'll talk after cake. I need two eggs. Crack them into a separate bowl first, that way if one is bad it won't contaminate the other ingredients, and you'll be able to pick out fragments of eggshell more easily."
    bhk "Okay. But after, can you please listen to me more?"
    "I want to tell her I just want those eggs, but she is apparently very good at multitasking and cracking eggs, deftly breaking open the shells with one hand and dropping them into a small bowl. Can't complain."
	play music "snd/blank.ogg"
    mc "..."
    mc "Ffffffffffffffffff..."
    mc "Fine."
	jump quit
label ending_bad:
	$renpy.block_rollback()
    "The game is done. I start playing through it to see if it's any good."
    "..."
    show sophie happy 
    bhk "I think it's nice."
    mc "No! It sucks!"
    show sophie neutral 
    play music "snd/LOLDRAMA.ogg"
    mc "We're redoing everything!"
    mc "Do you see how the things that were completed in the beginning, in both script and art, look different from that which was completed later?"
    mc "It's because your art and my writing evolved during the creation of the game! Now, looking back at it, not only is the first part inconsistent with the second stylistically, but it sucks!"
    mc "We're redoing everything!"
	play music "snd/blank.ogg"
    show sophie frown 
    bhk "Aw..."
    mc "Don't worry, if we're together, we can accomplish it!"
    show sophie confused 
    bhk "..."
    show sophie blush 
    bhk "Um... I... Really? I... I'm getting a lot of mixed messages..."
	mc "Shut up!"
	jump quit
label quit:
	$renpy.quit()