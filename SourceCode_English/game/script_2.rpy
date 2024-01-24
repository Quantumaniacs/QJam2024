# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Quanta = Character("Quanta", color="#29C101")
define Q_Bit = Character("Q_Bit", color="#0138C1")

screen superposición():
    add "gadget bag2"
    modal True

    imagebutton auto "gadget_bag_superposition_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Superposition Gadget")
        unhovered SetVariable("screen_tooltip", "")
        action Jump("parte2")
        
screen Oráculo():
    add "gadget bag2"
    modal True

    imagebutton auto "gadget_bag_oracle_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Oracle Gadget")
        unhovered SetVariable("screen_tooltip", "")
        action Jump("parte3")

screen Difusor():
    add "gadget bag2"
    modal True

    imagebutton auto "gadget_bag_difusser_%s.png":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Diffuser Gadget")
        unhovered SetVariable("screen_tooltip", "")
        action Jump("parte4")

screen game_over():
    #$ renpy.music.stop()  # Stop any currently playing music.
    #$ renpy.music.play("audio/game_over_music.mp3", loop=True)  # Start playing the game over music.
    add "game_over_screen2" 
    modal True

    imagebutton auto "game_over_screen_%s.png":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Game Over")
        unhovered SetVariable("screen_tooltip", "")
        action Jump("script2_start")

# Initialize a variable to count incorrect choices:
default incorrect_choices = 0

# The game starts here.

label script2_start:

    scene bg 2
    play music "Zane Little - Sideways City.mp3" loop fadein 2.0 volume 0.3

    "The City of Superposition, a place where reality doubles, triples, and more, in a dance of possibilities..."
    
    show quanta base at left with moveinleft:
        zoom 0.75
    Quanta "Great! It looks like this is the place. Q-Bit, activate the Superposition Scanner."

    show qbit base at Position(xpos=0.95, ypos=0.4) with moveinright
    Q_Bit "Scanning... Detecting multiple paths, at least 16 to where the professor is. Grover's algorithm will be essential here Quanta."

    hide quanta base at left
    hide qbit base at Position(xpos=0.95, ypos=0.4) with dissolve
    show quanta bravo2 at left:
        zoom 0.75
    Quanta "Grover's algorithm?"

    hide quanta bravo2 at left
    show qbit base at Position(xpos=0.95, ypos=0.4) with moveinright
    Q_Bit "We're going to need a hands-on demonstration. Ready for a little interactive lesson?"

    hide qbit base at Position(xpos=0.95, ypos=0.4) with dissolve
    show quanta determinado2 at left:
        zoom 0.75
    Quanta "Always! We have no time to waste, we cannot take each path one at a time, the professor needs us!"

    hide quanta determinado2 at left
    show qbit base at Position(xpos=0.95, ypos=0.4) with moveinright
    Q_Bit "Correct, Quanta. First, let's place all paths in a Superposition state with our Superposition Gadget. Select it, please."

    scene green_b
    call screen superposición

label parte2:
    scene bg 2s

    show quanta base at left with moveinleft:
        zoom 0.75
    Quanta "Impressive..."

    show qbit base at Position(xpos=0.95, ypos=0.4) with moveinright
    Q_Bit "Now, we will use the Oracle to mark the right path. But remember, its signal is weak at first due to the nature of superposition."
    
    scene green_b
    call screen Oráculo

label parte3:
    scene bg 3s

    show quanta determinado2 at left:
        zoom 0.75
    Quanta "So, how do we reinforce the Oracle signal?"

    hide quanta determinado2 at left
    show qbit base at Position(xpos=0.95, ypos=0.4) with moveinright
    Q_Bit "That is the function of our Diffuser Gadget, Quanta. It acts as an amplifier for our probabilities."

    show quanta base at left with moveinleft:
        zoom 0.75
    Quanta "I understand, let me select the Diffuser now."

    scene green_b
    call screen Difusor

label parte4:
    scene bg 4s

    show quanta base at left with moveinleft:
        zoom 0.75
    Quanta "Can we be sure that's the right way to go among the 16 paths, Q-Bit?"

    hide quanta base at left
    show qbit base at Position(xpos=0.95, ypos=0.4) with moveinright
    Q_Bit "We will need to iterate the process we just did, to amplify the signal of the correct path. The number of iterations depends on the total number of paths."

    show quanta determinado2 at left:
        zoom 0.75
    Quanta "How do we determine the number of iterations?"

label parte4b:

    hide quanta determinado2 at left
    Q_Bit "In general, the square root of the total number of paths will give us a good starting point although it is only an approximation. With four paths, it would be two iterations. And with sixteen paths..."

    scene green_b
    show seleccion at truecenter
    Q_Bit "How many iterations of this process do we need if we have 16 possible paths?"
    
    menu:
        "Four.":
            hide seleccion
            hide qbit base at right
            $ incorrect_choices = 0  # Reset the count for correct choice.
            jump end

        "Five.":
            $ incorrect_choices += 1  # Increase the count for incorrect choice.
            "Q_Bit" "Mmm, no need for so much repetition Quanta."
            if incorrect_choices >= 2:  # Check if the player made too many wrong choices.
                call screen game_over
            else:
                jump parte4b

        "Two.":
            $ incorrect_choices += 1
            "Q_Bit" "That would be for the case of 4 paths, Quanta. We have 16."
            if incorrect_choices >= 2:
                call screen game_over
            else:
                jump parte4b

label end:

    scene bg final
    show quanta determinado2 at left:
        zoom 0.75
    Quanta "We will need about four, if we follow that logic, correct?"

    hide quanta determinado2 at left
    show qbit base at Position(xpos=0.95, ypos=0.4) with moveinright
    Q_Bit "Exactly! Each iteration of the process will improve our odds. So, in this case, we will repeat the process four times."

    hide qbit base at Position(xpos=0.95, ypos=0.4) with moveinright
    show qbit preparado at Position(xpos=0.95, ypos=0.4)
    Q_Bit "Excellent work Quanta! You have successfully amplified the right path signal."

    stop music fadeout 1.5

    hide qbit preparado at Position(xpos=0.95, ypos=0.4)
    show quanta base at left with moveinleft:
        zoom 0.75
    Quanta "It seems that Grover's algorithm now clearly indicates the way forward. Let go Q-Bit, toward the professor!"
    play music "HEROICCC(chosic.com).mp3" loop fadein 3.0

    call script3_start from _call_script3_start

    return
