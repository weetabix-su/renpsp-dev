
# You can place the script of your game in this file
# cherry blossom petals.
image sakura filmstrip = anim.Filmstrip("sakura.png", (20, 20), (2, 1), .10)
image snowblossom = SnowBlossom("sakura filmstrip")


# Declare images below this line, using the image statement.
init:   
    # tinted night
    image nosstand = im.MatrixColor("o00.png",
                                         im.matrix.saturation(.5) * im.matrix.tint(.90, .75, 1.0))
    image ncorstand = im.MatrixColor("c00.png",
                                         im.matrix.saturation(.5) * im.matrix.tint(.90, .75, 1.0))
    image nlilstand = im.MatrixColor("l00.png",
                                         im.matrix.saturation(.5) * im.matrix.tint(.90, .75, 1.0))
    image gerpup5 = im.MatrixColor("g07.png",
                                         im.matrix.saturation(.5) * im.matrix.tint(.90, .75, 1.0))
    image gerpup3 = im.MatrixColor("g06c.png",
                                         im.matrix.saturation(.5) * im.matrix.tint(.90, .75, 1.0))
    image gerpup4 = im.MatrixColor("g06d.png",
                                         im.matrix.saturation(.5) * im.matrix.tint(.90, .75, 1.0))
    image ngerpup1 = im.MatrixColor("g06a.png",
                                         im.matrix.saturation(.5) * im.matrix.tint(.90, .75, 1.0))
    image nosmad2 = im.MatrixColor("o14.png",
                                         im.matrix.saturation(.5) * im.matrix.tint(.90, .75, 1.0))
    image nosmad1 = im.MatrixColor("o13.png",
                                         im.matrix.saturation(.5) * im.matrix.tint(.90, .75, 1.0))
    image noswrites = im.MatrixColor("o03.png",
                                         im.matrix.saturation(.5) * im.matrix.tint(.90, .75, 1.0))
    image nosmile1 = im.MatrixColor("o01.png",
                                         im.matrix.saturation(.5) * im.matrix.tint(.90, .75, 1.0))
    
    # Define some new transitions here.
    $ aaa = Dissolve(0.1)    
    $ flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')
    $ flashbulb2 = Fade(0.1, 0.0, 0.1, color='#fff')
    $ flashbulb3 = Fade(0.1, 0.0, 0.1, color='#f60e14')
    $ cup = Character('Corvus',
                         color="#349164",
                        what_slow_cps=40,
                        what_outlines=[ (1, "#333333") ], ctc=anim.Blink("paw.png"),
                        window_xpos=400,
                        window_ypos=147)
    $ oup = Character('Os',
                         color="#839134",
                        what_slow_cps=30,
                        what_outlines=[ (1, "#333333") ], ctc=anim.Blink("paw.png"),
                        window_xpos=400,
                        window_ypos=147)
    $ gup = Character('Puppy in heat',
                         color="#605dd1",
                        what_slow_cps=50,
                        what_outlines=[ (1, "#333333") ], ctc=anim.Blink("paw.png"),
                        window_xpos=400,
                        window_ypos=147)
    $ gup2 = Character('Gervase',
                         color="#605dd1",
                        what_slow_cps=50,
                        what_outlines=[ (1, "#333333") ], ctc=anim.Blink("paw.png"),
                        window_xpos=400,
                        window_ypos=147)
    # Use it in subtitle mode.
    $ gsub = Character(None,
                            what_size=28,
                            what_outlines=[(3, "#605dd1", 2, 2), (3, "#605dd1", 0, 0)],
                            what_layout="subtitle",
                            what_xalign=0.5,
                            what_text_align=0.5,
                            window_background=None,
                            window_yminimum=0,
                            window_xfill=False,
                            window_xalign=0.5)
    $ csub = Character(None,
                            what_size=28,
                            what_outlines=[(3, "#2f5d3a", 2, 2), (3, "#349164", 0, 0)],
                            what_layout="subtitle",
                            what_xalign=0.5,
                            what_text_align=0.5,
                            window_background=None,
                            window_yminimum=0,
                            window_xfill=False,
                            window_xalign=0.5)
    $ osub = Character(None,
                            what_size=28,
                            what_outlines=[(3, "#547728", 2, 2), (3, "#91b611", 0, 0)],
                            what_layout="subtitle",
                            what_xalign=0.5,
                            what_text_align=0.5,
                            window_background=None,
                            window_yminimum=0,
                            window_xfill=False,
                            window_xalign=0.5)
    $ vsub = Character(None,
                            what_size=28,
                            what_outlines=[(3, "#801f1f", 2, 2), (3, "#d71717", 0, 0)],
                            what_layout="subtitle",
                            what_xalign=0.5,
                            what_text_align=0.5,
                            window_background=None,
                            window_yminimum=0,
                            window_xfill=False,
                            window_xalign=0.5)
    # Fanservice Mode
    $ oq= Character('Os',
                        color="#839134",
                        what_slow_cps=30,
                        what_outlines=[ (1, "#333333") ], ctc=anim.Blink("paw.png"),
                        window_left_padding=160,
                        show_side_image=Image("frame_os.png", xalign=0.0, yalign=1.0))
    $ cq= Character('Corvus',
                        color="#349164",
                        what_slow_cps=40,
                        what_outlines=[ (1, "#333333") ], ctc=anim.Blink("paw.png"),
                        window_left_padding=160,
                        show_side_image=Image("frame_corvus.png", xalign=0.0, yalign=1.0))
    $ vq= Character('Vosges',
                        color="#d6533d",
                        what_slow_cps=20,
                        what_outlines=[ (1, "#333333") ], ctc=anim.Blink("paw.png"),
                        window_left_padding=160,
                        show_side_image=Image("frame_vosges.png", xalign=0.0, yalign=1.0))
    $ gq= Character('Gervase',
                        color="#605dd1",
                        what_slow_cps=50,
                        what_outlines=[ (1, "#333333") ], ctc=anim.Blink("paw.png"),
                        window_left_padding=160,
                        show_side_image=Image("frame_gervase.png", xalign=0.0, yalign=1.0))
    $ lq= Character('Lilja',
                        color="#cd79e2",
                        what_slow_cps=80,
                        what_outlines=[ (1, "#333333") ], ctc=anim.Blink("paw.png"),
                        window_left_padding=160,
                        show_side_image=Image("frame_lilja.png", xalign=0.0, yalign=1.0))
    
image osstand= LiveComposite(
        (300, 544),
        (0, 0), "o00.png",
        (99, 115), anim.SMAnimation("a",
            anim.State("a", "o00a.png"),
            anim.State("b", "o00b.png"),
            anim.State("c", "o00c.png"),
            anim.Edge("a", 2.0, "a", prob=2),
            anim.Edge("a", 0.06, "b"),
            anim.Edge("b", 0.06, "c"),
            anim.Edge("c", 0.14, "a"),
        ),
        )
image oskstand= LiveComposite(
        (300, 544),
        (0, 0), "o05.png",
        (99, 115), anim.SMAnimation("a",
            anim.State("a", "o00a.png"),
            anim.State("b", "o00b.png"),
            anim.State("c", "o00c.png"),
            anim.Edge("a", 2.0, "a", prob=2),
            anim.Edge("a", 0.06, "b"),
            anim.Edge("b", 0.06, "c"),
            anim.Edge("c", 0.14, "a"),
        ),
        )
image corstand= LiveComposite(
        (327, 490),
        (0, 0), "c00.png",
        (50, 177), anim.SMAnimation("a",
            anim.State("a", "c00a.png"),
            anim.State("b", "c00b.png"),
            anim.State("c", "c00c.png"),
            anim.Edge("a", 2.0, "a", prob=2),
            anim.Edge("a", 0.06, "b"),
            anim.Edge("b", 0.06, "c"),
            anim.Edge("c", 0.14, "a"),
        ),
        )
image corstand2= LiveComposite(
        (300, 544),
        (0, 0), "c03.png",
        (85, 174), anim.SMAnimation("a",
            anim.State("a", "c03a.png"),
            anim.State("b", "c03b.png"),
            anim.State("c", "c03c.png"),
            anim.Edge("a", 2.0, "a", prob=2),
            anim.Edge("a", 0.06, "b"),
            anim.Edge("b", 0.06, "c"),
            anim.Edge("c", 0.14, "a"),
        ),
        )
image corhstand= LiveComposite(
        (349, 600),
        (0, 0), "cor00.png",
        (92, 96), anim.SMAnimation("a",
            anim.State("a", "cor00a.png"),
            anim.State("b", "cor00b.png"),
            anim.State("c", "cor00c.png"),
            anim.Edge("a", 2.0, "a", prob=2),
            anim.Edge("a", 0.06, "b"),
            anim.Edge("b", 0.06, "c"),
            anim.Edge("c", 0.14, "a"),
        ),
        )
image vostand= LiveComposite(
        (335, 489),
        (0, 0), "v00.png",
        (93, 131), anim.SMAnimation("a",
            anim.State("a", "v00a.png"),
            anim.State("b", "v00b.png"),
            anim.State("c", "v00c.png"),
            anim.Edge("a", 2.0, "a", prob=2),
            anim.Edge("a", 0.06, "b"),
            anim.Edge("b", 0.06, "c"),
            anim.Edge("c", 0.14, "a"),
        ),
        )
image vostand2= LiveComposite(
        (335, 489),
        (0, 0), "v06.png",
        (93, 131), anim.SMAnimation("a",
            anim.State("a", "v00a.png"),
            anim.State("b", "v00b.png"),
            anim.State("c", "v00c.png"),
            anim.Edge("a", 2.0, "a", prob=2),
            anim.Edge("a", 0.06, "b"),
            anim.Edge("b", 0.06, "c"),
            anim.Edge("c", 0.14, "a"),
        ),
        )
image gerstand= LiveComposite(
        (424, 600),
        (0, 0), "g00.png",
        (101, 140), anim.SMAnimation("a",
            anim.State("a", "g00a.png"),
            anim.State("b", "g00b.png"),
            anim.State("c", "g00c.png"),
            anim.Edge("a", 2.0, "a", prob=2),
            anim.Edge("a", 0.06, "b"),
            anim.Edge("b", 0.06, "c"),
            anim.Edge("c", 0.14, "a"),
        ),
        )
image lilstand= LiveComposite(
        (346, 609),
        (0, 0), "l00.png",
        (65, 75), anim.SMAnimation("a",
            anim.State("a", "l00a.png"),
            anim.State("b", "l00b.png"),
            anim.State("c", "l00c.png"),
            anim.Edge("a", 2.0, "a", prob=2),
            anim.Edge("a", 0.06, "b"),
            anim.Edge("b", 0.06, "c"),
            anim.Edge("c", 0.14, "a"),
        ),
        )
image eccstand= LiveComposite(
        (309, 606),
        (0, 0), "e01.png",
        (108, 307), anim.SMAnimation("a",
            anim.State("a", "e01a.png"),
            anim.State("b", "e01b.png"),
            anim.State("c", "e01c.png"),
            anim.Edge("a", 2.0, "a", prob=2),
            anim.Edge("a", 0.06, "b"),
            anim.Edge("b", 0.06, "c"),
            anim.Edge("c", 0.14, "a"),
        ),
        )
#ROUTES#
image coroute1="cor_route01.png"
image coroute1a="coroute1a.png"
image coroute2="cor_route02.png"
image coroute2a="cor_route02a.png"
image coroute2b="cor_route02b.png"
image corend="cor_route03.png"
image vosroute1= LiveComposite(
        (800, 600),
        (0, 0), "vos_route01.png",
        (0, 0), anim.SMAnimation("a",
            anim.State("a", "vos_route01.png"),
            anim.State("b", "vos_route02.png"),
            anim.Edge("a", 0.3, "a", ),
            anim.Edge("a", 0.09, "b"),
            anim.Edge("b", 0.09, "a"),
        ),
        )
image vosroute2="vos_route03.png"
image vosgend="vos_route04a.png"
image vosbend="vos_route04b.png"
image geroute1="ger_route01.png"
image geroute2="ger_route02.png"
image geroute3="ger_route03.png"
image gergend="ger_route04a.png"
image gerbend="ger_route04b.png"
image gbadend="ger_broute.png"
image lbadend="lil_broute.png"
image vbadend="vos_broute.png"

image intro01="intro01.png"
image intro02="intro02.png"
image intro03="intro03.png"
image intro04="intro04.png"
image bg01="f01.png"
image bg01a="f01a.png"
image bg01b="f01b.png"
image bg02="f02.png"
image bg02a="f02a.png"
image bg03="f03.png"
image bg04="f04.png"
image bg04a="f04a.png"
image bg05="f05.png"
image fs="fs.png"
image fn01="fs01.png"
image fn02="fs02.png"
image fn03a="fs03a.png"
image fn03b="fs03b.png"
image fn03c="fs03c.png"
image fn03d="fs03d.png"
image fn04a="fs04a.png"
image fn04b="fs04b.png"
image fn04c="fs04c.png"
image fn04d="fs04d.png"
image fn04e="fs04e.png"
image fn05="fs05.png"
image fn06="fs06.png"
image fn07="fs07.png"

