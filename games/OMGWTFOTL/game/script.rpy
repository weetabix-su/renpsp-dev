init:
	#backgrounds
	image weet cred = "img/portcred.jpg"
	image weet title = "img/title.jpg"
	image bg 1-3 = "img/1-3.jpg"
	image bg 2-2 = "img/2-2.jpg"
	image bg 4-2 = "img/4-2.jpg"
	image bg dogeza = "img/dogeza.jpg"
	image bg ex1 = "img/ex1.jpg"
	image bg ex2 = "img/ex2.jpg"
	image bg ex3 = "img/ex3.jpg"
	image bg gocchi = "img/gocchi.jpg"
	image bg gocchi_eye = "img/gocchi_eye.jpg"
	image bg gocchi_to_p = "img/gocchi_to_p.jpg"
	image bg gocchi2 = "img/gocchi2.jpg"
	image bg karasu = "img/karasu.jpg"
	image bg mount_p = "img/mount_p.jpg"
	image bg nihontou = "img/nihontou.jpg"
	image bg taoreyukana = "img/taoreyukana.jpg"
	image bg tukkomi = "img/tukkomi.jpg"
	image bg yukana = "img/yukana.jpg"
	image bg yuuhi = "img/yuuhi.jpg"
	#chardecs
	define p = Character('Player')
	define os = Character('Osaka Bancho')
	define kn = Character('Kanagawa Bancho')
	define sm = Character('Sommelier Bancho')
	define tu = Character('Tsukkomi Bancho')
	define bo = Character('Boke Bancho')
	define go = Character('Master Gotch')
	define yu = Character('Yukana')
	define cp = Character('Captain')
label start:
	"WARNING: OMGWTFOTL may contain adult content. Proceed at your own risk"
	scene weet cred
	$renpy.pause(2)
label title:
	play music "snd/dogeza.ogg"
	scene weet title
	"Scripting: HANPANMANIA-SOFT" "Scenario: Ryouichi Fucking Watanabe" "Translation: Nanatuha, with supervision of Seung 'gp32' Park" "With Participation of al|together 2006 Staff"
	menu:
		"BEGIN":
			jump tomo
		"GENUFLECT":
			jump inu
		"RUN AWAY":
			jump kill
label a:
	play music "snd/dogeza.ogg"
	jump tomo
label tomo:
	scene bg 1-3
	os "You so eager to buy the goddamn farm, suckah?  If not, genuflect RIGHT NOW!"
	"Osaka Bancho wasn't messing around. At this rate, I could tell that I was seriously gonna be pushing up daisies before long."
	menu:
		"Genuflect":
			jump inu
		"Don't genuflect":
			jump neko
label inu:
	scene bg dogeza
	"It was total humiliation to be genuflecting before the man who had raped my little sister and scooped out my best friend's eyes."
	"But I didn't want to die. While there is life, there is hope.  My precious life is irreplaceable."
	"So I plastered an obsequious smile on my face and meekly got down on my hands and knees."
	os "YA FUCKIN' LOSER! NO MAN WOULD BOW DOWN SO EASILY!" "Die like the dog you are!"
	"Osaka Bancho then lifted one of his legs, and sent it hurtling toward my prostrated head."
	"Its heel sank into the back of my head with a disgusting crunch."
	"My head cracked open like a pomegranate and fresh blood splattered everywhere ..."
	"And I died."
	jump f
label neko:
	scene bg 2-2
	p "As if!"
	p "You pathetic snot, don't you know that a REAL man never gives up?! So shut your trap and bring it on, suckah!"
	"Osaka Bancho stared at me as if I were a specimen under glass."
	os "If THAT'S yer idea of a real man, then I'll CRUSH YOU LIKE AN INSECT!"
	os "Go ahead and try, fool!"
	p "Gladly, dawg!"
	"Osaka Bancho's diamond headbutt exploded against my nose."
	"And my entire skull reverberated with the echoes of the hideous crunching sound."
	"Crimson blood spattered everywhere."
	p "Aaaaaggggghhhh!"
	scene bg 4-2
	"Goddamn it, I was screwed."
	"It was totally hopeless.  Here I was fighting with all my strength, and Bancho was still just warming up."
	"I mean, sure, my manhood was damn important, but guess what?  My life was even more goddamn important."
	"It wasn't too late. Maybe if I genuflected now ...?"
	"After all, if you define death as the ultimate defeat, genuflecting could be seen as a net win, in some ways."
	"That's right! Gotta look on the bright side of life ... errr ... death."
	menu:
		"Genuflect":
			jump inu
		"Don't genuflect":
			jump b
