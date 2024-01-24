# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define Quanta = Character("Quanta", color="#29C101")
define Q_Bit = Character("Q_Bit", color="#0138C1")
define Alice = Character("Alice", color="#2660db")
define Bob = Character("Bob", color="#540f7c")

"""
Carolina's comment: I decided to do this almost step by step to make it clear so the code is not optimize... but it works! You can inspire yourself from it and do it better.
"""

init python:
    import random # La siempre confiable random de Python.

    # Variables to track each pair's placement:
    pairs_completed = {
        "h1p1": False,
        "h2p2": False,
        "h3p3": False,
        "h4p4": False,
        "h5p5": False,
        "h6p6": False,
        "t1p7": False,
        "t2p8": False,
        "t3p9": False,
        "t4p10": False,
        "t5p11": False,
        "t6p12": False,
    }

    def check_all_pairs_completed():
        return all(pairs_completed.values())

    def dragged_func1(dragged_items, dropped_on):
        if dropped_on is not None: # To avoid Ren'Py error message if H1 is place in any random place.
            if dragged_items[0].drag_name == "h1" and dropped_on.drag_name == "p1": # When H1 is dropped in position 1 [...]
                dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.5) # It will be drag like a magnet to p1.
                renpy.play("253887__themusicalnomad__positive_beeps.wav") # [...] yous should listen this sound.
                pairs_completed["h1p1"] = True
                if check_all_pairs_completed():
                    renpy.jump("zeroB_continue")
    
    def dragged_func2(dragged_items, dropped_on):
        if dropped_on is not None:
            if dragged_items[0].drag_name == "h2" and dropped_on.drag_name == "p2":
                dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.5)
                renpy.play("253887__themusicalnomad__positive_beeps.wav")
                pairs_completed["h2p2"] = True
                if check_all_pairs_completed():
                    renpy.jump("zeroB_continue")
    
    def dragged_func3(dragged_items, dropped_on):
        if dropped_on is not None:
            if dragged_items[0].drag_name == "h3" and dropped_on.drag_name == "p3":
                dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.5)
                renpy.play("253887__themusicalnomad__positive_beeps.wav")
                pairs_completed["h3p3"] = True
                if check_all_pairs_completed():
                    renpy.jump("zeroB_continue")

    def dragged_func4(dragged_items, dropped_on):
        if dropped_on is not None:
            if dragged_items[0].drag_name == "h4" and dropped_on.drag_name == "p4":
                dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.5)
                renpy.play("253887__themusicalnomad__positive_beeps.wav")
                pairs_completed["h4p4"] = True
                if check_all_pairs_completed():
                    renpy.jump("zeroB_continue")

    def dragged_func5(dragged_items, dropped_on):
        if dropped_on is not None:
            if dragged_items[0].drag_name == "h5" and dropped_on.drag_name == "p5":
                dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.5)
                renpy.play("253887__themusicalnomad__positive_beeps.wav")
                pairs_completed["h5p5"] = True
                if check_all_pairs_completed():
                    renpy.jump("zeroB_continue")

    def dragged_func6(dragged_items, dropped_on):
        if dropped_on is not None:
            if dragged_items[0].drag_name == "h6" and dropped_on.drag_name == "p6":
                dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.5)
                renpy.play("253887__themusicalnomad__positive_beeps.wav")
                pairs_completed["h6p6"] = True
                if check_all_pairs_completed():
                    renpy.jump("zeroB_continue")

    def dragged_func7(dragged_items, dropped_on):
        if dropped_on is not None:
            if dragged_items[0].drag_name == "t1" and dropped_on.drag_name == "p7":
                dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.5)
                renpy.play("253887__themusicalnomad__positive_beeps.wav")
                pairs_completed["t1p7"] = True
                if check_all_pairs_completed():
                    renpy.jump("zeroB_continue")

    def dragged_func8(dragged_items, dropped_on):
        if dropped_on is not None:
            if dragged_items[0].drag_name == "t2" and dropped_on.drag_name == "p8":
                dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.5)
                renpy.play("253887__themusicalnomad__positive_beeps.wav")
                pairs_completed["t2p8"] = True
                if check_all_pairs_completed():
                    renpy.jump("zeroB_continue")

    def dragged_func9(dragged_items, dropped_on):
        if dropped_on is not None:
            if dragged_items[0].drag_name == "t3" and dropped_on.drag_name == "p9":
                dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.5)
                renpy.play("253887__themusicalnomad__positive_beeps.wav")
                pairs_completed["t3p9"] = True
                if check_all_pairs_completed():
                    renpy.jump("zeroB_continue")

    def dragged_func10(dragged_items, dropped_on):
        if dropped_on is not None:
            if dragged_items[0].drag_name == "t4" and dropped_on.drag_name == "p10":
                dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.5)
                renpy.play("253887__themusicalnomad__positive_beeps.wav")
                pairs_completed["t4p10"] = True
                if check_all_pairs_completed():
                    renpy.jump("zeroB_continue")

    def dragged_func11(dragged_items, dropped_on):
        if dropped_on is not None:
            if dragged_items[0].drag_name == "t5" and dropped_on.drag_name == "p11":
                dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.5)
                renpy.play("253887__themusicalnomad__positive_beeps.wav")
                pairs_completed["t5p11"] = True
                if check_all_pairs_completed():
                    renpy.jump("zeroB_continue")

    def dragged_func12(dragged_items, dropped_on):
        if dropped_on is not None:
            if dragged_items[0].drag_name == "t6" and dropped_on.drag_name == "p12":
                dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.5)
                renpy.play("253887__themusicalnomad__positive_beeps.wav")
                pairs_completed["t6p12"] = True
                if check_all_pairs_completed():
                    renpy.jump("zeroB_continue")

