-------------------
--- STRING FUNCS --
-------------------


LEXEM = {
		string = function(txt) return {data=txt,type='string'} end,
		word = function(txt) return {data=txt,type='word'} end,
		tolua = function(cmd,from,to)
			local result
			if cmd[from].type == 'string' then
				result = '\''..cmd[from].data..'\''
			else
				result = cmd[from].data
			end
			for i=from+1,to do
				if cmd[i].type == 'string' then
					result = result..' '..'\''..cmd[i].data..'\''
				else
					result = result..' '..cmd[i].data
				end		
			end
			return result
		end
	}

function countSpace(str)
	if str == nil then
		return 0
	end

	local cnt = 0
	local i
	for i=1, string.len(str) do
		if string.sub(str,i,i) == ' ' then
			cnt = cnt + 1
		elseif string.sub(str,i,i) == '\t' then
			cnt = cnt + 4
		else
			break
		end
	end	
	return cnt
end

function readNonWhiteLine(f)
	while true do
		local l = f:read("*l")
		if l == nil then return nil end

		for i=1,string.len(l) do
			if not TEXT:isWhite(string.sub(l,i,i)) then
				return l
			end
		end
	end
end

function explodeLexer(str)
	if str == nil then
		return {LEXEM.word('return')}
	end
	local result = {}
	local n = 1
	local start = 1
	local inQ = false
	local whatQ = nil
	local prev = ' '
	local i = 1
	local ignorewhite = false

	
	while i<=string.len(str) do
		chr = string.sub(str,i,i)
		local newLexem = false
		newLexem = newLexem or (TEXT:isWhite(chr))
		newLexem = newLexem or (TEXT:isLetter(chr) and not TEXT:isLetterNumber(prev))
		newLexem = newLexem or (chr=='=' and prev~='=')
		if (chr == '"' or chr == '\'') and not ignorewhite then
			if not inQ then
				whatQ = chr
				if not TEXT:isWhite(prev) then
					result[n]=LEXEM.string(string.sub(str,start,i-1))
					n = n+1
				end
				start = i+1
				inQ = true
			elseif chr==whatQ then
				result[n]=LEXEM.string(string.sub(str,start,i-1))
				n = n+1
				start = i+1
				inQ = false
			end
		elseif chr == '#' and not inQ then
			if  start~=i then
				result[n]=LEXEM.word(string.sub(str,start,i-1))
			end
			if table.maxn(result) > 0 then
				return result
			end
			return {LEXEM.word('pass')}
		elseif chr == '\\' and inQ then
	 		chr = string.sub(str,i+1,i+1)
			local tmp
			if chr == '\\' then
				tmp = '\\'
			elseif chr == '"' then
				tmp = '"'
			elseif chr == 'n' then
				tmp = '\n'
			end
			str = string.sub(str,0,i-1)..tmp..string.sub(str,i+2,string.len(str))
		elseif newLexem and not inQ and not ignorewhite then
			if start ~= i then
				result[n]=LEXEM.word(string.sub(str,start,i-1))
				n = n+1
			end
			if TEXT:isWhite(chr) then
				start = i+1
			else
				start = i
			end
		elseif chr == ':' and not inQ then
			if  start~=i then
				result[n]=LEXEM.word(string.sub(str,start,i-1))
				n = n+1
			end
			result[n]=LEXEM.word(':')
			n = n+1
			start = i+1
		elseif chr == '$' and not inQ then
			if  start~=i then
				result[n]=LEXEM.word(string.sub(str,start,i-1))
				n = n+1
			end
			result[n]=LEXEM.word(chr)
			n = n+1
			ignorewhite = true
			start = i+1
		end
		prev = chr
		i = i + 1
	end
	if start<string.len(str) then
		result[n] = LEXEM.word(string.sub(str,start,string.len(str)))
	end
	if table.maxn(result)==0 then
		return {LEXEM.word('pass')}
	end
	return result
end