label b:
	scene bg 2-2
	"Who the fuck would genuflect at this late hour?!"
	"AND WHAT THE FUCK DOES GENUFLECT MEAN ANYWAY?!"
	p "What was that, a tickle?! If yer gonna kill me, do it right, ya fuckin' pansy!"
	"I roared as blood dripped from my nose."
	"A man with nothing to lose is the most dangerous man on Earth. Right! My fatal fury was like that of a hungry wolf now!"
	"And this stooge right here ... was nothing but prey."
	"Kill him? Fuck that. When I was done with him, there'd be nothing left but bones, man, BONES!"
	os "Yer nothin' but a barrel of laughs, aintcha?  Sure, then, fine ..."
	p "What the FUCK is that supposed to mean?!"
	"I glared daggers at him, just like in one of those gangster movies you see on TV."
	os "... I'll grant yer wish FOR DEATH."
	"And with that, Osaka Bancho's diamond fist hammered into my face."
	"My sight darkened, and my nose and mouth filled with blood. I couldn't breathe anymore."
	scene bg 4-2
	"Goddamn it, I was TOTALLY screwed."
	"No amount of guts were gonna make up for the total difference in EVERYTHING between Osaka Bancho and me."
	"On top of that, Osaka Bancho wanted to kill me, and to make matters worse, I wanted to die."
	menu:
		"Genuflect":
			jump inu
		"Don't genuflect":
			jump c
		"Beg Karl Gotch for help":
			jump x
label c:
	"I spit all the blood in my mouth out at Osaka Bancho."
	os "FUCK! MY EYES! I can't see anything!"
	"Osaka Bancho staggered and writhed like a wrestler who had just been hit with The Great Kabuki's mysterious poison mist attack."
	p "I'VE GOT YOU NOW!"
	"I screamed as I tackled him head-on."
	os "FUCK! I'm blind! You dirty bastard!"
	"By the time my blood rage subsided, I'd somehow managed to sit astride his helpless body."
	scene bg mount_p
	"And from there, I pounded him with all my might -- punch after punch after punch."
	os "FUCK!"
	os "What the HELL is it with this avalanche of punches?!" "It hurts! It hurts!"
	p "Then genuflect!"
	os "WTF?! Why the HELL do I have to genuflect?!"
	menu:
		"Make him genuflect":
			jump d
		"Don't make him genuflect":
			jump e
		"Make myself genuflect":
			jump inu
label d:
	scene bg mount_p
	p "Then genuflect RIGHT NOW! And taste the feeling of your pride being torn apart!"
	os "Okay, sir, anything you say! But please get off me, or I won't even be able to genuflect."
	"So I said 'Very well'"
	"and then I stood up and got off him."
	scene bg 1-3
	os "YOU'RE GOIN' DOWN, SUCKAH!"
	p "What?!"
	"Osaka Bancho whipped a pistol out of his jacket, just like he were James Bond or something."
	os "What, didja REALLY expect me to genuflect like a sorry sonuvabitch?! Now KNEEL AND PERISH!"
	"Well, I lost." "Nothing I could do about it now." "It was almost thrilling to be defeated so thoroughly, and for some reason everything seemed to be so funny."
	p "Sure, fine, I'll genuflect."
	"But I found it so funny to be kneeling and saying, 'I beg your pardon, please, sir,' that I burst out laughing instead."
	"I felt a rush of total euphoria."
	"Osaka Bancho pressed the muzzle of his gun against my temple and said,"
	os "Now say it loud and clear, dawg!"
	"And then I screamed,"
	p "YOU'RE THE ONE WHO'S GOIN' DOWN, SUCKAH!"
	os "WTF?!"
	scene black
	"And that was the last thing I heard."
	"I died."
	jump h
