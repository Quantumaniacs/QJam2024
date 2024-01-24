# Personaje:
define Planck = Character("Professor Planck", color="#FF7F50")

# Empieza el nivel:
label script003_start:

play music "audio/misterio.ogg" loop fadein 3.0 volume 0.3

scene black with fade

scene universidad:

"""In the corridors of the university..."""

scene pasillos:

"""Everything seemed to be going well, students and teachers were walking, chatting, debating, solving equations."""

"""But there was someone missing, Professor Planck..."""

scene estudiantes:

"""Professor Planck was what they called a genius, or a mad scientist."""

show profesor explicando2 at left with moveinleft:
        zoom 1.9
        
Planck "Dear students, today, we will learn: Extreme Science HAHAHAHAHA!"
hide profesor explicando2 at left

"""He was one of the most outstanding professors at the university and one of the most fun to be around."""

scene científicos:
        
"""He gave his lectures, and published his most recent scientific advances."""

show profesor explicando at center with moveinleft:
#        zoom 2.25

Planck "This is why this discovery is essential in the development of quantum computing."

scene black with fade
hide profesor explicando at center

"""Until one day..."""

scene oficina:
        
"""He disappeared without a trace."""

"""That day was called: The Ultraviolet Catastrophe!"""

scene policia:
        
"Police, private investigators, teachers, and students did everything to find him."

scene mundo:

"But it seemed that Professor Planck was no longer in this world. And indeed he wasn't..."

scene black with fade

"Only one trace of his disappearance remained, a letter."

"And it just said:"

scene carta:

"DECOHERENCE..."

scene nivel 1:
        zoom 1.1

"""In a hidden corner of the multiverse, where reality intertwines with the impossible, lies Professor Planck's secret laboratory."""

scene black with fade

show quanta base completo at center with moveinleft:
            zoom 0.85
            xalign 0.5
            yalign 0.5

"Quanta, a young spy physicist, has a mission: to rescue his mentor, Professor Planck from the hands of Decoherence."

scene black with fade

"Here, this adventure begins..."

stop music fadeout 1.0

call start1 from _call_start1

return
