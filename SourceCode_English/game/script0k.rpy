define Q_Bit = Character("Q_Bit", color="#0138C1")

define pov = Character("[povname]", color="#286055")

label start:

play music "audio/entrenamiento.ogg" fadein 3.0 volume 0.3

label parte0a:

scene black with fade

Q_Bit "Hi! I'm Q-Bit."

Q_Bit "Can you see me?"

Q_Bit "I don't think so..."

scene blanco:
     
show qbit base at center with moveinleft:
     xalign 0.5
     yalign 0.5
     
Q_Bit "Now, if you see me dear adventurer:"

#Q_Bit "What is your name, dear quantum adventurer?"

$ povname = renpy.input("What is your name? (Just write it and press enter!)")

pov "My name is [povname]."

Q_Bit "Nice to meet you [povname]. Welcome to the Quantum Quest!"

Q_Bit "I, Q-Bit, will be your partner in this adventure. People call me the QUANTUM COMPUTING ROBOT."

label parte0b:

Q_Bit "This game is a visual novel, where your decisions and your answers affect the flow of the story."

# Q_Bit "When facing a challenge or a series of questions, you will have 3 opportunities to overcome the challenge."
Q_Bit "In certain scenarios of this game, you are given a specific number of chances to surmount the challenge. Failure to do so results in game over." # It is not always 3 in all the scenarios.

Q_Bit "If you answer correctly, you continue to advance in the story. Otherwise, you go back to the beginning of the level."

Q_Bit "Have you understood the rules?"

menu:
    "Yes.":
        jump parte0c

    "No.":
        jump parte0b

label parte0c:
    
Q_Bit "Well [povname], before we continue, we will take a walk through the numerical sets..."

Q_Bit "But first let's go to the training room."

scene entrenamiento

show qbit base with moveinleft:
     xalign 0.95
     yalign 0.4

Q_Bit "[povname], welcome to the training room. Here, you'll be introduced to the game's dynamics through numerical sets, while also becoming familiar with the style of Visual Novels."

Q_Bit "If you've never played a Visual Novel before, feel free to check the 'Help' section in the main menu for guidance."
Q_Bit "You can also use the buttons at the bottom to review the 'History' so far and to 'Save' your progress."

call script001_start from _call_script001_start

return