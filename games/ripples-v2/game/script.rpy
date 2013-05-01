init:
    #weetabix prerequisites
	image weet cred = "portcred.jpg"
	image weet logo = "bg/logo.jpg"
	image weet title = "title.jpg"
    #Kuu Sprite Data
	image kuu 115 = "char/01_b1e1m5.png"
        image kuu 116 = "char/01_b1e1m6.png"
        image kuu 117 = "char/01_b1e1m7.png"
        image kuu 126 = "char/01_b1e2m6.png"
        image kuu 147 = "char/01_b1e4m7.png"
        image kuu 221 = "char/01_b2e2m1.png"
        image kuu 222 = "char/01_b2e2m2.png"
        image kuu 224 = "char/01_b2e2m4.png"
        image kuu 224bl2 = "char/01_b2e2m4bl2.png"
        image kuu 225 = "char/01_b2e2m5.png"
        image kuu 226 = "char/01_b2e2m6.png"
        image kuu 227 = "char/01_b2e2m7.png"
        image kuu 228 = "char/01_b2e2m8.png"
        image kuu 264bl2 = "char/01_b2e6m4bl2.png"
        image kuu 267 = "char/01_b2e6m7.png"
        image kuu 273 = "char/01_b2e7m3.png"
        image kuu 274 = "char/01_b2e7m4.png"
        image kuu 278 = "char/01_b2e7m8.png"
        image kuu 281 = "char/01_b2e8m1.png"
        image kuu 282 = "char/01_b2e8m2.png"
        image kuu 282bl2 = "char/01_b2e8m2bl2.png"
        image kuu 284 = "char/01_b2e8m4.png"
        image kuu 284bl2 = "char/01_b2e8m4bl2.png"
        image kuu 288 = "char/01_b2e8m8.png"
        image kuu 315 = "char/01_b3e1m5.png"
        image kuu 324 = "char/01_b3e2m4.png"
        image kuu 325bl1 = "char/01_b3e2m5bl1.png"
        image kuu 327 = "char/01_b3e2m7.png"
        image kuu 328 = "char/01_b3e2m8.png"
        image kuu 335 = "char/01_b3e3m5.png"
        image kuu 337 = "char/01_b3e3m7.png"
        image kuu 338 = "char/01_b3e3m8.png"
        image kuu 368 = "char/01_b3e6m8.png"
        image kuu 377 = "char/01_b3e7m7.png"
        image kuu 384s = "char/01_b3e8m4s.png"
        image kuu 388s = "char/01_b3e8m8s.png"
        image kuu 415 = "char/01_b4e1m5.png"
        image kuu 426 = "char/01_b4e2m6.png"
        image kuu 455 = "char/01_b4e5m5.png"
        image kuu 457 = "char/01_b4e5m7.png"
        image kuu 466 = "char/01_b4e6m6.png"
    #Backgrounds and CG
	image park day = "bg/day.jpg"
        image park sunset = "bg/sunset.jpg"
        image park night = "bg/night.jpg"
        image cg 01 = "cg01.jpg"
        image cg 01b = "cg01b.jpg"
        image table 01 = "bg/table1.jpg"
        image table 02 = "bg/table2.jpg"
    define k = Character('Koda')
    define c = Character('Kuu')
    define x = Character('???')
label start:
    $voc = false
    scene weet cred
    $renpy.pause(2)
    scene weet logo
    $renpy.pause(2)
    scene weet title
    "Written by:     Ayu Sakata" "Illustrated by: M. Beatriz Garcia" "Music by:       Marc Conrad Tabula"
    menu:
        "Vocals on":
            $voc = true
            jump begin
        "Vocals off":
            jump begin
