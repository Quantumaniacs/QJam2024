define Q_Bit = Character("Q_Bit", color="#0138C1")

define pov = Character("[povname]", color="#286055")

label script002_start:

play music "audio/Socceroos-Progress.ogg" fadein 1.0 volume 0.3

scene naturales

show qbit base with moveinleft:
     xalign 0.5
     yalign 0.5

Q_Bit "We have arrived [povname], this is the world of Natural Numbers."

Q_Bit "These numbers are very nice, you can even see the peace of their world."

Q_Bit "Do you like this world [povname]?"

hide qbit base

menu:
    "Yes, it's very nice.":
        jump parte002a

    "Nah, it gives me a weird feeling.":
        jump parte003a

label parte002a:
    
    show qbit base with moveinright:
     xalign 0.5
     yalign 0.5
     
Q_Bit "Yes, me also I like it a lot."

jump parte004a

label parte003a:
    
    show qbit base with moveinright:
     xalign 0.5
     yalign 0.5
     
Q_Bit "Mmm, yeah, boring."

jump parte004a

label parte004a: 
    
Q_Bit "In an easy way, the natural numbers would represent the number of individual items you are counting, such as the number of chairs, pencils, or books."
    
Q_Bit "They are positive, whole numbers, and start from 1."
    
Q_Bit "And are important because they are the fundamental basis of mathematics and are used to count and order objects in everyday life."

Q_Bit "As well as to perform basic mathematical operations."

label parte005a:
    
show qbit base with moveinleft:
     xalign 0.95
     yalign 0.4
     
show vennmediano with moveinright:
    xalign 0.5
    yalign 0.5
    
Q_Bit "Well, it seems that we already know this world. Let's go to the next, WOOO!"

label parte006a:
    
scene black with fade

Q_Bit "Oh, it seems to be a little dark."

scene enteros 

show qbit base with moveinright:
     xalign 0.5
     yalign 0.5

Q_Bit "Ah! Welcome, welcome, welcome to the world of integers."

label parte007a:
    
show qbit base with moveinleft:
     xalign 0.5
     yalign 0.5

Q_Bit "For example, if you also consider objects that you have lost or borrowed, you might have negative numbers, such as -2 books (indicating that you have lost two books)."

Q_Bit "In that sense, integers encompass all positive and negative numbers, along with zero."

Q_Bit "They're important because they allow both positive and negative quantities to be represented."

Q_Bit "Being essential in situations where debts, profits, temperatures and other concepts involving opposite directions need to be modeled."

Q_Bit "Oh! You seem a bit disoriented, shall we move on to the next world or go over everything again? "

menu:
    "All perfect, let's continue.":
        jump parte008a

    "Again, please.":
        jump parte007a

label parte008a:
    show qbit base with moveinright:
     xalign 0.95
     yalign 0.4

show vennmediano with moveinright:
    xalign 0.5
    yalign 0.5
    
Q_Bit "Let's continue!"

label parte009a:
    
scene racionales 

show qbit base with moveinright:
     xalign 0.5
     yalign 0.5
     
Q_Bit "This is the world of rational numbers. But everyone knows it as fractions."

Q_Bit "Imagine you are dividing a pizza among friends. The amount of pizza each person gets could be expressed as a rational number."

Q_Bit "Includes all numbers that can be expressed as a quotient of two integers where the denominator is not zero."

Q_Bit "They're important because they represent fractions and proportions in everyday and mathematical situations, facilitating the accurate expression of non-integer quantities."

Q_Bit "This world includes the world of the natural and the integers."

Q_Bit "Now, a small question: which of these two numbers is a fraction?"

menu:
    "0.5 = 1/2 ":
        jump parte0010a

    "10":
        jump parte0011a
        
label parte0010a:
show qbit base with moveinright:
     xalign 0.5
     yalign 0.5

Q_Bit "That is correct!"
jump parte0012a
       
label parte0011a:
show qbit base with moveinright:
     xalign 0.5
     yalign 0.5

Q_Bit "This is incorrect, remember [povname] that after the training level if you make a mistake you will lose! You must always pay close attention. In this case, 10 was an integer."
jump parte0012a
       
label parte0012a:
    show qbit base with moveinright:
     xalign 0.95
     yalign 0.4

show vennmediano with moveinright:
    xalign 0.5
    yalign 0.5
    
Q_Bit "Here we go!"

label parte0013a:
    
scene irracionales

show qbit base with moveinright:
     xalign 0.5
     yalign 0.5
     
Q_Bit "This [povname], is the world of irrational numbers, where decimals are infinite and many things make or do not make sense."

Q_Bit "If you measure the diagonal of a square whose sides have length 1, you will get the square root of 2, which is an irrational number."

Q_Bit "These types of numbers are characterized by having an infinite decimal part."

Q_Bit "That is, numbers that cannot be expressed as a fraction."

Q_Bit "Numbers such as pi and Euler's number are irrational numbers."

Q_Bit "They allow modeling phenomena such as fractal geometry and wave propagation. Their presence extends the understanding and description of complex aspects in various scientific fields."

Q_Bit "Now let's see if you understood!"

Q_Bit "Can irrational numbers be represented as simple fractions?"

menu:
    "No.":
        jump parte0014a

    "Yes.":
        jump parte0015a
        
label parte0014a:
    
show qbit base with moveinright:
     xalign 0.5
     yalign 0.5

Q_Bit "Correct!"

jump parte0016a
       
label parte0015a:
    
show qbit base with moveinright:
     xalign 0.5
     yalign 0.5

Q_Bit "No, remember: Irrational numbers are numbers that cannot be expressed as the ratio of two integers."

jump parte0016a   

label parte0016a:
    
    show qbit base with moveinright:
     xalign 0.95
     yalign 0.4

show vennmediano with moveinright:
    xalign 0.5
    yalign 0.5
    
Q_Bit "Now let's go to the final world, pay close attention!"

label parte0017a:
    
scene imaginarios

show qbit base with moveinright:
     xalign 0.5
     yalign 0.5
     
Q_Bit "Complex numbers are an extension of the set of real numbers that includes an imaginary unit, denoted as i, which has the property that its square is equal to -1."

Q_Bit "These numbers include natural, integer, rational, and irrational numbers!"

Q_Bit "In quantum mechanics, wave functions, which describe the quantum state of a system, often involve imaginary numbers."

Q_Bit "In addition, quantum gates, which are the building blocks of quantum algorithms, often operate in complex space, which includes imaginary numbers."

Q_Bit "The presence of imaginary numbers makes it possible to model quantum phenomena more accurately and efficiently."

Q_Bit "Well, here we finished our journey through the numerical sets and we could see their importance..."

Q_Bit "In particular, in quantum computing 😉."

Q_Bit "Now, let's go back to our training site."

label parte0018a:
    
scene entrenamiento
    
show qbit base with moveinright:
     xalign 0.5
     yalign 0.5

Q_Bit "We have finished the training and the introductory level [povname]!"

Q_Bit "Congratulations on getting this far."

Q_Bit "Remember, when the game starts you must answer correctly and pay close attention. You will have a certain number of attempts. If these run out, you will have to start from the beginning."

Q_Bit "In this game, you'll be stepping into the paws of Quanta, a tiny raccoon spy, navigating the Quantum World!"

Q_Bit "Best of luck and see you soon [povname]! Your very own quantum computing adventure as Quanta is about to unfold."

call script003_start from _call_script003_start

return