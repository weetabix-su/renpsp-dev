-------------------
-- CONTROLS FUNCS -
-------------------

function ENGINE:CtrlHelp(pad,oldpad)
	if pad:select() and not oldpad:select() then
		helpexit = true
	elseif (pad:r() and not oldpad:r()) or (pad:right() and not oldpad:right()) then
		if page < pagemax then
			page = page + 1
		end
	elseif (pad:l() and not oldpad:l()) or (pad:left() and not oldpad:left()) then
		if page >1 then
			page = page - 1
		end
	end
end

-------------------
-- DRAWING FUNCS --
-------------------

function ENGINE:ReadFile(fname)
	local f = io.open(fname, "r")
	local lines = {}
	local i = 1
	local line = f:read("*l")
	while (line~=nil) do
		lines[i]=line
		i=i+1
		line = f:read("*l")
	end
	f:close()
	return lines
end

HELPFILE = nil

function ENGINE:Help(helptxt)
	if helptxt ~= nil then
		help = self:ReadFile(helptxt)
	elseif helptxt == nil then
		help = self:ReadFile(self.homepath .. "/help.txt")
	end
	
	pages = {}
	pagemax = 1
	tmp = {}
	k = 1

	for i=1,table.maxn(help) do
		if  string.sub(help[i],1,4)=='----' then
			pages[pagemax] = tmp
			tmp = {}
			k = 1
			pagemax = pagemax + 1
		else
			tmp[k] = help[i]
			k = k + 1
		end
	end
	pages[pagemax] = tmp

	page = 1

	backup_font = TEXT.curFontId
	TEXT:UseFont('lucida_b')

	helpexit = false
	while not helpexit do
		GAME_draw()
			screen:clear(Color.new(255, 255, 255))
			self.state.chars["lurk"] = {state='default'}
			self.state.chars["lurk"].position = "left"
			self:ShowChar('lurk')
			TEXT:WriteParagraph(135,5,pages[page],50)
			TEXT:WriteLine(5,255,string.format('%d/%d',page,pagemax),50)
		GAME_nodraw()
		self:Control('CtrlHelp') 
	end
	self.state.chars["lurk"].position = "none"
	TEXT:UseFont(backup_font)
end
