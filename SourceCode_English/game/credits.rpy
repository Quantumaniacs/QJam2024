# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

# El juego comienza aquí.

define Decoherence = Character("Decoherence", color="#cc1010")

image decoherence_base:
    'decoherencia base.png'

label credits:
#label start:
    
    image creditsa = "final_credits_a.png"
    image creditsb = "final_credits_b.png"

    scene creditsa  with fade

    pause 2.0

    scene creditsb with fade

    pause 5.0 

    scene black with fade
    show decoherence_base at Position(xpos=0.3, ypos=0.25) with dissolve:
        zoom 2.0
    play sound "643721__snowfightstudios__devil-demon_you-are-next.mp3" volume 0.6

    hide decoherence_base with pixellate
    scene black with fade

    $ MainMenu(confirm=False)()

    return
