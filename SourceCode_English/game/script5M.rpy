# Place your game code in this file.

# Declare the characters used in the game as in the example:

define Q_Bit = Character("Q_Bit", color="#0138C1")
define pov = Character("[povname]", color="#286055")

#******** Electron Plate without Letters ********

image barras4 = "barras4.png"
image barras5 = "barras5.png"
image barras6 = "barras6.png"
image barras7 = "barras7.png"
image barras8 = "barras8.png"
image barras9 = "barras9.png"
image barras10 = "barras10.png"
image barras11 = "barras11.png"
image barras12 = "barras12.png"
image barras13 = "barras13.png"
image barras14 = "barras14.png"
image barras15 = "barras15.png"

#************* Define the Visual Style of the Time Bar ***************

style the_bars2:
    left_bar "idle_bar2.png"
    thumb "bar_thumb2.png"
    thumb_offset 9
    xysize(1200,80)
    xalign 0.5
    yalign 0.9

#************** Define the Visual Style of the Time Bar ***********

style the_bars:
    right_bar "bar_empty.png"
    thumb "bar_thumb.png"
    thumb_offset 9
    xysize(800,163)
    xalign 0.5
    yalign 0.2

#*************************************************

screen bars:

    bar:
        style "the_bars"
        value VariableValue("x",12)
        left_bar "[prefix_]bar.png"
        #xalign 0.5
        #yalign 0.25

#************ Define the Button to Press *****************

screen redButton():
    imagebutton:
        xalign 0.5
        yalign 0.6
        auto "red_button_%s.png" action [ToggleScreen("redButton"),Jump("firestore")]
return

#*************************************************************

image letra = "PantallaPrueba.png"

default x = 0

# Code took in internet:

transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0

init: ### Just setting variables in advance so there are no undefined variable problems.
    $ timer_range = 10
    $ time = 12

# ****** IMAGES OF THE QUANTUM EXPERIMENT **************

image pistola = "light_pistol.png"
image dobleRendija = "double_slit.png"
image detector = "screen.png"
image experimento = "montaje_doble_rendija.png"

#*********************************

screen game_over4M(): 
    add "game_over_screen2" 
    modal True

    imagebutton auto "game_over_screen_%s.png":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Game Over")
        unhovered SetVariable("screen_tooltip", "")
        action Jump("start5M")

# Initialize a variable to count incorrect answers:
default incorrect_choicesM = 0

# The game starts here:

label start5M:

    scene lab1 with fade
    play music "Kevin MacLeod - Hustle.mp3" loop fadein 3.0

    show qbit base at Position(xpos=0.95, ypos=0.4) with moveinright
    Q_Bit "Here we are in an actual Quantum Lab! This is a special bonus level where you, [povname], get to directly engage with some cool quantum experiments."
    
    Q_Bit "It's a chance to take a little break, immerse yourself in a different setting, and learn about quantum properties through a different dynamic."

    Q_Bit "Isn't it exciting to be in the heart of a quantum laboratory, conducting experiments firsthand [povname]?"

    Q_Bit "Nevertheless, you have the option to do this bonus level or continue the story as Quanta. What do you say?"
    hide qbit base at Position(xpos=0.95, ypos=0.4)

    menu:
        "Engage in the quantum lab experiment.":
            jump quantum_lab_experiment
        "Continue the story as Quanta.":
            jump start6

label quantum_lab_experiment:

    show experimento
    Q_Bit "Perfect! Let's dive into what we're going to do: That is the setup."
    hide experimento

    show pistola
    Q_Bit "There is an electron gun."
    hide pistola

    show detector with moveinright:
        xalign 0.5
        yalign 0.5
    Q_Bit "And an electron detector (or screen)."
    hide detector

    show dobleRendija with moveinright:
        xalign 0.5
        yalign 0.5
    Q_Bit "Also, double slit between them!"
    hide dobleRendija

    show qbit base at Position(xpos=0.95, ypos=0.4) with moveinright
    Q_Bit "Did you get the parts? I will explain the mini-game now."

    Q_Bit "Your goal is to have fun shooting electrons for a given amount of time. Keep an eye on the bar at the top of the screen, which represents the distance between the electron guns and the electron detectors."

    Q_Bit "For instance, choosing a value of 4 means you are closer to the screen. Conversely, a value of 12 means you are farther away."

    Q_Bit "The right end of the bar indicates a closer distance between the guns and detectors, while the left end represents a greater distance."

    Q_Bit "Use this visual guide to understand the relative proximity of the electron guns and detectors throughout the game."

    Q_Bit "Adjust your gameplay according to the position of the bar. Don't worry to much about it, just have fun and pay attention to the pictures."

    Q_Bit "Good luck and again, have fun exploring the distance bar!"
    hide qbit base at Position(xpos=0.95, ypos=0.4)