image osmile1="o01.png"
image osmile2="o02.png"
image oswrites="o03.png"
image oswrites2="o03a.png"
image oswis="o04.png"
image osmad1="o13.png"
image osmad2="o14.png"
image osksmile="o06.png"
image osksmile2="o07.png"
image oskblush="o08.png"
image oskhe="o09.png"
image oskblush2="o10.png"
image oskmad="o01.png"
image oskble="o12.png"
image osknife="o19.png"
image osooo="o19a.png"
image oshe="o19b.png"
image osblussh="o19c.png"
image oswut="o20.png"
image oscry="o21.png"
image osehh="o22.png"
image osmad3="o11.png"
image coros1="o15.png"
image coros2="o16.png"
image coros3="o18.png"
image corblush="c06.png"
image cormad2="c05.png"
image corsur2="c07.png"
image corsur="c04.png"
image cormad="c01.png"
image corblush2="c02.png"
image corscared="c08.png"
image corlaugh="c09.png"
image corhshout="cor01.png"
image corhsmile1="cor02.png"
image corhsmile2="cor03.png"
image corhsur="cor04.png"
image corhblush="cor05.png"
image corhblush2="cor06.png"
image corhgah="cor07.png"
image corhit="cor08.png"
image corsad="c10.png"
image corcrys="c11.png"
image corhgasp="cor09.png"
image vosmile="v05.png"
image vosmad="v02.png"
image vosmad2="v01.png"
image vosblush="v03.png"
image voswut="v04.png"
image vosmad3="v07.png"
image vosmile2="v08.png"
image vosblush2="v09.png"
image vosos1="v10.png"
image vosos2="v11.png"
image vosangry="v12.png"
image vosaaa="v12a.png"
image germad="g01.png"
image gerlick="g02.png"
image gerangry="g03.png"
image gerblush="g04.png"
image gerpup1="g06a.png"
image gerpup2="g06b.png"
image geros1="g08.png"
image geros2="g09.png"
image gerthink="g10.png"
image gersmile="g11.png"
image lilsmile="l01.png"
image lilnstand="l02.png"
image lilnsmile="l03.png"
image lilbye="l04.png"
image lilroute1="lil_route01.png"
image lilroute2="lil_route02.png"
image lilgend="lil_route03a.png"
image lilbend="lil_route03b.png"
image eccblush="e02.png"
image eccmad="e03.png"
image splash1="splash01.png"
image splash2="splash02.png"
image splash3="splash03.png"
image splash4="splash04.png"
image splash5="splash05.png"
image scene1="scen01.png"
image cr01="cr01.png"
image cr01a="cr01a.png"
image cr02="cr02.png"
image cr03="cr03.png"
image cr04="cr04.png"
image cr05="cr05.png"
image cr06="cr06.png"
image junkbox ="cgmenu02.png"

# Declare characters used by this game.

define o = Character('Os', color="#839134",
                        what_slow_cps=30,
                        what_outlines=[ (1, "#333333") ], ctc=anim.Blink("paw.png"))
define c = Character('Corvus', color="#349164",
                        what_slow_cps=40,
                        what_outlines=[ (1, "#333333") ], ctc=anim.Blink("paw.png"))
define v = Character('Vosges', color="#d6533d",
                        what_slow_cps=20,
                        what_outlines=[ (1, "#333333") ], ctc=anim.Blink("paw.png"))
define g = Character('Gervase', color="#605dd1",
                        what_slow_cps=50,
                        what_outlines=[ (1, "#333333") ], ctc=anim.Blink("paw.png"))
define vo = Character('Kid that stinks', color="#d6533d",
                        what_slow_cps=20,
                        what_outlines=[ (1, "#333333") ], ctc=anim.Blink("paw.png"))
define co = Character('Weird looking chicken', color="#349164",
                        what_slow_cps=40,
                        what_outlines=[ (1, "#333333") ], ctc=anim.Blink("paw.png"))
define ge = Character('Puppy on heat', color="#605dd1",
                        what_slow_cps=50,
                        what_outlines=[ (1, "#333333") ], ctc=anim.Blink("paw.png"))
define r = Character('dsadsa', color="879f8d",
                        what_slow_cps=20,
                        what_outlines=[ (1, "#333333") ], ctc=anim.Blink("paw.png"))
define os = Character('???', color="#839134",
                        what_slow_cps=30,
                        what_outlines=[ (1, "#333333") ], ctc=anim.Blink("paw.png"))
define oss = Character('Os', color="#839134",
                        what_slow_cps=10,
                        what_outlines=[ (1, "#333333") ], ctc=anim.Blink("paw.png"))
define l = Character('Lilja', color="#cd79e2",
                        what_slow_cps=80,
                        what_outlines=[ (1, "#333333") ], ctc=anim.Blink("paw.png"))
define ls = Character('WTF', color="#cd79e2",
                        what_slow_cps=80,
                        what_outlines=[ (1, "#333333") ], ctc=anim.Blink("paw.png"))
define e = Character('Ecchin', color="#25e3cf",
                        what_slow_cps=70,
                        what_outlines=[ (1, "#333333") ], ctc=anim.Blink("paw.png"))


# Add the gallery to the main menu.
$ config.main_menu.insert(2, ('Gallery', "gallery", "True"))

# The entry point to the gallery code.
label gallery:
    python hide:

        # Construct a new gallery object.
        g = Gallery()

        # The image used for locked buttons.
        g.locked_button = "locked.png"

        # The background of a locked image.
        g.locked_background = "cgmenu02.png"

        # Frames added over unlocked buttons, in hover and idle states.
        g.hover_border = "overh.png"
        g.idle_border = "over.png"

        # An images used as the background of the various gallery pages.
        g.background = "cgmenu01.png"

        # Lay out the gallery images on the screen.
        # These settings lay images out 3 across and 4 down.
        # The upper left corner of the gird is at xpos 10, ypos 20.
        # They expect button images to be 155x112 in size.
        g.grid_layout((4, 3), (210, 38), (104, 122))

        g.page("CG Scenes")

        # Our first button is a picture of the beach.
        g.button("thcg01.png")
        g.unlock_image("vosroute1")
        g.button("thcg04.png")
        g.unlock_image("geroute1")
        g.button("thcg07.png")
        g.unlock_image("lilroute1")
        g.button("thcg10.png")
        g.unlock_image("coroute1")
        
        g.button("thcg03.png")
        g.unlock_image("vosroute2") 
        g.button("thcg06.png")
        g.unlock_image("geroute3") 
        g.button("thcg09.png")
        g.unlock_image("lilroute2")
        g.button("thcg12.png")
        g.unlock_image("coroute2") 
        
        g.button("thcg02.png")
        g.unlock_image("vbadend") 
        g.button("thcg05.png")
        g.unlock_image("gbadend")
        g.button("thcg08.png")
        g.unlock_image("lbadend")
        g.button("thcg11.png")
        g.unlock_image("coroute2a")
        
        
        g.page("Backgrounds")
        
        g.button("thbg01.png")
        g.unlock_image("bg01")
        g.button("thbg02.png")
        g.unlock_image("bg02")
        g.button("thbg03.png")
        g.unlock_image("bg03")
        g.button("thbg04.png")
        g.unlock_image("bg04")
 
        # Now, show the gallery.
        g.show()
    return
    

# The game starts here.
label splashscreen:
    scene splash1 with aaa
    pause 1
    show splash2 with dissolve
    pause 1
    show splash3 with aaa
    pause 2
    hide splash2 with aaa
    hide splash3  with aaa
    show splash4 with dissolve
    pause 1
    show splash5 with aaa
    pause 2
    hide splash4 with aaa
    hide splash5 with aaa
    pause 2
    return
    
label start:

    $ has_visited_kitchen = False
    $ has_visited_kitchen2 = False
    $ has_visited_basement = False
    $ has_visited_basement2 = False
    $ has_visited_watchtower = False
    $ has_visited_watchtower2 = False

    $ vos_01 = False
    $ ger_01 = False
    
    $ persistent.end_01
    $ persistent.end_02
    $ persistent.end_03
    $ persistent.end_04
    

    $ corvus = 0
    $ vosges = 0
    $ gervase = 0
    $ lilja = 0
    
    stop music fadeout 1.5
    $ renpy.play('waterdrop1.wav')
    scene intro01 with dissolve
    pause 3
    scene intro02 with dissolve
    pause 5
    scene intro03 with dissolve
    pause 5
    scene intro04 with dissolve
    pause 3
    
    scene bg01 with dissolve

    
    r"From the depths of her cursed slumber, the girl awakes."
    window show
    show osstand at left with dissolve
    play music "intro_theme.ogg"
    os"..."
    r"L-Lady Os?"
    o"..."
    show corstand at right with dissolve
    co"Praise the Gods! You're alive! YOU'RE ALIVE!"
    o"..."
    co"Huh? Wait..."
    o"..."
    hide corstand with aaa
    show corsur2 at right with aaa
    $ renpy.play('fwaon1.wav')
    with vpunch
    co"What's..."
    $ renpy.play('fwaon2.wav')
    with hpunch
    co"WHAT'S THAT ON YOUR NECK?!"
    o"..."
    hide corsur2 with aaa
    show corstand at right with aaa
    co"Good Lord! So you can't speak?!"
    o"*nods*"
    co"Let me cast a spell on you so you can speak to me with your mind."
    $ renpy.play('bukimi1.wav')
    o"!"
    co"That's it! Try sending me your thoughts, my lady."
    co"..." 
    hide corstand with aaa
    show corsur2 at right with aaa
    $ renpy.play('fwaon3.wav')
    with vpunch
    co"WHAT?! You don't remember me? What is this witchcraft!?"
    o"..."
    hide corsur2 with aaa
    show corstand at right with aaa
    co"My lady, it pains me DEEPLY to hear that. I'm your loyal Corvus, and I've been serving your family since I was born. True story!"
    o"..."
    c"I just woke up, so I'm just as confused as you are, but..."
    c"From the condition of this room- *sneeze* -it looks like we've been sleeping for quite some time. Some bastardly traitor probably cast some kind of spell on us."
    c"Also, that knife on your neck must be cursed. That's why you can't remember a thing. Atrocious, absolutely atrocious!"
    c"What this ruffian did to you has no name! Your precious porcelain skin- *cough* I mean your neck and your voice has been ruined!"
    o"..."
    c"My lady, allow me to refresh your memory."
    c"You are the heir to the throne of the Kingdom of Ulla, the most beautiful kingdom in this vast land."
    c"With your speeches and your, ahem, discipline, our territory spread like wildfire during your reign. Oh, the riches we had! Your father, Lord Skedel, was so proud of you! *sniff*"
    c"But it seems somebody grew jealous of your glory."
    c"On your 17th birthday, you came to this tower to have some fun with the prisoners. I followed you to make sure you got back in time for your birthday ceremony."
    o"..."
    c"Alas, the sleep spell conquered me as soon as I entered the tower. I didn't catch even a single glimpse of the culprit."
    c"Judging from the knife on your neck, the traitor must have tried to kill you right after that!" 
    c"Oh, I'm so glad you managed to survive, Lady Os! Your father will be so happy to see you again!"
    o"..."
    c"Gahaha, don't worry! We'll catch the culprit and make him give you your memories back!" 
    o"..."
    stop music fadeout 1.5
    c"Why don't we explore the tower a little? If the sleep spell affected everybody, the prisoners should be waking up right about now."
    o"*nods*"
    
label firstmenu:
    if has_visited_basement2 and has_visited_kitchen2 and has_visited_watchtower2:
        jump room
    else:
        
        play music"intro_theme.ogg"
        menu:

            "Go to the basement." if has_visited_basement2 == False:
                if has_visited_basement == False:
                    jump ba
                else:
                    jump ba2
            
            "Go to the kitchen." if has_visited_kitchen2 == False:
                if has_visited_kitchen == False:
                    jump ki
                else: 
                    jump ki2
          
            "Go to the balcony." if has_visited_watchtower2 == False:
                if has_visited_watchtower == False:
                    jump wt
                else:
                    jump wt2

                    
                    
label ba:
    $ has_visited_basement = True
    stop music fadeout 1.5
    scene black with dissolve
    $ renpy.play('mizu.wav')
    pause 1
    $ renpy.play('mizu2.wav')
    pause 1
    $ renpy.play('mizu.wav')
    pause 1
    $ renpy.play('mizu2.wav')
    pause 1
    window show dissolve
    c"Watch your step, Lady Os! The floor's covered in, uh, fertilizer."
    o"!"
    show bg02 with dissolve
    c"Nnngh!"
    c"This flatulence is killing me!"
    show osstand at left with aaa
    show corstand2 at left with aaa
    show vostand at right with dissolve
    vo"That's mean, Corvus."
    c"You!"
    play music "vosges_theme.ogg"
    vo"To what do I owe this honor?"
    show vosmile at right with aaa
    hide vostand with aaa
    c"Don't get too full of yourself. Lady Os is just looking around after her brief nap."
    show voswut at right with aaa
    hide vosmile with aaa
    vo"Brief? Are you serious? We've been here for four years. Trapped like rats."
    c"F-four years?! How can you be so sure of that?"
    show vostand at right with aaa
    hide voswut with aaa
    vo"Can you see the little window there?"
    vo"Gaze at the sky, and you will see an small green light there. That's the venturous star."
    vo"It appears every 14 years. Before this mess occurred I happened to look up the number of years that would pass before it would appear again."
    c"Hmmph. That makes sense, I guess..."
    o"..."
    c"I'm sorry, my lady! This is Vosges, the magician of the castle. At least, that's what he thinks..."
    v"What's this? She has amnesia?"
    v"Heh. Hope you have fun figuring out which one of us did this."
    c"What do you mean?"
    v"You should pay more attention to what happens around you, Corvus, instead of drooling on your lady."
    hide corstand2 with aaa
    show corblush at left with aaa
    c"H-how dare you!"
    v"Well, I suppose I should explain the situation we find ourselves in, since you're obviously clueless."
    show cormad2 at left with aaa
    hide corblush with aaa
    v"Four years ago, someone attempted to murder Lady Os in this tower."
    c"How did you know?"
    v"On her 17th birthday, I received a strange note."
    hide cormad2 with aaa
    show corstand2 at left with aaa
    c"What did it say?"
    v"It said that Lady Os was going to be killed in this tower that day."
    hide corstand2 with aaa
    show corsur at left with aaa
    c"WHAT?!"
    v"I was invited to watch."
    c"And you didn't warn Lady Os of this?! You filthy traitor!"
    v"*shrugs* What else did you expect me to do?"
    o"..."
    hide corsur with aaa
    show corstand2 at left with aaa
    c"Does Vosges hate you, my lady? Let's just put it this way... I wouldn't be surprised if it turns out that he was the one who attempted to kill you."
    c"Because of the barrier surrounding this tower, nobody can get in or out, which means that the traitor has to be one of the prisoners."
    o"..."
    c"Oh, but you are the sole exception, my lady!"
    c"As the creator of this barrier, you can come and go as you please. I only managed to get in because I was following very closely behind you."
    v"How naive."
    c"Are you thinking of something unpleasant again, with that decaying brain of yours?"
    v"The presence of the barrier merely means that the culprit has to be someone who was in the tower at the time."
    v"Sure, it could be me. It could be Gervase."
    c"That's what I've been saying!"
    v"It could also be... {w}you."
    show cormad2 at left with aaa
    hide corstand2 with aaa
    c"How dare you insult me, you smelly stinkhorn! There's nobody more loyal to Lady Os than me! Nobody!"
    v"Oh, I don't think anybody can possibly doubt that."
    o"..."
    hide cormad2 with aaa
    show corstand2 at left with aaa
    c"Do {i}I{/i} hate you? Of course not! I would give my life for you!" 
    o"..."
    c"{i}Why{/i} does he hate you? Well-"
    v"So you really don't remember anything. {w}What a pity."
    show vosmile at right with aaa
    hide vostand with aaa
    v"You wiped out my town and killed every single person I was attached to."
    c"You also confined him to this basement, where he has to pick through the dirt and crap to find the old books you left for him to read."
    c"Which is hilarious, because some of those books are corrupted magic tomes that you put there to mislead him in his pursuit of knowledge."
    show vosmad at right with aaa
    v"-what?"
    c"Oh, and the hat he's wearing stops him from growing. He should be around twenty, but his body will forever be that of a thirteen-year-old."
    v"That can't be..!"
    show vosmad2 at right with aaa
    hide vosmad with aaa
    c"Oops. Sorry, were you listening?"
    v"Damn you, witch! Words cannot express the intensity of my hatred for you!"
    o"..."
    c"Watch your stinky mouth, Vosges! My lady is sensitive to your foul breath."
    o"..."
    menu:

        "Pat the kid.":
        
            jump pa
            
        "...I'm hungry.":
        
            jump hu