screen drag_and_drop_puzzle:
    image "tablepuzzle1.png"
    draggroup: #Without this there are properties of drap and drop you cannot use.
        # Draggable state for H1:
        $ hxpos1, hypos1 = random.uniform(0.1, 0.9), random.uniform(0.1, 0.5) # In a random position for replay purpose.
        drag:
            align(hxpos1, hypos1)
            drag_raise True # Each time you take it would be above all.
            drag_offscreen False # You cannot take the piece outside the screen.
            drag_name "h1"
            dragged dragged_func1
            image "h1.png" xysize(200,200) # The image with an adapt size.
        # Draggable state for H2:
        $ hxpos2, hypos2 = random.uniform(0.1, 0.9), random.uniform(0.1, 0.5)
        drag:
            align(hxpos2, hypos2)
            drag_raise True
            drag_offscreen False
            drag_name "h2"
            dragged dragged_func2
            image "h2.png" xysize(200,200)
        # H3:
        $ hxpos3, hypos3 = random.uniform(0.1, 0.9), random.uniform(0.1, 0.5)
        drag:
            align(hxpos3, hypos3)
            drag_raise True
            drag_offscreen False
            drag_name "h3"
            dragged dragged_func3
            image "h3.png" xysize(200,200)
        # H4:
        $ hxpos4, hypos4 = random.uniform(0.1, 0.9), random.uniform(0.1, 0.5)
        drag:
            align(hxpos4, hypos4)
            drag_raise True
            drag_offscreen False
            drag_name "h4"
            dragged dragged_func4
            image "h4.png" xysize(200,200)
        $ hxpos5, hypos5 = random.uniform(0.1, 0.9), random.uniform(0.1, 0.5) 
        drag:
            align(hxpos5, hypos5)
            drag_raise True
            drag_offscreen False
            drag_name "h5"
            dragged dragged_func5
            image "h5.png" xysize(200,200)
        $ hxpos6, hypos6 = random.uniform(0.1, 0.9), random.uniform(0.1, 0.5)
        drag:
            align(hxpos6, hypos6)
            drag_raise True
            drag_offscreen False
            drag_name "h6"
            dragged dragged_func6
            image "h6.png" xysize(200,200)

        # Tails states:
        $ txpos1, typos1 = random.uniform(0.1, 0.9), random.uniform(0.5, 0.9)
        drag:
            align(txpos1, typos1)
            drag_raise True
            drag_offscreen False
            drag_name "t1"
            dragged dragged_func7
            image "t1.png" xysize(200,200)
        $ txpos2, typos2 = random.uniform(0.1, 0.9), random.uniform(0.5, 0.9)
        drag:
            align(txpos2, typos2)
            drag_raise True
            drag_offscreen False
            drag_name "t2"
            dragged dragged_func8
            image "t2.png" xysize(200,200)
        $ txpos3, typos3 = random.uniform(0.1, 0.9), random.uniform(0.5, 0.9)
        drag:
            align(txpos3, typos3)
            drag_raise True
            drag_offscreen False
            drag_name "t3"
            dragged dragged_func9
            image "t3.png" xysize(200,200)
        $ txpos4, typos4 = random.uniform(0.1, 0.9), random.uniform(0.5, 0.9)
        drag:
            align(txpos4, typos4)
            drag_raise True
            drag_offscreen False
            drag_name "t4"
            dragged dragged_func10
            image "t4.png" xysize(200,200)
        $ txpos5, typos5 = random.uniform(0.1, 0.9), random.uniform(0.5, 0.9)
        drag:
            align(txpos5, typos5)
            drag_raise True
            drag_offscreen False
            drag_name "t5"
            dragged dragged_func11
            image "t5.png" xysize(200,200)
        $ txpos6, typos6 = random.uniform(0.1, 0.9), random.uniform(0.5, 0.9)
        drag:
            align(txpos6, typos6)
            drag_raise True
            drag_offscreen False
            drag_name "t6"
            dragged dragged_func12
            image "t6.png" xysize(200,200)
            
        # The drops:
        # Position for the first drop: P1. Here we're going to put H1:
        drag:
            align(0.173, 0.42) # Right place for H1.
            draggable False
            drag_raise False
            drag_name "p1"
            image Solid("#9fde6f88") xysize(200,200)
        # Position for the second drop: P2. Here we're going to put H2:
        drag:
            align(0.296, 0.42) # Right place for H2.
            draggable False
            drag_raise False
            drag_name "p2"
            image Solid("#9fde6f88") xysize(200,200)
        drag:
            align(0.42, 0.42) # Right place for H3.
            draggable False
            drag_raise False
            drag_name "p3"
            image Solid("#9fde6f88") xysize(200,200)
        drag:
            align(0.54, 0.42) # Right place for H4.
            draggable False
            drag_raise False
            drag_name "p4"
            image Solid("#9fde6f88") xysize(200,200)
        drag:
            align(0.662, 0.42) # Right place for H5.
            draggable False
            drag_raise False
            drag_name "p5"
            image Solid("#9fde6f88") xysize(200,200)
        drag:
            align(0.785, 0.42) # Right place for H6.
            draggable False
            drag_raise False
            drag_name "p6"
            image Solid("#9fde6f88") xysize(200,200)
        # Position for the 7th drop: P7. Here we're going to put T1:
        drag:
            align(0.173, 0.67) # Right place for T1.
            draggable False
            drag_raise False
            drag_name "p7"
            image Solid("#9fde6f88") xysize(210,210)
        drag:
            align(0.296, 0.67) # Right place for T2.
            draggable False
            drag_raise False
            drag_name "p8"
            image Solid("#9fde6f88") xysize(210,210)
        drag:
            align(0.42, 0.67) 
            draggable False
            drag_raise False
            drag_name "p9"
            image Solid("#9fde6f88") xysize(210,210)
        drag:
            align(0.54, 0.67) 
            draggable False
            drag_raise False
            drag_name "p10"
            image Solid("#9fde6f88") xysize(210,210)
        drag:
            align(0.662, 0.67) 
            draggable False
            drag_raise False
            drag_name "p11"
            image Solid("#9fde6f88") xysize(210,210)
        drag:
            align(0.785, 0.67) 
            draggable False
            drag_raise False
            drag_name "p12"
            image Solid("#9fde6f88") xysize(210,210)