label start2:

    scene lab1
    $ timer_jump = 'winner'                    ### Set where you want to jump once the timer runs out.
    show screen countdown                      ### Call and start the timer
    show screen bars
    call screen redButton

screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.005), false=[Hide('countdown'), Jump(timer_jump)])
    bar style "the_bars2" value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve

label firestore:

    if x == 1:
        hide screen bars
        hide screen countdown
        show barras4
        "Result: x=4"
    elif x == 2:
        show barras5
        hide screen bars
        hide screen countdown
        "Result: x=5"
    elif x == 3:
        show barras6
        hide screen bars
        hide screen countdown
        "Result: x=6"
    elif x == 4:
        show barras7
        hide screen bars
        hide screen countdown
        "Result: x=7"
    elif x == 5:
        show barras8
        hide screen bars
        hide screen countdown
        "Result: x=8"
    elif x == 6:
        show barras9
        hide screen bars
        hide screen countdown
        "Result: x=9"
    elif x == 7:
        show barras10
        hide screen bars
        hide screen countdown
        "Result: x=10"
    elif x == 8:
        show barras11
        hide screen bars
        hide screen countdown
        "Result: x=11"
    elif x == 9:
        show barras12
        hide screen bars
        hide screen countdown
        "Result: x=12"
    elif x == 10:
        show barras13
        hide screen bars
        hide screen countdown
        "Result: x=13"
    elif x == 11:
        show barras14
        hide screen bars
        hide screen countdown
        "Result: x=14"
    elif x == 12:
        show barras15
        hide screen bars
        hide screen countdown
        "Result: x=15"

    jump start2

label winner:

    hide screen bars  # This line hides the bar when the player reach this last label.
    hide screen countdown

    show qbit base at Position(xpos=0.95, ypos=0.4) with moveinright
    Q_Bit "Great! Did you have fun? Let's test a bit what you learn."

    Q_Bit "What is the lesson here? Now you know a bit about interference!"

    Q_Bit "In the double slit experiment, interference is the pattern of light and dark bands created when waves, like light or electrons, pass through two slits and overlap, showing both wave-like and particle-like properties."

    Q_Bit "So, dear [povname], what effect does increasing the distance to the screen have on the interference pattern?"
    hide qbit base at Position(xpos=0.95, ypos=0.4)

    menu:
        "The interference pattern disappear entirely, showing only a single, bright spot.":
            # Wrong Answer
            #$ incorrect_choicesM += 1
            show qbit base at Position(xpos=0.95, ypos=0.4) with moveinright
            qbit "Actually no. The bands get wider and fewer bands appear on the screen. But don't worry! You can do the bonus level back after."
            hide qbit base at Position(xpos=0.95, ypos=0.4)
            #if incorrect_choicesM >= 1:
            jump levelBonus_end

        "The bands get wider and fewer bands appear on the screen.":
            # Correct Answer
            show qbit base at Position(xpos=0.95, ypos=0.4) with moveinright
            qbit "You won, yes!"
            hide qbit base at Position(xpos=0.95, ypos=0.4)
            #$ incorrect_choicesM = 0  # Reset the count for correct choice.
            jump levelBonus_end

label levelBonus_end:
    show qbit base at Position(xpos=0.95, ypos=0.4) with moveinright
    Q_Bit "I hope you liked this bonus level, [povname]. Time to continue the story, see you!"
    hide qbit base at Position(xpos=0.95, ypos=0.4)

    $ timer_range = 10
    $ time = 12

    stop music fadeout 1.0
    scene black with fade

    call start6 from _call_start6

    return

