-------------------------------------------
-- This script uses Lucida Console font. --
-------------------------------------------

-------------------------------------------
--  It is encoded to CP-1251 to extract  --
--   1251-encoded symbol's coordinates   --
-------------------------------------------

TEXT = {fonts={}}
TEXT.fonts['lucida_b'] =  {
		img = RENPSP_FOLDER.."/fonts/lucida_black.png",
		fontDx = 7,
		fontDy = 11
	}
	
TEXT.fonts['lucida_w'] =  {
		img = RENPSP_FOLDER.."/fonts/lucida_white.png",
		fontDx = 7,
		fontDy = 11
	}

function TEXT:UseFont(name)
	GAME_print('loading font '..name..' from '..TEXT.fonts[name].img)
	self.curFont   = Image.load(TEXT.fonts[name].img)
	self.curFontDx = TEXT.fonts[name].fontDx
	self.curFontDy = TEXT.fonts[name].fontDy
	self.curFontId = name
end

function TEXT:isWhite(chr)
	return chr==' ' or chr == '\t' or chr == '\r' or chr == '\n'
end

function TEXT:isLetter(chr)
	return (chr >= 'a' and chr <= 'z') or (chr >= 'A' and chr <= 'Z') or (chr == '_')
end

function TEXT:isNumber(chr)
	return (chr >= '0' and chr <= '9')
end

function TEXT:isLetterNumber(chr)
	return TEXT:isLetter(chr) or TEXT:isNumber(chr)
end

function TEXT:getSymbol(b)
	local fontDx = self.curFontDx
	local fontDy = self.curFontDy

	if	 (b>='À') and (b<='ß') then
		return {x = fontDx*(string.byte(b)-string.byte('À')), y=fontDy*0}
	elseif (b>='à') and (b<='ÿ') then
		return {x = fontDx*(string.byte(b)-string.byte('à')), y=fontDy*1}
	elseif (b>='A') and (b<='Z') then
		return {x = fontDx*(string.byte(b)-string.byte('A')), y=fontDy*2}
	elseif (b>='a') and (b<='z') then
		return {x = fontDx*(string.byte(b)-string.byte('a')), y=fontDy*3}
	elseif (b>=' ') and (b<='@') then
		return {x = fontDx*(string.byte(b)-string.byte(' ')), y=fontDy*4}
	elseif (b>='[') and (b<='`') then
		return {x = fontDx*(string.byte(b)-string.byte('[')), y=fontDy*5}
	elseif (b>='{') and (b<='~') then
		return {x = fontDx*(string.byte(b)-string.byte('{')), y=fontDy*6}
	elseif (b=='¨') then
		return {x = fontDx*33, y=fontDy*0}
	elseif (b=='¸') then
		return {x = fontDx*33, y=fontDy*1}
	elseif (b=='¹') then
		return {x = fontDx*34, y=fontDy*4}
	elseif (b=='«') then
		return {x = fontDx*7, y=fontDy*5}
	elseif (b=='»') then
		return {x = fontDx*8, y=fontDy*5}
	elseif (b=='—') then
		return {x = fontDx*9, y=fontDy*5}
	elseif (b=='©') then
		return {x = fontDx*7, y=fontDy*6}		
	elseif (b=='\r') or (b=='\t') or (b=='\n') then
		return {x = 0, y=fontDy*4}
	end
	return {x = 0, y=fontDy*7}
end

function TEXT:WriteLine(x,y,line)
	local i
	for i=1,string.len(line) do
		local chr = string.sub(line, i,i)
 		local symbol = self:getSymbol(chr)
		GAME_superblit(
				x+(i-1)*(self.curFontDx+1),
				y,
				self.curFont,
				symbol.x,
				symbol.y,
				self.curFontDx,
				self.curFontDy
			)
	end 
end

function TEXT:WriteLineCenter(y,line)
	self:WriteLine( (480-string.len(line)*(self.curFontDx+1))/2, y, line)
end

function TEXT:WriteLineLong(x,y,line,maxx)
	local i
	local dx = 0
	local dy = 0
	for i=1,string.len(line) do
		local chr = string.sub(line, i,i)
 		local symbol = self:getSymbol(chr)		
		GAME_superblit(
				x+dx*self.curFontDx,
				y+dy*self.curFontDy,
				self.curFont,
				symbol.x,
				symbol.y,
				self.curFontDx,
				self.curFontDy
			)
		dx = dx + 1
		if dx >= maxx or chr=='\n' then
			dx = 0
			dy = dy + 1
		elseif self:isWhite(chr) then
			local nearest_space = string.len(line)+1
			local j
			for j=i+1,string.len(line) do
				if self:isWhite(string.sub(line, j,j)) then
					nearest_space = j
					break
				end
			end
			if (nearest_space-i)+dx>=maxx then
				dx = 0
				dy = dy + 1
			end
		end
	end
	return dy+1
end

function TEXT:WriteParagraph(x,y,lines,maxx)
	local linenumber = 0
	for iii,line in pairs(lines) do
		linenumber = linenumber + self:WriteLineLong(x,y+linenumber*(self.curFontDy+1),line,maxx)
	end 
end
