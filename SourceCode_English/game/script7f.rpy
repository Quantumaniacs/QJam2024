# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Quanta = Character("Quanta", color="#29C101")
define Q_Bit = Character("Q_Bit", color="#0138C1")
define Professor = Character("Professor Planck", color="#14aa84")
define Decoherence = Character("Decoherence", color="#cc1010")

image professor_explicando:
    'profesor explicando2.png'

image professor_base:
    'profesor base.png'
    
image professor_excited:
    'profesor emocionado.png'

image quanta_determined:
    'quanta determinado2.png'

image quanta_brave:
    'quanta bravo2.png'

image decoherence_base:
    'decoherencia base.png'

image decoherence_laughing:
    'decoherencia malvado.png'

image decoherence_damaged:
    'decoherencia atacado.png'

        # ################################################## #
init python:
    answer = None

    quanta_min_hp = 0
    quanta_hp = quanta_min_hp

    decoherence_min_hp = 0
    decoherence_hp = decoherence_min_hp

    questions = {
                1: 'What does it mean the term "Superposition"?',
                2: '''If you were to apply the Grover's algorithm to search for something, what would you use in order to amplify the Oracle's signal?''',
                3:'''Approximately how many iterations for the Grover's algorithm will be required to do if we were to search for an item among 36 options?''',
                4: '''If we combine two quantum systems, one with 3 possible states and the other with 4, then, what is the number of basis vectors that would represent each possible combined state?''',
                5: '''If each of these two combined systems are in superposition, then the state of one depends on the other?''',
                6:'''According to the Uncertainty Principle, what does it mean that two variables are 'conjugate' between them?''',
                7:'''What is the corresponding conjugate variable for the Energy?'''
                }

    def evaluate_answer(hp_character, character_answer, right_answer):
        if character_answer != right_answer:
            hp_character = hp_character-1
        else:
            hp_character = hp_character+1
        return hp_character

    def next_question(from_question):
        return from_question+1

    i = 1

    # ################################################## #

    # ################################################## #

    # THIS BLOCK OF CODE IS JUST FOR DOCUMENTING THE OPTIONS/ANSWERS:

    options_question1 = {
                        "A": "It is the ability of a quantum system to exist in multiple states simultaneously",
                        "B": "It is when the state of a quantum system depends on the state of another",
                        "C": "It is when a particle due to its wave-like nature can be on both sides of a potential energy barrier simultaneously",
                        "D": "It is the maintenance of phase relationships between different quantum states",
                        }


    right_answers = {1: "B", 2: "C", 3: "D", 4: "A", 5: "C", 6: "D", 7: "C"}
    # ################################################## #

screen question1:

    vbox:
        align((0.5, 0))

        hbox:
            spacing 80
            imagebutton auto "ans1_optionA_%s.png":
                focus_mask True
                action [SetVariable("answer", "A"), SelectedIf(answer=="A"), Jump("wrong")]
            imagebutton auto "ans1_optionB_%s.png":
                focus_mask True
                action [SetVariable("answer", "B"), SelectedIf(answer=="B"), Jump("correct")]
        hbox:
            spacing 80
            imagebutton auto "ans1_optionC_%s.png":
                focus_mask True
                action [SetVariable("answer", "C"), SelectedIf(answer=="C"), Jump("wrong")]
            imagebutton auto "ans1_optionD_%s.png":
                focus_mask True
                action [SetVariable("answer", "D"), SelectedIf(answer=="D"), Jump("wrong")]

screen question2:
    vbox:
        align((0.5, 0))

        hbox:
            spacing 80
            imagebutton auto "ans2_optionA_%s.png":
                focus_mask True
                action [SetVariable("answer", "A"), SelectedIf(answer=="A"), Jump("wrong")]
            imagebutton auto "ans2_optionB_%s.png":
                focus_mask True
                action [SetVariable("answer", "B"), SelectedIf(answer=="B"), Jump("wrong")]
        hbox:
            align((0.5, 0.5))
            spacing 80
            imagebutton auto "ans2_optionC_%s.png":
                focus_mask True
                action [SetVariable("answer", "C"), SelectedIf(answer=="C"), Jump("correct")]

screen question3:
    vbox:
        align((0.5, 0))

        hbox:
            spacing 80
            imagebutton auto "ans3_optionA_%s.png":
                focus_mask True
                action [SetVariable("answer", "A"), SelectedIf(answer=="A"), Jump("wrong")]
            imagebutton auto "ans3_optionB_%s.png":
                focus_mask True
                action [SetVariable("answer", "B"), SelectedIf(answer=="B"), Jump("wrong")]
        hbox:
            spacing 80
            imagebutton auto "ans3_optionC_%s.png":
                focus_mask True
                action [SetVariable("answer", "C"), SelectedIf(answer=="C"), Jump("wrong")]
            imagebutton auto "ans3_optionD_%s.png":
                focus_mask True
                action [SetVariable("answer", "D"), SelectedIf(answer=="D"), Jump("correct")]

