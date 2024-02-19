print(" Welcome to my computer quiz")

playing = input("Do you want to play? \n ")

if playing.lower() != "yes":
    quit()

print("okay, let's play ;)")
score =0

answer = input (" what does cpu stands for? \n")
if answer.lower() == "central processing unit ":
    print ("correct!")
    score+=1
else:
    print( "not this is not true")

answer = input (" what does gpu stands for? \n")
if answer.lower() == "graphics processing unit ":
    print ("correct!")
    score += 1
else:
    print( "not this is not true")

answer = input (" what does ram stands for? \n")
if answer.lower() == "random access memory ":
    print ("correct!")
    score +=1
else:
    print( "not this is not true")

answer = input (" what does haha stands for? \n")
if answer.lower() == "only haha":
    print ("correct!")
    score +-1
else:
    print( "not this is not true")

print ( " you got" + str(score) + "correct ")
print ( " you got" + str((score / 4)* 100) + "percentage ")
