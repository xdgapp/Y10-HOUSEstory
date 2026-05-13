from os import system

def start():
	global showered, sisterKilled, blocked, mumBlinded, rugPulled, trapdoorLocked, crawlspaceDark, dadBlinded, dadBlinded, flashlight, key, keys, skull, sistersBody
	showered = 0
	sisterKilled = 0
	blocked = 1
	mumBlinded = 0
	rugPulled = 0
	trapdoorLocked = 1
	crawlspaceDark = 1
	dadBlinded = 0
	flashlight = 0
	key = 0
	keys = 0
	skull = 0
	sistersBody = 0
	system('cls')
	print("------------------------------------")
	print("Welcome to...")
	print("  _   _  ___  _   _ ____  _____     _                   		  ____||____")
	print(" | | | |/ _ \| | | / ___|| ____|___| |_ ___  _ __ _   _ 		 ///////////\\")
	print(" | |_| | | | | | | \___ \|  _| / __| __/ _ \| '__| | | |		///////////  \\")
	print(" |  _  | |_| | |_| |___) | |___\__ \ || (_) | |  | |_| |		|    _    |  |")
	print(" |_| |_|\___/ \___/|____/|_____|___/\__\___/|_|   \__, |		|[] | | []|[]|")
	print("                                                  |___/ 		|   | |   |  |")
	print("------------------------------------")
	print("You wake up in your room, and according to your clock, it is 9:09 on a Saturday morning. The next thing you realised is that you were grounded by your parents the night before for hiding your sister's prized possession: her flashlight.")
	print("You get a text on your phone from your friends, inviting you to go out. You've got to find a way to escape the house.")
	print("Commands are indicated with square brackets and case-sensitive, for example [take sword].")
	print("To look around the room, input [look].")
	print("To look at your inventory, input [inventory].")
	print("Good luck.")
	bedroom()

def bedroom():
	global userInput
	options = ["look", "north", "east", "inventory"]
	print("------------------------------------")
	print("YOUR BEDROOM")
	print("------------------------------------")
	print("Your bedroom looks the same as it was the day before, nothing interesting. The clock says it is 9am.")
	print("To your [north], your personal bathroom. To your [east], the hallway outside your room.")
	print("------------------------------------")
	userInput = ""
	while userInput not in options:
		userInput = input().lower()
		if userInput == "look":
			bedroom()
		elif userInput == "north":
			bathroom()
		elif userInput == "east":
			hallway()
		elif userInput == "inventory":
			inventory()
			bedroom()
		else:
			sorry()
			bedroom()

def bathroom():
	global userInput, showered
	options = ["look", "south", "shower", "inventory"]
	print("------------------------------------")
	print("YOUR PERSONAL BATHROOM")
	print("------------------------------------")
	print("Regular old bathroom, with basic amenities, and a shower lined with mold. The window is open, but your pubescent body cannot fit through.")
	print("To your [south], your bedroom.")
	print("------------------------------------")
	if showered == 0:
		print("You can choose to [shower], but no one's telling you to do so.")
		print("------------------------------------")
	userInput = ""
	while userInput not in options:
		userInput = input()
		if userInput == "look":
			bathroom()
		elif userInput == "south":
			bedroom()
		elif userInput == "shower":
			if showered == 0:
				showered = 1
				print("------------------------------------")
				print("You have showered and you feel clean. You hate it.")
				print("------------------------------------")
				userInput = ""
			elif showered == 1:
				print("------------------------------------")
				print("You hate taking a shower, and you just showered. Are you some masochist?")
				print("------------------------------------")
				userInput = ""
		elif userInput == "inventory":
			inventory()
			bathroom()
		else:
			sorry()
			bathroom()

def hallway():
	global userInput
	options = ["look", "north", "east", "downstairs", "west", "inventory"]
	print("------------------------------------")
	print("THE HALLWAY")
	print("------------------------------------")
	print("Nothing out of the normal here, just a hallway to different rooms.")
	print("To your [north], the guest room that has never been used. To your [east], your sister's room. To your [west], your bedroom. [downstairs], the family living room.")
	print("------------------------------------")
	userInput = ""
	while userInput not in options:
		userInput = input()
		if userInput == "look":
			hallway()
		elif userInput == "north":
			guestRoom()
		elif userInput == "east":
			if sisterKilled == 0:
				sistersRoom()
			else:
				deadSistersRoom()
		elif userInput == "downstairs":
			livingRoom()
		elif userInput == "west":
			bedroom()
		elif userInput == "inventory":
			inventory()
			hallway()
		else:
			sorry()
			hallway()