label e:
	"No, the time to be making him genuflect was over. Time to kill him and devour him instead!"
	"And so I kept hitting him over and over until his breathing stopped."
	"Osaka Bancho died in short order."
	"Anyway, I got so into it that I burst out laughing as I beat him into a pulp, and then I realized that I was getting really hungry.  Which was why, as I waxed poetic about the depth of the Bay of Toyama, I ate him. For real."
	"He was yummy. For real."
	"And after that, I couldn't hold it all in and I ended up kinda taking a dump in my pants during class. That was all yesterday."
	"Oh, right, the day before yesterday, all of us with the Kanto Alliance went skating, and it was there that we found out that Kanagawa Bancho didn't know how to tie his shoes. We all laughed at him like crazy."
	"So instead of skating, we started examining what Kanagawa Bancho could and couldn't do."
	"We burst out laughing again when we found out that he didn't know what the difference between cabbage and lettuce was, and we also found out that he was somehow waaaaay slower than everyone else when he took the escalator."
	"And we burst out laughing yet again when we handed him a Pepsi and convinced him that it was a Coke, not a Pepsi."
	"Finally, on our way back, when Kanagawa Bancho tried to be a know-it-all and told us 'dudes, if you make sure that even your asshole is suntanned, you'll never get sick', we all died laughing."
	jump j
label f:
	play music "snd/gameovew.ogg"
#	weetabix note: THIS SHOULD BE PLAYED ONCE!
	menu:
		"Get a clue":
			jump g
		"No time for that shit":
			jump a
label g:
	scene bg 1-3
	os "Kennedy died of starvation, suckah!"
	os "Yeah, that's right, homey g dawg, if I hadn't eaten all the steaks in Dallas that shit might never have gone down."
	os "My bad, my bad, yo!"
	os "Anyway, dawg, Osaka Bancho here. You little fool, don'tcha see that ya can't just genuflect to yer enemy like that? DEATH TO ALL COWARDS!"
	os "Got it, homes? THEN GO TRY AGAIN!"
	jump title
label h:
	play music "snd/gameovew.ogg"
#	weetabix note: THIS SHOULD BE PLAYED ONCE!
	menu:
		"Get a clue":
			jump i
		"No time for that shit":
			jump a
label i:
	scene bg 1-3
	os "Apartheid is an evil institution, homey g! Even the manager of Lucky Kitchen agrees with me!"
	os "Anyway, dawg, Osaka Bancho here. Listen, and listen good, 'cause you slacked off in the middle of a fight you were winning" "and that's why you totally fucked up, suckah!"
	os "There's only one rule around here: kill or be killed."
	os "Got it, suckah?! Then go start over! If you don't get it, then DIE. I'll come after you even in yer DREAMS. And you'll have MANLY NIGHTMARES FOREVER."
	jump title
label j:
	play music "snd/blank.ogg"
	menu:
		"Hear Kanagawa Bancho out":
			jump k
		"No time for that shit":
			jump a
label k:
	scene bg karasu
	kn "Yo, surf's up! Kanagawa Bancho here, dude. From here on out nothing has anything to do with the main story. Totally tubular, don'tcha think?"
	kn "Anyway, my pride and joy is in spinning yarns about perverted make-believe scenarios."
	kn "Hey, yo, don't look at me like that! I've got TONS of experience with women, my man, TONS (all as a really inept subway molester, but let's not get into that)! Whaddaya say?  Might be fun, after all, let's SHRED!"
	menu:
		"Argumentative childhood friend":
			jump l
		"Eroge King's beast fetish":
			jump m
		"Genuflect":
			jump inu
		"Roll staff credits":
			jump n
label n:
	$renpy.pause(0.2)
	play music "snd/end2.ogg"
#	weetabix note: THIS SHOULD BE PLAYED ONCE!
	"Scenario      : When I." "Illustration  : Tried to tan." "Music         : Only my balls." "Script        : At the beach." "Chores        : Gordon Freeman was eaten alive by a headcrab."
	"Eroge King    : Masao Takemoto"
	scene black
	play music "snd/blank.ogg"
	$renpy.pause(0.7)
	jump title
