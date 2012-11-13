WGPATH = RENPSP_FOLDER.."/skin/"

-------------------
--- BACKGROUNDS ---
-------------------

function ENGINE:Scene(bg)
	if  self.state.bgname == bg then
		return
	end
	self.state.bgname = bg

	if self.media.colors[bg]~=nil then
		self.media.background = bg
	elseif self.media.images[bg]~=nil then
		GAME_print('loading background '..bg..' from '..self.media.images[bg])
		self.media.background = Image.load(self.media.images[bg])
	else
		self.media.background = 'black'
		self:ErrorState('ENGINE:scene('..bg..') failed to find bg')
	end
end

function ENGINE:ClearScene()
	if self.media.images[self.state.bgname] == nil then
		return
	elseif self.media.images[self.state.bgname] ~= nil then
       	GAME_print('self.media.background to clear (LPE ONLY) = '..self.media.images[self.state.bgname])
		if CURRENT_SYSTEM == "LPE" then
            self.media.prevbg = self.media.background
            self.media.background = 'black'
           	Image.free(self.media.prevbg)
		elseif CURRENT_SYSTEM ~= "LPE" then
			return
		end
	end
end

-------------------
--- CHARACTERS ----
-------------------

function ENGINE:ClearChars()
	self.state.chars = {}
	for who,what in pairs (self.media.imgcache) do 
		self.media.imgcache[who].surf:clear()
		-- if CURRENT_SYSTEM == "LPE" then
			-- while self.media.imgcache[who].state ~= nil do 
				-- charstate = self.media.imgcache[who].state
				-- img = self.media.images
				-- Image.free(img[who..' '..charstate])
			-- end
		-- end
		self.media.imgcache[who] = nil
	end

end

function ENGINE:ShowChar(name)
	ch = self.state.chars[name]
	img = self.media.images

	if ch==nil or img[name..' '..ch.state]==nil then
		self:ErrorState('ENGINE:ShowChar('..name..') failed to find character')
		ENGINE.state.chars[name] = nil
		return
	end

	if  self.media.imgcache[name] == nil or self.media.imgcache[name].state ~= ch.state then
		GAME_print('Clearing '..self.media.imgcache[name].state..' (LPE ONLY)')
		if CURRENT_SYSTEM == LPE and self.media.imgcache[name].state ~= ch.state then
			prevsurf = self.media.imgcache[name].surf
			Image.free(prevsurf)
		end
		GAME_print('loading character '..name..' from '..img[name..' '..ch.state])
		loadedsurf = Image.load(img[name..' '..ch.state])
		self.media.imgcache[name] = { state = ch.state , surf = loadedsurf }
	end

	surf = self.media.imgcache[name].surf

	state = name .. ' ' .. ch.state
	if ch.position == 'left' then
		screen:blit(100-GAME_imagewidth(surf)/2, 0, surf)
	elseif ch.position == 'right' then
		screen:blit(380-GAME_imagewidth(surf)/2, 0, surf)
	elseif ch.position == 'twoleft' then
		screen:blit(160-GAME_imagewidth(surf)/2, 0, surf)
	elseif ch.position == 'tworight' then
		screen:blit(320-GAME_imagewidth(surf)/2, 0, surf)
	elseif ch.position == 'center' then
		screen:blit(240-GAME_imagewidth(surf)/2, 0, surf)
	elseif ch.position == 'offscreenleft' then
		screen:blit(25-GAME_imagewidth(surf)/2, 0, surf)
	elseif ch.position == 'offscreenright' then
		screen:blit(455-GAME_imagewidth(surf)/2, 0, surf)
	elseif ch.position == '1four' then
		screen:blit(96-GAME_imagewidth(surf)/2, 0, surf)
	elseif ch.position == '2four' then
		screen:blit(192-GAME_imagewidth(surf)/2, 0, surf)
	elseif ch.position == '3four' then
		screen:blit(288-GAME_imagewidth(surf)/2, 0, surf)
	elseif ch.position == '4four' then
		screen:blit(384-GAME_imagewidth(surf)/2, 0, surf)
    --elseif ch.position <= 1 then
        --posval = ch.position * 480
        --screen:blit(posval-GAME_imagewidth(surf)/2, 0, surf)
    --elseif ch.position > 1 then
        --posval = ch.position
        --screen:blit(posval-GAME_imagewidth(surf)/2, 0, surf)
    --else
        --self:ErrorState('ENGINE:ShowChar('..name..') invalid position')
	end