def guestRoom():
	global userInput
	options = ["look", "south", "examine", "climb out", "inventory"]
	print("------------------------------------")
	print("THE UNUSED GUEST ROOM")
	print("------------------------------------")
	print("The plainest room you've ever encountered, white walls, white bed, white door. Only things of any interest is the wardrobe in the corner (which you can [examine]), and a wide open window you can [climb out] of.")
	print("To your [south], the hallway.")
	print("You still don't understand why this room has never been used. Wait, what's that smell?")
	print("------------------------------------")
	userInput = ""
	while userInput not in options:
		userInput = input()
		if userInput == "look":
			print("------------------------------------")
			print("The plainest room you've ever encountered, white walls, white bed, white door. Only things of any interest is the wardrobe in the corner (which you can [examine]), and a wide open window you can [climb out] of.")
			print("To your [south], the hallway.")
			print("You still don't understand why this room has never been used. Wait, what's that smell?")
			print("------------------------------------")
			print("Suddenly, you become dizzy and discombobulated. \"Wait, that smell... It's asbestos isn't it?\" You drop to the floor, unconscious.")
			print("------------------------------------")
			print("(YOU HAVE UNLOCKED THE ASBESTOS ENDING, AKA THE DEATH BY ROOM ENDING, 1 OF 6 POSSIBLE ENDINGS. WOULD YOU LIKE TO PLAY AGAIN? yes/no)")
			userInput = ""
			playAgain()
		elif userInput == "south":
			hallway()
		elif userInput == "examine":
			print("------------------------------------")
			print("Empty. Makes a lot of sense. Suddenly, you become dizzy and discombobulated. \"Wait, that smell... It's asbestos isn't it?\" You drop to the floor, unconscious.")
			print("------------------------------------")
			print("(YOU HAVE UNLOCKED THE ASBESTOS ENDING, AKA THE DEATH BY ROOM ENDING, 1 OF 6 POSSIBLE ENDINGS. WOULD YOU LIKE TO PLAY AGAIN? yes/no)")
			userInput = ""
			playAgain()
		elif userInput == "climb out":
			outTheWindow()
		elif userInput == "inventory":
			inventory()
			guestRoom()
		else:
			sorry()
			guestRoom()
            
def outTheWindow():
	print("------------------------------------")
	print("As you try to fit your body through the window, you become disorientated, and you foolishly fall down the second storey of your house, headfirst.")
	print("------------------------------------")
	print("(YOU HAVE UNLOCKED THE FALL ENDING, AKA THE DUMB ESCAPE PLAN ENDING, 1 OF 6 POSSIBLE ENDINGS. WOULD YOU LIKE TO PLAY AGAIN? yes/no)")
	userInput = ""
	playAgain()

def sistersRoom():
	global userInput, sisterKilled
	print("------------------------------------")
	print("YOUR SISTER'S BEDROOM")
	print("------------------------------------")
	print("At a first glance, your sister's room doesn't look all that interesting. However, your sister's room only has one item of interest, YOUR SISTER. \"WHO SAID YOU COULD COME INTO MY ROOM! I'M GONNA KILL YOU!\"")
	print("------------------------------------")
	if showered == 1:
		print("With nothing at your disposal to fend for yourself, you stand there frozen in the middle of the room, and so your sister viciously tears apart your limbs, both legs at once with excruciating pain. ")
		print("")
		print("As you bring your arms to your head, your sister detaches both arms, leaving your head exposed. Bleeding out, you plead to your sister in a last attempt of survival. She reaches out her hand. She moves it closer to your head.")
		print("")
		print("Then- SPLAT. With her bare hand, your sister crushes your skull.")
		print("------------------------------------")
		print("(YOU HAVE UNLOCKED THE SISTER ENDING, AKA THE EMBARASSING DEATH ENDING, 1 OF 6 POSSIBLE ENDINGS. WOULD YOU LIKE TO PLAY AGAIN? yes/no)")
		userInput = ""
		playAgain()
	else:
		sisterKilled = 1
		print("With nothing at your disposal to fend for yourself, you stand there frozen in the middle of the room. Your sister lets out an ear-piercing scream.")
		print("")
		print("You know that you are done for, wait, hold on, the scream is no longer a scream. The yell that launched out of your sister's throat malformed into a seemingly endless stream of vomit. Your sister falls to the ground, faceup to the ceiling, and the next thing you hear is violent choking noises. You didn't shower.")
		print("")
		print("No longer frozen, you walk up to your sister's body and you look down on her. She has died. Better her than you. You begin to [look] around the room.")
		deadSistersRoom()

