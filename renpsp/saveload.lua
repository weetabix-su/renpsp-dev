function fileWriteLine(f,l)
	f:write(tostring(l))
	f:write('\n')
end

function fileWriteParagraph(f,p)
	fileWriteLine(f,tostring(table.maxn(p)))
	for i,l in pairs(p) do
		fileWriteLine(f,l)
	end
end

function fileReadParagraph(f)
	local t = {}
	local maxi  = tonumber(f:read("*l"))
	for i=1,maxi do
		t[i] = f:read("*l")
	end
	return t
end

function objClone(obj)
	if type(obj) == 'table' then
		return tblClone(obj)
	else
		return obj		
	end
end

function tblClone(tbl)
	local tmp = {}
	for i,j in pairs(tbl) do
		tmp[i] = objClone(j)
	end
	return tmp
end

function stateClone(state)
	local tmp = {env={}}
	for i,j in pairs(state) do
		if  i == 'env' then
			tmp.env={}
			for ii,jj in pairs(j) do
				if  ii == 'renpy' then
					-- do nothing
				elseif ii == 'persistent' then
					-- do nothing
				else
					tmp.env[ii] = objClone(jj)
				end
			end
		else
			tmp[i] = objClone(j)
		end
	end
	tmp.env.renpy = RENPY
	tmp.env.persistent = PERSISTENT
	return tmp
end

function fileWriteObject(f,j)
	local t = type(j)
	if t == 'table' then
		fileWriteTable(f,j)
	elseif t == 'number' then
		fileWriteLine(f,"#")
		fileWriteLine(f,tostring(j))
	elseif t == 'string' then
		fileWriteLine(f,'X')
		fileWriteLine(f,j)
	elseif j == true then
		fileWriteLine(f,'T')
	elseif j == false then
		fileWriteLine(f,'F')		
	else
		fileWriteLine(f,'nil')
	end
end

function fileWriteTable(f,tbl)
	fileWriteLine(f,"[")
	for i,j in pairs(tbl) do
		fileWriteObject(f,i)
		fileWriteObject(f,j)
	end
	fileWriteLine(f,"]")
end

function debugPrintObject(obj)
	local t = type(j)
	if t == 'table' then
		GAME_print("[")
		for i,j in pairs(tbl) do
			debugPrintObject(i)
			debugPrintObject(j)
		end
		GAME_print("]")
	elseif t == 'number' then
		GAME_print("#")
		GAME_print(tostring(j))
	elseif t == 'string' then
		GAME_print('X')
		GAME_print(j)
	else
		GAME_print('nil')
	end
end

function fileWriteEnv(f,env)
	fileWriteLine(f,"[")
	for i,j in pairs(env) do
		if i == 'renpy' then
			-- do nothing
		elseif i == 'persistent' then
			-- do nothing
		else
			fileWriteObject(f,i)
			fileWriteObject(f,j)
		end			
	end
	fileWriteLine(f,"]")
end

function fileReadTable(f)
	local l = f:read("*l")
	if l ~= '[' then return nil end
	return fileReadTableProc(f)
end

function fileReadObject(f)
	local data = f:read("*l")
	if data == '[' then
		data = fileReadTableProc(f)
	elseif data == '#' then
		data = tonumber(f:read("*l"))
	elseif data == 'X' then
		data = f:read("*l")
	elseif data == 'T' then
		data = true
	elseif data == 'F' then
		data = false
	elseif data == ']' or data==nil then
		data = ']'
	else
		GAME_print('Error: data is '..data)
		data = nil
	end
	return data
end

function fileReadTableProc(f)
	local t = {}
	local l = fileReadObject(f)
	while l ~=nil and l ~= ']' do
		local data = fileReadObject(f)
		t[l] = data
		l = fileReadObject(f)
	end
	return t
end

function ENGINE:LoadStateFromFile(fname)
	self:StopMusic(0)
	self:StopMusic(1)

	local state = {menu = {}}

	f = io.open(fname,"r")
        if f == nil then
            return f
        end

	local current_file = f:read("*l")
	local current_position = tonumber(f:read("*l"))

	local current_bg = f:read("*l")

	state.text = fileReadParagraph(f)
	state.menu.a = fileReadParagraph(f)
	state.menu.jmp = fileReadParagraph(f)
	state.music = fileReadTable(f)
	for ch,data in pairs(state.music) do
		if data.loop then
			self:PlayMusic(data.name,data.chan,data.loop)
		end
	end

	state.env = fileReadTable(f)
	state.env.renpy = RENPY
	state.env.persistent = PERSISTENT

	state.chars = {}
	who = f:read("*l")
	while who~=nil do
		pos = f:read("*l")
		stat= f:read("*l")
		state.chars[who]  = {position=pos, state=stat}
		who = f:read("*l")
	end

	f:close()

	return {st=state,f=current_file,pos=current_position,bck=current_bg}