label pa:
    $ vosges += 2
    window hide dissolve
    show vosroute1 with dissolve
    pause 2
    scene bg02 with dissolve
    window show dissolve
    show osstand at left with aaa
    show corsur at left with aaa
    show voswut at right with aaa
    v"W-what are you doing?!"
    c"M-m-my laaaaady!"
    c"You dirty shroom! Be grateful that Lady Os has deigned to gift her divine touch unto a festering fungus like you!"
    o"..."
    c"!"
    c"...she{w} says{w} she {w}{size=8}is{/size} {w}{size=5}sorry..{/size}"
    v"What?"
    hide corsur with aaa
    show corstand2 at left with aaa
    c"She's sorry! For what she has done to you..."
    v"---"
    show vosblush at right with aaa
    hide voswut with aaa
    v"I'm quite speechless."
    o"..."
    v"A simple apology like that is useless, and you know it."
    c"Ugh, I'm sick of your ungratefulness. Let's go, my lady."
    o"*nods*"
    hide corstand2 with aaa
    hide osstand with aaa
    pause 2
    v"...it's just a damn apology..."
    v"...so... {w}why?"
    stop music fadeout 1.5
    scene black with dissolve 
    scene bg01 with aaa
    show osstand at left with aaa
    show corstand at right with aaa
    c"That stinky shroom...! Ugh, he pisses me off!"
    o"Why did you do that, Lady Os?"
    menu:

        "Because he's cute.":
        
            jump cuvo
            
        "I felt like it.":
        
            jump wut

label cuvo:
    $ vosges += 1
    c"W-what are you thinking, my lady!? {w}{color=#adc6ba}{i}I feel defeated by that shrimp...{/i}{/color}"
    stop music fadeout 1.5
    scene black with dissolve 
    scene bg01 with aaa
    show osstand at left with aaa
    show corstand at right with aaa
    jump cho2
    
label hu:
    stop music fadeout 1.5
    $ renpy.play('Stomach Growls.mp3')
    o"..."
    c"..."
    v"..."
    v"Is this supposed to be funny?"
    v"Get out."
    scene black with dissolve
    scene bg01 with aaa
    show osstand at left with aaa
    show corstand at right with aaa
    c"Gyahaha, of course you're hungry. You've been sleeping for four years!"
    o"*nods*"
    jump cho2
label wut:
    $ corvus += 1
    c"You're so kind, my lady. It moves my bird entrails. *sniff*"
    jump cho2
    
label ba2:
    $ has_visited_basement2 = True
    stop music fadeout 1.5
    scene black with aaa
    scene bg02 with aaa
    show vostand at right with aaa
    show osstand at left with aaa
    show corstand2 at left with aaa
    c"You two again? What do you want?"
    menu:

        "Why do you stink like that?":
            jump stink
            
        "Just passing by.":
        
            jump vpass

label stink:
    $ vosges -= 1
    show vosmad2 at right with aaa
    show corlaugh at left with aaa
    hide corstand2 with aaa
    c"Gyahahahaha!"
    v"Do you never tire of mocking me?"
    v"This smelly hat that {i}you{/i} put on me renders me unable to eat or drink regular food, and I have to consume the 'fertilizer' magically generated in this dungeon instead."
    show vostand at right with aaa
    hide vosmad2 with aaa
    v"Now leave. Please. I've had enough."
    hide corlaugh with aaa
    show cormad at left with aaa
    c"We were leaving already."
    o"..."
    hide osstand with aaa
    hide cormad with aaa
    scene black with dissolve
    scene bg01 with aaa
    show osstand at left with aaa
    show corstand at right with aaa
    jump cho2
    
    
label vpass:
    v"Don't stay too long."
    v"Wouldn't want you to get the impression that I can actually tolerate your presence."
    c"..."
    scene black with dissolve
    scene bg01 with aaa
    show osstand at left with aaa
    show corstand at right with aaa
    c"For once, I feel the same way he does." 
    jump cho2
    
label cho2:
    c"Well, where shall we go?"
    jump firstmenu
    
label ki:
    $ has_visited_kitchen = True
    stop music fadeout 1.5
    scene black with dissolve
    $ renpy.play('foot1.wav')
    pause 3
    o"..."
    scene bg03 with aaa
    show osstand at left with aaa
    show corstand at right with aaa
    c"Of course! Let me find something for you to eat. Just wait a minute!"
    hide corstand with aaa
    o"..."
    show gerpup1 at center with aaa
    pause
    c"Lady Os! There's..." 
    window hide dissolve
    show corsur2 at right with aaa
    cup"WHAT'S THAT?!"
    cup"A puppy?"
    $ renpy.play('inu1.ogg')
   
    hide corsur2 with aaa
    show corstand at right with dissolve
    cup"How cute!"
    hide gerpup1 with aaa
    show gerpup2 at left with aaa
    oup"..."
    cup"WHAT ARE YOU-"
    gup"Titties! I want to touch some, wan wan!"
    gup"I've been trapped here for so long... I'm so lonely, wan wan!"
    scene black with aaa
    $ renpy.play('punch.wav')
    with vpunch
    $ renpy.play('punch3.mp3')
    with hpunch
    $ renpy.play('punch.wav')
    with vpunch
    r"The puppy has been owned..."
    
    pause 1
    play music "gervase_theme.ogg"
    window show dissolve
    scene bg03 with aaa
    show osstand at left with aaa
    show cormad2 at left with aaa
    c"I'm not surprised that I didn't remember you, Gervase."
    show gerstand at right with dissolve
    c"You're so unpleasant that my mind blocked out every memory of your loutish presence."
    g"Shut the fuck up."
    show germad at right with aaa
    hide gerstand with aaa
    g"Like I give a poop about what you think about me."
    c"And why are you here again? You're supposed to guard Vosges and make sure he doesn't do anything stupid!"
    g"Yeah, right, let the dog watch the prisoner and leave no food so it can starve to death..."
    hide cormad2 with aaa
    show corstand2 at left with aaa
    g"I just woke up and came here to find something to eat, but there's absolutely nothing!"
    show gerstand at right with aaa
    hide germad with aaa
    if has_visited_basement or has_visited_watchtower:
        c"Well, we've been sleeping in this tower for four years, so all of the food here must have rotted away."
        g"Four YEARS?! No wonder I'm feel like I haven't eaten in ages..."
        jump nofood
    else:
        c"Looks like all of the food's rotted away. We must have been sleeping for a very long time..."
        jump nofood
label nofood:
    g"Os! Open the barrier and let us out! At this rate, we're all going to starve to death!"
    c"Lady Os is suffering from amnesia right now, so..."
    g"Wait, what?! Does that mean we're trapped here?"
    c"Oh, the King must be worried sick...! I don't even want to {i}think{/i} about what's been going on in Ulla while my lady was sleeping..."
    g"Hah, with that senile old bastard on the throne? Face it, birdie, Ulla's probably in ruins by now."
    hide corstand2 with aaa
    show corsur at left with aaa
    c"...in ruins?! Our precious Ulla?!"
    show germad at right with aaa
    hide gerstand with aaa
    g"Pfft! 'Our'? Don't make me laugh. Ulla was hell for everyone except this bitch here."
    hide corsur with aaa
    show cormad2 at left with aaa
    c"You-! Don't dare to speak to her like that!"
    o"..."
    hide cormad2 with aaa
    show corstand2 at left with aaa
    c"My dear lady, you shouldn't waste your time on this ruffian. His name is Gervase. You made him guard the prisoners in this tower as punishment."
    g"Don't talk like that was the only punishment she gave me!"
    g"She fucking enjoyed torturing me. I see her all the time in my nightmares... {w}her sadistic face as she boinks me with her stick!"
    o"..."
    c"Well, you were strict to the ones who deserved it. Gervase tried to betray you so many times..."
    show gerangry at right with aaa
    hide germad with aaa
    g"NOBODY deserves the kind of torture this demon put me through! So go fuck yourself, Corvus! AND YOU TOO, BITCHOS! "
    hide corstand2 with aaa
    show cormad2 at left with aaa
    c"How dare you talk to us like that?! Animal!"
    g"YOU'RE AN ANIMAL TOO!"
    c"At least I'm cute!"
    g"I'M CUTER THAN YOU!"
    c"You smell like poop!"
    g"YOU LOOK LIKE POOP AND I BET YOU TASTE LIKE POOP TOO!"
    c"...why... you...!"
    o"..."
    r"Gervase's body is incredibly beaten up." 
    menu:

        "Change his bandages." :
        
            jump ban
            
        "...I'm hungry.":
        
            jump hu2

label ban:
    $ gervase += 1
    $ ger_01 = True
    show geroute1 with dissolve
    window hide dissolve
    gsub"!!!!"
    gsub"Don't touch me!"
    show geroute2 with dissolve
    gsub"Aaann..."
    csub"M-my lady! NOOOOOOOO!"
    hide geroute1 with aaa
    hide geroute2 with aaa
    scene bg03 with dissolve
    show osstand at left with aaa
    show corsur at left with aaa
    show gerblush at right with aaa
    window show dissolve
    c"...*sniff*"
    g"Why... why did you do that?"
    o"..."
    c"My lady says that your wounds look painful..."
    show germad at right with aaa
    hide gerblush with aaa
    g"Pff! Now you want to play nice, huh? Fuck off, bitch! Don't expect gratitude from me."
    hide corsur with aaa
    show cormad at left with aaa
    c"Whatever. Let's go, my lady."
    o"..."
    hide cormad with aaa
    hide osstand with aaa
    show gerstand at right with aaa
    hide germad with aaa
    g"...hmph."
    scene black with dissolve
    pause 1
    stop music fadeout 1.5
    scene bg01 with aaa
    show osstand at left with aaa
    show corstand at right with aaa
    c"Please don't do that anymore, ruffians like Gervase don't deserve your compassion..."
    c"Also, it might be dangerous."
    menu:

        "Refuse.":
        
            jump cant
            
        "Agree.":
        
            jump will
    
label cant:
    $ gervase += 1
    c"Fine. Fine! Just... be more careful! I'll be watching your back anyway..."
    jump cho2
label will:
    $ corvus += 1
    c"You will?"
    o"*nods*"
    c"My lady! I'm so grateful!"
    jump cho2
label hu2:
    stop music fadeout 1.5
    $ gervase -= 1
    $ renpy.play('Stomach Growls.mp3')
    o"..."
    c"..."
    g"..."
    show gerstand at right with aaa
    hide germad with aaa
    g"Get out of my sight."
    scene black with aaa
    scene bg01 with dissolve
    show osstand at left with aaa
    show corstand at right with aaa
    c"My lady, look! There's a nest of tarantulas right behind you!" 
    r"Os turns around."
    r"She plucks out the tarantulas and plops them one by one into her mouth."
    show osmile2 at left with aaa
    hide osstand with aaa
    c"A-ah, my lady, leave some for me too!"
    jump cho2
    
label ki2:
    $ has_visited_kitchen2 = True
    stop music fadeout 1.5
    scene black with aaa
    scene bg03 with aaa
    show gerstand at right with aaa
    show osstand at left with aaa
    show corstand2 at left with aaa
    g"What do you want?"
    o"..."
    menu:

        "Just passing by.":
        
            jump gpass
            
        "Does it hurt less?" if ger_01 == True:
             jump groute01
             
label gpass:
    $ gervase -= 1
    g"Hmph, then fuck off."
    scene black with aaa
    scene bg01 with aaa
    show osstand at left with aaa
    show cormad at right with aaa
    c"Brainless beast..."
    hide cormad with aaa
    show corstand at right with aaa
    jump cho2
    
label groute01:
    $ gervase += 2
    show gerblush at right with aaa
    g"...do you really care?"
    o"*nods*"
    c"..."
    g"Just a little bit less..."
    g"There, happy now?"
    o"*nods*"
    g"Fine, now get lost."
    hide corstand2 with aaa
    hide osstand with aaa
    scene black with dissolve
    scene bg01 with aaa
    show osstand at left with aaa
    show corstand at right with aaa
    c"Bleh!"
    jump cho2
    