def deadSistersRoom():
	global userInput, skull, flashlight, sistersBody
	options = ["look", "west", "take", "lift", "inventory"]
	print("------------------------------------")
	print("YOUR (DEAD) SISTER'S BEDROOM")
	print("------------------------------------")
	if skull == 1 and sistersBody == 0:
		print("Again, there's nothing too interesting in this room, well, nothing but the dead body of your sister. Hold on a moment, ever since you've obtained that strange skull, you can [lift] anything, including your sister's body!")
	elif sistersBody == 0:
		print("Again, there's nothing too interesting in this room, well, nothing but the dead body of your sister. Too heavy to lift anyways.")
	else:
		print("After taking your sister's corpse, there's nothing of interest in her room.")
	if flashlight == 0:
		print("Hold on, you see your sister's prized possession, her shiny, bright flashlight. Since she's dead, there's no harm in stealing it, so just [take] it.")
	print("To your [west], the hallway.")
	print("------------------------------------")
	userInput = ""
	while userInput not in options:
		userInput = input()
		if userInput == "look":
			deadSistersRoom()
		elif userInput == "west":
			hallway()
		elif userInput == "take":
			if flashlight == 0:
				flashlight = 1
				print("------------------------------------")
				print("You have obtained your sister's flashlight.")
				print("------------------------------------")
				userInput = ""
			else:
				print("------------------------------------")
				print("You've already got the flashlight.")
				print("------------------------------------")
				userInput = ""
		elif userInput == "lift":
			if skull == 1:
				sistersBody = 1
				print("------------------------------------")
				print("With little effort, you pick up your sister's corpse (who felt weightless), and lift her onto your shoulders.")
				print("------------------------------------")
			else:
				sorry()
				deadSistersRoom()
			userInput = ""
		elif userInput == "inventory":
			inventory()
			deadSistersRoom()
		else:
			sorry()
			deadSistersRoom()

def livingRoom():
	global userInput, rugPulled, trapdoorLocked
	options = ["look", "south", "west", "upstairs", "downstairs", "pull", "use the key", "inventory"]
	print("------------------------------------")
	print("THE LIVING ROOM")
	print("------------------------------------")
	print("Since you got a PC in your room, you've barely spent time here in the living room. Everything feels nostalgic though.")
	print("To your [south], your parents' joint bedroom. To your [west], the kitchen. [upstairs], the hallway.")
	if rugPulled == 1 and trapdoorLocked == 0:
		print("[downstairs], the crawlspace under the house that you didn't know had existed.")
	if rugPulled == 0:
		print("You notice something under the rug, you might want to [pull] away the rug.")
	if rugPulled == 1 and trapdoorLocked == 1:
		print("Under the rug was a rusty trapdoor with an old-fashioned keyhole.")
		if key == 1:
			print("This old-fashioned key you have may fit in it, so [use the key].")
		else:
			print("You don't have anything like a key to try to open it though.")
	print("------------------------------------")
	userInput = ""
	while userInput not in options:
		userInput = input()
		if userInput == "look":
			livingRoom()
		elif userInput == "south":
			if blocked == 1:
				blockedParentsRoom()
			else:
				parentsRoom()
		elif userInput == "west":
			kitchen()
		elif userInput == "upstairs":
			hallway()
		elif userInput == "downstairs":
			if trapdoorLocked == 0:
				crawlspace()
			else:
				sorry()
		elif userInput == "pull":
			if rugPulled == 1:
				print("------------------------------------")
				print("You've already pulled away the rug.")
				print("------------------------------------")
				userInput = ""
			else:
				rugPulled = 1
				print("------------------------------------")
				print("Under the rug was a rusty trapdoor with an old-fashioned keyhole.")
				if key == 1:
					print("This old-fashioned key you have may fit in it, so [use the key].")
				else:
					print("You don't have anything like a key to try to open it though.")
				print("------------------------------------")
				userInput = ""
		elif userInput == "use the key":
			print("------------------------------------")
			if trapdoorLocked == 1:
				trapdoorLocked = 0
				print("The key unlocked the trapdoor. [downstairs], the crawlspace under the house that you didn't know had existed.")
			else:
				print("You've already unlocked the trapdoor with the key.")
			print("------------------------------------")
			userInput = ""
		elif userInput == "inventory":
			inventory()
			livingRoom()
		else:
			sorry()
			livingRoom()

