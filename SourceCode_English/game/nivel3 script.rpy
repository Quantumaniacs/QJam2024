# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define q = Character("Quanta", color="#29C101")
define decoherencia = Character("Decoherence", color="#cc1010")
define qb = Character("Q-Bit", color="#0138C1")
image q = "quanta base.png"

# El juego comienza aquí.

label script3_start:

    "After overcoming the challenge of Superposition and following this arduous path, we have arrived at..."
    image 3 = "nivel 3.png"
    scene 3 
    with fade 
    "DECOHERENCE LAIR"
    "The place where the villain Decoherence brought Professor Planck..."
    "We can observe the lair where noise dwells, where every action, every look, makes everything collapse, through the noisy environment..."
    
    show decoherencia base at Position(xpos=0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)
    decoherencia "HAHAHAHA! You will never find the professor." 
    hide decoherencia base

    show qbit preparado at Position(xpos=0.15, xanchor=0.5, ypos=0.5, yanchor=0.5)
    qb "It's the evil Decoherence!"
    hide qbit preparado

    show quanta bravo2 at left:
        zoom 0.75
    q "We will rescue the professor!"
    hide quanta bravo2 left

    show decoherencia malvado at Position(xpos=0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)
    decoherencia "To pass, you must first demonstrate your understanding of entanglement. I don't think you have mastered that concept yet Quanta."
    hide decoherencia malvado
    with dissolve 

    show quanta determinado2 at left:
        zoom 0.75
    q "Oh! You think so? Well, you're wrong."
    q "Entanglement, one of the basis of quantum communication and quantum computing - we accept your challenge!"
    hide quanta determinado2 at left

    stop music fadeout 1.5
    "Immediately after Quanta finished his sentence the evil Decoherence left for the Entanglement Forest. They needed to run after it!"

    call script4_start from _call_script4_start
    return