label l:
	play music "snd/blank.ogg"
	scene bg yukana
	"Dramatis personae:"
	"Me:" "a cheerful high school junior."
	"Yukana Aihara:" "a cute high school freshman. My childhood friend. She gets really pissed when anyone talks about her flat chest."
	"The setting: Tomorrow is our school festival. Now, Yukana belongs to the Art Club, but their preparations aren't complete yet."
	"Actually, Yukana is the only one working on the preparations at all; everyone else is either sick or playing hooky. Which means that somehow, I got roped into helping her ..."
	play music "snd/nichijyou.ogg"
	yu "Hmm."
	"Yukana is busy putting up decorations, perched on tip-toes high atop a stepladder."
	"To be more exact, right now she's trying to mount an oil painting on an unreasonably high location."
	"And her stance is really, really precarious."
	"I mean, I even told her I'd do it for her, but she flat-out refused, saying that this painting was really important to her."
	"It's a piece of abstract art, and I REALLY DON'T GET WHAT IT'S SUPPOSED TO MEAN. The only thing I can say for sure is that it's a depiction of this vaguely humanoid figure in yellow and white in the middle of campus."
	"I'll admit that it DOES give you the warm fuzzies. Kind of."
	p "Don't fall now, okay?"
	"I call out to her from across the room, where I'm spreading out some blackout curtains."
	yu "I know, I know,"
	"she replies, with that almost boyish lilt in her voice that has always been there, even since she was a little kid."
	"She mumbles a few things to herself for a while, and then turns to me and cheerfully exclaims,"
	yu "I'm finished!"
	"At the moment, the stepladder sways, and Yukana loses her balance."
	menu:
		"Save her":
			jump la
		"Sit back and pick my nose":
			jump lll
		"Genuflect":
			jump inu
label lll:
	play music "snd/blank.ogg"
	"Hmm, I'm digging out some impressively huge boogers here."
	"Hmm, that's weird, the stepladder's fallen over, and Yukana's under it. Her neck's kinda bent weird."
	"Hmm, that's odd, why's there all this blood flowing from her nose?"
	"Well, eh, whatever, not my problem. It's late, so I'm going home."
	"..."
	"The following day, the school was in an uproar and I was scolded to the point of trauma about having kept quiet about Yukana's death."
	play music "snd/gameovew.ogg"
#	weetabix note: THIS SHOULD BE PLAYED ONCE!
	menu:
		"Get a clue":
			jump llll
		"No time for that shit":
			jump a
label llll:
	scene bg 1-3
	os "As I watched dogs being born, I slowly came to the revelation that only fascism will save the world."
	os "Maybe that's what made Hitler go off and do all that shit, ya dig ...?"
	os "Anyway, Osaka Bancho here, suckah!"
	os "So you chose snot over a girl, dawg? Hmph, I guess that's one way to be manly."
	os "If you have no regrets, hey, whatever. Better than dying yourself."
	os "But listen up, homes. If yer so bored that yer pickin' yer goddamn nose, then do something constructive for a change. Like jerk off. Or somethin'."
	jump title
label la:
	scene bg taoreyukana
	"I dive and catch Yukana as she falls, protecting her from the impact with my body."
	"." "." "." "."
	p "Are you all right?"
	"After an odd silence, she nods."
	yu "Yeah."
	"... anyway, this is NOT GOOD."
	"I mean, here I am, lying on the floor, and there Yukana is, lying on top of me, her arms tight around me."
	"And to make matters worse, she's got her face buried against my chest."
	p "Are you hurt anywhere?"
	yu "No, not at all. It's not that ..."
	"But her voice has none of its usual spunk."
	yu "It's not that ..."
	p "Then are you not feeling well, or ...?"
	yu "I'm not sick, and I'm not hurt at all either, silly!"
	"She says crossly."
	p "Then get off me."
	yu "I can't."
	p "Why?"
	yu "'cause I like you."
	p "What?!"
	yu "I like you ... I like you, so I don't want to move from here."
	"Even though it's getting really dark in the classroom, it's obvious that Yukana is blushing."
	yu "I've loved you for so long, but every single time I tried to confess to you, I got so embarrassed that I couldn't do it. If I don't do it now ... if I let you go now ... I may never screw up the courage to do it again ... so ... let me say it one more time ..."
	"She puts her arms around my neck and murmurs,"
	yu "I love you very much."
	yu "There," 
	"she continues,"
	yu "now I've said it. The ball's in your court."
	""
	p "What's THAT supposed to mean?!"
	"Man, this tension is already too much for me, and Yukana isn't making it any better. In fact, she's making it ten ... no, a hundred ... no, a THOUSAND times worse!"
	yu "Um,"
	"Yukana murmurs softly,"
	yu "just tell me what you really feel. I won't mind."
	yu "I know I'm not that pretty, and that my personality isn't all that great ... and that there are a lot of girls who are a lot cuter than me out there ..."
	"Great, what now?"
	menu:
		"'I love you too'":
			jump lc
		"Knock her out":
			jump ls
		"Genuflect":
			jump inu