def blockedParentsRoom():
	global userInput, blocked, mumBlinded
	options = ["use flashlight on mum"]
	print("------------------------------------")
	print("You attempt to open the door to your parents' room, but the knob won't turn. Seconds later, your mum peeks out through the door, \"Oh, good morning darling, had a good sleep last night?\" You gave an ambiguous answer, and asked whether you could go out with friends. \"Don't you remember, dear? You were grounded last night for hiding your sister's flashlight!\"")
	if flashlight == 1:
		print("As your mum talks, you realise the flashlight she mentioned was in your hands at that very moment. You wonder, what would happen if I [use flashlight on mum]...")
		print("------------------------------------")
	else:
		print("She doesn't wait for a answer and slams the door on you.")
		livingRoom()
	userInput = ""
	while userInput not in options:
		userInput = input()
		if userInput == "use flashlight on mum":
			blocked = 0
			mumBlinded = 1
			print("------------------------------------")
			print("You quickly turn on and turn off the flashlight at your poor mother's eyes, effectively blinding her. \"AAGGHHHH!\" she says as she stumbles and finally falls on to the king-sized bed. You begin to look around the room.")
			parentsRoom()
		else:
			sorry()
			print("You return to the living room...")
			livingRoom()

def parentsRoom():
	global userInput, key
	options = ["look", "north", "take", "inventory"]
	print("------------------------------------")
	print("YOUR PARENTS' BEDROOM")
	print("------------------------------------")
	print("Your blinded mother lays on the bed, as you stand in the middle of the room.")
	if key == 0:
		print("You search every drawer and container for the house keys, until you find some sort of key that you can [take].")
	print("To your [north], the living room.")
	print("------------------------------------")
	userInput = ""
	while userInput not in options:
		userInput = input()
		if userInput == "look":
			parentsRoom()
		elif userInput == "north":
			livingRoom()
		elif userInput == "take":
			if key == 0:
				key = 1
				print("------------------------------------")
				print("This... is certainly not the key for the front door, it's way too old-fashioned to fit into the keyhole. Why would your parents even have this key, there's nothing that would need this key in this house.")
				print("------------------------------------")
				userInput = ""
			else:
				print("------------------------------------")
				print("You've already got the old-fashioned key")
				print("------------------------------------")
				userInput = ""
		elif userInput == "inventory":
			inventory()
			parentsRoom()
		else:
			sorry()
		
def crawlspace():
	global userInput, crawlspaceDark, flashlight, keys
	options = ["look", "use flashlight", "south", "take", "upstairs", "inventory"]
	print("------------------------------------")
	print("THE HIDDEN CRAWLSPACE")
	if crawlspaceDark == 0:
		print("------------------------------------")
		print("In this very tight crawlspace, you can see a passage to your [south] faintly glowing purple, as well as something shiny on the ground. ")
		if keys == 0:
			print("You should probably [take] the shiny object, but the purple glow allures you, maybe you should check that first.")
		print("To your [south], a room. [upstairs], the living room.")
		print("------------------------------------")
	else:
		print("------------------------------------")
		print("You cannot see anything. You should [use flashlight].")
		print("------------------------------------")
	userInput = ""
	while userInput not in options:
		userInput = input()
		if userInput == "look":
			crawlspace()
		elif userInput == "use flashlight":
			if flashlight == 1:
				crawlspaceDark = 0
				print("------------------------------------")
				print("You can now see some things.")
				crawlspace()
			else:
				sorry()
				crawlspace()
		elif userInput == "south":
			skullRoom()
		elif userInput == "take":
			if keys == 0:
				keys = 1
				print("------------------------------------")
				print("This shiny object is indeed, the house keys, which you have been looking for this entire time. ")
				print("------------------------------------")
				userInput = ""
			else:
				print("------------------------------------")
				print("You've already got the house keys.")
				print("------------------------------------")
				userInput = ""
		elif userInput == "upstairs":
			print("------------------------------------")
			print("Before you leave the dark underground you turn your flashlight back off to conserve power.")
			crawlspaceDark = 1
			livingRoom()
		elif userInput == "inventory":
			inventory()
			crawlspace()
		else:
			sorry()
			crawlspace()
			
