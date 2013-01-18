init:
    image weet cred = "weet/portcred.jpg"
    #3-Panel intro
    image 3panel_a = "img/3panel_a.png"
    image 3panel_b = "img/3panel_b.png"
    image 3panel_c = "img/3panel_c.png"
    #CGs
    image in 0 = "img/cg/in0.png"
    #WEETABIX NOTE: Instead of character-defining, we use pseudo-speechbubbles
    image bubble fnd = "img/ui/textbox_fnd.png"
    image bubble boy = "img/ui/textbox_boy.png"
label start:
    scene weet cred
    $renpy.pause(2)
    scene juniperblack
    $renpy.pause(1)
    show 3panel_a
    $renpy.pause(1)
    show 3panel_b
    $renpy.pause(1)
    show 3panel_c
    $renpy.pause(6)
    "Much of these stone walls and floors have weathered into dirt and dust, revealing the foundation."
    "Much of the ceiling, too, has crumbled to the ground, layering in flecks and bits."
    "Below me now is such tired soil."
    "Tired, tired soil."
    show bubble fnd
    "Pah..."
    hide bubble
    "... There isn't much to do here but burn dead leaves and wait."
    "Watch the smoke rise—curl up fresh and tickle the inside of your nose."
    "Dull as bones, it is."
    "But what can I do? I'm stuck."
    "Some might say cursed; I'd rather say bound."
    "I don't like to think very much about it."
    hide 3panel_a
    hide 3panel_b
    hide 3panel_c
    $renpy.pause(1)
    scene in 0
    $renpy.pause(2)
    "I kneel to the small fire I've started, taking up a few embers and loam into my palm."
    "It's this glow that stirs me and reminds me that my heart is still beating."
    "I bring the scorched earth close to my face, shut my eyes and breathe it in. I taste it and spit."
    "It's barren."
    "I'm probably going to wait here for ever."
    