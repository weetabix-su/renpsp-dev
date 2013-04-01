init:
    image bg ext musclub day = "ext_musclub_day.jpg"
    image bg int musclub day = "int_musclub_day.jpg"

    image cg     rowrow= "rowrow.jpg"

    image cccp   sad   = "cccp_sad.png"
    image cccp   happy = "cccp_smile1.png"

    image slavya sad   = "slavya_sad.png"
    image slavya happy = "slavya_smile1.png"
	
	$ egghunt = 0


label never:
    "Непоказанный текст"

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
        "Описание возможностей":
            menu:
                "Структура сценария":
                    jump scen
                "Фоны и персонажи":
                    jump bgch
                "Встроенные функции":
                    jump func
        "Menu, if, else test":
            jump ifelsetest
        "On-Screen Keyboard":
            jump osk

label scen:
    "В данный момент подгружаются все *.rpy файлы из каталога /game/ игры. Каждый файл содержит код, совместимый с обычным RenPy (http://renpy.org)."
    jump start

label bgch:
    "scene - команда смены фона и удаления всех персонажей с экрана"
    scene red
    "Есть возможность использовать цвета как фон:\n\n    scene red"
    scene green
    $renpy.pause(0.5)
    scene blue
    $renpy.pause(0.5)
    scene black
    $renpy.pause(0.5)
    scene gray
    $renpy.pause(0.5)
    scene white
    "Пока что только предопределенные цвета в файле media.lua"
    scene black
    "Другой вариант - изображение в качестве фона"
    "Сначала нужно выполнить команду image, связывающую имя изображения (\"cg rowrow\") с именем файла (\"ext_musclub_day.jpg\"):\n\n    image bg ext musclub day = \"ext_musclub_day.jpg\""
    scene bg ext musclub day
    "Затем мы можем указать имя изображения как параметр для scene:\n\n    scene cg rowrow"
    "Персонажи объявляются той же коммандой image:\n\n    image cccp happy = \"cccp_smile1.png\""
    show cccp happy
    "Команда show выводит персонажа:\n\n    show cccp happy"
    show cccp happy at right
    "Можно указать позицию:\n\n    show cccp happy at right"
    show slavya happy at left
    "Можно указать позицию:\n\n    show slavya happy at left"
    hide slavya
    "Можно скрывать персонажей:\n\n    hide slavya"
    show cccp sad at center
    "Можно двигать персонажей и менять эмоции:\n\n    show cccp sad at center"
    "Пока что это все"
    jump start

label func:
    "Функция задержки:\n\n    $renpy.pause(sec), где sec - время задержки"
    scene black
    $ renpy.pause(3)
    scene blue
    $ renpy.pause(3)
    scene black
    "Вот как этот работает"
    "Блокировка перемотки обратно:\n\n    $block_rollback()"
    $ renpy.block_rollback()
    "Попробуйте перемотать обратно - не получится"
    "Для остановки игры можно использовать:\n\n    $renpy.quit()"
    menu:
        "Не выходить":
            pass
        "Выйти":
            $ renpy.quit()
    "Для перехода по меткам:\n\n    $renpy.jump(lbl) - перейти к метке lbl\n    $renpy.has_label(lbl) - проверить существование метки lbl"
    $ sample = 'exist'
	$ samplekill = 'afkjsdfkljawddf'
    if renpy.has_label(sample) and not renpy.has_label(samplekill):
		$ renpy.jump(sample)
    else:
        "FAIL"

label exist:
    "Эта метка существует"
    jump start

label osk:
	"ACHTUNG!" "The following feature has been recently tested on a PSP-2000 on 5.50 Gen-D Prometheus-4. The results are not stellar."
	"Continue?"
	menu:
		"Yes":
			jump oskcont
		"No":
			egghunt = egghunt + 1
			if egghunt < 7:
				jump easter
			else:
				jump menu

label oskcont:
    "weetabix segment:" "On-Screen Keyboard"
    "If you want to use the on-screen keyboard, use the following function:" "renpy.input(desc,def)" "" "(Where 'desc' = input description; 'def' = default answer)"
    "Usage:\n\n$ varosk = renpy.input('Test keyboard','DEFAULT OUTPUT')" "(Where variable 'varosk' is assigned to the output of the OSK)"
    "Please note that this function is only compatible with Lua Player Euphoria and Lua Player Plus. Using Lua Player 0.20 on Windows or PSP will only return the default value." "" "Press X to continue."
    jump osknow

label osknow:
    $varosk = renpy.input('Test keyboard','DEFAULT OUTPUT')
    if varosk == "DEFAULT OUTPUT":
        "Output unchanged!"
        jump oskdone
    else:
        $varflunk = ("Output is \""..varosk.."\"")
        $renpy.text(varflunk)

label oskdone:
    menu:
        "Repeat OSK":
            jump osknow
        "Main Menu":
            jump start
        "Quit":
            $renpy.quit()
			
label easter:
	"EASTER EGG MODE ACTIVATED!"
	"lol just kidding, return to menu."
	egghunt = 0
	jump menu