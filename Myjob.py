#PRINT What's your job? "myjob1"
job= input("What's your job? ")

#PRINT "myjob1"? That's a stupid job! What's your favorite animal? "MYjob2"
print(job+" That's a stupid job") 

fanimal= input("What's your favorite animal? ")

#PRINT "myjob2"? You should train those for a living! It's better than being some, what? "MYjob1"!? Besides which, your boss could likely hire a "MYjob2" to be a "MYjob1"!
print (fanimal+ "?! You should train those for a living! It's better than being some "+ job+"!")
advice =input ("Do you like receiving my advice? Y/N ")
if advice== "Y":
    print("Really? Only someone working as "+job+" would need my advice that badly.")
elif advice== "N":
    print("Too bad, suck it up, you're just a " +job+" who loves "+ fanimal)
else:
    print("Did you not understand the question you idiotic "+job+" who is not as intelligent as the beloved " +fanimal)

while True:
    ignorance=input ("Do you know how ignorant everyone else finds you? Y/N? ")
    if ignorance== "Y":
        print("Really? 'Cause if so, why do you keep burdening the rest of us?")
        break
    elif ignorance== "N":
        print("Of course you don't. Duh.")
        break
    else:
        print("ANSWER THE QUESTION, I DEMAND OF YOU!!!")
            
employer= input("Who do you work for? ")
guess=input("Wow, I heard "+employer+" only hired idiots but I wasn't sure until now. Guess what I'm about to say? ")
print("...you thought I was going to say something hurtful, didn't you? HOW DARE YOU?!?! I'm done with this conversation! Good-bye")
input()