end

-------------------
----- COLORS ------
-------------------

ENGINE.media.colors = {}
ENGINE.media.colors['red']   = Color.new(255, 0, 0)
ENGINE.media.colors['green'] = Color.new(0, 255, 0)
ENGINE.media.colors['blue']  = Color.new(0, 0, 255)
ENGINE.media.colors['black'] = Color.new(0, 0, 0)
ENGINE.media.colors['white'] = Color.new(255, 255, 255)
ENGINE.media.colors['gray']  = Color.new(128, 128, 128)

ENGINE.media.colors['bg red']   = Color.new(255, 0, 0)
ENGINE.media.colors['bg green'] = Color.new(0, 255, 0)
ENGINE.media.colors['bg blue']  = Color.new(0, 0, 255)
ENGINE.media.colors['bg black'] = Color.new(0, 0, 0)
ENGINE.media.colors['bg white'] = Color.new(255, 255, 255)
ENGINE.media.colors['bg gray']  = Color.new(128, 128, 128)

-------------------
-- FALLING MENU ---
-------------------

FALLING_MENU_DX = 75
FALLING_MENU_X0 = 20

function LdWg(c,f)
	return {
		comment = c,
		image = Image.load(WGPATH..f),
	}
end

falling_menu_bframe = Image.load(WGPATH.."button_frame.png")
falling_menu = {}
falling_menu[1] = LdWg("help","button_help.png")
falling_menu[2] = LdWg("load","button_load.png")
falling_menu[3] = LdWg("save","button_save.png")
falling_menu[4] = LdWg("conf","button_settings.png")
falling_menu[5] = LdWg("skip","button_skip.png")
falling_menu[6] = LdWg("exit","button_exit.png")

--help
ENGINE.media.images['lurk default'] = WGPATH.."lurkmoar.png"

-------------------
-- GAME WIDGETS ---
-------------------

ENGINE.media.text_frame = Image.load(WGPATH.."frame.png")
ENGINE.media.answer_frame = Image.load(WGPATH.."answer.png")

-------------------
-- SKIN RELOAD ----
-------------------

function LdWgNew(path,c,f)
	switch = path
	return {
		comment = c,
		image = Image.load(switch.."/"..f),
	}
end

function ENGINE:SkinReload(skinpath)
	GAME_print('UNLOADING FALLING MENU DATA AND GAME WIDGETS (LPE ONLY)')
	GAME_print('Reloading from path: '..skinpath)
	if CURRENT_SYSTEM == LPE then
		unload.text = ENGINE.media.text_frame
		unload.answer = ENGINE.media.answer_frame
		unload.bframe = falling_menu_bframe
		unload.help = falling_menu[1].image
		unload.load = falling_menu[2].image
		unload.save = falling_menu[3].image
		unload.conf = falling_menu[4].image
		unload.skip = falling_menu[5].image
		unload.exit = falling_menu[6].image
		Image.free(unload.text)
		Image.free(unload.answer)
		Image.free(unload.bframe)
		Image.free(unload.help)
		Image.free(unload.load)
		Image.free(unload.save)
		Image.free(unload.conf)
		Image.free(unload.skip)
		Image.free(unload.exit)
	end
	TEXT.fonts['custom'] =  {
		img = skinpath.."/customfont.png",
		fontDx = 7,
		fontDy = 11
	}
	ENGINE.media.text_frame = Image.load(skinpath.."/frame.png")
	ENGINE.media.answer_frame = Image.load(skinpath.."/answer.png")
	ENGINE.media.images['lurk default'] = skinpath.."/lurkmoar.png"
	falling_menu_bframe = Image.load(skinpath.."/button_frame.png")
	falling_menu[1] = LdWgNew(skinpath,"help","button_help.png")
	falling_menu[2] = LdWgNew(skinpath,"load","button_load.png")
	falling_menu[3] = LdWgNew(skinpath,"save","button_save.png")
	falling_menu[4] = LdWgNew(skinpath,"conf","button_settings.png")
	falling_menu[5] = LdWgNew(skinpath,"skip","button_skip.png")
	falling_menu[6] = LdWgNew(skinpath,"exit","button_exit.png")
	TEXT:UseFont('custom')
	HELPFILE = skinpath.."/help.txt"