label wt:
    $ has_visited_watchtower = True
    stop music fadeout 1.5
    scene black with dissolve
    $ renpy.play('foot1.wav')
    pause 2
    c"My lady, from here we should be able to see the castle."
    o"..."
    c"Y-you're afraid of heights?!"
    scene bg04 with flashbulb
    show osstand at left with aaa
    show corstand2 at left with aaa
    show lilstand at right with aaa
    c"..."
    o"..."
    ls"..."
    c"Who are you?"
    c"{color=#adc6ba}{i}I've never seen this guy in my life...{/i}{/color}"
    ls"Do you expect me to tell you everything? Why don't you figure it out yourself? Oh wait, that might be too difficult for your tiny little bird brain to handle."
    c"..."
    ls"Well, if you don't have anything more useful to say, get out of my way. I have tons of books to arrange before it's afternoon. So shoo, shoo!"
    play music "lilja_theme.ogg"
    c"{color=#adc6ba}{i}What on earth is this guy talking about?! I can't see any books here except for the one he's holding...{/i}{/color}"
    ls"What?"
    c"{color=#adc6ba}{i}I should choose my words carefully... Who knows how this lunatic will react?{/i}{/color}"
    c"Excuse me, sir. Are you a new servant, perhaps?"
    show lilsmile at right with aaa
    hide lilstand with aaa
    ls"HAHAHAHHAAHAAHAHAHHAHHA. Servant? Me? Are you blind as well as incurably stupid?"
    show lilstand at right with aaa
    hide lilsmile with aaa
    ls"My name is Lilja. {w}I'm a God."
    hide corstand2 with aaa
    show corsur at left with aaa
    c"WHAT?!"
    c"If that's a joke, it's not a very funny one!"
    l"Lady Os knows me very well, so she will confirm that what I'm saying is true. But the truth should be obvious. You can tell just by looking at me that I'm {i}completely{/i} out of this world."
    hide corsur with aaa
    show corstand2 at left with aaa
    c"Uhmm, you see- Lady Os is an amnesiac right now. Someone tried to kill her and stabbed a knife on her neck."
    l"I can see the knife perfectly, as well as the curse that surrounds it."
    c"Really? So what can we do to remove it?"
    l"Let me check my books."
    hide lilstand with aaa
    c"{color=#adc6ba}{i}But there aren't any books here! He's just moving his hands about in thin air!{/i}{/color}"
    c"..."
    c"{color=#adc6ba}{i}Wait. I've read books describing an invisible library that only immortals can see. Could it be...?{/i}{/color}"
    c"My lady, is he really a God? Can you remember him?"
    o"..."
    c"I see, so you can't... "
    c"This is all rather shocking to me."
    c"I'm a bit religious, but to see a God with your own eyes... I think it's a little..."
    show lilstand at center with aaa
    with vpunch
    l"Too much for your itsy bitsy eyes to take? I know I'm gorgeous."
    hide corstand2 with aaa
    show corscared at left with aaa
    c"GAHHHHHHHHH!"
    hide lilstand  with aaa
    show lilsmile at right with aaa
    l"Yes! YES! Come on! I know you're excited! Shout more! Shout your lungs out! Ululate! Whip your hair about in my praise!"
    hide corscared with aaa
    show corstand2 at left with aaa
    c"..."
    l"Why so quiet? Has my beauty left you speechless? AHAHAHAHAHAHAHAHAHAHAHAHA!"
    hide corscared with aaa
    show corstand2 at left with aaa
    c"{color=#adc6ba}{i}What a weirdo...{/i}{/color} So you found something, Mr. Lilja?"
    hide lilsmile with aaa
    show lilstand at right with aaa
    l"Yes. According to my books, those knife curses were rather fashionable about four years ago."
    l"The only way to remove it is for it be drawn out by the person who did the curse."
    c"I see."
    l"Just be careful not to let some random person pull it off. It will instantly kill her."
    c"*gasp* And if we find the wrong culprit?"
    l"Like I said. It will kill her."
    c"*sniffle* Well, we have to be extremely careful then. I'm glad to find someone in this place who doesn't hate my lady."
    l"...who said I didn't hate her?"
    c"Huh?"
    l"It's her fault that I'm not reigning in the heavens." 
    l"I've been trapped here for four years while you were sleeping like babies. I became almost a mere mortal, doing banal things all day and aging with every second. {w}It's... {w}It's..."
    show lilsmile at right with aaa
    hide lilstand with aaa
    l"IT'S MAKING ME CRAZY HAHAHAHAHAHAHA!"
    c"Nnngh..."
    c"Let's go, my lady!"
    o"*nods*"
    scene black with dissolve
    scene bg01 with aaa
    stop music fadeout 1.5
    show osstand at left with aaa
    show corstand at right with aaa
    c"Gosh! That guy was nuts! Talking about Gods... pfft!"
    o"*nods*"
    c"I'm glad you agree, my lady!"
    jump cho2

label wt2:
  stop music fadeout 1.5
  $ has_visited_watchtower2 = True
  c"My lady, do you really want to return there?"
  o"..." 
  o"*shakes*"
  c"I thought so..."
  jump cho2  
  
label room:
    play music"intro_theme.ogg"
    c"... {w}Wait, my lady!"
    c"We should stop to think about what we've learned!"
    o"...*nods*"
    scene black with aaa
    pause 1 
    scene bg01 with dissolve
    show osstand at left with aaa
    show corstand at right with aaa
    
    c"This is really worrying, Lady Os..."
    c"Apart from us, there are three people in this tower."
    c"All of them hate you, so all of them would have a motive for trying to kill you."
    c"Due to your amnesia, we can't take down the barrier, so nobody can leave or enter."
    c"And the most important thing: the knife in your neck must be pulled out by the person who did the curse."
    c"There is no room for mistakes. We must identify the real culprit without fail."
    c"Ahh... what a mess."
    o"..."
    c"We should question them further..."
    c"Let's start with Gervase. He's supposed to be the guard, after all."
    o"..."
    c"Eh? You want to go alone? Why?"
    o"..."
    c"D-do you think so my lady? I'm annoying?"
    o"*nods*"
    hide corstand with aaa
    show corcrys at right with aaa
    c"*tears*"
    c"Well, I can't go against your will..."
    hide corcrys with aaa
    show corstand at right with aaa
    c"But even so, your father entrusted your safety to me, so please take this whistle."
    o"...?"
    c"If you are in trouble, just use it and I'll fly to your side in the blink of an eye!"
    o"*nods*"
    c"Please be careful, Lady Os. I'll be waiting for you!"
    scene black with dissolve
    $ renpy.play('foot1.wav')
    pause 2
   
label kitchen:
    stop music fadeout 1.5
    pause 1
    scene bg03 with dissolve
    show osstand at left with aaa
    show gerpup1 at center with aaa
    g"Not you again... I'm tired. Give it a rest, will you?"
    o"*shakes*"
    g"Why don't you speak already?"
    r"Os points at her neck."
    g"...{w}what the fuck is that?! Argh, all right then... "
    show gerstand at right with flashbulb
    hide gerpup1 with aaa
    g"So, what do you want?"
    play music"gervase_theme.ogg"
    show oswrites at left with aaa
    hide osstand with aaa
    r"Os takes a little book out of her pocket and writes something in it. Then she hands it to Gervase."
    show osstand at left with aaa
    hide oswrites with aaa
    g"Hey."
    o"?"
    show gerblush at right with aaa
    hide gerstand with aaa
    g"Do you expect me to know how to read?"
    o"!"
    show oswis at left with aaa
    hide osstand with aaa
    $ renpy.play('karasu1.mp3')
    with hpunch
    c"WOOOOOOOOOOOOOOOOOOOOO!"
    g"Eh?"
    show osstand at left with aaa
    hide oswis with aaa
    show cormad2 at left with aaa
    c"Did he try to touch you again, my lady?"
    o"*shakes*"
    show gerstand at right with aaa
    hide gerblush with aaa
    c"Ah, he can't read. Can't say I'm surprised. He {i}is{/i} a dog, after all."
    hide cormad2 with aaa
    show corstand2 at left with aaa
    g"I'm proud to be one..."
    c"Anyway. We are trying to find the person who did this to Lady Os. You may be interested, since it's the culprit's fault that she can't remember how to get out of here."
    g"That means I can leave this place if I find the culprit?"
    c"Eh. That's for Lady Os to decide."
    show germad at right with aaa
    hide gerstand with aaa
    g"Well then, eat shit. I'm not helping if there's nothing in return for me."
    hide corstand2 with aaa
    show cormad2 at left with aaa
    c"...You lowlife-"
    o"..."
    hide cormad2 with aaa
    show corstand2 at left with aaa
    c"Ugh! Lady Os wants to know what you want in return."
    g"Now we're talking! Let's see..."
    show gerthink at right with aaa
    hide germad with aaa
    g"..."
    pause 2
    c"{color=#adc6ba}{i}I hope his brain implodes from thinking too much...{/i}{/color}"
    show germad at right with aaa
    hide gerthink with aaa
    g"I know what I want!"
    c"That was fast!"
    show gerstand at right with aaa
    hide germad with aaa
    g"{size=11}Tits{/size} {w}... lots of them." 
    c"...you're joking right?"
    g"...no."
    c"{color=#adc6ba}{i}THIS GODDAMN CREATURE...{/i}{/color}"
    c"Do you have no shame? At least have the courtesy to request something decent..."
    show gerlick at right with aaa
    hide gerstand with aaa
    g"Umm... how about pussies? I like pussies."
    c"..."
    o"..."
    c"My lady says whatever as long as you shut up."
    show gersmile at right with aaa
    hide gerlick with aaa
    g"Then it's a deal! Hahaha!"
    c"*sigh* Well, Gervase, your cooperation is essential, since you were the one who watches the door."
    c"This is highly unlikely, since Lady Os's barrier is impenetrable, but could you tell us if someone suspicious entered the tower before we were trapped here?"
    show gerstand at right with aaa
    hide gersmile with aaa
    g"Nobody else entered apart from you two."
    g"Though, Corvus, I never saw you enter..."
    c"I flew!"
    g"Ah. Well."
    g"After Os came, I went on my usual night rounds through the tower."
    g"Vosges was in the basement as usual, doing his mage things, but I could tell it wasn't harmful at all. Then I took a peek at the kitchen, which was empty.
    But then when I went to the third floor, something weird happened..."
    c"And?"
    show germad at right with aaa
    hide gerstand with aaa
    g"I can't remember what happened. My eyes went blurry out of nowhere, and then I fell asleep and rolled down the stairs. My ass hurt like there was no tomorrow when I woke up."
    c"...I see."
    c"This was a waste of time after all."
    show gerstand at right with aaa
    hide germad with aaa
    g"What else did you expect? I did my part as the watchdog I am."
    c"Well, you sure are a great one, because according to your story, there were four people including you, while there are really five."
    show germad at right with aaa
    hide gerstand with aaa
    g"Five? What the fuck are you talking about?"
    c"There's a guy named Lilja on the balcony."
    show gerstand at right with aaa
    hide germad with aaa
    g"That's impossible. I went there a few minutes ago and it was empty."
    c"Huh? Maybe he went somewhere else?"
    o"..."
    c"My lady says that we've heard enough from you."
    c"We'll be back later."
    g"Fine."
    hide corstand2 with aaa
    hide osstand with aaa
    stop music fadeout 1.5
    pause 1
    g"A guy in the balcony? What the fuck is he talking about?"
    show gerangry at right with aaa
    hide gerstand with aaa
    g"...nngh...!"
    g"...my head..."
    g"..."
    show germad at right with aaa
    hide gerangry with aaa
    g"...ah!"
    
    scene black with dissolve
    scene bg01 with aaa
    show osstand at left with aaa
    show corstand at right with aaa    
    c"Do you think that Lilja went to another part of the tower?"
    o"*shrugs*"
    c"Well, I think Vosges should be next."
    o"..."
    c"You're right. I'll go check the balcony then."
    o"*nods*"
    c"Don't forget to call me if you need me!"
    scene black with dissolve
    pause 2
    
label base:
    stop music fadeout 1.5
    $ renpy.play('mizu.wav')
    pause 1
    $ renpy.play('mizu2.wav')
    pause 1
    $ renpy.play('mizu.wav')
    pause 1
    $ renpy.play('mizu2.wav')
    pause 1
    scene black with dissolve
    pause 1
    scene bg02 with aaa
    show bg02a with aaa
    show osstand at left with aaa
    show vostand at right with aaa
    o"..."
    play music"vosges_theme.ogg"
    v"Never in my life have I received so many visits in one day. What do you want this time?"
    o"..."
    v"Where is your shadow? Without him we can't communicate."
    o"..."
    show oswrites at left with aaa
    hide osstand with aaa
    r"Os takes a little book out of her pocket and starts writing something. Then she hands it to Vosges."
    show osstand at left with aaa
    hide oswrites with aaa
    v"Well, that was unexpected."
    v"Let's see... 'Where did you read about the star?'"
    show vosmile at right with aaa
    hide vostand with aaa
    v"Hmph. You really do have amnesia, don't you."
    show vostand at right with aaa
    hide vosmile with aaa
    v"I got that information from one of the books you so kindly left for me here..."
    v"All of them bear the stamp of the Great Library of Ulla. Even the corrupted volumes."
    v"I have no idea how you managed to counterfeit that mark. You really went to great lengths to make sure I couldn't tell the corrupted books from the authentic ones, didn't you?"
    o"..."
    v"No matter... it's telling that you simply dumped all those books, both real and fake, into this festering shithole."
    v"It's incredible how a kingdom like Ulla, whose victories are founded on violence and sadism, has this kind of abandoned knowledge..."
    v"And it's even more incredible how you've completely disregarded that heritage." 
    o"..."
    v"More questions?"
    o"*nods*"
    show oswrites at left with aaa
    hide osstand with aaa
    r"The small ritual of paper and pencil resumes."
    show osstand at left with aaa
    hide oswrites with aaa
    show voswut at right with aaa
    hide vostand with aaa
    v"Oh. The note."
    v"Of course I was telling the truth about the note. Even though I despise you, Os, I am not like you."
    show vostand at right with aaa
    hide voswut with aaa
    v"I wouldn't try to kill you, or stab that thing on your neck."
    show osmile1 at left with aaa
    hide osstand with aaa
    o"..."
    show vosblush at right with aaa
    hide vostand with aaa
    v"Why... are you smiling?"
    show oswrites at left with aaa
    hide osmile1 with aaa
    o"*writes*"
    show osstand at left with aaa
    hide oswrites with aaa    
    show vosmad at right with aaa
    hide vosblush with aaa
    v"Because I'm a good kid? I'm not a kid!"
    show vostand at right with aaa
    hide vosmad with aaa
    v"I think the one you should doubt... {w}is Corvus."
    o"?"
    v"He seems very false to me. Especially when he said that he would give his life for you. That's extremely hard to believe, especially given his... circumstances..."
    show oswrites at left with aaa
    hide osstand with aaa
    o"*writes*"
    show osstand at left with aaa
    hide oswrites with aaa
    v"You really trust him? If so, why isn't he here?"
    show oswrites at left with aaa
    hide osstand with aaa
    o"*writes*"
    show osstand at left with aaa
    hide oswrites with aaa
    v"'He's very annoying and when he is around all of you are upset.'"
    v"{color=#adc6ba}{i}...I think she doesn't realize we are upset because of her.{/i}{/color}"
    show oswrites at left with aaa
    hide osstand with aaa
    o"*writes*"
    show osstand at left with aaa
    hide oswrites with aaa
    v"A favor? You have some nerve, asking a favor from an enemy."
    v"But I must say I'm quite curious. So, spill the beans."
    menu:
        
        "What can I do to make you not hate me?":
         jump vosroute2
        
        "Call for Corvus.":
         jump coroute1
         
             
