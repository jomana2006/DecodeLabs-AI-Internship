# DecodeLabs Project 1 Brief:
# General Study Helper Bot is a chatbot that helps students with general study problems like handling exam stress, dealing with procrastination, how to effectively study and take notes, and how to manage your time.
# The bot stores it's automatic responses in a dictionary where the key is a string that contains a keyword and the value is the bot's response associated with the keyword.
# Once the terminal is active, it greets the user and awaits input, which is searched for the keyword in the dictionary.

import time

automaticResponses = {
     "hello" : "Hello!",
     "effectively" : "Use active recall and spaced repetition instead of just re-reading notes. Study in short focused sessions, take breaks, and test yourself regularly to reinforce memory.",
     "stress" : "Take deep breaths, break your study material into smaller chunks, get enough sleep, and avoid cramming last minute. Stay consistent and trust your preparation.",
     "time" : "Plan your day the night before, prioritise tasks by importance, use a timer for focused study sessions, and avoid multi-tasking. Break big tasks into smaller manageable steps.",
     "note" : "There are several popular methods for note-taking: Cornell Method splits your page into notes, cues, and summary sections. Mind Mapping using diagrams to connect ideas. Outline Method organises notes in a hierarchy. Boxing Method groups related topics together.",
     "procrastination" : "Start with the smallest possible step to build momentum. Remove distractions, set a timer for just 10 minutes, and reward yourself after completing tasks. Done is better than perfect.",
     "bye" : "Goodbye!"
}

greeting = "Hello, user!\nWhat can I help you with?"

for character in greeting:
          print(character, end='' , flush=True)
          time.sleep(0.03)
print()

while (True):
     userInput = input()
     cleanInput = userInput.lower().strip()
     
     if cleanInput == "exit":
          break
     
     reply = None
     for key in automaticResponses:
               if key in cleanInput:
                    reply = automaticResponses.get(key)
                    break
               
     if reply == None:
          reply = "I don't understand."
     
     for character in reply:
          print(character, end='' , flush=True)
          time.sleep(0.03)
     print()