-- this folder
ROOT_FOLDER = System.currentDir()

-- folder of RenPSP engine
RENPSP_FOLDER = ROOT_FOLDER.."/renpsp"

-- folder to store game dirs
GAMES_FOLDER = ROOT_FOLDER.."/games"

-- SHOULD be "LPE"/"LPP"/"WIN"
CURRENT_SYSTEM = "LPP"

-- SHOULD be true or false/nil
SHOW_FPS = false       

System.currentDir(RENPSP_FOLDER)
dofile("main.lua")