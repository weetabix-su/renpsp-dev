init:
    image bg ext musclub day = "ext_musclub_day.jpg"
    image bg int musclub day = "int_musclub_day.jpg"

    image cg     rowrow= "rowrow.jpg"

    image cccp   sad   = "cccp_sad.png"
    image cccp   happy = "cccp_smile1.png"

    image slavya sad   = "slavya_sad.png"
    image slavya happy = "slavya_smile1.png"


label never:
    "������������ �����"

label start:
    scene black
    menu:
        "persistent":
            "before"
            if not persistent.x:
                $ persistent.x = 1
            else:
                $ persistent.x = persistent.x + 1
            $ renpy.print(persistent.x)
            "after"
            jump start
        "�������� ������������":
            menu:
                "��������� ��������":
                    jump scen
                "���� � ���������":
                    jump bgch
                "���������� �������":
                    jump func
        "Menu, if, else test":
            jump ifelsetest
        "Errors gallery":
            jump errortesting

label scen:
    "� ������ ������ ������������ ��� *.rpy ����� �� �������� /game/ ����. ������ ���� �������� ���, ����������� � ������� RenPy (http://renpy.org)."
    jump start

label bgch:
    "scene - ������� ����� ���� � �������� ���� ���������� � ������"
    scene red
    "���� ����������� ������������ ����� ��� ���:\n\n    scene red"
    scene green
    $renpy.pause(0.5)
    scene blue
    $renpy.pause(0.5)
    scene black
    $renpy.pause(0.5)
    scene gray
    $renpy.pause(0.5)
    scene white
    "���� ��� ������ ���������������� ����� � ����� media.lua"
    scene black
    "������ ������� - ����������� � �������� ����"
    "������� ����� ��������� ������� image, ����������� ��� ����������� (\"cg rowrow\") � ������ ����� (\"ext_musclub_day.jpg\"):\n\n    image bg ext musclub day = \"ext_musclub_day.jpg\""
    scene bg ext musclub day
    "����� �� ����� ������� ��� ����������� ��� �������� ��� scene:\n\n    scene cg rowrow"
    "��������� ����������� ��� �� ��������� image:\n\n    image cccp happy = \"cccp_smile1.png\""
    show cccp happy
    "������� show ������� ���������:\n\n    show cccp happy"
    show cccp happy at right
    "����� ������� �������:\n\n    show cccp happy at right"
    show slavya happy at left
    "����� ������� �������:\n\n    show slavya happy at left"
    hide slavya
    "����� �������� ����������:\n\n    hide slavya"
    show cccp sad at center
    "����� ������� ���������� � ������ ������:\n\n    show cccp sad at center"
    "���� ��� ��� ���"
    jump start

label func:
    "������� ��������:\n\n    $renpy.pause(sec), ��� sec - ����� ��������"
    scene black
    $ renpy.pause(3)
    scene blue
    $ renpy.pause(3)
    scene black
    "��� ��� ���� ��������"
    "���������� ��������� �������:\n\n    $block_rollback()"
    $ renpy.block_rollback()
    "���������� ���������� ������� - �� ���������"
    "��� ��������� ���� ����� ������������:\n\n    $renpy.quit()"
    menu:
        "�� ��������":
            pass
        "�����":
            $ renpy.quit()
    "��� �������� �� ������:\n\n    $renpy.jump(lbl) - ������� � ����� lbl\n    $renpy.has_label(lbl) - ��������� ������������� ����� lbl"
    $ sample = 'exist'
    if renpy.has_label(sample) and not renpy.has_label('afkjsdfkljawddf'):
        $ renpy.jump(sample)
    else:
        "FAIL"

label exist:
    "��� ����� ����������"
    jump start

#WEETABIX NOTE: FORBIDDEN SEGMENT STARTS HERE, UNTIL WE GET THE OSK FIXED
label osk:
    "weetabix segment:" "On-Screen Keyboard"
    if CURRENT_SYSTEM == "LPE":
        "Detected Lua Player:" "Lua Player Euphoria"
        jump oskcont
    elif CURRENT_SYSTEM == "LPP":
        "Detected Lua Player:" "Lua Player Plus"
        jump oskcont
    elif CURRENT_SYSTEM == "WIN":
        "Detected Lua Player:" "Lua Player 0.20 (Windows/PSP)"
        jump oskcont

label oskcont:
    "If you want to use the on-screen keyboard, use the following function:" "renpy.input(desc,def)" "" "(Where 'desc' is the input description and 'def' is the default answer)"
    "Usage:\n\n$ varosk = renpy.input('Test keyboard','DEFAULT OUTPUT')" "(Where the variable 'varosk' is assigned to the output of the OSK)"
    "Please note that this function is only compatible with Lua Player Euphoria and Lua Player Plus. Using Lua Player 0.20 on Windows or PSP will only return the default value." "" "Press X to continue."
    jump osknow

label osknow:
    $varosk = renpy.input('Test keyboard','DEFAULT OUTPUT')
    $self.state.text = {'KEYBOARD OUTPUT:\n\n'..varosk}
    jump oskdone

label oskdone:
    menu:
        "Repeat OSK":
            jump osknow
        "Main Menu":
            jump start
        "Quit":
            $renpy.quit()