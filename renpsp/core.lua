-------------------
--- CORE FUNCS ----
-------------------

RENPY = {}
PERSISTENT = {}

function clearEngineState()
	return {
		state = {
			text = {},
			is_error = false,
			hide_text = false,
			menu = {active=1},
			chars = {},
			current_file = 'none',
			current_position = '0',
			env = {
				None  = nil,
				True  = true,
				False = false
			},
			music = {}
		},
		script = {
			gamelabels = {},
			gamefile = nil,
			continue = true,
			exit = false
		},
		timer = {
			timer_type = 'none',
			main_timer = Timer.new(),
			time_to_wait = nil
		},
		conf = {
			autoplay_time = 5000
		},
		fmenu = {
		},
		media = {
			names = {},
			images = {},
			imgcache = {},
			background = 'black'
		},
		history = {
			states={},
			i=0
		},
		control = {},
		homepath = GAME_curdir(),
		curgamepath = nil,
		cursavepath = nil
	}
end

ENGINE = clearEngineState()

function ENGINE:CtrlMenu(pad, oldpad)
	if pad:cross() and not oldpad:cross() and not self.state.is_error then
		self.script.continue = true
	elseif pad:up() and not oldpad:up() then
		if self.state.menu.active ~= 1 then
			self.state.menu.active = self.state.menu.active - 1
		end
	elseif pad:down() and not oldpad:down() then
		if self.state.menu.active ~= table.maxn(self.state.menu.a) then
			self.state.menu.active = self.state.menu.active + 1
		end
	end
end


function ENGINE:CtrlGame(pad, oldpad)
	if pad:start() and not oldpad:start() then
		self:FallingMenu()
	elseif pad:square() and not oldpad:square() then
		self.state.hide_text = not self.state.hide_text
	elseif pad:circle() and not oldpad:circle() then
		self.control.debug = not self.control.debug
	elseif pad:triangle() and not oldpad:triangle() then
		flutter = os.date("%Y%m%d%H%M%S")
		if CURRENT_SYSTEM == "WIN" then
			screen:save("screenshot.png")
		else
			if GAME_chkDir("ms0:/PICTURE/RenPSP") == false then
				GAME_makeDir("ms0:/PICTURE/RenPSP")
			end
			screen:save("ms0:/PICTURE/RenPSP/screenshot_"..tostring(flutter)..".png")
		end
	elseif pad:cross() and not oldpad:cross() and not self.state.is_error then
		self.state.hide_text = false
		if CURRENT_SYSTEM == "LPE" then
			ENGINE:Timer(100)
		else
			self.script.continue = true
		end
	elseif pad:l() and not oldpad:l() then
		self:PrevState()
	elseif pad:r() and not oldpad:r() and not self.state.is_error then
		self:NextState()
	end

	if self.state.menu.a ~= {} then
		if 	pad:up() and not oldpad:up() then
				if self.state.menu.active ~= 1 then
					self.state.menu.active = self.state.menu.active - 1
				end
		elseif 	pad:down() and not oldpad:down() then
				if self.state.menu.active ~= table.maxn(self.state.menu.a) then
					self.state.menu.active = self.state.menu.active + 1
				end
		end
	end

end

function ENGINE:DrawGame()
	if self.media.colors[self.media.background]~=nil then
		screen:clear(self.media.colors[self.media.background])
	else
		screen:blit(0, 0, self.media.background)
	end
	for name,ch in pairs(self.state.chars) do
		self:ShowChar(name)
	end
	if not self.state.hide_text then
		self:DrawMenu(self.state.menu)
	end
end

function ENGINE:DrawMenu(menu)
	if table.maxn(menu.a)~=0 then
		self.state.text = {menu.q}
		local y0 = (200 - table.maxn(menu.a)*25)/2
		if table.maxn(self.state.text)==0 then
            y0 = y0 + 40
        end
		for i=1,table.maxn(menu.a) do
			local l = menu.a[i]
			if i == menu.active then
				l = '>> '..l..' <<'
			end
			screen:blit(110, y0+(i-1)*25-2, self.media.answer_frame)
			TEXT:WriteLineCenter(y0+(i-1)*25,l)
		end	
	end

	if table.maxn(self.state.text)~=0 then
		screen:blit(0, 200, self.media.text_frame)
		TEXT:WriteParagraph(10,205,self.state.text,66)
		if self.control.debug then
		   	ENGINE:DrawDebug()
		end
	end
end

function ENGINE:DrawDebug()
	if CURRENT_SYSTEM == "WIN" then
		textdbg = 'Lua Player Windows: Debug Mode'
	else
		textdbg = 'System.getFreeMemory: ' .. tostring(System.getFreeMemory())
	end
	GAME_superblit(
			0,
			0,
			self.media.text_frame,
			0,
			GAME_imageheight(self.media.text_frame)-15,
			480,
			GAME_imageheight(self.media.text_frame)
		)
	TEXT:WriteLineCenter(2,textdbg)
end

function ENGINE:ErrorState(error_text)
	GAME_print('ERROR:'..error_text)
	self.script.continue = false
	self.state.text = {'ERROR:',error_text}
	self.state.is_error = true
end

function ENGINE:TextBoxOut(textin)
        self.script.continue = false
        self.state.text = {textin}
end

function ENGINE:ControlInit()
	self.control.pad = Controls.read()
end

function ENGINE:Control(func)
	self.control.oldpad = self.control.pad
	self.control.pad = Controls.read()
	self[func](self,self.control.pad,self.control.oldpad)
end

function ENGINE:DebugPrintCtrl(pad,oldpad)
	if pad:cross() and not oldpad:cross() then
		press = true
	end
end

function ENGINE:DebugPrint(txt)
	press = false
	local white = Color.new(255, 255, 255)
	while not press do
		GAME_draw()
			GAME_clear()
			screen:clear(white)
			TEXT:WriteParagraph(30,30,{'>'..txt..'<'},420)
		GAME_nodraw()	
		ENGINE:Control('DebugPrintCtrl') 
	end
end
