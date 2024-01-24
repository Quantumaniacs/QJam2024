# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Quanta = Character("Quanta", color="#29C101")
define Q_Bit = Character("Q_Bit", color="#0138C1")

image determinado:
    'quanta determinado.png'

image bravo:
    'quanta bravo.png'

# The game starts here.

label start1:

    play music "audio/PAX__Una_Aventura_Espacial.wav" loop fadein 3.0 volume 0.3 if_changed

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    
    scene black with fade

    scene nivel 1:
        zoom 1.1
    

    show qbit base at Position(xpos=0.95, ypos=0.4) with moveinright

    Q_Bit "Just in time Quanta! We have a crucial mission today."

    show quanta base at left with moveinleft:
        zoom 0.75

    Quanta "Ready as ever, Q-Bit. What happened?"

    Q_Bit """Decoherence... again. It has kidnapped Professor Planck and the key to our quantum resilience: an exceptionally stable and 100 percent fault tolerant qubit."""
    
    show bravo at Position(xpos=-0.015, ypos=0.29):
        zoom 1.375
        

    Q_Bit """But fear not! With my updated algorithms and your courage, we could track it!"""

    Q_Bit """Quanta, do you remember the principle of superposition?"""

    hide bravo
    show determinado at Position(xpos=-0.015, ypos=0.28):
        zoom 1.35

    Quanta """Of course, it is what allows a qubit to be in multiple states simultaneously, unlike a classical bit."""

    stop music fadeout 2.0
    Q_Bit """Perfect. That is because our first destination is the City of Superposition. Remember, in the quantum world, things are not as binary as they seem... {i}ba dumb tss{/i} 😀"""
    play sound "ba_dum_tss.wav" volume 0.1

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    stop music fadeout 1.0

    scene black with fade

    # This ends the game.
    call script2_start from _call_script2_start

    return