label vosroute2:
    $ vosges += 2
    show oswrites at left with aaa
    hide osstand with aaa
    o"*writes*"
    show osstand at left with aaa
    hide oswrites with aaa
    v"...?"
    v"Are you serious?"
    o"*nods*"
    v"I hate you, and there's nothing you can do to change that. Believing that it's possible is egotistical of you."
    show oswrites at left with aaa
    hide osstand with aaa
    o"*writes*"
    show osstand at left with aaa
    hide oswrites with aaa
    v"What would make me happy? That's a difficult question."
    show vosmile at right with aaa
    hide vostand with aaa
    v"I've realized that even if I manage to get out of Ulla and start again, there will be always this knot in my chest."
    v"I will never recover from the horrors you've inflicted upon me."
    show vostand at right with aaa
    hide vosmile with aaa
    v"So my answer is: I can be half-happy if I'm free."
    o"..."
    v"I really don't know what are you trying to pull. Perhaps you are faking so you can mock me like you used to. Well, too bad. I'm tired of your tricks."
    o"*shakes*"
    v"You aren't faking it? I find that very hard to believe, Os."
    v"Do you remember how you massacred my people? Do you remember what my village looked like before you devoured it all with your cold blue flames?"
    o"..."
    v"I do. Even now, in my dreams, I can see every stream, every field, every single blade of slick, shimmering grass."
    v"I grew up in that village. I was happy there, even though my parents worked me to the bone. Our village had always been enslaved by Ulla, so we pushed ourselves constantly to meet the expectations of your people."
    v"I first saw you when you came to visit the crop camp. You were so small and frail. I remember you even talked to the elders asking if we needed something. I thought{w} you were nice."
    v"Of course, months later, I realized I was wrong. Wrong to judge people by their looks. And to worse, to trust them so easily. I couldn't understand back then because I was a child, but now I know." 
    v"People like you exist."
    o"..."
    v"Please leave."
    o"*shakes*"
    show oswrites at left with aaa
    hide osstand with aaa
    o"*writes*"
    show osstand at left with aaa
    hide oswrites with aaa
    v"I'm not reading anything else you write."
    o"...{w}*nods*"
    hide osstand with aaa
    v"You are not fooling me again..."
    pause 1
    stop music fadeout 1.5
    scene black with dissolve
    scene bg01a with aaa
    show ncorstand at right with aaa
    show nosstand at left with aaa
    c"My lady, you're back!"
    c"Did that shroom say something useful?"
    o"...*nods*"
    c"Oh. {color=#adc6ba}{i}I want to ask more... argh!{/i}{/color}"
    jump cho4
    
label coroute1:
    $ corvus += 1
    show oswis at left with aaa
    hide osstand with aaa
    $ renpy.play('karasu1.mp3')
    with hpunch
    v"What's-"
    $ renpy.play('fall.wav')
    c"{size=10}mmm{/size}{size=11}mmm{/size}{size=12}mmm{/size}mmmmMY LADY!!"
    hide oswis with aaa
    show osstand at left with aaa
    c"What did this shroom do to you?!"
    show cormad2 at left with aaa
    v"I did nothing. What are you scheming, Os?"
    hide cormad2 with aaa
    hide osstand with aaa
    show oswrites2 at left with aaa
    o"*writes*"
    hide oswrites2 with aaa
    show osstand at left with aaa
    show corstand2 at left with aaa
    show voswut at right with aaa
    hide vostand with aaa
    v"What? Don't be ridiculous."
    c"?"
    show vostand at right with aaa
    hide voswut with aaa
    v"She's asking me to be your friend..."
    c"My lady, why is that?"
    o"..."
    c"But-"
    v"You can't force people to do whatever you want. I don't hate Corvus like I hate you, but he's not the kind of person I'd like to hang with."
    hide corstand2 with aaa
    hide osstand with aaa
    show oswrites2 at left with aaa
    o"*writes*"
    hide oswrites2 with aaa
    show osstand at left with aaa
    show corstand2 at left with aaa
    show scene1 with dissolve
    r"But both of you are good and kind."
    hide scene1 with aaa
    c"..."
    v"..."
    c"Let me think about it, my lady. I think Vosges needs to rest now. Why don't we return to your room?"
    o"*nods*"
    hide osstand with aaa
    hide corstand2 with aaa
    show corstand at left with aaa
    v"Wait, Corvus."
    c"What?"
    v"Don't play tricks with me. I know you're just doing this to please her."
    c"You don't trust my word? I may look like a bird, but I'm also a man. I said I would think about it, and so I will."
    c"Also. Even though it may be hard to believe... I do not hate you, Vosges. What I hate is that special treatment you received from Lady Os."
    v"What are you talking about?"
    c"Hah. And you're supposed to be the smart one..."
    v"Wait, what are you-"
    c"It's late."
    c"Go to sleep, kid."
    hide corstand with aaa
    v"I'm not a-"
    v"..."
    stop music fadeout 1.5
    scene black with dissolve
    scene bg01a with aaa
    show nosstand at left with aaa
    show ncorstand at right with aaa
    o"..."
    c"Ah, we had a little talk."
    o"..." 
    c"{color=#adc6ba}{i}What Vosges said may be partly true. I said that because I want to make you happy. My lady... why are you trying so hard to mend things?{/i}{/color}"
    c"{color=#adc6ba}{i}It's as if... you're feeling guilty...{/i}{/color}"
    o"...?"
    c"Oh, I'm sorry. I was lost in my thoughts..."
    jump cho4
    
label cho4:   
    c"Oh, right! I went to the balcony and that weirdo is still there!"
    c"I asked him if he saw Gervase and he told me that he only saw a cute puppy peeing on his books."
    c"Maybe Gervase can't see him?"
    o"*shrugs*"
    c"I don't think we'll get anything useful out of Lilja, but since there isn't anybody else to interrogate..."
    o"*nods*"
    pause 1
    gup2"...Wait!"
    window hide
    show ngerpup1 at right with aaa
    cup"Gervase? What are you doing here?"
    show gerpup3 at right with aaa
    hide ngerpup1
    gup2"Shut up, liar."
    gup2"I just remembered... that you were with Os in that room! My mind's hazy on the details, but you were doing something weird to her!" 
    gup2"You're the culprit!"
    cup"!!"
    cup"Stop-"
    r"Gervase tries to bite Corvus-"
    $ ui.timer(1.0, ui.jumps("coroute2"))
    menu:
         "Stop Gervase!":
            jump geroute2

label geroute2:
    $ gervase += 1
    scene black with dissolve
    scene bg01a with aaa
    show gerpup5 at center with vpunch
    show ncorstand at right with aaa
    g"Ahh!"
    g"You bitch!"
    g"Let go of me, goddamnit-"
    c"My lady!"
    g"Don't interfere, you-"
    hide ncorstand with flashbulb3
    $ renpy.play('punch1.mp3')
    with vpunch
    c"Ngh!"
    o"!!"
    hide gerpup5 with flashbulb3
    $ renpy.play('punch.wav')
    with hpunch
    show nosstand at left with aaa
    show gerpup3 at right with aaa
    pause 1
    gup2"You're doing it again, Os. Even if I try to be loyal to you like the FUCKING DOG I am, you always betray my trust."
    gup2"I hope you suffer for the rest of your life..."
    o"..."
    hide gerpup3 with aaa
    pause 1
    r"Corvus is on the floor unconscious."
    o"..."
    show nosmad2 at left with aaa
    window hide dissolve
    scene black with dissolve
    pause 1
    jump watch
    
label coroute2:
    $ corvus += 1
    scene black with aaa
    $ renpy.play('punch3.mp3')
    with hpunch
    c"Ngg-"
    scene bg01a with dissolve
    show nosstand at left with aaa
    show gerpup3 at center with aaa
    o"!!"
    r"Corvus falls to the floor violently."
    show nosmad2 at left with aaa
    show coroute1a with aaa
    pause 1
    hide coroute1a with aaa
    show gerpup4 at center with flashbulb2
    hide gerpup3
    gup2"{color=#adc6ba}{i}Those eyes! She's going to beat me up-!{/i}{/color}"
    gup2"Y-you will get what you deserve, Os. I came to warn you but you're just too stubborn to listen!"
    hide gerpup4 with dissolve
    hide nosmad2 with aaa
    o"..."
    pause 1
    window hide dissolve
    scene coroute1 with dissolve
    csub"M-my lady...I'm..."
    csub"...sorry..."
    show bg01a with dissolve
    hide coroute1 with aaa
    show nosstand at center with aaa
    window show dissolve
    r"Corvus passes out."
    o"..."
    pause 1
    show nosmad1 at center with aaa
    hide nosstand with aaa
    o"I'm the one who is sorry, Corvus."
    scene black with dissolve
    
label watch:
    r"You decided to go to the balcony..."
    scene black with dissolve
    $ renpy.play('foot1.wav')
    pause 3
    scene bg04a with aaa
    show nlilstand at right with aaa
    show nosstand at left with aaa
    window show dissolve
    l"..."
    l"We meet again, Lady Os."
    o"..."
    l"May I ask you something?"
    o"*nods*"
    l"What... do you find interesting about being mortal?"
    r"Os takes out her notebook and writes something."
    show noswrites at left with aaa
    hide nosstand with aaa
    o"*writes*"
    show nosstand at left with aaa
    hide noswrites with aaa
    l"So you don't know."
    l"That's great, because I don't care what you think."
    o"..."
    l"Life is too short. It's so short that I won't be able to fulfill even a single one of my dreams."
    l"Life must really suck for mortals."
    l"Every time I wake up, I remember I have one day less to live. It makes me think that no matter what I do, it's never going to make a difference."
    l"Because in the end {w}I'm going to die."
    l"And after death, there's nothing else. {w}No food, no books... no more me."
    l"Can you imagine that? A world without this glorious being in it?" 
    l"Life sure sucks for mortals."
    r"Lilja is utterly depressed..."
    menu:
        "Cheer him up.":
            jump lilroute1
            
        "Do nothing.":
            jump room2
            
label lilroute1:
    $ lilja += 4
    window hide dissolve
    show lilroute1 with dissolve
    pause 5
    scene bg04a with dissolve
    show nlilstand at right with aaa
    show nosstand at left with aaa
    window show dissolve
    l"So you're pitying me..."
    l"That's what I get for acting this uncool..."
    show noswrites at left with aaa
    hide nosstand with aaa
    o"*writes*"
    show nosstand at left with aaa
    hide noswrites with aaa
    l"Oh, no no no. Stop that."
    l"I know you're faking."
    o"..."
    pause 1
    show nosmile1 at left with aaa
    hide nosstand with aaa
    o"You knew?"
    l"When I said I could see the curse, I wasn't lying."
    l"But I only saw death surrounding the knife. That doesn't have anything to do with muteness or amnesia."
    o"I see."
    show nosstand at left with aaa
    hide nosmile1 with aaa
    o"It's better this way. I couldn't fake it much longer anyway."
    l"Why are you doing this?"
    o"Because, as you said, the life of a mortal sucks."
    o"There's nothing I could do to make a difference. Life is harsh and short."
    o"It overwhelms you-"
    l"Ah, stop it. I'm getting a headache-"
    o"I'm sorry."
    l"I think you should go. It's very late already."
    o"Are you going to be fine?"
    l"I think."
    scene black with aaa
    l"After all, I'm a God. {w}Patron of the suicidals..."
    scene bg01a with dissolve
    show nosstand at left with aaa
    jump room3
    
label room2:
    r"Os decides that it's better to leave him alone."
    scene black with dissolve
    scene bg01a with aaa
    
