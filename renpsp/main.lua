soundon = nil
if CURRENT_SYSTEM == "LPE" then
	soundchk = System.msgDialog("Turn on sound?",true)
	if soundchk == System.MSGDIALOG_RESULT_YES then
		soundon = true
	elseif soundchk == System.MSGDIALOG_RESULT_NO then
		soundon = false
	elseif soundchk == System.MSGDIALOG_RESULT_BACK then
		soundon = false
	elseif soundchk == System.MSGDIALOG_RESULT_UNKNOWN1 then
		soundon = false
	end
elseif CURRENT_SYSTEM == "LPP" then
	soundon = true
else
	soundon = false
end

dofile("platform.lua")
GAME_CPU(333)

-------------------
---- INCLUDES -----
-------------------
dofile("core.lua")
dofile("fakepython.lua")
dofile("fallmenu.lua")
dofile("help.lua")
dofile("lucida1251.lua")
dofile("media.lua")
dofile("saveload.lua")
dofile("script.lua")

-------------------
-- SYSTEM START ---
-------------------

GAME_start()
ENGINE:ControlInit()
TEXT:UseFont('lucida_w')
GAME_CPU(222)

RenpyClass(RENPY)
GAME_curdir('..')

ENGINE:SelectGame(GAMES_FOLDER)
ENGINE:PrepareAllInPath('game')
ENGINE:LoadPersistent()
ENGINE:GotoStart()

-------------------
---- MAIN LOOP ----
-------------------

while not ENGINE.script.exit or ENGINE.timer.time_to_wait do
	if ENGINE.script.continue then
		while ENGINE.script.continue and not ENGINE.state.is_error do
			ENGINE:Eval()
		end
		ENGINE:PushState()
	end
	
	GAME_draw()
		GAME_clear()
		ENGINE:DrawGame()
	GAME_nodraw()
	
	if ENGINE.timer.time_to_wait then
		if ENGINE.timer.main_timer:time()>ENGINE.timer.time_to_wait then
			ENGINE:TimerStop()
			ENGINE.state.hide_text = false
			ENGINE.script.continue = true
		end
	end

	if ENGINE.timer.time_to_wait == nil or ENGINE.timer.timer_type ~= 'auto' then
		ENGINE:Control('CtrlGame')
	end
end

ENGINE:SavePersistent()
GAME_quit()