function ENGINE:ExecuteScriptLine(cmd)
	if cmd[1].type == 'string' then
		self.state.text = {}
		for i=1,table.maxn(cmd) do
			self.state.text[i] = cmd[i].data
		end
		self.script.continue = false
		return
	end
	
	-- cmd[1].type == 'word'

	if cmd[1].data == 'scene' then
		bgname = cmd[2].data
		for i=3,table.maxn(cmd) do
			if cmd[i].data == 'with' then
				break
			end
			bgname = bgname..' '..cmd[i].data
		end
		self:ClearScene()	-- WEETABIX NOTE: Background clearing code transferred to media.lua
		self:Scene(bgname)
		self:ClearChars()
	elseif cmd[1].data == 'show' then
		local who = cmd[2].data
		local how = 'default'
		local pos = 'center'
		if  table.maxn(cmd)>2 and cmd[3].data == 'at' then
			pos = cmd[4].data
		elseif table.maxn(cmd)>2 then
			how = cmd[3].data
			for i=4,table.maxn(cmd) do
				if cmd[i].data == 'at' then
					pos = cmd[i+1].data
					break
				end
				how = how..' '..cmd[i].data
			end
		end
		self.state.chars[who] = {state = how, position = pos}
	elseif cmd[1].data == 'hide' then
		local who = cmd[2].data
		self.state.chars[who] = nil
                if  self.media.imgcache[who] then
			self.media.imgcache[who].surf:clear()
			if CURRENT_SYSTEM == "LPE" then
				prevsurf = self.media.imgcache[who].surf
				Image.free(prevsurf)
			end
			self.media.imgcache[who] = nil
		end
	elseif cmd[1].data == 'with' then
		-- do nothing
	elseif cmd[1].data == 'jump' then
		self:Jump(cmd[2].data)
	elseif cmd[1].data == 'play' then
		local cmdlua = LEXEM.tolua(cmd,3,table.maxn(cmd))
		local f = self:EvalLua('return '..cmdlua)
		if self.state.is_error or type(f)~='string' then
			return
		end

		if cmd[2].data == 'music' then
			self:PlayMusic(f)
		elseif cmd[2].data == 'sound' then
			self:PlaySound(f)
		else
			self:ErrorState('Unknown cmd: play '..cmd[2].data)
		end
	elseif cmd[1].data == 'stop' then
		if cmd[2].data == 'music' then
			self:StopMusic(f)
		elseif cmd[2].data == 'sound' then
			self:StopSound(f)
		else
			self:ErrorState('Unknown cmd: stop '..cmd[2].data)
		end
	elseif cmd[1].data == 'label' then
		-- do nothing
	elseif cmd[1].data == 'return' then
		self:Quit()
	elseif cmd[1].data == '$' then
		self:EvalLua(cmd[2].data)
	elseif cmd[1].data == 'pass' then
		-- do nothing
--	elseif cmd[1].data == 'centered' then
--		if self.media.names[cmd[2].data]~=nil then
--			cmd[2].data = self.media.names[cmd[2].data]
--		end
--		self.state.text = {}
--		for i=2,table.maxn(cmd) do
--			self.state.text[i] = cmd[i].data
--		end
--		self.script.continue = false
	else
		if self.media.names[cmd[1].data]~=nil then
			cmd[1].data = self.media.names[cmd[1].data]
		end
		self.state.text = {}
		for i=1,table.maxn(cmd) do
			self.state.text[i] = cmd[i].data
		end
		self.script.continue = false
	end
end

function ENGINE:Quit()
	self:Timer(3000)
	self:Scene('black')
	self:ClearChars()
	self.state.text = {'Thanks for using RenPSP!\n\n                                                      lb@iichan'}
	self.script.exit = true
	self.script.continue = false
end

function ENGINE:EvalLua(cmd)
	local chunk, errmsg = loadstring(cmd)
	if not chunk then
		self:ErrorState('Syntax error: '..errmsg..'at file '..self.state.current_file)
		return nil
	end
	setfenv(chunk,self.state.env)
	return chunk()
end

