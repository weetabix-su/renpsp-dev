Markov = {}
Markov.__index = Markov

function Markov.init(file){
	local mrkv = {}
	setmetatable(mrkv,Markov)
	mrkv.cache = {}
	mrkv.openFile = file
	mrkv.words = Markov:fileToWords()
	mrkv.wordSize = string.len(mrkv.words)
	Markov:database()
}

function Markov:fileToWords(){
	openedFile = io.open(mrkv.openFile,"r")
	data = openedFile:read("*all")
	words = {}
	for i in string.gmatch(data,"%S+") do
		table.insert(words,i)
	end
	return words
}

function Markov:triples(){
	if string.len(mrkv.words) < 3 then
		return
	end
	-- for i in range?(string.len(mrkv.words)-2) do yield? (mrkv.words[i], mrkv.words[i+1], mrkv.words[i+2]) end
}

function Markov:database(){
	for w1, w2, w3 in Markov:triples() do
		key = (w1, w2)
		if key in mrkv.cache then
			
	end
}

function Markov:generateText(size){
	if size == nil then
		size = 25
	end
	seed = 
}