end

-------------------
--SOUND AND MUSIC--
-------------------

function getExt(name)
	local x
	for i=1,string.len(name) do
		x = string.len(name)-i+1
		if string.sub(name,x,x)=='.' then
			break
		end
	end
	return string.lower(string.sub(name,x+1,string.len(name)))
end


function ENGINE:PlaySound(name,ch,loop)
	if ch == nil then ch = 1 end
	if loop == nil then loop = false end

	self:PlayMusic(name,ch,loop)
end

function ENGINE:PlayMusic(name,ch,loop)
	if ch == nil then ch = 0 end
	if loop == nil then loop = true end

	if self.state.music[ch]~=nil then
		self:StopMusic(ch)
	end

	local type = getExt(name)

	name = 'game/'..name
	GAME_print('starting '..name..' ('..type..') at '..ch)

	self.state.music[ch] = {}
	self.state.music[ch].type = type
	self.state.music[ch].chan = ch
	self.state.music[ch].name = name
	self.state.music[ch].loop = loop

	if GAME_hasMP3() then
		if type == 'mp3' then
			Mp3.load(name,ch)
			Mp3.play(loop,ch)
		elseif type == 'at3' then
			At3.load(name,ch)
			At3.play(loop,ch)
		elseif type == 'ogg' then
			Ogg.load(name,ch)
			Ogg.play(loop,ch)
		elseif type == 'wav' then
			Wav.load(name,ch)
			Wav.play(loop,ch)
		else
			self:ErrorState('Engine:PlayMusic( name='..name..', ch='..tostring(ch)..', loop='..tostring(loop)..'): unknown filetype')
		end
	end
end

function ENGINE:StopSound(ch)
	if ch == nil then ch = 1 end
	self:StopMusic(ch)
end

function ENGINE:StopMusic(ch)
	if ch == nil then ch = 0 end

	if self.state.music[ch]==nil then
		return
	end

    if self.state.music[ch].loop == false then
            loopkill = self.state.music[ch].loop
    elseif self.state.music[ch].loop == true then
            loopkill = false
    end

	local type = self.state.music[ch].type
	self.state.music[ch] = nil
	GAME_print('stopping '..type..' at '..ch)

	if GAME_hasMP3() then
		-- if CURRENT_SYSTEM == "LPE" then
			-- if ch == 0 then
				-- blankload = RENPSP_FOLDER..'/blank.ogg'
				-- Ogg.load(blankload,ch)
				-- Ogg.play(true,ch)
			-- elseif ch == 1 then
				-- return
			-- end
		-- elseif CURRENT_SYSTEM ~= "LPE" then
			if type == 'mp3' then
                --Mp3.play(loopkill,ch)
				Mp3.unload(ch)
				Mp3.stop(ch)
			elseif type == 'at3' then
                --At3.play(loopkill,ch)
				At3.unload(ch)
				At3.stop(ch)
			elseif type == 'ogg' then
                --Ogg.play(loopkill,ch)
				Ogg.unload(ch)
				Ogg.stop(ch)
			elseif type == 'wav' then
                --Wav.play(loopkill,ch)
				Wav.unload(ch)
				Wav.stop(ch)
			else
				self:ErrorState('Engine:StopMusic(ch='..tostring(ch)..'): unknown filetype')
			end
		-- end
	end

end

function ENGINE:SetVolume(vol,ch)
	if GAME_hasMP3() then
		Mp3.volume(vol,ch)
		At3.volume(vol,ch)
		Ogg.volume(vol,ch)
		Wav.volume(vol,ch)
	end
end
