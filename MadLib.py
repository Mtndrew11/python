#import modules
#from tkinter import ttk
#from tkinter import *

# Display window
#root = Tk()
#root.geometry('300x300')
#root.title('DataFlair-Mad Libs Generator')
#Label(root, text= 'Mad Libs Generator \n Have Fun!' , font = 'arial 20 bold').pack()
#Label(root, text = 'Click Any One :', font = 'arial 15 bold').place(x=40, y=80)


#Button(root, text= 'The Photographer', font ='arial 15', command= madlib1, bg = 'ghost white').place(x=60, y=120)
#Button(root, text= 'apple and apple', font ='arial 15', command = madlib3 , bg = 'ghost white').place(x=70, y=180)
#Button(root, text= 'The Butterfly', font ='arial 15', command = madlib2, bg = 'ghost white').place(x=80, y=240)
#root.mainloop()

## MAIN
#def madLib1():
noun1           = input('Enter a noun: ')
adjective1      = input('Enter a adjective: ')
noun2           = input('Enter a noun: ')
verbPastTense1  = input('Enter a verb past tense: ')
adverb1         = input('Enter a adverb: ')
adjective2      = input('Enter a adjective: ')
noun3           = input('Enter a Noun: ')
noun4           = input('Enter a Noun: ')
adjective3      = input('Enter a adjective: ')
verb            = input('Enter a verb: ')
adverb2         = input('Enter a adverb: ')
verbPastTense2  = input('Enter a verb past tense: ')
adjective4      = input('Enter a adjective: ') 

story = "Today I went to the zoo. I saw a(n)" + adjective1 + noun1 + " jumping up and down in its tree. He" + verbPastTense1 + adverb1 + " through the large tunnel that led to its" + adjective2 + noun2 + "."
" I got some peanuts and passed them through the cage to a gigantic gray"  + noun3 + " towering above my head. Feeding that animal made me hungry. I went to get a" + adjective3 + " scoop of ice cream."
"It filled my stomach. Afterwards I had to" + verb + adverb2 + " to catch our bus."
"When I got home I" + verbPastTense2 + " my mom for a" + adjective4 + " day at the zoo."

print(story)

#def madLib2():
#    noun1 = ''

    
#def madLib3():
#    noun1 = ''




#madLib1()