label ls:
	scene black
	play music "snd/konran.ogg"
	"I love her so much that I knock her out." "I have absolutely no idea what I'm doing." "I feel so trapped and cornered that I'm losing my mind."
	"I run down the corridor as fast as my legs can take me, vomiting blood as I go."
	scene bg nihontou
	"After that, I don't remember anything of what happened."
	"I have no memory of it at all."
	"All I know is that when I come to, I find myself charging into a U.S. Army base, buck naked, with a katana."
	"I cut down the first soldier I see, trembling with some indescribable emotion, yelling out every curse and swear word I know."
	"My consciousness fades again, and the next thing I know I've got two severed heads in one hand, and a katana dyed red with blood in the other."
	"I've been painted by several searchlights, and there's a bunch of U.S. soldiers with assault rifles, grenades, shotguns, machineguns, howitzers, and tanks surrounding my perimeter."
	"It's a perfect stage on which to die."
	"This scene reminds me of the famous words of the movie director, Orson Welles."
	"... ask not what you can do for your country. Ask what's for lunch."
	"Then I realize that if there were ever a pro wrestler who used drunkenness as his gimmick, then surely his finishing move would be a Drunkensteiner from the top rope."
	"And so I cry out:"
	p "Behold! This is the spirit of the kamikaze!"
	"I lunge as I raise my katana over my head."
	p "Long live the Emperor!"
	"Innumerable bullets from a machine gun mow me down."
	"It's an oddly satisfying sensation."
	play music "snd/gameovew.ogg"
#	weetabix note: THIS SHOULD BE PLAYED ONCE!
	menu:
		"Get a clue":
			jump as
		"Don't have time for that shit":
			jump a
label as:
	scene bg 1-3
	os "How best to hand down Gorbachev's revelation to the future generations, dawg?"
	os "I don't care HOW historians feel, but I'll NEVER be forgettin' that moment when he got fired up by a 50-cent discount coupon!"
	os "Anyway, Osaka Bancho here, suckah. For a cornered Japanese man, maybe kamikaze IS the best option, eh, homes?"
	os "Good call, good call. That all-out attack, man, that was THE SHIT."
	os "But, uh, dawg? Yer pretty weak if ya go berserk just from some girl confessin' to ya."
	jump title
label lc:
	p "Me too ..."
	yu "You too ... what?"
	"Yukana stares at me with a smile on her face."
	p "... nothing."
	"Oh, come on now."
	"She knows that I'm absolutely, head-over-heels in love with her, and yet she's teasing me like this."
	yu "Hey, c'mon, tell me, you meanie."
	p "Dude, YOU'RE the meanie."
	yu "But I'm not being mean ... I just wanna know ..."
	"Her face -- and those oh-so-cute blushing cheeks -- is so close to me."
	"I've never seen her face up this close before."
	"She's lovely."
	"I can't restrain myself any more."
	"I take her head in my hands and kiss her with everything I've got."
	"She flinches back for a moment, and then she relaxes and offers absolutely no resistance."
	scene black
	"." "." "."
	"By the time we get out, it's already pitch-dark outside."
	yu "Kinda cold, isn't it?"
	"She snuggles up against me as if it were the most natural thing in the world."
	"And I put an arm around her, as if it were the most natural thing in the world."
	"I pray this happiness will lasts forever..."
	"But then ..."
	play music "snd/blank.ogg"
	"I snap awake to the sound of Mozart's music."
	cp "Up trim!  Starboard full!"
	"It's the Captain's voice."
	"Hmmm, I must have been napping."
	cp "We shall declare our independence now!"
	"Yes! Finally the time has come!"
	"Can't afford to be napping at a time like this!"
	"After all, as a crewman aboard the submarine Yamato, I have no choice but to be stirred by my Captain's words."
	"The Soviet navy, the American navy, and the Japanese Navy."
	"From here on out, the fighting's just going to get more intense."
	"And this small warship is filled with the smell of tension and rejoicing."
	play music "snd/gameovew.ogg"
#	weetabix note: THIS SHOULD BE PLAYED ONCE!
	menu:
		"Hear Kanagawa Bancho out":
			jump cv
		"Don't have the time for that shit":
			jump a
label cv:
	scene bg karasu
	kn "Yo, dude, Kanagawa Bancho here. How was my erotic story? Oh, by the way, I've got no more stories from here on out. Totally tubular, don'tcha think?"
	kn "By the way, you know about the legend of corpses buried under cherry trees? Well, that doesn't compare with the deep shit buried in my stomach."
	kn "That's right, I'm FULL OF SHIT. LOLOLOLOLOLOL!"
	kn "Anyway, tell me, dude! What's the difference between split ends and splitting hair?"
	kn "No. I take that back. Never mind, yo!"
	kn "Anyway, this is the only way to get to the True End."
	kn "Want to see it? Or have you had enough?"
	menu:
		"Sure, why not?":
			jump zz
		"I've had enough":
			jump a
		"Genuflect":
			jump inu
