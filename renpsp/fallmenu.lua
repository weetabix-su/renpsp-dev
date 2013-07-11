function ENGINE:CtrlConf(pad,oldpad)
	if 	pad:cross() and not oldpad:cross() then
			confexit=true
			if confmenu.active == 1 then
				self.conf.autoplay_time = 0
			elseif confmenu.active == 2 then
				self.conf.autoplay_time = 5000
			elseif confmenu.active == 3 then
				self.conf.autoplay_time = 9100
			end
	elseif 	pad:up() and not oldpad:up() then
			if confmenu.active ~= 1 then
				confmenu.active = confmenu.active - 1
			end
	elseif 	pad:down() and not oldpad:down() then
			if confmenu.active ~= table.maxn(confmenu.a) then
				confmenu.active = confmenu.active + 1
			end
	end
end

HELPFILE = nil

function ENGINE:CtrlFallingMenu(pad,oldpad)
	if pad:start() and not oldpad:start() then
		menuexit = true
	elseif pad:right() and not oldpad:right() then
		if self.fmenu.menuactiveitem <6 then
			self.fmenu.menuactiveitem = self.fmenu.menuactiveitem + 1
		else
			self.fmenu.menuactiveitem = 1
		end
	elseif pad:left() and not oldpad:left() then
		if self.fmenu.menuactiveitem >1 then
			self.fmenu.menuactiveitem = self.fmenu.menuactiveitem - 1
		else
			self.fmenu.menuactiveitem = 6
		end
	elseif pad:cross() and not oldpad:cross() then
		local munuaction = falling_menu[self.fmenu.menuactiveitem].comment
		menuexit = true
		if munuaction == "help" then
			if HELPFILE == nil then
				self:Help()
			elseif HELPFILE ~= nil then
				self:Help(HELPFILE)
			end
		elseif munuaction == "load" then
			loadconf = self:Load()
                        if loadconf == false then
                            self:ErrorState('Default save file not found.')
                        end
		elseif munuaction == "save" then
			self:Save()
		elseif munuaction == "conf" then
			confexit = false
			
			confmenu = {q='Select skipping speed',a={},active=1}
			confmenu.a[1]='as fast as possible'
			confmenu.a[2]='5 seconds'
			confmenu.a[3]='more than 9000 milliseconds'
			while not confexit do
				GAME_draw()
					screen:clear(Color.new(255, 255, 255))
					self:DrawMenu(confmenu)
					self:Control('CtrlConf')
				GAME_nodraw()
			end
		elseif munuaction == "skip" then
			self.conf.autoplay = not self.conf.autoplay
			if self.conf.autoplay then
				self:Timer(self.conf.autoplay_time,'auto')
				self.script.continue = true
			else
				self:TimerStop()
			end
		elseif munuaction == "exit" then
			self.script.exit = true
		end
	end
end

function ENGINE:DrawFallingMenu(y)
	for i,el in pairs(falling_menu) do
		if i == self.fmenu.menuactiveitem then
			screen:blit((i-1)*FALLING_MENU_DX+FALLING_MENU_X0-3, y-3, falling_menu_bframe)
		end
		screen:blit((i-1)*FALLING_MENU_DX+FALLING_MENU_X0, y, el.image)
	end
end

function ENGINE:FMenu(i)
	GAME_draw()
		self:DrawGame()
		self:DrawFallingMenu(i)
	GAME_nodraw()
end

function ENGINE:FallingMenu()
	self:TakeScreenshot()
	for i=-20,1 do self:FMenu(i*4) end

	menuexit = false
	while not menuexit do
		self:FMenu(5)
		self:Control('CtrlFallingMenu')
	end

	ENGINE:SavePersistent()
	for i=-20,1 do self:FMenu((-19-i)*4) end
end