function ENGINE:Eval()
	if self.conf.autoplay and table.maxn(self.state.menu.a)==0 then
		self:Timer(self.conf.autoplay_time,'auto')
	end

	if table.maxn(self.state.menu.a)>0 then
		self:Jump(self.state.menu.jmp[self.state.menu.active])
		self.state.menu.a = {}
		self.state.menu.jmp = {}
		self.state.menu.active = 1
	end

	line = readNonWhiteLine(self.script.gamefile)
	current_position = self.script.gamefile:seek()
	spc = countSpace(line)
	cmd = explodeLexer(line)

	if cmd[1].data == 'menu' then
		self:TimerStop()
		repeat
			line = readNonWhiteLine(self.script.gamefile)
			spc1 = countSpace(line)
			pos = self.script.gamefile:seek()
			cmd1 = explodeLexer(line)
			if spc1 == spc+4 and cmd1[1].type == 'string' and cmd1[2].data==':' then
				local i = table.maxn(self.state.menu.a)+1
				self.state.menu.a[i]=cmd1[1].data
				self.state.menu.jmp[i]=pos
			end
		until line == nil or spc1<=spc
		if table.maxn(self.state.menu.a)<1 then
			self:ErrorState('ENGINE:eval() found an empty menu')
		end
		self.script.continue = false
	elseif cmd[1].data == 'if' then
		while 1 do
			cmdlua = LEXEM.tolua(cmd,2,table.maxn(cmd)-1)
			local cond = self:EvalLua('return '..cmdlua)
			if self.state.is_error then
				break
			end

			if type(cond) == 'number' then
				cond = (cond ~= 0)
			end
			--GAME_print(cmdlua..': '..tostring(cond))

			if type(cond) ~= 'boolean' then
				self:ErrorState('if '..cmdlua..': should be boolean')
				break
			elseif cond then
				break
			else
				repeat
					back = self.script.gamefile:seek()
					line = readNonWhiteLine(self.script.gamefile)
					spc1 = countSpace(line)
				until spc1<=spc

				if spc1 == spc then
					cmd = explodeLexer(line)
					if cmd[1].data ~= 'elseif' and cmd[1].data ~= 'elif' then
						if cmd[1].data ~= 'else' then
							self.script.gamefile:seek('set',back)
						end	
						break
					end
				else
					self.script.gamefile:seek('set',back)
					break	
				end
			end
		end
	elseif cmd[table.maxn(cmd)].data == ':' and spc>0 then
		repeat
			back = self.script.gamefile:seek()
			line = readNonWhiteLine(self.script.gamefile)
			spc1 = countSpace(line)
		until spc1<=spc
		self.script.gamefile:seek('set',back)
	else
		self:ExecuteScriptLine(cmd)
	end

	self.state.current_position = self.script.gamefile:seek()
end

function ENGINE:Prepare(fname)
	local tmpfile = io.open(fname, "r")
	tmpfile:seek('set',0)

	local line = readNonWhiteLine(tmpfile)
	while line~=nil do
		cmd = explodeLexer(line)
		if cmd[1].data == 'label' then
			self.script.gamelabels[cmd[2].data] = {fname, tmpfile:seek()}
			self.script.gamelabels[cmd[2].data..'@'..fname] = {fname, tmpfile:seek()}
		elseif cmd[1].data == 'image' then
			local key = cmd[2].data
			local additional = 'default'
			local i=3
			if cmd[3].data ~= '=' then
				additional = cmd[3].data
				i=4
				while cmd[i]~=nil and cmd[i].data~='=' do
					additional = additional .. ' ' .. cmd[i].data
					i = i + 1
				end			
			end
			self.media.images[key .. " " .. additional] = ENGINE.curgamepath..'/'..cmd[i+1].data
		elseif cmd[1].data == 'define' then
			local key = cmd[2].data
			local data = cmd[5].data
			if cmd[3].data == '=' and cmd[4].data == 'Character(' then
				self.media.names[key] = data
			else
				self:ErrorState('"define" supports only "= Character(..." option')
			end
		end
		line = readNonWhiteLine(tmpfile)
	end

	tmpfile:close()
