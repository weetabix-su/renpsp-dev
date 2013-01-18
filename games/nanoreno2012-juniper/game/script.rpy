init:
    image weet cred = "weet/portcred.jpg"
    image 3panel_a = "img/3panel_a.png"
    image 3panel_b = "img/3panel_b.png"
    image 3panel_c = "img/3panel_c.png"
    #WEETABIX NOTE: Instead of character-defining, we use pseudo-speechbubbles
    image bubble fnd = "img/ui/textbox_fnd.png"
    image bubble boy = "img/ui/textbox_boy.png"
label start:
    scene weet cred
    $renpy.pause(2)
    scene black
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