def skullRoom():
	global userInput, skull
	options = ["look", "take", "north", "inventory"]
	print("------------------------------------")
	print("THE SKULL ROOM")
	print("------------------------------------")
	print("You finally reach the room. In front of you, you see a large, stone, cylindrical pedestal, clearly too ancient to have been part of the house.")
	if skull == 0:
		print("Atop the pedestal, you see the source of the purple glow that had been drawing you in, a strange skull with its eyes replaced with that purple glow. ")
		print("You feel compelled to [take] it, but you also feel as if something's wrong.")
	print("To your [north], the entrance of the crawlspace")
	print("------------------------------------")
	userInput = ""
	while userInput not in options:
		userInput = input()
		if userInput == "look":
			skullRoom()
		elif userInput == "take":
			if skull == 0:
				skull = 1
				print("------------------------------------")
				print("As you lift the strange skull up from the stone pedestal, suspicious and bizarre sounds flare from outside the house. Probably nothing.")
				print("------------------------------------")
				userInput = ""
			else:
				print("------------------------------------")
				print("You've already got the strange skull")
				print("------------------------------------")
				userInput = ""
		elif userInput == "north":
			crawlspace()
		elif userInput == "inventory":
			inventory()
			skullRoom()
		else:
			sorry()
			skullRoom()

def kitchen():
	global userInput, dadBlinded, keys, flashlight, mumBlinded, showered
	options = ["look", "east", "west", "use flashlight on dad", "inventory"]
	print("------------------------------------")
	print("THE KITCHEN")
	print("------------------------------------")
	print("Various utensils and accessories surround the kitchen. None of them will be of use to you, however.")
	if dadBlinded == 0:
		print("Your dad sits on the kitchen counter, eating his Saturday morning avocado toast prescribed by his dietician.")
	print("To your [east], the living room. To your [west], the front door.")
	print("------------------------------------")
	userInput = ""
	while userInput not in options:
		userInput = input()
		if userInput == "look":
			kitchen()
		elif userInput == "east":
			livingRoom()
		elif userInput == "west":
			if keys == 1 and dadBlinded == 1:
				if skull == 1:
					trueEnding()
				else:
					goodEnding()
			elif keys == 1 and dadBlinded == 0:
				print("------------------------------------")
				print("Nup, you're not going out, especially after that ruckus with your sister last night.\" With your dad being physically much larger than you are, despite your pubescent body, you can't get pass him.")
				if flashlight == 1 and mumBlinded == 1:
					print("However, with the flashlight in your hand, you wonder if that thing that you did with your mum will work with your dad... [use flashlight on dad]")
				print("------------------------------------")
				userInput = ""
			else:
				print("------------------------------------")
				print("The door's locked.")
				print("------------------------------------")
				userInput = ""
		elif userInput == "use flashlight on dad":
			if flashlight == 1:
				dadBlinded = 1
				if showered == 1:
					print("------------------------------------")
					print("\"OH, YOU BLASTED-\" Your dad became disoriented and stumbles to the ground. No one is guarding the door now.")
					print("------------------------------------")
					userInput = ""
				else:
					print("------------------------------------")
					print("\"OH, YOU BLASTED-\" Your dad starts stumbling, but quickly reorients himself. \"Ohohoh, you dare try to defy my authority? You idiot of a son, I can smell you from all the way over here. ")
					print("Your blinded dad begins to charge towards you with full strength. You couldn't dodge quick enough to escape your dad's gigantic frame. He crushes you into the wall with no thought.")
					print("------------------------------------")
					print("(YOU HAVE UNLOCKED THE DAD ENDING, AKA THE TERRIFYING RAMMED ENDING, 1 OF 6 POSSIBLE ENDINGS. WOULD YOU LIKE TO PLAY AGAIN? yes/no)")
					userInput = ""
					playAgain()
			else:
				sorry()
				kitchen()
		elif userInput == "inventory":
			inventory()
			kitchen()
		else:
			sorry()
			kitchen()

