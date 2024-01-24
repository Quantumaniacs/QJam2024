define Q_Bit = Character("Q_Bit", color="#0138C1")

define pov = Character("[povname]", color="#286055")

screen Venn():
    add "entrenamiento"
    modal True

    imagebutton auto "venn_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Venn Machine")
        unhovered SetVariable("screen_tooltip", "")
        action Jump("afterselectVenn")

label script001_start:

play music "audio/Socceroos-Progress.ogg" fadein 3.0 volume 0.3    

scene entrenamiento

show qbit base at left:
     xalign 0.95
     yalign 0.4
     
Q_Bit "To travel through the numerical sets, we will have to use a machine that allows us to move from one to another."

Q_Bit "That machine is..."

show venn_idle with moveinright

Q_Bit "The Venn Machine!"

Q_Bit "It is named in honor of John Venn who was a British mathematician and logician born on August 4, 1834. He is best known for developing Venn Diagrams, which are used to visually represent relationships between sets."

Q_Bit "Come on [povname], press the machine to start our journey."

call screen Venn

label afterselectVenn:
Q_Bit "Excellent, here we go."

scene viaje

show vennmediano with moveinright:
    xalign 0.5
    yalign 0.5

show qbit base with moveinleft:
     xalign 0.95
     yalign 0.2

Q_Bit "WOOOO, this trip is so exciting no? WOOOO!"

Q_Bit "Now, we are crossing the joint portal, this leads us to our destination..."

call script002_start from _call_script002_start

return