screen drag_and_drop_result():
    add "tablepuzzle2.png"
    vbox xalign 1.0 yalign 1.0:
        imagebutton auto "buttom_%s" action [ToggleScreen("drag_and_drop_result"), Jump("one_question_more")]

screen last_puzzle_A():
    add "tablepuzzle3.png"
    vbox xalign 1.0 yalign 1.0:
        imagebutton auto "buttom_%s" action [ToggleScreen("last_puzzle_A"), Jump("tableH1T1")]

screen last_puzzle_B():
    add "tablepuzzle4.png"
    vbox xalign 1.0 yalign 1.0:
        imagebutton auto "buttom_%s" action [ToggleScreen("last_puzzle_B"), Jump("tableH1T2")]

screen game_over2():
    add "game_over_screen2" 
    modal True

    imagebutton auto "game_over_screen_%s.png":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Game Over")
        unhovered SetVariable("screen_tooltip", "")
        action Jump("start1")

# Initialize a variable to count incorrect answers:
default incorrect_choices2 = 0

# El juego comienza aquí.

label script4_start:

    # Reset the count of incorrect choices at the start of the game.
    $ incorrect_choices2 = 0 # Just in case the player is doing back the whole game, to don't be hyper punishing the second time and that tey have fresh 3 options back.

    scene nivel 4
    with fade
    play music "John Bartmann - broken-suspense-master.mp3" loop fadein 3.0

    "Here we are, the Entanglement Forest..."
    "As Quanta and Q-Bit venture deeper in it, they encounter two figures, Alice and Bob, standing beside a curious-looking table."

    show basealice at left with dissolve:
        zoom 0.80

    Alice "Welcome, Quanta and Q-Bit. To navigate through the Entanglement forest, you must understand the concept of entanglement."

    hide basealice at left
    show basebob at right with dissolve:
        zoom 0.80
    Bob "And to do that, you'll need to solve our puzzles. If you get 3 answers wrong, you would have to restart the game."

    hide basebob at right
    show qbit base at Position(xpos=0.95, ypos=0.4) with moveinright
    Q_Bit "Don't worry, Quanta. I'll help you through this!"
    hide qbit base at Position(xpos=0.95, ypos=0.4) 

    show basealice at left with moveinleft:
        zoom 0.80
    Alice "Let me explain my system first. I have a quantum coin."

    show alicecoin at Position(xpos=0.5, ypos=0.5) with moveinright