label  room3:
    $ renpy.play('corsleep.ogg')
    r"Corvus is still resting after the encounter with Gervase, and slowly, Os falls asleep too."
    r"It's been a long day."
    $ renpy.play('osigh.ogg')
    scene black with dissolve
    pause 2
    scene bg01b with aaa
    show osstand at left with aaa
    show corstand at right with aaa
    pause 1
    c"Lady Os..."
    o"..."
    c"I'm sorry about yesterday... G-Gervase wasn't lying. I should explain myself."
    o"That's ok, Corvus. I'm all ears."
    hide corstand with aaa
    show corsur2 at right with aaa
    c"M-my lady?! You can...?!"
    o"Yes."
    hide corsur2 with aaa
    show corstand at right with aaa
    c"Since?"
    o"Since forever. I faked being mute for a while because I needed time..."
    o"...time to figure out this mess of a situation..."
    pause 1
    hide osstand with aaa
    show osmad1 at left with aaa
    o"I'm confused, Corvus."
    play music"oscorvus_theme.ogg"
    o"Why..."
    o"Why I am still alive?"
    c"..."
    hide corstand with aaa
    show corsad at right with aaa
    r"Corvus has an incredibly sad face."
    c"So you were faking your amnesia too?"
    o"I'm sorry..."
    show osstand at left with aaa
    hide osmad1
    c"I can't believe it, my lady. You seemed so strong, so radiant..."
    c"How could you intend to commit suicide like that? If something was making you unhappy, you could have told...{w}me."
    hide corsad with aaa
    show corstand at right with aaa
    o"It didn't seem that way."
    show osmad1 at left with aaa
    hide osstand with aaa
    o"I felt like everything and everyone had turned against me. And I ended crashing myself against a wall."
    o"It all started when my father's health decayed."
    o"He shifted more and more responsibility to me until I ended up sitting on the throne."
    o"Did you know, Corvus...? It felt like I was sitting on the rubble of my childhood."
    o"The crown crushed my skull, and my mind inside it."
    hide osmad1 with aaa
    show osmad3 at left with aaa
    o"My chest collapsed inwards with every breath I took. But I had to keep on breathing. I had to give my best for my father, for Ulla."
    o"So I did. I kept breathing. I kept moving. I burnt up all my feelings so I could blind everybody with my brightness."
    o"Why is the sun so brilliant, Corvus? Because without hesitation, it eats itself up from the inside... and by doing so, reigns as the most majestic thing in the sky."
    c"My lady..."
    hide osmad3 with aaa
    show osmad1 at left with aaa
    o"I went on war after war, slaying sinners and innocents alike."
    o"All those years of nothing but bones and guts, and below all of that... {w}me."
    o"..."
    o"I decided then..."
    hide corstand with aaa
    show corsad at right with aaa
    c"Don't. Please, I don't want to hear anymore."
    o"..."
    o"Are you going to explain yourself, Corvus?"
    hide corsad with aaa
    show corstand at right with aaa
    c"...yes."
    pause 1
    show osstand at left with aaa
    hide osmad1 with aaa
    c"When you disappeared on your 17th birthday, the palace descended into chaos."
    c"I tore through the castle, searching for you..."
    c"...until I thought of checking my room."
    c"There I found a note which said that I had to go to the tower to get my reward. It also gave me the way to pass the barrier."
    c"I thought you were planning something, but I couldn't figure out what."
    c"I didn't want to stir everybody up even more, so I didn't say anything and just left."
    c"Gervase was downstairs, so I flew through the window of the kitchen and went silently in search of you..."
    c"Finally, I found you on the third floor... {w}just to see you stabbing yourself with a knife."
    show osmad1 at left with aaa
    hide osstand with aaa
    hide corstand with aaa
    show corsad at right with aaa
    c"By the time I reached your side, you were staring at the ceiling. Dead."
    c"Lady Os, you are going to hate me for what I've done..."
    c"But before I confess, I just wanted to say..."
    c"I do not regret what I did. And I never will."
    show osstand at left with aaa
    hide osmad1 with aaa
    o"I can't judge what I don't know, so speak."
    c"Very well."
    hide corsad with aaa
    show corstand at right with aaa
    c"Do you know what a pillar is?"
    o"It's a kind of chant."
    c"Yes, it is. It's a very powerful chant, capable of bringing even the dead back to life. But it has its cost."
    c"That day I invoked a pillar to resurrect you. In exchange, I needed to take years off the life of others."
    c"In other words, you are alive because you have one year of life of each person who was in the tower at that moment."
    hide corstand with aaa
    show corsad at right with aaa
    c"For four years, we have been dead, accompanying you till you could wake up. And it worked! As soon as I saw you alive again,{w} I... {w}I..."
    c"When you said you had amnesia, I thought that it was for the best... that you didn't remember the sorrow that drove you to this..."
    c"So I pretended that I didn't know what happened."
    show osmad2 at left with aaa
    hide osstand with aaa
    o"How could you?! You didn't gave a damn about what I wanted or about the others in the tower?"
    c"..."
    hide corsad with aaa
    show corstand at right with aaa
    c"No. I didnt care."
    o"Why?"
    c"I-"
    c"I'm an egotist. And I do not expect you or the others here to forgive me."
    hide osmad2 with aaa
    show osmad3 at left with aaa
    o"Corvus. I wanted to die. Couldn't you see that?"
    c"I did. But I wonder... why were you being nice to the others in the tower?"
    hide osmad3 with aaa
    show osstand at left with aaa
    c"Did you enjoy it?"
    show oswut at left with aaa
    o"!"
    hide oswut with aaa
    hide osstand with aaa
    show osmad3 at left with aaa
    o"I just felt... so much guilt."
    show osmad1 at left with aaa
    hide osmad3 with aaa
    o"But they wouldn't stop hating me anyway. I've messed up their lives too much to be forgiven."
    c"Lady Os, why don't you see this as a second chance? Death won't bring you happiness, but what about this change of heart?"
    show osstand at left with aaa
    hide osmad1 with aaa
    o"That's impossible."
    c"It doesn't have to be."
    pause 1
    hide corstand with aaa
    show cormad at right with aaa
    c"Damn it, Os, it's not every day you come back to life."
    o"Corvus..."
    o"Don't you hate me too?"
    hide  cormad with aaa
    show corstand at right with aaa
    c"Eh? Why would I-"
    show osmad1 at left with aaa
    hide osstand with aaa
    o"Because my father killed your family."
    hide corstand with aaa
    show corsad at right with aaa
    c"..."
    o"He made you my servant, when you were the heir of Ter, a magnificent country as powerful as Ulla."
    o"And my father destroyed it. Everything and everyone you loved. Just like I did to Vosges."
    o"I don't understand. Why don't you hate me?"
    hide corsad with aaa
    show corstand at right with aaa
    c"Do you want me to?"
    show osstand at left with aaa
    hide osmad1 with aaa
    o"...no."
    c"Then why are you asking me that question?"
    c"Promise me that you will give this a thought."
    o"Fine."
    c"I'll leave you alone then. I should visit Lilja and Vosges to confess my sin... Gervase must still be mad at me."
    o"..."
    stop music fadeout 1.5
    show osooo at left with aaa
    o"Corvus...!"
    c"Hmm?"
    menu:
        "Forgive him.":
          jump coroute3
        "Say nothing.":
            jump lilroute2
    
    
label coroute3:
    $ corvus += 1
    $ vosges -= 2
    o"I...I can't speak for everyone, but-"
    hide osooo with aaa
    o"I forgive you, for what have you done."
    c"..."
    c"I don't deserve it."
    o"Of course not."
    c"Ehh?"
    hide osstand with aaa
    show oshe at left with aaa
    o"I was joking. Ahaha... ha..."
    r"Silence."
    pause 1
    hide oshe with aaa
    show osmile1 at left with aaa
    o"Thank you, Corvus."
    hide corstand with aaa
    show corblush2 at right with aaa
    c"{color=#adc6ba}{i}I... I... I don't know what to say...{/i}{/color}"
    c"I-it's nothing!"
    hide corblush2 with aaa
    r"Corvus leaves the room, his face red."
    scene black with dissolve
    c"...Mother, Father..."
    c"Please forgive me."
    c"I'm a pathetic son after all."
    c"...I may really have fallen in love with her."
    pause 1
    jump end
        
label lilroute2:
    $ gervase -= 4
    hide osooo with aaa
    o"..."
    c"..."
    c"Think about it, please."
    hide corstand with aaa
    r"Corvus leaves the room with a sad face."
    show osmad1 at left with aaa
    hide osstand with aaa
    o"..."
    pause 1
    l"So that's why... I became mortal."
    show lilstand at right with aaa
    o"Were you listening, Lilja?"
    l"I couldn't help it."
    l"So, it was that bird's fault, huh?"
    o"It was all because of me."
    o"I didn't want to get you involved... I'm sorry..."
    l"Your apology is as strong as a mosquito bite."
    show osstand at left with aaa
    hide osmad1 with aaa
    l"It {i}is{/i} mostly your fault, you know? You should've just killed yourself quickly instead of praying to me for strength."
    l"I had no choice but to come and bless you so you could succeed."
    l"In the end, I'm paying the price for being a good patron."
    l"I should have listened to my colleagues. Honest work doesnt suit a God."
    o"..."
    l"Make yourself responsible for this mess!"
    o"How?"
    l"Give me my year of life back and I should at least be able to return to heaven."
    show osmad1 at left with aaa
    o"That's fine with me."
    l"Really?"
    menu: 
        "Yeah, I don't care anymore.":
           jump sad
        "Actually... I can't.":
            jump lilroute3
            
label sad:
    $ lilja -= 4
    o"I don't care. Take all the years that you want."
    l"..."
    l"What a boring mortal you are."
    l"Why don't you run through the window and kill yourself already."
    hide lilstand with aaa
    o"..."
    scene black with dissolve
    pause 1
    jump end
    
label lilroute3:
    $ lilja += 1
    show osstand at left with aaa
    hide osmad1 with aaa
    o"No. I don't want to."
    l"And why is that?"
    o"Because life is short, and if I'm going to die, I want to enjoy every year I have."
    l"..."
    l"What a boring mortal you are."
    show osmad2 at left with aaa
    hide osstand with aaa
    l"Why don't you run through the window and kill yourself already."
    o"Why don't you kill yourself instead."
    o"All you do is complain about being a suckish mortal."
    show lilsmile at right with aaa
    hide lilstand with aaa
    l"HAHAHAHAAAHHAHA! I like that!"
    show lilstand at right with aaa
    hide lilsmile with aaa
    hide osmad2 with aaa
    show osstand at left with aaa
    show oswut at left with aaa
    o"Eh?"
    l"I'm sick of being the patron of the suicidals. Having to help people kill themselves is so depressing."
    l"But you're different. I like your guts."
    l"I bet they're tasty."
    hide oswut with aaa
    o"You're weird."
    l"You and your birdy made me like that. I used to be totally normal."
    o"There must be a way... to return you to heaven."
    l"I certainly hope so."
    l"Well. I have to go clean my books now. They smell like piss."
    show osmile2 at left with aaa
    hide osstand with aaa
    o"*snicker*"
    l"By the way, Lady Os..."
    show osmile1 at left with aaa
    hide osmile2 with aaa
    o"Hmm?"
    l"You have a lovely voice."
    show oswut at left with aaa
    o"...eh?"
    show lilsmile at right with aaa
    hide lilstand with aaa
    l"AHAHAHAHAHAHHAA."
    show osstand at left with aaa
    o"..."
    scene black with dissolve
    pause 1
    jump end
    
label end:
    scene black with dissolve
    play music"oscorvus_theme.ogg"
    r"The sun floats to the top of the sky. Os is immersed in her thoughts."
    pause 2
    scene bg01 with dissolve
    show osstand at left with aaa
    c"My lady, I found some juicy cockroaches for you!"
    show corstand at right with aaa
    o"Corvus."
    c"Y-yes?"
    o"I've lifted the barrier."
    c"That means that..."
    show osmile1 at left with aaa
    hide osstand with aaa
    o"We're leaving this place. All of us will finally be free." 
    show osstand at left with aaa
    hide osmile1 with aaa
    o"You're right, Corvus. Dying won't solve anything."
    o"I'll pull this knife out and lift the curse I placed on myself."
    o"From now on, I'm going to give everything I have left, and see what happens."
    hide corstand with aaa
    show corcrys at right with aaa
    c"My lady...! You don't know how happy I am to hear that!"
    c"I'm going to tell everyone the good news!"
    o"Wait."
    hide corcrys with aaa
    show corstand at right with aaa
    c"Yes, my lady?"
    o"Before that, I want to..."
    menu:
        "...see the mushrooms in the basement.":
            jump vosroutefinal
        "...eat something in the kitchen.":
          jump geroutefinal
        "...watch the sunset before it gets dark.":
          jump lilroutefinal
        "...tell you something." if corvus == 5:
           jump coroutefinal 
           
label vosroutefinal:
        if vosges == 5:
           jump vosgood
        else:
           jump vosbad
label vosgood:
    $ persistent.end_01 = True
    $ persistent.ending = "Ending 1"
    o"I think I'm going to see the mushrooms at the basement..."
    c"The mushrooms? Oh."
    c"You mean... Vosges?"
    o"What? N-no..."
    c"Ah. Ahahaha. He's so lucky."
    o"Hmm?"
    c"Nothing, my lady. I will wait for you here, then."
    o"Right."
    scene black with dissolve
    $ renpy.play('foot1.wav')
    r"Corvus looks at Os as she disappears into the the basement. Something glitters in his eye."
    c"...it's for the best."
    pause 1
    stop music fadeout 1.5
    scene black with dissolve
    scene bg02 with aaa
    show vostand at right with aaa
    show osstand at left with aaa
    v"Oh, it's you again."
    o"..."
    show osooo at left with aaa
    o"Rejoice, prisoner of the tower where the watchdog resides, for you shall claim the reward..."
    show voswut at right with aaa
    v"!!"
    hide osooo with aaa
    v"You...!"
    show osooo at left with aaa
    o"...of being able to survive the witch. Today she shall die, with her throat slit open, and her shameful blood will gush onto the floor."
    hide osooo with aaa
    o"That was what your note said, right?"
    v"You were the one who wrote it?"
    v"Why-?"
    hide osstand with aaa
    show osknife at left with dissolve
    o"Because I'm the real traitor of Ulla."
    play music"v_end.ogg"
    scene black with aaa
    $ renpy.play('swordhit.wav')
    pause 0.1
    scene bg02 with dissolve
    show snowblossom
    show oskstand at left with aaa
    show vostand at right with aaa
    show vosaaa at right with aaa
    v"Ahh!"
    o"I stabbed this knife into my own neck that day. I no longer desired to live."
    show vosangry at right with aaa
    hide vosaaa with aaa
    v"You are incredibly egotistical, Os. Egotistical..."
    hide vosangry with aaa
    v"...and stupid."
    v"What did you expect me to do in this tower? Enjoy myself while I saw your dead body?"
    o"..."
    v"Eat your limbs? Throw the corpse into acid? I don't understand."
    v"I don't understand-"
    o"Vosges..."
    show vosangry  at right with aaa
    hide vostand with aaa
    v"Shut up! I despise people like you! You just ran away instead of facing up to what you did to us."
    v"Your death wouldn't have given me happiness. It would only have brought me more anger."
    v"How easy it is to die and let everyone go to hell."
    v"But that's ok, right? We're already too messed up to be saved-"
    o"That's not true."
    window hide aaa
    hide vosangry with aaa
    hide oskstand with aaa
    scene vosroute2 with dissolve
    osub"I can work hard to make this change."
    vsub"Stop.."
    vsub"...it..."
    osub"From now on, you are free, Vosges."
    scene bg02 with dissolve
    hide vosroute2 
    show snowblossom
    show oskstand at left with aaa
    show vostand2 at right with aaa
    show vosaaa at right with aaa
    o"You are free to do whatever you want."
    o"Back then you told me, that this would make you half-happy..."
    o"I'm not searching for your forgiveness, because I may never have that."
    o"Instead, please let me make you a little bit happier than before."
    hide vosaaa with aaa
    v"..."
    v"Don't do this. You should know I'm not better than you."
    v"After I read that horrible thing, I went out of the basement, hoping that I'd be able to see you to die with my own eyes."
    v"But I only made it to the first floor before turning back."
    v"Maybe I'm just a coward."
    o"You're a good kid, Vosges. Don't be so hard on yourself."
    v"I'm not a kid, Os. You know that."
    pause 0.1
    r"Silence."
    v"What are you going to do?"
    o"My father must be worried. I must return to his side."
    v"Will you go back to your old self?"
    stop music fadeout 1.8
    o"...I know that I just let you be free but... why don't you come with me, Vosges?"
    o"With you on my side, I'm sure I will never return to what I used to be."
    v"..."
    pause 2
    show oswut at left with aaa
    o"D-don't worry, you don't need to answer that."
    v"I will think about it, but I can't promise you anything."
    show osksmile at left with aaa
    hide oswut with aaa
    o"That's enough for me."
    hide vostand2 with aaa
    show vosmile2 at right with aaa
    v"..."
    hide osksmile with aaa
    o"Something wrong?"
    v"No... "
    v"I just feel..."
    scene black with dissolve
    v"...lighter."
    window hide dissolve
    pause 2
    play music "g_end.ogg"
    scene vosgend with dissolve
    pause 5
    jump lolcredits
    