end

function ENGINE:Jump(label)
	if label==nil then
		self:ErrorState('ENGINE:jump( nil ) was called')
		return
	elseif self.script.gamelabels[label]==nil then
		if tonumber(label)==nil then
			self:ErrorState('ENGINE:jump('..tostring(label)..') failed to find label')
		else
			self.script.gamefile:seek('set',tonumber(label))
		end
		return
	end

	if self.script.gamelabels[label][1]~=current_file then
		if self.state.current_file~='' then
			self.script.gamefile:close()
		end
		self.state.current_file = self.script.gamelabels[label][1]
		self.script.gamefile = io.open(self.script.gamelabels[label][1])
	end
	self.script.gamefile:seek('set',self.script.gamelabels[label][2])
end

function ENGINE:Timer(t,type)
		if type==nil then
			type = 'forced'
		end

		self.timer.main_timer:reset()
		self.timer.main_timer:start()
		self.timer.time_to_wait = t
		self.timer.timer_type = type
end

function ENGINE:TimerStop()
		self.timer.time_to_wait = nil
		self.timer.main_timer:stop()
end

function ENGINE:GotoStart()
	self:Scene('black')
	self.fmenu.menuactiveitem = 1
	self.state.current_file = ''
	self.state.current_position = 0
	self.state.env.renpy = RENPY
	self.state.env.persistent = PERSISTENT
	n_start = 0
	for i,j in pairs (self.script.gamelabels) do
		if string.sub(i,1,6)=='start@' then
			n_start = n_start+1
		end
	end
	
	if self.script.gamelabels['start']==nil then
		self:ErrorState('ENGINE:gotoStart(): No start label')
	elseif n_start == 1 then
		self:Jump('start')
	else
		self:ErrorState('ENGINE:gotoStart(): Several start labels')
	end
end

function ENGINE:PrepareAllInPath(path)
	local cwd = GAME_curdir(path)
	for idx,item in pairs(GAME_listdir()) do
		if item.name == '.' or item.name == '..' then
			-- do nothing
--		elseif GAME_isdir(item) then
--			self:PrepareAllInPath(item.name)
		elseif string.find(string.lower(item.name),'rpy$') ~=nil then
			GAME_print('Processing '..item.name..'...')
			self:Prepare(GAME_curdir()..'/'..item.name)
		end
	end
	GAME_curdir(cwd)
end

function ENGINE:SelectGame(path)
	GAME_curdir(path)

	local i=1
	ENGINE.script.continue = false
	ENGINE.state.menu = {a={},jmp={},active=1}
	idx = 1
	for i,j in pairs(GAME_listdir()) do
		if string.sub(j.name,1,1)~='.' then
			ENGINE.state.menu.a[idx] = j.name
			ENGINE.state.menu.jmp[idx] = j.name
			idx = idx + 1
		end
	end

	self:Scene('white')

	while not ENGINE.script.continue do
		GAME_draw()
			GAME_clear()
			ENGINE:DrawGame()
		GAME_nodraw()
		ENGINE:Control('CtrlMenu')
	end

	GAME_curdir(self.state.menu.jmp[self.state.menu.active])
	ENGINE.curgamepath = path..'/'..self.state.menu.jmp[self.state.menu.active]..'/game'
	ENGINE.cursavepath = path..'/'..self.state.menu.jmp[self.state.menu.active]..'/saves'
	ENGINE.curskinpath = path..'/'..self.state.menu.jmp[self.state.menu.active]..'/skin'
	GAME_print('ENGINE.curgamepath = '..ENGINE.curgamepath)
	ENGINE.state.menu = {a={},jmp={},active=1}
	if GAME_chkDir(ENGINE.cursavepath) == false then
		GAME_makeDir(ENGINE.cursavepath)
	end
	if GAME_chkDir(ENGINE.curskinpath) == true then
		self:SkinReload(ENGINE.curskinpath)
	end
end