label zeroA_Question:

    Alice "It's not like a regular classical coin, Quanta. In the quantum world, it can be in a state of Heads, which we denote as |H>, or Tails, denoted as |T>. Seems similar, but it is not."
    hide alicecoin at Position(xpos=0.5, ypos=0.5) with moveinright

    Alice "Here's the twist – in quantum mechanics, my coin can be in a superposition of both Heads and Tails at the same time! It's only when you measure it that it decides its state. Do you understand that Quanta?"
    
    menu:
        "Yes.":
            hide basealice at left
            jump zeroA_continue

        "No.":
            Alice "I will repeat."
            jump zeroA_Question

label zeroA_continue:

    scene nivel 4
    show quanta determinado2 at left:
        zoom 0.75
    Quanta "I think I'm starting to understand your system, Alice. Superposition is fascinating!"

    hide quanta determinado2 at left
    show basebob at right with moveinright:
        zoom 0.80
    Bob "Now it is my turn. My system is a bit different. I have a quantum dice. It has six faces, numbered from |1> to |6>."
    hide basebob at right

    show bobdice at Position(xpos=0.5, ypos=0.5) with dissolve

    show basebob at left with moveinleft:
        zoom 0.80
    Bob "Just like Alice's coin, my dice can exist in a state that is a superposition of all its possible outcomes. It's only when we observe it that it 'chooses' a number."

    hide basebob at left
    hide bobdice at Position(xpos=0.5, ypos=0.5) with dissolve
    show qbit base at Position(xpos=0.95, ypos=0.4) with moveinright
    Q_Bit "So, our task is to understand how these two systems can be combined and whether they can become entangled, right?"

    hide qbit base at Position(xpos=0.95, ypos=0.4)
    show basealice at left with moveinleft:
        zoom 0.80
    Alice "Exactly! When you combine our systems, you'll create a larger quantum system. The puzzle is to figure out how these combined states behave and interact. Are you ready for that?"