label vosbad:
    o"I think I'm going to see the mushrooms at the basement..."
    c"The mushrooms? Oh."
    c"You mean, Vosges?"
    show oswut at left with aaa
    o"What? N-no..."
    c"Ah. Ahahaha. He's so lucky."
    hide oswut with aaa
    o"Hmm?"
    c"Nothing, my lady. I will wait for you here, then."
    o"Right."
    hide osstand with aaa
    pause 1
    c"...Well, it's for the best."
    scene black with dissolve
    $ renpy.play('foot1.wav')
    pause 3
    scene bg02 with aaa
    show vostand at right with aaa
    show osstand at left with aaa
    v"Oh, you again..."
    o"..."
    v"Corvus came and enlightened me as to exactly how much of an imbecile he is."
    v"It looks like you're alive because of us."
    v"Life sure is full of irony."
    o"How much did he tell you?"
    v"So you can speak now?"
    o"..."
    v"He told me that he found you dead, and in order to resurrect you, he invoked a pillar using our lives as sacrifices."
    v"What I can't understand is who tried to kill you. Was it Gervase, after all?"
    o"It was me."
    show voswut at right with aaa
    hide vostand with aaa
    v"Huh?"
    o"I stabbed this knife through my neck. I wanted to die."
    v"..."
    show vosangry at right with aaa
    hide voswut with aaa
    v"You are beyond unbelievable."
    v"So you were the one who sent me that note?"
    show osmad1 at left with aaa
    hide osstand with aaa
    o"Yes."
    o"I wanted you to be there. I knew you hated me enough to finish the job, just in case I couldn't bring myself to do it."
    v"..."
    o"Vosges, I-"
    show osstand at left with aaa
    hide osmad1 with aaa
    v"I don't want to listen to you anymore. Each time you come here, it gets more and more difficult to stop myself from slapping you."
    o"I won't go anywhere."
    v"You're just a vile coward, who makes one stupid mistake after another..."
    pause 1
    show osmad2 at left with aaa
    hide osstand with aaa
    o"You think you're better than me?"
    o"Keep playing the role of victim if you want. You're nothing but an ignorant fool!"
    v"How dare you-"
    scene vbadend with dissolve
    window hide
    osub"You think I killed your people just for fun?"
    osub"I lost half my troops in a day! All of them were poisoned... {w}by the crops that your people sent us. You were traitors!"
    osub"They deserved to die! To be burned to ashes and be eaten by worms... {i}all of them{/i}."
    scene bg02 with aaa
    show vosos1 at center with flashbulb3
    $ renpy.play('swordhit.wav')
    stop music fadeout 1.5
    v"!!"
    window show 
    o"Ah..."
    show vosos2 at center with dissolve
    hide vosos1 with aaa
    v"Just... die."
    oss"I will never regret..."
    scene black with dissolve
    window hide dissolve
    pause 2
    play music "b_end.ogg"
    scene vosbend with dissolve
    pause 5
    jump lolcredits
    
label geroutefinal:
         if gervase == 5:
           jump gergood
         else:
           jump gerbad          
label gergood:
    $ persistent.end_02 = True
    $ persistent.ending = "Ending 2"
    o"I'm hungry. I'm going to the kitchen to find something to eat. I think I saw some spiders running around in there..."
    c"To the kitchen? Don't you want me to accompany you?"
    o"Why?"
    c"Gervase might still be mad. It could be dangerous."
    o"Don't worry about that. He's my dog, after all. I would be a lame owner if I couldn't tame his anger."
    c"Be careful!"
    o"Don't worry."
    stop music fadeout 1.5
    scene black with dissolve
    $ renpy.play('foot1.wav')
    pause 3
    scene bg03 with aaa
    show osstand at left with aaa
    r"Gervase is sitting in the darkest corner of the kitchen."
    play music "ger_end.ogg"
    o"What are you doing there?"
    g"..."
    o"Gervase, I'm speaking to you."
    show osmad1 at left with aaa
    hide osstand with aaa
    g"Don't come any closer. I'll bite you if you do."
    show osmad2 at left with aaa
    hide osmad1 with aaa
    o"I don't take orders from my pet."
    g"I told you-!"
    hide osmad2 with aaa
    o"Stay still!"
    window hide dissolve
    show geroute3 with dissolve
    gsub"Let me go! Annoying bitch! ARGGGHH!"
    osub"No. I won't let you go this time."
    osub"I've been a horrible owner, and I know that's why you keep running away from me..."
    pause 1
    scene bg03 with dissolve
    show geros1 at center with dissolve
    window show
    g"You sure are a quick learner, huh?"
    o"I'm sorry, Gervase."
    g"..."
    o"I really am!"
    pause 1
    show geros2 at center with dissolve
    hide geros1 with aaa
    g"...*sniff*"
    o"Gervase...?"
    g"It's hair in my eyes, that's all...{w}*sniff* {w}A lot of hair..."
    pause 0.3
    hide geros2 with aaa
    show osstand at left with aaa
    show gerstand at right with aaa
    g"What happened to you, Os? We used to play together all the time, then out of nowhere you became like a beast."
    g"Even beasts were tamer than you."
    show osmad1 at left with aaa
    o"I became Ulla's butcher, Gervase. I was my father's sword, my kingdom's shield. I couldn't afford to have any weaknesses."
    o"I took all the cracks in me and melded them shut with the corpses of my enemies, so that every second of every day, I could be what everybody needed me to be - the supreme ruler of Ulla."
    show germad at right with aaa
    hide gerstand with aaa
    g"I didn't need you to be Ulla's butcher or whatever the fuck they call you!"
    show gerblush at right with aaa
    hide germad with aaa
    g"I just wanted you to be... you again..."
    show osmile1 at left with aaa
    hide osmad1 with aaa
    o"Gervase..."
    show osstand at left with aaa
    hide osmile1 with aaa
    o"I hated myself. I still do. That's why I have this thing on my neck."
    g"You mean that...!"
    show germad at right with aaa
    hide gerblush with aaa
    o"Yes, I stabbed it myself."
    g"..."
    show osmile2 at left with aaa
    hide osstand with aaa
    o"But it looks like it wasn't my time... I'm a little happy for that."
    o"Because now I can make it up to everyone..."
    show osmile1 at left with aaa
    hide osmile2 with aaa
    o"...to you."
    o"So... will you come with me again?"
    show gerangry at right with aaa
    g"...if you hit me again, I will kill you-"
    show osstand at left with aaa
    hide osmile1 with aaa
    o"I'll be prepared for that then, if that was a yes."
    show gerstand at right with aaa
    hide gerangry with aaa
    g"It was."
    o"Then let's get ready! I will see if I can fulfill your wish."
    show osmile2 at left with aaa
    hide osstand with aaa
    stop music fadeout 1.8
    g"What wish?"
    o"Your harem!"
    show gerblush at right with aaa
    hide germad with aaa
    g"Ah... I don't want one."
    show oswut at left with aaa
    o"Huh?"
    scene black with dissolve
    g"I only want you."
    scene black with dissolve
    window hide dissolve
    pause 2
    play music "g_end.ogg"
    scene gergend with dissolve
    pause 5
    jump lolcredits
    
label gerbad:
     o"I'm hungry. I'm going to the kitchen to find something to eat. I think I saw some spiders running around in there..."
     c"To the kitchen? Don't you want me to accompany you?"
     o"Why?"
     c"Gervase might still be mad...It could be dangerous..."
     o"Don't worry about that. He's my dog, after all. I would be a lame owner if I couldn't tame his anger."
     c"Be careful!"
     o"I said don't worry. I'll be fine!"
     scene black with dissolve
     $ renpy.play('foot1.wav')
     pause 3
     scene bg03 with aaa
     show osstand at left with aaa
     o"...Gervase, are you there?"
     r"You see him trembling in the corner."
     g"D-don't come any closer..!"
     hide osstand with aaa
     o"Why you- don't give me orders like you-"
     g"No!"
     o"Stay still, you dog!"
     g"I SAID BACK OFF- DAMNIT!"
     scene gbadend with flashbulb3
     $ renpy.play('swordhit.wav')
     window hide 
     osub"Ah..."
     gsub"...Os?"
     gsub"Os! Wake up...OS!"
     gsub"Goddamnit..." 
     scene black with dissolve
     g"I killed her."
     stop music fadeout 1.5
     pause 2
     g"..."
     c"Gervase?"
     g"C-Corvus!"
     c"...why are you looking at me like that?"
     g"I-I'm just tired, that's all..."
     c"Well, have you seen Lady Os? She said she was coming here to get some food..."
     g"...yeah, I saw her. She said she would go ahead to the castle. S-she said that you should go there too." 
     c"Ehh? That's strange. She said that we'd all leave here together. She's taken down the barrier, did you know that?"
     g"...{color=#adc6ba}{i}Together? That's impossible-{/i}{/color}"
     c"I'll get going then. You should come soon too, all right?"
     g"Right."
     g"{color=#adc6ba}{i}He's going to come back when he doesn't find her...{/i}{/color}"
     g"{color=#adc6ba}{i}I'm doomed, fuck damnit. I don't have time to hide the corpse.{/i}{/color}"
     g"{color=#adc6ba}{i}If only I weren't this hungry... I'd be able to think more clearly...{/i}{/color}"
     g"If I...weren't hungry..."
     window hide dissolve
     scene black with dissolve
     pause 2
     play music "b_end.ogg"
     scene gerbend with dissolve
     pause 5
     jump lolcredits
label lilroutefinal:
     if lilja == 5:
           jump lilgood
     else:
           jump lilbad 
label lilgood:
    $ persistent.ending = "Ending 3"
    $ persistent.end_03 = True
    o"I'm going to the balcony. It's almost time for the sunset."
    c"But my lady, aren't you afraid of heights?"
    o"I think I got kind of used to it..."
    c"{color=#adc6ba}{i}What, since yesterday?!{/i}{/color}"
    c"Watch your step while you're on the staircase."
    o"Fine."
    stop music fadeout 1.5
    scene black with dissolve
    $ renpy.play('foot1.wav')
    pause 3
    scene bg04 with aaa
    show lilstand at right with aaa
    show osstand at left with aaa
    pause 1
    l"Haven't you wondered..."
    l"...what kind of book I have on my hands?"
    o"I was just about to ask."
    l"It's a book filled with empty pages... except the first."
    l"A question is written there. A question that I cannot answer."
    o"What question?"
    l"'Who are you?'"
    l"I think I'm supposed to write the answer down in the blank pages, but-"
    l"Who am I?"
    l"I... don't know anymore."
    l"I hold this book, so when I find the answer... I can write it down here."
    o"...Lilja, it's time for us to leave this tower."
    l"..."
    l"You can go. I won't hold a grudge against you or that bird."
    l"Maybe I was meant to end like this. I will stay here and read all these books."
    o"Don't give up so easily! Don't you want to see your friends?"
    l"...I don't have friends..."
    show oswut at left with aaa
    o"Huh?"
    l"Nobody wants to be friends with a manic depressive like me. All the goddesses avoid me." 
    hide oswut with aaa
    l"I wish I had a girfriend." 
    show osmile2 at left with aaa
    o"*chuckles*"
    l"This isn't funny, you know."
    show osmile1 at left with aaa
    hide osmile2 with aaa
    o"Sorry... it's just that..."
    o"You sound like a complete loser."
    l"..."
    hide osmile1 with aaa
    o"But I can't picture you like that. You don't look like a loser."
    o"As you said before, you {i}are{/i} gorgeous."
    show lilsmile at right with aaa
    hide lilstand with aaa
    l"Pfft-{w}HAHAHAHAHHAHAHA!"
    play music"lilja_theme.ogg"
    l"You really have guts!"
    show lilstand at right with aaa
    hide lilsmile with aaa
    c"Lady Os...!"
    l"You should be my girlfriend."
    show oswut at left with aaa
    o"Eh?"
    show corsur at left with aaa
    c"WHAAAAT?!"
    show lilsmile at right with aaa
    hide lilstand with aaa
    l"HAHAHAHAHAHHAAHAH! Os, have you removed your barrier?"
    show lilstand at right with aaa
    hide lilsmile with aaa
    o"Y-yes, I did. Why?"
    l"Because it's time to say goodbye."
    o"Huh?"
    l"I will use all the remaining energy that I have to return."
    show osooo at left with aaa
    o"No! What if you don't make it?"
    l"It's better for me to try instead of whining all day."
    l"Sorry, but I will never understand the advantages of being mortal."
    o"..."
    l"SO!"
    hide lilstand  with flashbulb
    show lilnstand at right with aaa
    c"HOLY-"
    show osblussh at left with aaa
    hide corsur
    show corblush at left with aaa
    o"...!"
    hide corblush with aaa
    show coros1 at left with aaa
    hide osblussh with aaa
    hide osstand with aaa
    hide osooo with aaa
    hide oswut with aaa
    c"Did you have to strip yourself?!"
    l"Yes. Where I come from, it's called fanservice."
    c"..."
    show coros2 at left with aaa
    hide coros1 with aaa
    o"And what about the book?"
    show lilnsmile at right with aaa
    hide lilnstand 
    l"Fuck the book."
    l"I've had a lot of fun already."
    window hide dissolve
    show lilroute2 with dissolve
    osub"..."
    osub"Do you think we will see him again?"
    csub"Who knows, my lady."
    csub"I just hope that he visits us again. With pants."
    stop music fadeout 1.5
    scene black with dissolve
    window hide dissolve
    pause 2
    play music "g_end.ogg"
    scene lilgend with dissolve
    pause 5
    jump lolcredits
   
