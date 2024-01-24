# Import necessary libraries:
init python:
    # POR FAVOR, NO CAMBIAR EL NOMBRE DE LAS CARTAS EN LA CARPETA DE IMAGENES.
    def randomize_cards():
        global cards
        cards = []

        # Loop to create specific pairs, each pair added twice:
        for i in range(1, 9, 2):  # Iterate through pairs.
            for _ in range(2):  # Add each pair twice.
                # Add two specific consecutive cards (e.g., card-1 and card-2)
                cards.append(["card-%s" % i, "deselected", "visible"])      # e.g., card-1, that this a component of the total angular moment
                cards.append(["card-%s" % (i + 1), "deselected", "visible"])  # e.g., card-2, , that this another component of the total angular moment
                # The other pairs: card-3 and card-4 (angular position, and angular momentum); card-5 and card-6 (linear position, and momentum); card-7 and card-8 (time, and energy).

        renpy.random.shuffle(cards) # Shuffle the cards to randomize their order.

    def select_card(card_index):
        global selected_cards
        global match_found

        # Prevent selecting a new card if two cards are already selected (no vas a pasar este nivel a la random por solo cliquear rápido)
        if len(selected_cards) == 2:
            return  # Do nothing if two cards are already selected.

        # Mark the selected card and add it to the list of selected cards:
        cards[card_index][1] = "selected"
        selected_cards.append(card_index)

        # Logic to determine a match for specific pairs:
        if len(selected_cards) == 2:
            # Extract numbers from card identifiers (por eso les pido no cambiar el nombre).
            first_card_num = int(cards[selected_cards[0]][0].split('-')[1])
            second_card_num = int(cards[selected_cards[1]][0].split('-')[1])

            # Check if the selected cards form a valid pair:
            if ((first_card_num % 2 == 1 and second_card_num == first_card_num + 1) or
                (second_card_num % 2 == 1 and first_card_num == second_card_num + 1)):
                match_found = True

    def deselect_cards():
        global selected_cards

        # Deselect the cards if two cards have been selected:
        if len(selected_cards) == 2:
            for card in cards:
                if card[1] == "selected":
                    card[1] = "deselected"
        selected_cards = []

    def hide_matches():
        global selected_cards
        global match_found
        global hidden_cards

        # Hide matched cards and update the count of hidden cards:
        cards[selected_cards[0]][2] = "hidden"
        cards[selected_cards[1]][2] = "hidden"
        hidden_cards += 2
        deselect_cards()
        match_found = False

    def reset_memory_game():
        global match_found
        global hidden_cards
        global game_count

        # Reset the game state for a new round or jump to the end of the game.
        # Como realmente no es un juego de memoria pero si un juego de pares que la gente esta haciendo una primera vez, al menos yo considero es bueno lo hagan una segunda vez para forzar recordar los pares.
        match_found = False
        hidden_cards = 0
        game_count += 1
        if game_count < 2:
            randomize_cards()
        else:
            renpy.jump("after_memory_game")

transform card_fadein:
    # Fade-in transformation for card appearance:
    alpha 0.0
    easein 0.5 alpha 1.0

screen memory_mini_game:
    image "background_cards.png"
    
    vbox:
        align (0.5, 0.5)  # Center the grid on the screen.
        xmaximum 900  # Set the maximum width of the grid.
        ymaximum 650  # Set the maximum height of the grid.

        grid 4 4:
            spacing 10
            for i, card in enumerate(cards):
                fixed:
                    xmaximum 210  # Maximum width for each card.
                    ymaximum 270  # Maximum height for each card.
                    if card[1] == "deselected" and card[2] == "visible":
                        imagebutton idle "card-back.png" action Function(select_card, card_index = i) at card_fadein
                    elif card[1] == "selected" and card[2] == "visible":
                        image "%s.png" % card[0] at card_fadein
                    else:
                        null

    # Logic to handle matched cards or reset the game:
    if match_found:
        timer 1.0 action Function(hide_matches) repeat True
    elif len(selected_cards) == 2:
        timer 1.0 action Function(deselect_cards) repeat True
    elif hidden_cards == card_amount:
        timer 0.5 action Function(reset_memory_game) repeat False

