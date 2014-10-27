import time
def emotional_burdening():
     """this function has no parameter to it, because it isn't like sin(degrees). unlike sine, this function's output will always be the same."""
     #if true:
     print ("Don't you love me anymore?!")
     time.sleep(1)
     print ("...you don't think I'm getting fat, do you?")
     time.sleep(2)
     print ("You haaaate me!")
     time.sleep(1)
     print ("we are so over!")
     #if false
     #
            

name1= input("What's your name? ")

gender1= input("Hi, "+name1+", are you a boy or a girl? ")
if gender1.lower()=="boy":
     guy1= input ("Good for you! Would you say you were a good guy? " )
     if guy1.lower()=="yes":
          print("...I doubt that. ")
     elif guy1.lower()=="no":
          print("I know! Me too! ")
elif gender1.lower()== "girl":
     print ("Really? 'Cause I only sent this to guys, soooo...")
else:
     print("...so are you a teletubby, ooooor...? ")
ready1= input ("Okay {0}, are you ready? ".format(name1)).lower()
if ready1== "yes":
     print("Let's do this.")
     print("Relax, I know what I'm doing")    
elif ready1=="no":
     print("Then why is this program open?")
     time.sleep(2)
q1= input ("So, tell me about yourself. Where are you from? ")
q2= input ("Oooooh... that's... nice. I guess. Are you sure you're not from somwhere more exciting than " +q1+ " ? ").lower()
if q2 is "yes":
     print("LIAR! THIS DATE IS OVER! ")
     time.sleep(1)
     print("I hate you! My mother was right about you!")
     time.sleep(2)
     print("Soooo... you're still picking up the check, right?")

if q2== "no":
     time.sleep(1)
     print("....")
     time.sleep(2)
     print("...that's kind of sad, don't you think?")
     time.sleep(1)
     print("I mean, I can't imagine living a life knowing I'm from {0} I mean, I couldn't even get up in the morning.".format(q1))
     time.sleep(3.5)
     print("...uh, never mind. Sorry I asked.")
#I'm trying to create a loop of emotional burdening...
q3= input ("You want to learn more about me too, riiiiiight? ").lower()
if q3 is "yes":
     print("Of course you do.")
     time.sleep(.5)
     print("Obviously, you must have already figured out my sign; I mean, I'm lucky, artistic, and I get grumpy when it rains. Well, my life story begins...")
     time.sleep (1)
     print("blah blah blah blah blah blah blah blah blah blah blah blah, baseball, blah blah blah blah blah blah blah...!")
     print ("blah blah blah blah, my car, blah blah blah blah blah blah blah blah blah blah blah blah blah!")
     winless= input ("...where you listening to me?! ").lower()
     if winless is "no": 
        correction1= input ("...are you serious right now? ")
        if correction1== "yes":
                    print("Oh, we are so done! Goodbye!")
        if correction1 is "no":
                    print("That's not funny! I can't believe you'd say that!")
     if winless== "yes":
          print("I don't believe you. You're the kind of guy who lies to get what he wants, like my ex-boyfriend blah blah blah blah blah blah blah blah blah blah, baseball, blah blah blah blah blah blah blah-blah blah blah blah blah blah blah blah blah blah, blah blah blah blah blah blah blah...")
          time.sleep(4)
          print("Did you just fall asleep again?")
          time.sleep(1)
          print("I don't believe this! Ugh! You are the worst!")
time.sleep(2)
q4= input ("Okay, now that you've gotten to know me, you can go ahead and say something too! ")
time.sleep(3)
print ("Boring! Back to me!")
q5= input ("Okay, you remember how you were going on and on about all that boring stuff? " +q4+ " ...or something? Well, I was talking to Linda the other day, and she said that no " +gender1+ " was good enough for me. Don't you agree? ").lower()

if q5 is "yes":
     print("You're totally right! This date is over!")
if q5 is "no":
     print("How dare you? Are you saying just any old " +gender1+ " is good enough for me?")
     time.sleep(1)
     print("Whatever, I don't care anyways!")
elif q5 is " ":
     print(".....you're emotionally closed off!")

emotional_burdening()