screen question4:
    vbox:
        align((0.5, 0))

        hbox:
            spacing 80
            imagebutton auto "ans4_optionA_%s.png":
                focus_mask True
                action [SetVariable("answer", "A"), SelectedIf(answer=="A"), Jump("correct")]
            imagebutton auto "ans4_optionB_%s.png":
                focus_mask True
                action [SetVariable("answer", "B"), SelectedIf(answer=="B"), Jump("wrong")]
        hbox:
            spacing 80
            imagebutton auto "ans4_optionC_%s.png":
                focus_mask True
                action [SetVariable("answer", "C"), SelectedIf(answer=="C"), Jump("wrong")]
            imagebutton auto "ans4_optionD_%s.png":
                focus_mask True
                action [SetVariable("answer", "D"), SelectedIf(answer=="D"), Jump("wrong")]
        

screen question5:
    vbox:
        align((0.5, 0))

        hbox:
            spacing 80
            imagebutton auto "ans5_optionA_%s.png":
                focus_mask True
                action [SetVariable("answer", "A"), SelectedIf(answer=="A"), Jump("wrong")]
            imagebutton auto "ans5_optionB_%s.png":
                focus_mask True
                action [SetVariable("answer", "B"), SelectedIf(answer=="B"), Jump("wrong")]
        hbox:
            align((0.5, 0.5))
            spacing 80
            imagebutton auto "ans5_optionC_%s.png":
                focus_mask True
                action [SetVariable("answer", "C"), SelectedIf(answer=="C"), Jump("correct")]

screen question6:
    vbox:
        align((0.5, 0))

        hbox:
            spacing 80
            imagebutton auto "ans6_optionA_%s.png":
                focus_mask True
                action [SetVariable("answer", "A"), SelectedIf(answer=="A"), Jump("wrong")]
            imagebutton auto "ans6_optionB_%s.png":
                focus_mask True
                action [SetVariable("answer", "B"), SelectedIf(answer=="B"), Jump("wrong")]
        hbox:
            spacing 80
            imagebutton auto "ans6_optionC_%s.png":
                focus_mask True
                action [SetVariable("answer", "C"), SelectedIf(answer=="C"), Jump("wrong")]
            imagebutton auto "ans6_optionD_%s.png":
                focus_mask True
                action [SetVariable("answer", "D"), SelectedIf(answer=="D"), Jump("correct")]
        

screen question7:
    vbox:
        align((0.5, 0))

        hbox:
            spacing 80
            imagebutton auto "ans7_optionA_%s.png":
                focus_mask True
                action [SetVariable("answer", "A"), SelectedIf(answer=="A"), Jump("wrong")]
            imagebutton auto "ans7_optionB_%s.png":
                focus_mask True
                action [SetVariable("answer", "B"), SelectedIf(answer=="B"), Jump("wrong")]
        hbox:
            spacing 80
            imagebutton auto "ans7_optionC_%s.png":
                focus_mask True
                action [SetVariable("answer", "C"), SelectedIf(answer=="C"), Jump("correct")]
            imagebutton auto "ans7_optionD_%s.png":
                focus_mask True
                action [SetVariable("answer", "D"), SelectedIf(answer=="D"), Jump("wrong")]
        


# The game starts here.

label start7:

    play music "audio/PAX__Una_Aventura_Espacial.wav" loop fadein 0.5

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    
    scene black with fade

    """In the Decoherence Lair..."""

    scene nivel 3:
        zoom 1.1
    

    show professor_explicando at Position(xpos=0.75, ypos=0.35):
        zoom 1.35

    show qbit base at Position(xpos=0.95, ypos=0.4) with moveinright

    Q_Bit "Hey, look Quanta! There is the Professor Planck!"

    show quanta base at left with moveinleft:
        zoom 0.75

    hide professor_explicando
    show professor_excited at Position(xpos=0.75, ypos=0.35):
        zoom 1.1
    
    Professor "Q-Bit!, Quanta! I knew you would find me!"

    stop music
    play music "audio/Una_Ultima_Batalla.wav" noloop fadein 0.2
    
    show decoherence_base at Position(xpos=0.52, ypos=0.7) with pixellate

    Decoherence "HO-HO, Quanta!, I have to admit I'm really impressed that you have come this far!"

    Decoherence "But I'm not worried, I bet you still don't understand ANYTHING about the Quantum World!"

    show quanta_brave at left:
        zoom 0.75

    Quanta "Huh, you're so wrong, probably now I know more about the Quantum World than you!"
    
    hide decoherence_base
    show decoherence_laughing at Position(xpos=0.42, ypos=0.37):
        zoom 1.2

    Decoherence "HA-HA-HA!!, Do you really think you can beat me?"
    Decoherence "It'll only take me a couple of questions about Quantum Mechanics to prove that you're nothing more than a silly boy."

    hide quanta_brave
    show quanta_determined at left:
        zoom 0.75
    
    Quanta "Huh, go ahead! Ask me whatever you want, I'm gonna show you..."
    
    # Decoherence "HA-HA-HA!!, Do you really think you can beat me? Don't make me laugh!"

    # hide professor_excited
    
    # show professor_base at Position(xpos=0.75, ypos=0.35):
    #     zoom 1.35

    # Professor """If you are so confident in what you're saying, then you won't be
    # afraid to face Quanta in an intellectual battle over Quantum Mechanics concepts, right?"""
    
    # # Q_Bit "C'mon Quanta! We're finally ready to fight with Decoherence!"
    
    # Decoherence "Of course I'm not scared to fight! And you, Quanta?"

    # hide quanta_brave
    # show quanta_determined at left:
    #     zoom 0.75
    
    # Quanta "I'm gonna show you..."

    # hide professor_base
    
    # show professor_excited at Position(xpos=0.75, ypos=0.35):
    #     zoom 1.1

    # Professor "So, let the battle begin!"
    
    scene black with fade

    call question_start(i) from _call_question_start