# Before calling the drag_and_drop_game label, reset the pairs_completed dictionary:
$ pairs_completed = {key: False for key in pairs_completed}

label drag_and_drop_game:
    call screen drag_and_drop_puzzle

label zeroB_continue:
    Alice "Well done Quanta! Figuring out how systems combine to make bigger systems is something we do a lot in physics."
    hide basealice at left

    show basebob at right with moveinright:
        zoom 0.80
    Bob "Each key in the table denotes our basis vector for our combined system."
    hide basebob at right

label one_question_more:
    show basealice at left with moveinleft:
        zoom 0.80
    Alice "For example, you noticed there was a key labeled H3."

    Alice "Which state H3 represents in our combined system?"
    
    menu:
        "Coin shows Heads and the dice shows the number 3.":
            # Correct.
            hide basealice at left
            jump tableunderstood

        "Coin shows Tails and the dice shows the number 3.":
            $ incorrect_choices2 += 1 # Wrong.
            Alice "I think you need to see the state-labels back..."
            if incorrect_choices2 >= 3:
                call screen game_over2
            else:
                call screen drag_and_drop_result

label tableunderstood:

    scene nivel 4
    show quanta determinado2 at left:
        zoom 0.75
    Quanta "Easy, the state labeled H3 represents a state in the combined system of you two in which the coin shows Heads and the dice shows the number 3."
    hide quanta determinado2 at left

    show qbit base at Position(xpos=0.95, ypos=0.4) with moveinright
    Q_Bit "And in the combined system, there are 12 basis vectors altogether."
    hide qbit base at Position(xpos=0.95, ypos=0.4) 

    show basebob at right with dissolve:
        zoom 0.80
    Bob "Indeed. Now, I have a question also for you Quanta. Let's focus on two specific states: |H1> and |T1>."
    hide basebob at right

    call screen last_puzzle_A

label tableH1T1:

    show basebob at right with dissolve:
        zoom 0.80
    Bob "As you saw, this means Alice's coin is either in Heads and my dice is in state 1, or Alice's coin is in state Tails my dice is still in state 1."
    
    Bob "Does the state of Alice's coin depend on the state of my dice in this scenario?"
    
    menu:
        "Yes.":
            $ incorrect_choices2 += 1# Incorrect Answer
            hide basebob at right
            show qbit base at Position(xpos=0.95, ypos=0.4) with moveinright
            Q_Bit "Think about this Quanta: There's a consistent pattern, but does Alice's coin really affect Bob's dice here?"
            hide qbit base at Position(xpos=0.95, ypos=0.4) 
            if incorrect_choices2 >= 3:
                call screen game_over2
            else:
                call screen last_puzzle_A

        "No.":
            hide basebob at right
            # Correct Answer
            jump tableH1T1_continuation

label tableH1T1_continuation:

    show quanta base at left with moveinleft:
        zoom 0.75
    Quanta "No. The states are independent."
    hide quanta base at left

    show basealice at left with dissolve:
        zoom 0.80
    Alice "Excellent Quanta. The coin and the dice are in a superposition of states, but these states are independent of each other."
    Alice "My coin being Heads or Tails doesn't change the fact that Bob's dice is showing 1. Therefore, we said that these states are not entangled."
    hide basealice at left

    show basebob at right with dissolve:
        zoom 0.80
    Bob "As Alice mentioned, since the state of one system doesn't tell you anything specific about the state of the other system, they are not entangled."
    hide basebob at right