def goodEnding():
	print("------------------------------------")
	print("OUTSIDE(!)")
	print("------------------------------------")
	print("You did it, you finally made it out of the house, now you can meetup with your friends. Hopefully your sister didn't mind getting killed.")
	print("As you walk towards the bus stop, you update your friends on your status and tell them you're on your way.")
	print("------------------------------------")
	print("(YOU HAVE UNLOCKED THE GOOD ENDING, AKA THE BORING ESCAPED ENDING, 1 OF 6 POSSIBLE ENDINGS. WOULD YOU LIKE TO PLAY AGAIN? yes/no)")
	userInput = ""
	playAgain()

def trueEnding():
	global userInput
	print("------------------------------------")
	print("OUTSIDE(?)")
	print("------------------------------------")
	print("You did it, you finally made it out of the house, now you can meetup with your friends. Hopefully your sister didn't mind getting killed.")
	print("Hold on, something's wrong. You look up at the sky and see that it had turned purple.")
	print("Checking your phone, your friends ask you, \"WHERE HAVE YOU BEEN?\", and send you images and videos of strange occurences that had happened around them, such as neighbours getting picked up by giant winged creatures and a strange pink beast vomiting out fire.")
	print("------------------------------------")
	print("All of a sudden, a hole is punched into an imaginary wall in front of you, on the other side is a slender, dark figure in a space filled with white light. A voice from this hole booms at you, \"YOU THERE. YOU DID THIS. YOU FAILED TO GUARD THE JERRICRANIUM.\"")
	print("You cannot believe it. The world may possibly be ending, and it may be your fault.")
	print("\"NOW WE SHALL REQUIRE A HUMAN BODY TO REPLACE IT. YOU WILL DO.\"")
	if sistersBody == 1:
		trueTrueEnding()
	else:
		print("------------------------------------")
		print("(YOU HAVE UNLOCKED THE TRUE ENDING, AKA THE HELL ON EARTH ENDING, 1 OF (NOW) 7 POSSIBLE ENDINGS (7th ENDING UNLOCKED). WOULD YOU LIKE TO PLAY AGAIN? yes/no)")
		userInput = ""
		playAgain()

def trueTrueEnding():
	global userInput
	print("\"Wait,\" you blurted out, \"take my sister instead!\" You present your dead sister's corpse to the shadowy figure.")
	print("\"SO BE IT.\" The world warped and disfigured itself, until it started to become an unrecognisable, unintelligable mess. That is before-")
	print("------------------------------------")
	print("You wake up in your room, and according to your clock, it is 9:10 on a Saturday morning.")
	print("You get a text on your phone from your friends, inviting you to go out.")
	print("Might as well, it's nice outside.")
	print("------------------------------------")
	print("(YOU HAVE UNLOCKED THE *TRUE* TRUE ENDING, AKA THE SISTER SACRIFICED ENDING, THE SECRET 7TH ENDING. WOULD YOU LIKE TO PLAY AGAIN? yes/no)")
	userInput = ""
	playAgain()

def playAgain():
	global userInput
	print("------------------------------------")
	userInput = ""
	while userInput != "yes" or "no":
		userInput = input()
		if userInput == "yes":
			system('cls')
			start()
		elif userInput == "no":
			system('cls')
			print("------------------------------------")
			print("Thanks for playing HOUSEstory, come back next time to get all the endings.")
			print("------------------------------------")
			quit()
		else:
			print("Please input [yes] or [no]")

def inventory():
	global flashlight, key, keys, skull, sistersBody
	print("------------------------------------")
	print("Here is what you have:")
	if flashlight == 1:
		print("Your sister's [flashlight]")
	if key == 1:
		print("An old-fashioned [key]")
	if keys == 1:
		print("The house [keys]")
	if skull == 1:
		print("A strange [skull] with a PURPLE GLOW")
	if sistersBody == 1:
		print("Your sister's dead [body](!?)")

def sorry():
	global userInput
	if "use" in str(userInput):
		print("------------------------------------")
		print("Sorry, that item cannot be used right now (check your inventory)")
	else:
		print("------------------------------------")
		print("Sorry, I don't understand (commands are indicated with square brackets, [])")
	userInput = ""

start()


#credits:

#Azura Akbar - programmer / game designer / playtester
#Shafye M - playtester
#William M - playtester