# Default variables for the game:
default card_amount = 16 # Total number of cards in the game.
# default card_rows = 3
default cards = [] # List to store card states.
default selected_cards = [] # List to track selected cards.
default hidden_cards = 0 # Count of hidden cards.
default match_found = False # Flag to indicate if a match is found.
default game_count = 0 # Counter for the number of game rounds.

# Define characters and images:
define quanta = Character("Quanta", color="#29C101")
define qbit = Character("Q_Bit", color="#0138C1")
define schrodinger = Character("Schrödinger's Cat", color="#bd0202")

screen game_over3(): # El problemita que tenías Antonia es que tenías que cambiar aquí el númerito y poner 3. Tipo definir una nueva pantalla.
    add "game_over_screen2" 
    modal True

    imagebutton auto "game_over_screen_%s.png":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Game Over")
        unhovered SetVariable("screen_tooltip", "")
        action Jump("start6")

# Initialize a variable to count incorrect answers:
default incorrect_choices3 = 0

# Game introduction starts here:
label start6:
    scene fondo incertidumbre with fade
    play music "HoliznaCC0 - Letting Go Of The Past.mp3" loop fadein 3.0

    "Quanta and Q-Bit continues their adventure. Now, Quanta and Q-Bit find themselves in a peculiar place, known as the 'Quantum Uncertainty Valley'."
    "It is here that the enigmatic and whimsical Schrödinger's Cat awaits to test their understanding of the quantum world."

    show scho base at right with dissolve:
    schrodinger "Welcome, quantum explorers! I won't let you pass until you play my memory game, let's think a bit into the wonders of quantum mechanics."
    hide scho base at right

    show quanta bravo2 at left:
        zoom 0.75
    quanta "How so?"
    hide quanta bravo2 at left

    # Quantum Mechanics Descriptions to understand the Principle:

    show scho feliz at right with dissolve:
        zoom 2
    schrodinger "Quantum and classical mechanics share some similarities, yet they diverge in their abstractions. In quantum mechanics, the concept of a 'state' is much more complex than in the classical world."
    schrodinger "In classical mechanics, understanding a state is straightforward - like knowing the position and speed of a particle. But in quantum mechanics, states and measurements are two entirely different things."
    hide scho feliz at right
    
    show qbit base at Position(xpos=0.95, ypos=0.4) with moveinright
    qbit "That's right, Quanta. The connection between the labels defining a state and those used for measuring it is not at all straightforward."
    hide qbit base at Position(xpos=0.95, ypos=0.4)

    show quanta base at left with moveinleft:
        zoom 0.75
    quanta "That actually makes sense. Professor Planck taught me that an experiment isn't just about the system under study; it also includes an apparatus for measurements and recording results."
    hide quanta base at left

    show qbit base at Position(xpos=0.95, ypos=0.4) with moveinright
    qbit "Yes. Every experiment requires an external apparatus for interaction and recording, making it invasive by nature."
    hide qbit base at Position(xpos=0.95, ypos=0.4)

    show scho feliz at right with dissolve:
        zoom 2
    schrodinger "HO-HO Precisely! Every experiment in quantum mechanics is invasive. Unlike classical physics, where measurements can be unobtrusively made, quantum measurements always influence the system being measured."
    schrodinger "This leads us to the heart of quantum mechanics: the uncertainty principle, also know as Heisenberg's principle. It's not just about position and momentum; it applies to all pairs of quantum properties."
    hide scho feliz at right

