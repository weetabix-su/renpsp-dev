function RenpyClass(renpy)
	renpy.sound  = {}
	renpy.music  = {}
	renpy.random = {}

	--original functions:

	function renpy.pause(nseconds)
		ENGINE:Timer(tonumber(nseconds*1000))
		ENGINE.state.hide_text = true
		ENGINE.script.continue = false
	end

	function renpy.block_rollback()
		ENGINE:DestroyHistory()
	end

	function renpy.error(err)
		ENGINE:ErrorState(tostring(err))
	end

	function renpy.quit()
		ENGINE:Quit()
	end

	function renpy.jump(lbl)
		ENGINE:Jump(lbl)
	end

	function renpy.has_label(lbl)
		return ENGINE.script.gamelabels[lbl]~=nil
	end

	function renpy.sound.play(snd,ch,loop)
		ENGINE:PlaySound(snd,ch,loop)
	end

	function renpy.sound.stop(ch)
		ENGINE:StopSound(ch)
	end

	function renpy.sound.set_volume(vol,ch)
		ENGINE:SetVolume(vol,ch)
	end

	function renpy.music.play(snd,ch,loop)
		ENGINE:PlayMusic(snd,ch,loop)
	end

	function renpy.music.stop(ch)
		ENGINE:StopMusic(ch)
	end

	function renpy.music.set_volume(vol,ch)
		ENGINE:SetVolume(vol,ch)
	end

	function renpy.take_screenshot()
		ENGINE:TakeScreenshot()
	end

	function renpy.screenshot(fname)
		screen:save(fname)
	end

	--selfmade functions:

	function renpy.print(l)
		GAME_print(tostring(l))
	end
	
	function renpy.input(desc,def)
		if CURRENT_SYSTEM == "LPE" then
			ans, res = System.osk(desc,def)
			if (res==System.OSK_RESULT_UNCHANGED) then
				return def
			elseif (res==System.OSK_RESULT_CANCELLED) then
				return def
			elseif (res==System.OSK_RESULT_CHANGED) then
				return ans
			end
		elseif CURRENT_SYSTEM == "LPP" then
			System.oskInit(desc,def)
			res, ans = System.oskUpdate()
			if res == true then
				return ans
			elseif res == false then
				return def
			end
		else
			return def
		end
	end
end