label question_start(i):
    scene nivel 3 with fade:
        zoom 1.1

    play music "audio/Enemigos.wav" noloop fadein 0.2


    "Question [i]..."

    # show professor_base at Position(xpos=0.75, ypos=0.35) with moveinbottom:
    #     zoom 1.35
    show decoherence_laughing at Position(xpos=0.75, ypos=0.35) with dissolve:
        zoom 1.5

    $ question = questions[i]

    # Professor "[question]"
    Decoherence "[question]"

    $ question_number = "question" + str(i)

    call screen expression question_number


label correct:
    scene nivel 3:
        zoom 1.1
    
    stop music fadeout 0.5

    show professor_base at Position(xpos=0.75, ypos=0.35):
        zoom 1.35

    show quanta base at left:
        zoom 0.75

    show decoherence_damaged at Position(xpos=0.53, ypos=0.72)

    play music "audio/Subir_de_Nivel.wav" noloop fadein 0.2

    show qbit base at Position(xpos=0.95, ypos=0.4)
    Q_Bit "Good job, Quanta!"

    $ i = i + 1

    $ answer = None

    if i > 7:
        call win from _call_win
    
    call question_start(i) from _call_question_start_1

label wrong:
    scene nivel 3:
        zoom 1.1
    
    stop music fadeout 0.5

    show professor_base at Position(xpos=0.75, ypos=0.35):
        zoom 1.35

    show quanta_determined at left:
        zoom 0.75

    show decoherence_laughing at Position(xpos=0.53, ypos=0.72)

    play music "audio/Planeta_XKZ.wav" noloop fadein 0.2

    show qbit base at Position(xpos=0.95, ypos=0.4)
    
    Q_Bit "C'mon, Quanta! You can do it better."
    
    Decoherence "Don't be silly, Quanta! You can't beat me >>:D"

    hide quanta_determined
    show quanta_brave at left:
        zoom 0.75

    $ answer = None

    $ i = 1

    call game_over from _call_game_over


label game_over:
    stop music fadeout 0.5
    play music "audio/Game_Over.wav" noloop fadein 0.2

    $ answer = None

    call screen game_over_screen

screen game_over_screen:
    
    add "game_over_screen2" 
    modal True

    imagebutton auto "game_over_screen_%s.png":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Game Over")
        unhovered SetVariable("screen_tooltip", "")
        action Jump("start7")

    # This ends the game.

label win:
    scene nivel 3:
        zoom 1.1
    
    stop music fadeout 0.5

    show professor_base at Position(xpos=0.75, ypos=0.35):
        zoom 1.35

    show quanta base at left:
        zoom 0.75

    show decoherence_damaged at Position(xpos=0.53, ypos=0.72)


    show qbit base at Position(xpos=0.95, ypos=0.4)

    Decoherence "(Quietly) Oh... I didn't expected this..."
    hide decoherence_damaged with dissolve

    Q_Bit "Good job, Quanta!"

    show decoherence_base at Position(xpos=0.53, ypos=0.72) with dissolve
    hide decoherence_base with pixellate

    Quanta "Look! Decoherence has escaped again!"

    Q_Bit "Woohooo! We did it!"

    Professor "Fantastic! You made it, Quanta! I'm more than grateful that you found me."
    Professor "Now, lets go to the lab. We need to be prepared..."

    Quanta "Yeah, of course! But... Prepared for what, professor?"

    Professor "Well... I bet that this is not the last time that we will see Decoherence..."
    
    play music "audio/Victoria.wav" noloop fadein 0.2

    hide qbit base with pixellate
    hide professor_base with pixellate
    hide quanta base with pixellate

    scene black with fade

    pause 2.0

    #$ MainMenu(confirm=False)()
    call credits from _call_credits

    return
