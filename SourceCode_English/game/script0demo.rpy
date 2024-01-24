# The script of the intro goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Q_Bit = Character("Q_Bit", color="#0138C1")
define player = Character("[name]")

# The game starts here.

label start_old:

    play music "529264__zhr__emotional-strings.mp3" loop fadein 3.0 if_changed

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    
    scene black with fade

    $ name = ""

    # Introduction to the visual novel concept
    scene white
    show qbit depie resize at Position(xpos=0.5, xanchor=0.5, ypos=0.4, yanchor=0.4)

    Q_Bit "Hello there! Welcome to the Quantum Quest! My name is Q-Bit! People call me the QUANTUM COMPUTING ROBOT!"
    Q_Bit "This is a Visual Novel game, you will read through a story, making choices that affect the outcome."
    Q_Bit "If you've never played a Visual Novel before, feel free to check the 'Help' section in the main menu for guidance."
    Q_Bit "You can also use the buttons at the bottom to review the 'History' so far and to 'Save' your progress."
    # Introduction of Quanta, the tiny raccoon spy
    Q_Bit "In this game, you'll be stepping into the paws of Quanta, a tiny raccoon spy, navigating the Quantum World!"

    Q_Bit "This world is inhabited by different quantum mechanics properties! For some, these properties are tools for computation. Others use them for research."
    Q_Bit "Myself...I study these properties as an assistant of Professor Planck."
    Q_Bit "First..."

    $ name = renpy.input("What's your name? (Don't worry, just write it and press enter.)")
    $ name = name.strip()

    if name == "":
        $ name = "Quanta"

    Q_Bit "Right! So your name is [name]!"
    Q_Bit "[name], your very own quantum computing adventure as Quanta is about to unfold! A world of dreams and challenges in the Quantum World awaits! Let's go!"

    stop music fadeout 1.0

    scene black with fade

    # Transition to the next part of the game.
    #call start1 from _call_start1

    return