label m:
	scene bg ex3
	play music "snd/konran.ogg"
	"Innumerable tentacles wriggled with glee, entering every single orifice (including pores) that the victim -- a beautiful woman -- had."
	"Thus violated, the woman writhed with unspeakable pleasure."
	"And then."
	"She died."
	"A man ran to try to help the woman, and then he died too."
	"Two brown bears abruptly started copulating next to the two corpses!"
	"Their hips were violently crashing into each other!"
	"With indescribable force!"
	"Whoa! I never knew that brown bears having sex was an invincible force of nature!"
	"Wait! The female brown bear's moans! OMGWTFBBQ!"
	"Bear" "Ia! Ia! Hastur! Hastur cf'ayak'vulgtmm, vugtlagln, c'vulgtmm! Ai! Ai! Hastur!"
	"My god ... that's the beginning to the devil summoning ritual! How could a bear do that?!"
	"This means the world ends today! Tomorrow will never come!"
	"Ejaculation!  A baby bear was born!"
	"That bear cub was really cute, too, especially the way it was smiling, yes?"
	"And then Gordon Freeman came along and beat the bear cub to death with a crowbar. Mission accomplished."
	"WAIT, IS THIS GORDON FREEMAN'S SO-CALLED HEROISM?!"
	play music "snd/gameovew.ogg"
#	weetabix note: THIS SHOULD BE PLAYED ONCE!
	menu:
		"Listen on":
			jump fff
		"Don't have time for that shit":
			jump a
label fff:
	scene bg karasu
	kn "Yo, dude, Kanagawa Bancho here. Anyway, yeah, I know, that was totally uncool. I don't have any imagination OR motivation, my good man! Gao-gao."
	kn "Anyway! Just let me say one last thing! One last thing, I swear!"
	kn "Y'know, they say that the only thing hatred gives birth to is hatred. That's wrong, don'tcha think?"
	kn "See, when you hate, you become hungry." "When you cast that hatred onto vegetables, curry rice gets made in a flash, right?  
	kn "THEREFORE, HATRED GIVES BIRTH TO CURRY! QED."
	jump title
label x:
	scene bg gocchi
	"The strongest of the strong, Master Karl Gotch, was just walking by."
	p "Master Gotch, I beg you, please help me!"
	"I pathetically screamed as I ran up to him."
	go "What's happened to you, boy? Yes, I am Karl Gotch, the wrestling master."
	scene bg ex1
	os "What, trying to pick a fight, old geezer? Hah!"
	scene bg ex2
	go "Oh, a street fight. I wouldn't ever stoop down to that lev-- ..."
	"Before Master Gotch could finish his sentence, though, Osaka Bancho's diamond fist exploded into Master Gotch's head."
	scene bg gocchi_eye
	"But Master Gotch didn't even seem to notice. Instead, he stared down Osaka Bancho with a look so murderous that it could probably have killed a lesser man on the spot."
	go "Hmmm. I may be old, but my blood still BOILS FOR COMBAT!"
	menu:
		"Aid Master Gotch":
			jump xa
		"Fall in love with Osaka Bancho":
			jump xb
		"Genuflect":
			jump inu
		"Break up the fight":
			jump xc
label xa:
	scene bg gocchi
	p "Master Gotch, let's wipe him out!"
	"Ecstatic with the prospect of having Master Gotch at my side, I charged into battle."
	p "... What the?!"
	"That very moment, Master Gotch gripped my arm and locked my elbow joint with no effort at all."
	"My elbow joint then made a grinding noise, and then suddenly snapped like a chicken wing as my arm bent in a direction that nature never intended it to."
	"I took a deep breath and then I screamed as if the end of the world had come."
	go "Do you really think I need your help, boy?"
	"A hand grabbed my neck and tightened like a vise."
	scene black
	"It was foolish to think that Master Gotch was a nice guy."
	"As fresh blood poured from from my mouth and nose I heard the sound of the two men fighting from far away."
	"Then my eyes failed me and ..."
	"I died."
	jump xaq
label xaq:
	play music "snd/gameovew.ogg"