label tableH2T1:

    show basealice at left with dissolve:
        zoom 0.80
    Alice "Last question Quanta. Let's focus on two different states: |H2> and |T1>."
    hide basealice at left
    
    call screen last_puzzle_B

label tableH1T2:

    show basealice at left with dissolve:
        zoom 0.80
    Alice "This means, when my coin shows Heads, Bob's dice shows 2. But when my coin is Tails, his dice shows 1."
    
    Alice "Does the state of my coin depend on the state of Bob's dice in this scenario?"
    
    menu:
        "Yes.":
            # Correct Answer
            hide basealice at left
            jump tableH2T1_continuation

        "No.":
            hide basealice at left
            $ incorrect_choices2 += 1# Incorrect Answer
            show qbit base at Position(xpos=0.95, ypos=0.4) with moveinright
            Q_Bit "Consider this, Quanta: When Alice observes her coin, there are two equally probable outcomes, Heads or Tails. This observation isn't just about the coin itself, but affects the whole system."
            Q_Bit "If Alice observes Heads in this scenario, the entire system instantly collapses to the state |H2>, meaning Bob will definitely find his dice showing 2. On the other hand, if she observes Tails, the system collapses to |T1>, and Bob's dice will show 1."
            Q_Bit "So, the outcome isn't completely random. Alice's observation influences the state of the entire system, hinting at a deeper connection. Don't you think?"
            hide qbit base at Position(xpos=0.95, ypos=0.4)
            if incorrect_choices2 >= 3:
                call screen game_over2
            else:
                call screen last_puzzle_B

label tableH2T1_continuation:

    show quanta base at left with moveinleft:
        zoom 0.75
    Quanta "Yes! The state of the coin seems to be connected to the state of the dice, suggesting entanglement."

    show qbit base at Position(xpos=0.95, ypos=0.4) with moveinright
    Q_Bit "Exactly Quanta. Despite the randomness of Alice's coin, the state of the entire system is not completely random."
    hide qbit base at Position(xpos=0.95, ypos=0.4)
    hide quanta base at left

    show basealice at left with dissolve:
        zoom 0.80
    Alice "For us Quanta, you've grasped the concept of quantum entanglement."
    show basebob at right with dissolve:
        zoom 0.80
    Bob "Yes, impressive indeed! As promised, you may pass through the forest."
    hide basealice at left
    hide basebob at right

    show quanta base at left with moveinleft:
        zoom 0.75
    Quanta "Thank you! By the way, did Decorence pass this way?"
    hide quanta base at left
    
    show basealice at left with dissolve:
        zoom 0.80
    Alice "Ehh... no, villains don't really follow the rules, Quanta."
    hide basealice at left
    
    show qbit base at Position(xpos=0.95, ypos=0.4) with moveinright
    Q_Bit "Sounds like it's avoiding observation to prevent collapse Quanta. Quite the quantum trickster, isn't it?... {i}ba dumb tss{/i} 😀"
    play sound "ba_dum_tss.wav" volume 0.1
    hide qbit base at Position(xpos=0.95, ypos=0.4) with moveinright

    show quanta bravo2 at left:
        zoom 0.75
    Quanta "I think I'm starting to understand your system also, Q-Bit. Every bad joke is just a superposition of being funny and not funny at the same time!"

    show qbit base at Position(xpos=0.95, ypos=0.4) with moveinright
    Q_Bit "Come on! It was a bit fun 😀"
    play sound "ba_dum_tss.wav" volume 0.1
    hide qbit base at Position(xpos=0.95, ypos=0.4) with moveinright
    hide quanta bravo2 at left
    
    "Everyone shares a laugh, appreciating the quirky humor before continuing their journey through the forest to the exit: the Uncertainty Valley."

    stop music fadeout 1.0
    scene black with fade
    
    call start5M from _call_start5M

    return