label lilbad:
    scene black with dissolve
    $ renpy.play('foot1.wav')
    pause 3
    scene bg04 with aaa
    show osstand at left with aaa
    show lilstand at right with aaa
    o"..."
    o"It's beautiful."
    l"It is?"
    o"Yes."
    l"But beauty is useless."
    o"I know."
    show oscry at left with dissolve
    l"Why are you crying?"
    o"Because I lied. I'm not leaving this tower with all of you."
    stop music fadeout 1.5
    o"At least, not by the door."
    scene black with aaa 
    $ renpy.play('run.wav')
    l"You-!"
    $ renpy.play('wind2.mp3')
    window hide dissolve
    scene lbadend with flashbulb2
    pause 3
    scene black with dissolve
    pause 2
    play music "b_end.ogg"
    scene lilbend with dissolve
    pause 5
    jump lolcredits
    
label coroutefinal:
    stop music fadeout 1.5
    $ persistent.ending = "Ending 4"
    $ persistent.end_04 = True 
    show osooo at left with aaa
    o"I-I want to tell you something."
    play music "cor_theme.ogg"
    hide osooo with aaa
    c"Hmm? What's that, my lady?"
    o"I..." 
    c"...?"
    c"My lady, can I be bold and ask you a favor?"
    o"Yes, it's fine."
    c"Please take that knife off your neck..."
    o"Ah. Right, the knife."
    hide osstand with aaa
    show osknife at left with dissolve
    o"Nggh..."
    c"Lady Os!"
    window hide aaa
    scene black with aaa
    $ renpy.play('swordhit.wav')
    scene coroute2a with flashbulb
    pause 1
    show coroute2b with dissolve
    osub"Eh?"
    pause 1
    window show dissolve
    scene bg01 with dissolve
    show oskstand at left with aaa
    show corhstand at right with dissolve
    show snowblossom
    o"...!" 
    show corhshout at right with aaa
    hide corhstand with aaa
    c"My lady! Are you all right?"
    show oswut at left with aaa
    o"That face... are you Corvus?"
    show corhsmile1 at right with aaa
    hide corhshout with aaa
    c"Why, of course. Ah, you've never seen me like this before, right?"
    hide oswut with aaa
    o"No..."
    c"Lord Skedel prohibited me from showing myself like this in front of you."
    o"Why is that?"
    c"I don't know, my lady."
    show osksmile2 at left with aaa
    hide oskstand with aaa
    o"You're handsome!"
    show corhblush2 at right with aaa
    hide corhsmile1 with aaa
    c"Eh?"
    show oskblush at left with aaa
    hide osksmile2 with aaa
    o"D-did I say that out loud?"
    c"...y-yes...?"
    r"A few moments pass in awkward silence."
    pause 1
    show corhsmile2 at right with dissolve
    hide corhblush2 with aaa
    c"What did you want to tell me?"
    o"W-would you like...to come with me to the castle?"
    c"But... I already live there."
    show oskstand at left with aaa
    hide oskblush with aaa
    o"Not as a servant, Corvus."
    o"As an equal."
    show corhsur at right with aaa
    hide corhsmile2 with aaa
    c"My lady... I'm very grateful, but Lord Skedel won't allow that."
    show corhstand at right with aaa
    hide corhsur with aaa
    o"I'll talk to him. I can't just follow his will forever, you know?"
    c"My lady...!"
    show corhgah at right with aaa
    hide corhstand
    c"Please... stop. All you're doing is giving me false hope."
    o"What are you talking about?"
    c"...{color=#adc6ba}{i}Would it be fine to tell her?{/i}{/color}"
    show corhstand at right with aaa
    hide corhgah with aaa
    hide oskstand with aaa
    show osehh at center with aaa
    o"Corvus? You're trembling.."
    c"..."
    c"I-I'm sorry..."
    c"But I can't stand it anymore."
    window hide dissolve
    scene coroute2 with dissolve
    osub"."
    osub".."
    osub"..."
    pause 2
    window show dissolve
    scene bg01 with dissolve
    show snowblossom
    show coros3 at center with dissolve
    o"!"
    c"I love you."
    o"What are you doing?! YOU IDIOT-!"
    hide coros3 with flashbulb3
    $ renpy.play('punch.wav')
    with vpunch
    show oskblush at left with aaa
    show corhit at right with aaa
    c"Ow!"
    o"That was my first..."
    show corhblush2 at right with aaa
    hide corhit with aaa
    c"Your first...?!"
    hide corhblush2 with aaa
    show corhgasp at right with aaa
    c"L-L-Lady Os, I'm so sorry- I didn't mean- please forgive this good-for-nothing servant!"
    o"...Stop it."
    show oskstand at left with aaa
    hide oskblush with aaa
    c"Huh?"
    stop music fadeout 1.5
    o"I told you. You're my equal now."
    c"My lady..."
    hide oskstand with aaa
    show oskblush2 at left with dissolve
    o"Here, take my hand."
    hide corhgasp with aaa
    show corhblush at right with dissolve
    c"Yes... my lady."
    scene black with dissolve
    window hide dissolve
    pause 2
    play music "g_end.ogg"
    scene corend with dissolve
    pause 5

label lolcredits:
    scene black with dissolve
    scene splash1 with aaa
    show cr01 with dissolve
    pause 3
    hide cr01 with aaa
    show cr01a with dissolve
    pause 3
    hide cr01a with aaa
    show cr02 with dissolve
    pause 4
    hide cr02 with aaa
    show cr03 with dissolve
    pause 4
    hide cr03 with aaa
    show cr04 with dissolve
    pause 6
    hide cr04 with aaa
    show cr05 with dissolve
    pause 6
    hide cr05 with aaa
    show cr06 with dissolve
    pause 5
    hide cr06 with aaa
    stop music fadeout 1.5
    pause 2
    scene black with dissolve   
    if  persistent.end_01 and persistent.end_02 and persistent.end_03 and persistent.end_04:
        jump extra
    else:
       return
     
label extra:
    scene black with dissolve
    stop music fadeout 1.5
    pause 1
    play music"ecc_theme.ogg"
    scene bg05 with dissolve
    l"I-I can't believe I made it..."
    show lilnstand at right with dissolve
    l"It feels I've been travelling for ages.."
    l"..."
    l"I don't remember this place being so... boring."
    r"Ahh!"
    l"?"
    l"Oh, it's you, Ecchin."
    show eccblush at left with dissolve
    e"For the love of God, Lilja, cover your disgrace."
    l"It's not my fault you're so short that your face is in my crotch."
    hide eccblush with aaa
    show eccmad at left with aaa
    e"Why- you...!"
    l"Did you miss me?"
    show eccstand at left with aaa
    hide eccmad with aaa
    e"You went somewhere?"
    r"Silence."
    l"Yes... I was away for four years..."
    e"Ah. I didn't notice."
    r"Silence."
    l"I see. No matter where I go... the only thing that awaits me is my own depression."
    e"Come on, dude. Cheer up a little."
    e"Oh! I know what can cheer you up!"
    r"She takes a photo out of her pocket."
    l"What's this?"
    e"Hehehe, it's me in a swimsuit!"
    l"I don't see the appeal. You're a horrible goddess of fanservice."
    show eccmad at left with aaa
    hide eccstand with aaa
    e"W-W-W-WHAT?!"
    l"You know what? We should totally change jobs. Your photo makes me want to kill myself."
    e"LILJA YOU BAST-"
    l"You lack impact! Emotion! Who the hell gave you this job-"
    l"I'm gonna show you-"
    hide lilnstand with aaa
    hide eccmad with aaa
    show fs with flashbulb
    pause 2
    show lilnstand at right with aaa
    show eccstand at left with aaa
    e"-What the fuck?!"
label fanservice:
    
    menu:
        
        "Gakuen Traitor":
           jump gatr
        "Rule 63":
           jump r63
        "Fanservice Os I":
            jump fso1
        "Haircuts":
           jump hcuts
        "Fanservice Os II":
            jump fs02
        "Pantyshot (it's not what you think)":
            jump pshot
        "On the Beach":
            jump beach
        "PLEASE, NO MORE":
               jump exitt
               
label gatr:
    scene black with dissolve
    window hide
    show fn03a with dissolve
    pause 1
    cq"Holy moly! What's this?!"
    lq"I bet we would be more popular this way."
    vq"Why do I have to lend you all my glasses?"
    lq"Because you are a mix of various fetishes."
    vq"Ehh?!"
    scene fn03b with dissolve
    window hide
    pause 1
    cq"GYAHAHAHAHA!"
    vq"Excellent way to look uncool."
    lq"..."
    gq"What?! I can't see anything."
    scene fn03c with dissolve
    window hide
    pause 1
    gq"Woah! I look so... smart!"
    vq"No."
    cq"Gahahaha- no."
    scene fn03d with dissolve
    window hide
    pause 1
    vq"I-its not that I like you or anything-"
    cq"Shh! Lady Os is watching! Just smile... he he he..."
    oq"..."
    scene black with dissolve
    show bg05 with aaa
    show lilnstand at right with aaa
    show eccstand at left with aaa
    jump fanservice
    
label  r63:
    scene black with dissolve
    vq"What's this rule 63?"
    lq"There is always a female version of a male character..."
    vq"This is going to be so wrong..."
    scene fn04a with dissolve
    window hide
    pause 1
    cq"OH MY GOD-"
    gq"Take that off the screen please!"
    cq"*sniff*"
    vq"You are surprisingly cute as a girl..."
    gq"Hahahaha, Vosges likes girls his size."
    vq"SHUT UP!"
    scene fn04b with dissolve
    window hide
    pause 1
    cq"Ugh."
    gq"Fuck! It should be a sin to be this sexy."
    vq"I guess it doesnt matter what sex you are, Gervase. You will always be stupid."
    cq"GYAHAHA!"
    gq"Sh-shut up you-"
    scene fn04c with dissolve
    window hide
    pause 1
    cq"..."
    vq"..."
    gq"I don't get it."
    scene fn04d with dissolve
    window hide
    pause 1
    cq"W-"
    vq"-H-"
    gq"-AT!"
    lq"I was totally expecting this."
    scene fn04e with dissolve
    window hide
    pause 1
    cq"M-my lady?!"
    gq"I can't believe she looks more macho than us."
    vq"I knew that this was going to be so wrong."
    scene black with dissolve
    show bg05 with aaa
    show lilnstand at right with aaa
    show eccstand at left with aaa
    jump fanservice
    
label fso1:
    scene black with dissolve
    window hide dissolve
    scene fn01 with dissolve
    pause 2
    cq"..."
    vq"..."
    gq"I think I can see her underwear..."
    cq"Is the only thing you can think about? Underwear?"
    vq"Of course it is."
    gq"COME ON! Don't tell me you aren't looking! Are you really guys?"
    vq"That doesn't mean you have to think with your testicles."
    cq"I agree with the kid."
    lq"There's nothing to be ashamed of, you two. The world goes around sex."
    vq"You were looking too, right?"
    lq"...yes."
    oq"HEY GUYS! Did you know I made a new law?"
    oq"Every pervert caught red handed, will be impaled by the BUTT!"
    oq"You heard me?!"
    pause 1
    oq"...h-hey, it was just a joke! Ha... haha..."
    scene black with dissolve
    show bg05 with aaa
    show lilnstand at right with aaa
    show eccstand at left with aaa
    jump fanservice
    
label hcuts:
    scene black with dissolve
    scene fn05 with dissolve
    window hide
    pause 1
    cq"Dannn"
    vq"Dannnnnn"
    gq"DANNNNNNN"
    lq"LAHHHHHHHHHHHHHHHHHHHHHHHH"
    scene black with dissolve
    show bg05 with aaa
    show lilnstand at right with aaa
    show eccstand at left with aaa
    jump fanservice
    
label fs02:
    scene black with dissolve
    scene fn02 with dissolve
    window hide
    pause 1
    cq"M-m-m-my lady!"
    gq"Yummy!"
    cq"SHUT UP YOU FILTHY PERVERT! I won't allow you to look at my lady's body like that!"
    gq"...what body? Her hair reminds me of cotton candy."
    cq"..."
    gq"You sure are a dirty bird..."
    scene black with dissolve
    show bg05 with aaa
    show lilnstand at right with aaa
    show eccstand at left with aaa
    jump fanservice

label pshot:
  scene black with dissolve
  scene fn06 with dissolve
  window hide
  pause 1
  cq"I-I wasn't expecting anything else!"
  vq"...me neither."
  gq"You liars..."
  scene black with dissolve
  show bg05 with aaa
  show lilnstand at right with aaa
  show eccstand at left with aaa
  jump fanservice
  
  
label beach:
    scene black with dissolve
    scene fn07 with dissolve
    window hide
    pause 1
    cq"Lala"
    vq"Lalalala"
    gq"LAAAAAAAAAHH"
    lq"LAAAALALLLAAAAAAAAAAALA"
    scene black with dissolve
    show bg05 with aaa
    show lilnstand at right with aaa
    show eccstand at left with aaa
    jump fanservice
    
label exitt:
    l"Do you really want to exit? You won't be able to see this after you get out!"
    e"That's lame you know?"
    menu:
        
        "yes":
            l"Ah, it can't be helped."
            l"Well, thank you so much for wasting your precious mortal minutes with us." 
            l"The god of gaming will be pleased with this offering."
            l"Hope you enjoyed this gorgeous game!"
            e"Heh. Yeah right-"
            hide lilnstand with aaa
            show lilbye at right with aaa
            l"BYE!"
            window hide dissolve
            scene black with dissolve
            stop music fadeout 1.5
            pause 1
            return
        "No":
            l"Ah! Excellent."
            jump fanservice
