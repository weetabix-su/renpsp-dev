label ifelsetest:
    $ cccp = 0
    $ slavya = 0
label menulabel:
    menu:
        "USSR-tan":
            menu:
                "show happy":
                    show cccp happy at right
				    $ cccp = 1
                "show sad":
                    show cccp sad at right
				    $ cccp = -1
                "hide":
                    hide cccp
				    $ cccp = 0
        "Slavya":
            menu:
                "show happy":
                    show slavya happy at left
				    $ slavya = 1
                "show sad":
                    show slavya sad at left
				    $ slavya = -1
                "hide":
                    hide slavya
				    $ slavya = 0
	if slavya == cccp:
    	if slavya > 0:
			"Both are happy"
    	elseif slavya == 0:
			"Nobody shown"
    	else:
			"Both are sad"
	elif slavya*cccp:
		"One is happy, other is sad"
	else:
		if slavya:
			"USSR-tan is hidden"
		else:
			"Slavya is hidden"
    jump menulabel
