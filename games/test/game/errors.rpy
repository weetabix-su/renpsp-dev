label errortesting:
    scene white
    menu:
        "undefined bg":
            scene something_unknown
        "undefined char":
            show somebody_unknown
			"..."
        "undefined jump":
            jump somewhere_unknown
        "undefined sayer":
            somebody_unknown "No error?"
        "Lua error":
            $ something wrong
        "Back to Main Menu":
            jump start
    jump errortesting