#	weetabix note: THIS SHOULD BE PLAYED ONCE!
	menu:
		"Get a clue":
			jump xaw
		"Don't have time for that shit":
			jump a
label xaw:
	scene bg gocchi
	go "I am Karl Gotch, the god of pro wrestling."
	go "Did you think I needed your help?"
	go "Yes, it might have been you who petitioned me for aid in the first place."
	go "But the fight had become mine. And mine alone."
	go "If you did not understand that, then you deserved to die."
	go "You need to understand your place! You are the dog eating scraps from the table after the master has eaten his fill!"
	go "In other words, don't charge forward and try to devour Osaka Bancho. Step back and let a master do his work."
	jump title
label xb:
	scene bg 1-3
	play music "snd/konran.ogg"
	"Suddenly, I found myself falling in love with Osaka Bancho. This explained everything! Our fight was just a radical kind of sadomasochism, that was all!"
	"Everything made sense now. I'd loved him so much, for so long. I just didn't understand that until now."
	"So I shouted at Osaka Bancho, with everything I had:"
	p "I, I love you!!"
	"Osaka Bancho was so surprised that even his voice got distorted."
	os "WTF?! The hell's wrong with ya, dawg?! You so punch-drunk that you've gone mentally retarded or somethin'?!"
	p "Don't try to deny it! Look deep inside your heart. You're definitely in love with me too!"
	scene bg gocchi
	go "Yes, that is right. Your eyes are those of a lover. I know this well from my own experience."
	scene bg 1-3
	os "I ... I love you too!"
	"I ran up to him."
	os "And this is my love!"
	"Osaka Bancho screamed as he crushed me in his embrace and kissed me brutally."
	"I almost went crazy with ecstacy."
	"Osaka Bancho then took a long object out of his coat and threw it at Master Gotch."
	"A sword whose edge glittered dangerously in the dark."
	os "Hey, geezer!  Run us through with dat, will ya?!"
	scene bg gocchi2
	go "What for, boy?"
	os "Now that I've fallen in love, I've got no more right to be called a Bancho, dawg!"
	"That made sense. So my love didn't allow Osaka Bancho to be Osaka Bancho anymore ..."
	go "I understand, boy.  What a tragic way for things to"
	go "end ..."
	scene bg gocchi_to_p
	"Master Gotch took up the sword, and skewered both me and Osaka Bancho on it as we embraced each other."
	"The pain ran through my chest."
	os "THIS IS THE PROOF OF OUR LOVE!"
	"I had no regrets."
	"I lost my consciousness in happiness."
	jump xbv
label xbv:
	play music "snd/gameovew.ogg"
#	weetabix note: THIS SHOULD BE PLAYED ONCE!
	menu:
		"Hear Kanagawa Bancho out":
			jump xbnm
		"Don't have time for that shit":
			jump a
label xbnm:
	scene bg karasu
	kn "Yo, surf's up! Kanagawa Bancho here, dude. From here on out nothing has anything to do with the main story. Totally tubular, don'tcha think?"
	kn "Anyway, my pride and joy is coming up with totally perverted make-believe scenarios. THAT'S totally tubular too. Yeah."
	kn "Wanna hear one? I guarantee you'll have a good time, my man.
	kn "Eh, if you don't, then go ahead, select the staff credits."
	kn "Yeah, yeah, I'm absolutely mentally ill. Anyway! LET'S ROLL!"
	menu:
		"Argumentative childhood friend":
			jump l
		"Eroge King's beast fetish":
			jump m
		"Genuflect":
			jump inu
		"Roll staff credits":
			jump n
label xc:
	scene bg 1-3
	$renpy.pause(2)
	scene bg gocchi
	$renpy.pause(2)
	scene bg 1-3
	$renpy.pause(2)
	scene bg gocchi
	"I tried to stop them because fighting was wrong, but they'd already started and I couldn't get a word in edgewise."
	"They didn't care about me any more."
	"So I shrugged and went back home."
	scene black
	"When I got back, Kanagawa Bancho had dropped by to hang out."
	"We warmed up by talking about perverted plans which we could have executed, but that we did not have the courage to do."
	"For example, setting up a hidden camera inside the girls' locker room, or perhaps pulling a girl's panties down knowing that we'd get suspended."
	"The old woman who lived next-door got so annoyed with our loud laughter that she came and scolded us. In revenge, we poisoned a sweetcake and fed it to her dog."
	"We burst out laughing when the dog started vomiting after a bit."
	"Totally tubular."
	menu:
		"Hear Kanagawa Bancho out":
			jump xbnm
		"Don't have time for that shit":
			jump a