label begin:
    scene table 01
    play music "bgm/memories-loop.ogg"
    "There's something about people that just rubs me the wrong way."
    "I think it started in grade school. Our teacher blew up a balloon, wrote 'Self Esteem' on the side, and taped it to the wall."
    "She explained to us that we were all like the balloon. If we didn't have any self esteem, we would only be limp and small and sad."
    "Everyone else seemed really inspired, but it didn't click very well with me."
    "Watching that balloon on the wall deflate a little bit each day until it whithered away...I felt that self esteem didn't do much other than make people falsely large for a little while."
    "But no one else seemed to notice. Everyone kept going along their short little lives, puffed up with their self esteem, getting smaller and smaller each day."
    "What I hate the most are those idealistic people who think they can change the world."
    "Behind all those grand ideas of a better life, I think they're just desperate to be remembered. Desperate to keep their whithering balloons filled so they can feel important."
    "But things never change. No matter how hard you fight, it hardly makes a difference."
    "One person's life is just a drop in a bucket."
    "A lot of people think I'm a real pessimist because I think this way, but it doesn't really bother me at all."
    "It's easier to live life if I don't have to worry about changing the world. That way, I can just concentrate on what I want, like my photography."
    "The pictures I take will last a lot longer than I ever will. Not like it matters."
    "All I ever photograph is nature. Things that will be the same until the end of time."
    "I hate photographing people. I hate people who leap into my view and prance around and wave their arms, desperate to be captured on film so they'll be remembered."
    play music "bgm/blank.ogg"
    "There's no way I'll ever capture such worthless things on film. When people die, they're gone, and that's fine with me."
    play music "bgm/dayout-loop.ogg"
    "The city I live in isn't very large, but there are so many places hidden away that I always find something new whenever I explore."
    scene park day
    "Today, it's this place: a small park tucked away between a row of trees and an old school building."
    "There doesn't seem to be much here worth photographing, but at least there aren't any people either."
    "I aim my camera at a nearby bush to check the lighting. It's late afternoon, but the sun is still high enough for me to get some decent shots."
    "What's that sound?"
    "Something behind the bush is moving. I creep forward, holding my camera in front of me as if it would actually provide a decent shield, should something leap out at me."
    "Considering how much this camera cost, I'd probably be better off if I just took the hit."
    scene cg 01
    "It's a girl. What is she doing here?"
    "Is she...crying?"
    "I take an uncertain step back. If some girl is using this place as her secret crying spot, I want no part of it."
    "But the sound of crying sounds more like..."
    "But the sound of crying sounds more like... cats..."
    scene cg 01b
    if voc == true:
        play sound "voice/01.wav"
    else:
        pass
    x "Oh, hello!"
    "The girl looks up at me calmly, and I realize that she's patting a small kitten on the head."
    "Two more kittens are rolling around with each other on the ground beside her. They must be the source of the crying I heard."
    if voc == true:
        play sound "koda/01.wav"
    else:
        pass
    k "Uh...hey."
    if voc == true:
        play sound "koda/02.wav"
    else:
        pass
    k "Sorry to bother you. I'm just gonna...go."
    if voc == true:
        play sound "voice/02.wav"
    else:
        pass
    x "You're not a bother. Stay."
    "The kitten that she's patting yawns lazily and paws at her hand."
    scene cg 01
    if voc == true:
        play sound "voice/03.wav"
    else:
        pass
    x "Oh, here you go."
    "She pulls out a cookie and holds it above the kitten's mouth. It reaches up and bats at the cookie with its paw before clamping the cookie firmly between it's tiny teeth."
    if voc == true:
        play sound "koda/03.wav"
    else:
        pass
    k "What are you feeding them?"
    scene park day
    show kuu 228
    if voc == true:
        play sound "voice/04.wav"
    else:
        pass
    x "Cookies. I baked them myself this morning."
    if voc == true:
        play sound "koda/04.wav"
    else:
        pass
    k "Sure seems like a waste to give that to a bunch of cats."
    show kuu 284
    if voc == true:
        play sound "voice/05.wav"
    else:
        pass
    x "No, it's worth it."
    if voc == true:
        play sound "koda/05.wav"
    else:
        pass
    k "They're just gonna die anyway, you know. Strays rarely live long on the streets."
    show kuu 225
    if voc == true:
        play sound "voice/06.wav"
    else:
        pass
    x "So?"
    if voc == true:
        play sound "koda/06.wav"
    else:
        pass
    k "So why bother feeding them?"
    show kuu 126
    if voc == true:
        play sound "voice/07.wav"
    else:
        pass
    x "They're hungry. Do I need any more reason than that?"
    if voc == true:
        play sound "koda/07.wav"
    else:
        pass
    k "I guess not. But why cookies?"
    show kuu 338
    if voc == true:
        play sound "voice/08.wav"
    else:
        pass
    x "Because they're the only ones who will eat it..."
    if voc == true:
        play sound "koda/08.wav"
    else:
        pass
    k "What?"
    scene park sunset
    show kuu 384s
    if voc == true:
        play sound "voice/09.wav"
    else:
        pass
    x "I'm sorry, I have to be home soon."
    show kuu 284
    "She gives the kitten in her arms a fond pat on the head before leaving."
    scene park sunset
    "She didn't even say goodbye to me. I'm not sure whether or not I should be offended, but I guess it doesn't really matter."
    "The kittens swarm around my feet, and I kneel down to take a few pictures of them."
    scene park night
    "Ah...but it's already getting too dark to get any decent shots. At least, not with this camera. I guess I won't be taking many pictures today, after all."
    scene park day
    "I don't know why I came back here."
    "I keep telling myself it's just for photography, since I didn't get any good shots yesterday, but..."
    "I'm pretty sure I'm just lying to myself."
    show kuu 221
    if voc == true:
        play sound "voice/10.wav"
    else:
        pass
    x "Ah, you came back."
    if voc == true:
        play sound "koda/09.wav"
    else:
        pass
    k "I just wanted to take a couple pictures."
    show kuu 278
    if voc == true:
        play sound "voice/11.wav"
    else:
        pass
    x "I'll get out of the way, then."
    k "..."
    show kuu 288
    "I snap a few half-hearted shots, but I keep glancing at her and all the kittens swarming around her."
    if voc == true:
        play sound "koda/10.wav"
    else:
        pass
    k "What are you feeding them today?"
    show kuu 147
    if voc == true:
        play sound "voice/12.wav"
    else:
        pass
    x "Hm... I guess you could call them donuts."
    if voc == true:
        play sound "koda/11.wav"
    else:
        pass
    k "Did you make those too?"
    show kuu 282
    if voc == true:
        play sound "voice/13.wav"
    else:
        pass
    x "Sure did. This morning before school. I had to get up early to make them."
    if voc == true:
        play sound "koda/12.wav"
    else:
        pass
    k "Why?"
    show kuu 225
    if voc == true:
        play sound "voice/14.wav"
    else:
        pass
    x "Well, the dough needs time to rise properly, you see."
    if voc == true:
        play sound "koda/13.wav"
    else:
        pass
    k "That's not what I meant."
    show kuu 226
    if voc == true:
        play sound "voice/15.wav"
    else:
        pass
    x "Oh? Then what?"
    if voc == true:
        play sound "koda/14.wav"
    else:
        pass
    k "Why work so hard just to make food for a bunch of cats?"
    show kuu 281
    if voc == true:
        play sound "voice/16.wav"
    else:
        pass
    x "I told you. It's because they eat it."
    k "..."
    show kuu 224bl2
    if voc == true:
        play sound "voice/17.wav"
    else:
        pass
    x "I've always loved baking, you know. The best thing about it is being able to share with others."
    show kuu 264bl2
    if voc == true:
        play sound "voice/18.wav"
    else:
        pass
    x "There was a point in time when I wanted to own my own bakery."
    if voc == true:
        play sound "koda/15.wav"
    else:
        pass
    k "So?"
    show kuu 328
    if voc == true:
        play sound "voice/19.wav"
    else:
        pass
    x "Last year, for a class project, I baked muffins for the entire class."
    show kuu 368
    if voc == true:
        play sound "voice/20.wav"
    else:
        pass
    x "I woke up early so they'd be fresh, and I filled them with the best ingredients I could afford. I wanted them to be something special."
    show kuu 337
    if voc == true:
        play sound "voice/21.wav"
    else:
        pass
    x "Except...no one liked them. A lot of girls wouldn't even try them, claiming they had strict diets. I was so happy when some boys took a couple, but then they just threw them at each other."
    show kuu 335
    if voc == true:
        play sound "voice/22.wav"
    else:
        pass
    x "I even gave some to the teachers, who seemed to appreciate it. But at the end of the day, I found them in the trash."
    if voc == true:
        play sound "koda/16.wav"
    else:
        pass
    k "Well, yeah. People never appreciate things they're supposed to. Working so hard for them is a waste of time."
    show kuu 377
    if voc == true:
        play sound "voice/23.wav"
    else:
        pass
    x "Maybe..."
    show kuu 368
    if voc == true:
        play sound "voice/24.wav"
    else:
        pass
    x "After school, I came here. I wanted to cry, but these little guys came and cheered me up."
    show kuu 228
    if voc == true:
        play sound "voice/25.wav"
    else:
        pass
    x "I fed them the rest of the muffins, and they ate them without hesitation."
    show kuu 288
    if voc == true:
        play sound "voice/26.wav"
    else:
        pass
    x "Ever since then, I've brought them something every day. As a way of saying thanks."
    if voc == true:
        play sound "koda/17.wav"
    else:
        pass
    k "Thanks for what?"
    show kuu 282bl2
    if voc == true:
        play sound "voice/27.wav"
    else:
        pass
    x "For being happy when they eat my food."
    k "..?"
    show kuu 222
    if voc == true:
        play sound "voice/28.wav"
    else:
        pass
    x "What I like more than anything else is seeing people smile when they eat what I bake."
    show kuu 221
    if voc == true:
        play sound "voice/29.wav"
    else:
        pass
    x "I want to cheer people up and make the world a better place."
    if voc == true:
        play sound "koda/18.wav"
    else:
        pass
    k "That's stupid."
    show kuu 457
    if voc == true:
        play sound "voice/30.wav"
    else:
        pass
    x "Stupid?"
    if voc == true:
        play sound "koda/19.wav"
    else:
        pass
    k "Cheering people up is pointless. They'll just get depressed again anyway. And then they die."
    show kuu 415
    if voc == true:
        play sound "voice/31.wav"
    else:
        pass
    x "...Do you really think that?"
    if voc == true:
        play sound "koda/20.wav"
    else:
        pass
    k "Um...yeah."
    show kuu 466
    if voc == true:
        play sound "voice/32.wav"
    else:
        pass
    x "I see. That's awfully nihilistic of you."
    if voc == true:
        play sound "koda/21.wav"
    else:
        pass
    k "Don't tell me you're going to go all philosophy on me."
    scene park sunset
    show kuu 227
    if voc == true:
        play sound "voice/33.wav"
    else:
        pass
    x "No. Well, I have to get going. I'll see you tomorrow."
    if voc == true:
        play sound "koda/22.wav"
    else:
        pass
    k "What?"
    show kuu 224
    if voc == true:
        play sound "voice/34.wav"
    else:
        pass
    x "My name is Kuu. And you are?"
    if voc == true:
        play sound "koda/23.wav"
    else:
        pass
    k "Koda..."
    show kuu 284
    if voc == true:
        play sound "voice/35.wav"
    else:
        pass
    c "Then I'll see you tomorrow, Koda."
    if voc == true:
        play sound "koda/24.wav"
    else:
        pass
    k "Don't count on it."
    show kuu 274
    if voc == true:
        play sound "voice/36.wav"
    else:
        pass
    c "Of course."
    scene park night
    "She smiles fondly at me and leaves. Again, the kittens turn their attention to me, but I don't bother to take any pictures of them."
    "This place is so boring, and it's much too dark, anyway."
    "Even though I didn't get many shots today, I don't think I'll be coming back here."
    scene park day
    "And yet...somehow..."
    show kuu 282
    if voc == true:
        play sound "voice/37.wav"
    else:
        pass
    c "Hello, Koda."
    k "..."
    show kuu 274
    if voc == true:
        play sound "voice/38.wav"
    else:
        pass
    c "You're only here to take pictures, right?"
    if voc == true:
        play sound "koda/25.wav"
    else:
        pass
    k "Yeah. The ones I developed yesterday weren't very good."
    show kuu 115
    if voc == true:
        play sound "voice/39.wav"
    else:
        pass
    c "You develop your photos?"
    "She sounds genuinely surprised. For some reason, I feel a little victorious."
    if voc == true:
        play sound "koda/26.wav"
    else:
        pass
    k "Digital is too easy. There's no fun in it anymore. Makes you sloppy, too, since you can afford to make mistakes."
    show kuu 116
    if voc == true:
        play sound "voice/40.wav"
    else:
        pass
    c "I see."
    show kuu 224
    if voc == true:
        play sound "voice/41.wav"
    else:
        pass
    c "This is for you."
    "She hands me a small plastic bag tied with a ribbon."
    if voc == true:
        play sound "koda/27.wav"
    else:
        pass
    k "What is it?"
    show kuu 282
    if voc == true:
        play sound "voice/42.wav"
    else:
        pass
    c "Cookies. You want some, right?"
    if voc == true:
        play sound "koda/28.wav"
    else:
        pass
    k "What makes you think that?"
    show kuu 273
    if voc == true:
        play sound "voice/43.wav"
    else:
        pass
    c "You came back, didn't you?"
    show kuu 224
    play sound "sfx/paperbag.wav"
    "With a sigh, I open the package. I'm greeted with the sweet smell of cinnamon and chocolate."
    "I take a bite of one. It's actually quite good. For a moment, I wonder why anyone would even think to dislike this girl's cooking."
    "But I guess that's just the nature of people."
    show kuu 324
    if voc == true:
        play sound "voice/44.wav"
    else:
        pass
    c "I'm sorry."
    if voc == true:
        play sound "koda/29.wav"
    else:
        pass
    k "What?"
    show kuu 337
    if voc == true:
        play sound "voice/45.wav"
    else:
        pass
    c "You're not smiling. It must not be very good."
    if voc == true:
        play sound "koda/30.wav"
    else:
        pass
    k "That's not it. I'm just a bit angry that people don't appreciate your baking."
    show kuu 282bl2
    if voc == true:
        play sound "voice/46.wav"
    else:
        pass
    c "You shouldn't be. If you think it tastes good, then smile!"
    if voc == true:
        play sound "koda/31.wav"
    else:
        pass
    k "Why are you trying so hard to get me to smile?"
    show kuu 225
    if voc == true:
        play sound "voice/47.wav"
    else:
        pass
    c "You don't look like a happy person."
    "Her honesty is like an arrow to my heart."
    if voc == true:
        play sound "koda/32.wav"
    else:
        pass
    k "That's really none of your business."
    show kuu 228
    if voc == true:
        play sound "voice/48.wav"
    else:
        pass
    c "It is if you keep coming here to see me."
    if voc == true:
        play sound "koda/33.wav"
    else:
        pass
    k "I didn't say I was coming here to see you."
    show kuu 288
    if voc == true:
        play sound "voice/49.wav"
    else:
        pass
    c "You didn't have to."
    if voc == true:
        play sound "koda/34.wav"
    else:
        pass
    k "Besides, it doesn't matter. I'll just be depressed again tomorrow, anyway."
    show kuu 284
    if voc == true:
        play sound "voice/50.wav"
    else:
        pass
    c "Then I'll bring you more cookies tomorrow."
    if voc == true:
        play sound "koda/35.wav"
    else:
        pass
    k "Do you really want to see me smile that badly?"
    show kuu 281
    if voc == true:
        play sound "voice/51.wav"
    else:
        pass
    c "I want to see everyone smile."
    if voc == true:
        play sound "koda/36.wav"
    else:
        pass
    k "Huh. Another impossible dream. This is why I hate people so much."
    show kuu 315
    if voc == true:
        play sound "voice/52.wav"
    else:
        pass
    c "You don't like people?"
    if voc == true:
        play sound "koda/37.wav"
    else:
        pass
    k "Of course not! They always ruin things."
    show kuu 327
    if voc == true:
        play sound "voice/53.wav"
    else:
        pass
    c "How so?"
    if voc == true:
        play sound "koda/38.wav"
    else:
        pass
    k "They leap into pictures when I don't want them to, or obsess over how they look as if it really makes a difference."
    if voc == true:
        play sound "koda/39.wav"
    else:
        pass
    k "I can't stand it! They're all so annoying."
    show kuu 325bl1
    if voc == true:
        play sound "voice/54.wav"
    else:
        pass
    c "Am I annoying?"
    if voc == true:
        play sound "koda/40.wav"
    else:
        pass
    k "Uh..."
    "Optimists like Kuu have always aggravated me, but there's something about her straightforward honesty that's actually really refreshing."
    if voc == true:
        play sound "koda/41.wav"
    else:
        pass
    k "I don't know."
    show kuu 388s
    "She giggles and turns back to the kittens, patting one of them fondly on the head."
    show kuu 228
    if voc == true:
        play sound "voice/55.wav"
    else:
        pass
    c "Fair enough."
    if voc == true:
        play sound "koda/42.wav"
    else:
        pass
    k "It's not that you're annoying or anything. It's just..."
    "I strain my mind, trying to figure out how to explain my feelings."
    if voc == true:
        play sound "koda/43.wav"
    else:
        pass
    k "I just don't like people who think they can change the world."
    show kuu 117
    if voc == true:
        play sound "voice/56.wav"
    else:
        pass
    c "Why not?"
    play music "bgm/blank.ogg"
    if voc == true:
        play sound "koda/44.wav"
    else:
        pass
    k "Because it's dumb! One person's life is just a drop in the bucket, after all."
    play music "bgm/cherished-loop.ogg"
    show kuu 267
    if voc == true:
        play sound "voice/57.wav"
    else:
        pass
    c "You don't really believe that."
    if voc == true:
        play sound "koda/45.wav"
    else:
        pass
    k "Yes I do!"
    if voc == true:
        play sound "koda/46.wav"
    else:
        pass
    k "It's better than believing that I actually change anything!"
    show kuu 455
    if voc == true:
        play sound "voice/58.wav"
    else:
        pass
    c "Then why are you here?"
    if voc == true:
        play sound "koda/47.wav"
    else:
        pass
    k "Wh-what?"
    show kuu 426
    if voc == true:
        play sound "voice/59.wav"
    else:
        pass
    c "You want to believe it, but you're just afraid to. You're afraid that you can't make a difference, so you don't try."
    if voc == true:
        play sound "koda/48.wav"
    else:
        pass
    k "That's not-"
    show kuu 117
    "I can't actually bring myself to deny her statement."
    show kuu 222
    if voc == true:
        play sound "voice/60.wav"
    else:
        pass
    c "Koda..."
    if voc == true:
        play sound "koda/49.wav"
    else:
        pass
    k "Yeah?"
    show kuu 284bl2
    if voc == true:
        play sound "voice/61.wav"
    else:
        pass
    c "Even if my life is just a single drop, every drop of water leaves ripples."
    scene park day
    "She leaves before I can respond. I don't have a response, anyway. Normally, I'd be angry if someone tried to sell some trite inspirational phrase to me."
    "But this is different. She's not trying to sell me anything. It's really what she believes."
    "Kuu is so cheerful and confident, but there's nothing about her that's desperate or puffed up."
    "She believes she can change the world with nothing more than cookies and a smile. Honestly...I don't know if she can or not..."
    "But I do know that she managed to change me."
    scene park sunset
    "The sun is setting, and as I raise my camera to photograph it, I can't help but wonder what she'll bring me tomorrow. Maybe I should bring something for her."
    "Maybe I'll ask if I can take her picture."
    scene black
    "This is only the first drop."
    scene table 02
    "Produced by sakevisual" "" "Writing" "Ayu Sakata"
    "Produced by sakevisual" "" "Art" "M. Beatriz Garcia"
    "Produced by sakevisual" "" "Original Soundtrack" "Marc Conrad Tabula"
    "Produced by sakevisual" "" "Engine" "RenPSP by lolbot" "ported by weetabix"
    "Thank you for reading!"
$renpy.quit()