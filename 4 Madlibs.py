## 4. Simple Mad Libs
#**Functions needed:** `input()`, `print()`
#**Concepts:** String formatting with f-strings
#**Hints:** Ask for multiple words (noun, verb, adjective), then insert them into a story template.

print("Hi! To play, please provide the following words: ")

#inputs
adjective1 = input("Enter an adjective (something that explains): ")
noun = input("Enter a noun (person/place/thing): ")
pluralnoun = input("Enter a plural noun: ")
verbing = input("Enter a verb ending in -ing: ")
sillyword = input("Enter a silly, made up word: ")
largenumber = input("Enter a large number (1-infinity): ")
typeoffood = input ("Enter a type of food (plural): ")
adjective2 = input ("Enter another adjective: ")
celebrityname = input ("Enter a celebrity name (someone popular or otherwise): ")
exclamation = input("Enter an exclamation (you shout this in the story): ")

print(f"Your Completed Space Adventure\n")
print(f"Captain's Log, Stardate:{largenumber}. Our mission to explore the {adjective1} Nebula has taken a strange turn. Our sensors have detected a strange {noun} floating near a cluster of {pluralnoun}.")
print(f"As we moved closer, we saw it was {verbing} rhythmically and emitting a soft glow. Suddenly, our communications console lit up and a voice said, {sillyword}! We come in peace!")
print(f"The alien, who introduced itself as Flarp, invited us to a diplomatic dinner. The main course was {typeoffood}, which had a surprisingly {adjective2} flavour. To our astonishment, their leader was none other than {celebrityname}!")
print(f"We all looked at each other and shouted, {exclamation}! This was the most bizarre first contact in history.")

#Your Completed Space Adventure
#Captain's Log, Stardate [Large Number]. Our mission to explore the [Adjective] Nebula has taken a strange turn. Our sensors have detected a strange [Noun] floating near a cluster of [Plural Noun].
#As we moved closer, we saw it was [Verb (ending in -ing)] rhythmically and emitting a soft glow. Suddenly, our communications console lit up and a voice said, "[Silly Word]! We come in peace!"
#The alien, who introduced itself as Flarp, invited us to a diplomatic dinner. The main course was [Type of Food (plural)], which had a surprisingly [Adjective] flavor. To our astonishment, their leader was none other than [Celebrity Name]!
#We all looked at each other and shouted, "[Exclamation]!" This was the most bizarre first contact in history.

# What I've learned
# f strings in python is like concatenate in excel and google sheets, where we can piece string together, but its a bit simpler, f"string" but you dont need commas (,) to insert a variable between texts, you just need {} which is rather awkward but it is acceptable
# wonder if there is a way to f string the inputs as well
# \n works as expected, it line breaks. \n\n also works as expected, where it line breaks twice. but then its easier to just have a new print function which also line breaks once..
# therefore.. if i have 2 print functions, and end the first print with \n, the second print function will print 2 line below! lets try that on line 20