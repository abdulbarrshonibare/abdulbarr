import math

'''CODE LAGOS PHYTHON STUDENT GRADING'''

giveMeAName = input("give me a name")

maths = int(input("mathematics score"))
english = int(input("english score"))
physics = int(input("physics score"))
chemistry = int(input("chemistry score"))
biology = int(input("biology score"))
phython = int(input("phython score"))

total = (maths+ english+ physics+ chemistry+ biology+ phython)
average = (maths+ english+ physics+ chemistry+ biology+ phython)/(6)
percentage = (maths+ english+ physics+ chemistry+ biology+ phython)/(6)*100

if (percentage >= 70):
    print("A")
elif (percentage > 50 and percentage < 70):
    print("B")
elif (percentage > 40 and percentage < 50):
    print ("C")
elif (percentage > 30 and percentage < 40):
    print ("D")
elif (percentage > 35 and percentage < 30):
    print ("E")
    
else:
    print ("F")

if (percentage >= 40):
    print ("CONGRATULATION YOU HAVE PASSED THIS STAGE")

else:
    print ("I AM SO SORRY, YOU HAVE REPEATED THIS STAGE")
        


    