label zz:
	scene black
	play music "snd/end.ogg"
	"I was standing on the beach alone."
	"It was odd, as the sounds of the waves crashing against the shore were gradually fading away."
	"And there was a tightness in my chest, for some reason."
	"I didn't get it."
	"Perhaps I was thinking about the men who had turned toward the red evening sun and were now no more."
	"And as I thought that, memory upon memory flooded back into my mind."
	"I wondered if the days of life-or-death battles with Osaka Bancho would never come back."
	"I wondered if I'd never see the like of Master Gotch and his burning indomitable spirit again."
	"I wondered if I'd never be able to listen to Kanagawa Bancho's erotic hallucinations again."
	"And I wondered if the dog I poisoned wouldn't rise from its grave."
	"Yeah"
	"Probably"
	"They'd all never come back again."
	"Somehow I knew this to be true."
	"The carmine evening glow -- so much like blood -- painted the beach with its eerie light."
	"A bloody legend had ended, and now I awaited the beginning of a new legend ..."
	"." "." "." "." 
	play music "snd/dogeza_rock4.ogg"
	"IN THE NEXT EPISODE:" "Everything explodes into a burning immolation!"
	"It's a neverending bloody summer of Banchos!" "Can you even look at it without going blind?!"
	"The pure-white light of summer shines on the disused tracks." "Two men have a fateful encounter on a railway made brown with time and rust." "Their names are Shachi Sakurazaka and Karasu Nazuki."
	"And now, blood will rain as the Kansai Alliance strikes back!" "The sunlight of the summer of 2001 will disappear in a bloody mist!"
	"It all starts with one man: Osaka Bancho. And then Kanagawa Bancho, Master Gotch and even the legendary Sommelier Bancho join the fray." "An all-start cast will come together to form the greatest Bancho visual novel ever made in Japan!"
	"Big Bang (tentative title)"
	scene bg karasu
	kn "Shachi is like a flame, you see."
	"Karasu says, a smug smile on his face."
	kn "The greater the fuel, the larger the flame."
	"Sommelier Bancho laughs maniacally as he swirls the wineglass in his right hand (no doubt to check for the wine's legs)."
	sm "Then when the conflict ends, YOU'LL BE THE FIRST TO BE BURNED TO A CRISP."
	kn "No, I'm ice. Flames can't hurt me." "No, you'd better be watching your own back, dawg."
	sm "Heh, I'm the earth. No matter how many trees are burnt, the earth itself will endure unscathed. Hah!"
	"Sommelier Bancho gulps down the high-class wine, 'The Prime of Manhood' (1982 reserve vintage), with a single smooth motion."
	"."
	os "Listen up, we'll show those Kanto dogs who's boss! We'll annihilate 'em all! And we'll start with this little present here!"
	"Then Osaka Bancho, who has brought 300 school gang leaders of the Kansai Alliance under his leadership, pushes Daigaran High School's Bancho -- who's been tied up hand and foot -- onto the railway tracks."
	"And a bullet train rushes through the station."
	"Daigaran High School's Bancho screams ..."
	"... as the express train rips him to pieces."
	scene bg tukkomi
	"???" "Kansai Alliance dogs, are you?  Well then ..."
	"Two strange men are standing in Shachi's way. No, 'standing' isn't quite the right word for it."
	"A small man of about 4 feet and 3 inches is sitting on the shoulder of a huge well-built man who is about 6 feet and 7 inches."
	tu "That's right. I'm Tsukkomi Bancho, and this is ..."
	"The little guy pokes the huge guy's head."
	"???" "Uhhhhhh ... juice."
	tu "WTF?! Your NAME, idiot! Not juice!"
	"???" "I wanna juice."
	"The gigantic man slowly grumbles."
	tu "Quit it with the juice. Just introduce yourself already!"
	"???" "Uh, ummmmmmmmmm ... ketchup."
	tu "OMGWTF?!?! What on earth is that supposed to mean?!"
	"???" "Drink."
	tu "OMGWTFBBQ?!?!?! YOU DON'T DRINK KETCHUP!!!"
	bo "Uhhhhhhh ... I'm Boke Bancho ..."
	tu "OMGWTFOTL!!!!!! YOU'RE TOO SLOW!!!!"
	"" "Now stop masturbating and look forward to it!"
	scene bg yuuhi
	jump title
label kill:
	return