end

function ENGINE:FileSeek(fname,pos)
	if self.state.current_file ~= fname then
		if self.state.current_file ~= nil then
			self.script.gamefile:close()
			GAME_print('Closing '..self.state.current_file)
		end
		self.script.gamefile = io.open(fname,"r")
		GAME_print('Opening '..fname)
	end
	self.state.current_file = fname
	self.script.gamefile:seek('set',pos)
end

function ENGINE:FileSeekToState(st)
	self:FileSeek(st.current_file, st.current_position)
end

function ENGINE:Load(xtra)
        if xtra ~= nil then
            savname = xtra
        elseif xtra == nil then
            savname = "default"
        end
	local loaded = self:LoadStateFromFile(ENGINE.cursavepath.."/"..savname..".sav")
        if loaded == nil then
            return 1 < 0
        end
	self:FileSeek(loaded.f, loaded.pos)
	self.state = stateClone(loaded.st)
	self.state.menu.active = 1
	self:Scene(loaded.bck)
	continue = false

	self.history.i = 1
	self.history.states = {}
	self.history.states[1] = stateClone(self.state)
        
end

function ENGINE:Save(xtra)
        if xtra ~= nil then
            savname = xtra
        elseif xtra == nil then
            savname = "default"
        end
	f = io.open(ENGINE.cursavepath.."/"..savname..".sav","w")
	fileWriteLine(f,self.state.current_file)
	fileWriteLine(f,self.script.gamefile:seek())
	fileWriteLine(f,self.state.bgname)
	fileWriteParagraph(f,self.state.text)
	fileWriteParagraph(f,self.state.menu.a)
	fileWriteParagraph(f,self.state.menu.jmp)
	fileWriteTable(f,self.state.music)
	fileWriteEnv(f,self.state.env)
	for name,ch in pairs(self.state.chars) do
		if ch.position ~= 'none' then
			fileWriteLine(f,name)
			fileWriteLine(f,ch.position)
			fileWriteLine(f,ch.state)
		end
	end
	f:close()
	saveScreen(ENGINE.cursavepath.."/default.png")
	f = io.open(ENGINE.cursavepath.."/default.lst","w")
	for name,d in pairs(_G) do
		fileWriteLine(f,name)
	end
	f:close()
end

function ENGINE:TakeScreenshot()
	x = 240
	y = 136
	ENGINE.tmp_retImage = Image.createEmpty(x,y)
	for i=0,x-1 do
		for j=0,y-1 do
			col = GAME_imagegetpixel(screen,i*GAME_imagewidth(screen)/x,j*GAME_imageheight(screen)/y)
			GAME_imagesetpixel(ENGINE.tmp_retImage,i,j,col)
		end
	end
end

function saveScreen(path)
	ENGINE.tmp_retImage:save(path)
end


function ENGINE:LoadPersistent()
	fname = ENGINE.cursavepath.."/persistent"
	f = io.open(fname,"r")
	if not f then
		PERSISTENT = {}
		GAME_print('Persistent not found at '..fname)
		self:SavePersistent()
		GAME_print('Created empty persistent')
	else
		PERSISTENT = fileReadTable(f)
		f:close()
	end
end

function ENGINE:SavePersistent()
	fname = ENGINE.cursavepath.."/persistent"
	f = io.open(fname,"w")
	GAME_print("opening for write "..fname)
	fileWriteTable(f,PERSISTENT)
	f:close()
end

function ENGINE:PushState()
	self.history.i = self.history.i+1
	self.history.states[self.history.i] = stateClone(self.state)
end

function ENGINE:PrevState()
	if 	self.history.i > 1 then 
		self.history.i = self.history.i-1
		self:FileSeekToState(self.history.states[self.history.i])
		self.state = stateClone(self.history.states[self.history.i])
		self:Scene(self.state.bgname)
	end
end

function ENGINE:NextState()
	if 	self.history.i < table.maxn(self.history.states) then 
		self.history.i = self.history.i+1
		self:FileSeekToState(self.history.states[self.history.i])
		self.state = stateClone(self.history.states[self.history.i])
		self:Scene(self.state.bgname)
	else
		self.script.continue = true
	end
end

function ENGINE:DestroyHistory()
	local st = stateClone(self.history.states[self.history.i])
	self.history.i = 1
	self.history.states[self.history.i] = stateClone(st)
end