label intromemorypairs:
    # Introduction to the Memory Game:
    show scho base at right with dissolve:
    schrodinger "Alright, ready for a fun challenge? I've got a memory game that's a bit different. It's about making pairs, but not just any pairs - they're special uncertainty principle pairs!"

    # Schrödinger's Cat Explanation:
    schrodinger "In quantum mechanics, there are the 'conjugate pairs' of the uncertainty principle. For instance, position (X) and linear momentum (P) are one such pair."
    show quanta base at left with moveinleft:
        zoom 0.75
    quanta "Conjugate pairs, huh?"
    schrodinger "Exactly! And there are more than just position and momentum. There's also angular momentum (L) and angular position (O), where knowing more about one means you know less about the other."
    hide scho base at right
    show qbit base at Position(xpos=0.95, ypos=0.4) with moveinright
    qbit "In other words Quanta: the more precisely one measures the angular position (O), the less precisely the angular momentum (L) can be known, and vice versa."
    hide qbit base at Position(xpos=0.95, ypos=0.4)
    quanta "I see."
    show scho base at right with dissolve:
    schrodinger "Then there's the energy-time pair. The more precisely you measure a system's energy (E), the less you know about the time (T) of measurement."
    quanta "Interesting!"
    schrodinger "So in my game, you'll find cards labeled with 'P' for momentum, 'X' for linear position, 'T' for time, 'E' for energy, 'O' for angular position, and 'L' for angular momentum."
    schrodinger "Plus, cards labeled 'J' with tiny indices like 'i' and 'j' in the infirior right corner - they look similar but are different components of total angular momentum."
    hide scho base at right
    show qbit base at Position(xpos=0.95, ypos=0.4) with moveinright
    qbit "Yes, the two orthogonal components of the total angular momentum operator of an object. That is also another pair in the uncertainty principle, Quanta. Then: just try to pair the J."
    hide qbit base at Position(xpos=0.95, ypos=0.4)
    quanta "Okay, so I need to pair these based on their quantum relationship, right?"
    show scho base at right with dissolve:
    schrodinger "Exactly! The game is all about finding and remembering these special pairs. We'll play it twice to make sure you've got the hang of it. Ready to test your memory and learn a bit about quantum mechanics?"

    menu:
        "Yes.":
            hide scho base at right
            jump after_pair_explanation

        "No.":
            quanta "Could you please repeat all this for me once more?"
            hide quanta base at left
            jump intromemorypairs

label after_pair_explanation:
    quanta "Ready to give it a try!"
    hide quanta base at left

    # Game begins here.
    $randomize_cards()
    call screen memory_mini_game
    # Game finish here.

label after_memory_game:
    "After successfully completing the memory game, Schrödinger's Cat seems impressed with Quanta knowledge."

    show scho feliz at right with dissolve:
        zoom 2
    schrodinger "So cool! You have a firm grasp on these complex concepts. Now, let's see if you can apply this knowledge to find Professor Planck."
    hide scho feliz at right

    # Schrödinger's Cat poses a final question:
    show scho base at right with dissolve:
    schrodinger "According to Heisenberg's uncertainty principle, my final questions to you are: what is the Heisenberg's principle, Quanta?"
    hide scho base at right

    show quanta bravo2 at left:
        zoom 0.75
    quanta "Heisenberg's principle states that it is impossible to know the position and momentum of a particle with precision at the same time."
    hide quanta bravo2
    
    show scho base at right with dissolve:
    schrodinger "And what does that mean again, Quanta?"
    hide scho base at right

    show quanta bravo2 at left:
        zoom 0.75
    quanta "It means that even if we can measure the position of a particle with precision, then its momentum will be indeterminate. And vice versa."
    hide quanta bravo2

    show scho base at right with dissolve:
    schrodinger "I know, so... is the professor lost forever if you know his position? If you answer wrong just once, you will repeat all this level Quanta."
    hide scho base at right
    
    menu:
        "Yes.":
            # Wrong Answer
            $ incorrect_choices3 += 1
            show qbit base at Position(xpos=0.95, ypos=0.4) with moveinright
            qbit "Mmm, no I don't think so."
            hide qbit base at Position(xpos=0.95, ypos=0.4)
            if incorrect_choices3 >= 1:
                call screen game_over3

        "No.":
            # Correct Answer
            $ incorrect_choices = 0  # Reset the count for correct choice.
            jump level6_end
    
label level6_end:

    show quanta bravo2 at left:
            zoom 0.75
    quanta "No, because the professor is a human being, then the principle does not apply to humans."
    hide quanta bravo2

    show scho feliz at right with dissolve:
        zoom 2
    schrodinger "Well done! Your journey to understand the quantum world is advancing. For me, you can pass Quanta. But remember, there are always new mysteries to unravel."
    hide scho feliz at right

    show quanta base at left with moveinleft:
        zoom 0.75
    quanta "Are we ready to return to Decoherence's Lair?"
    hide quanta base at left

    show qbit base at Position(xpos=0.95, ypos=0.4) with moveinright
    qbit "We're prepared for whatever comes next. Let's go, Quanta! Back to Decoherence Lair."
    hide qbit base at Position(xpos=0.95, ypos=0.4)

    stop music fadeout 1.0
    scene black with fade

    call start7 from _call_start7

    return