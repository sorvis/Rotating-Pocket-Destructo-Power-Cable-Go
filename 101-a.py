import time
print( "Welcome to Christopher's 101-a computer program. Wait one moment please.")
time.sleep(1)
print( "Thank you for holding. Please enter your age.")
time.sleep(3)
age1=int( input("...oh, right, I gotta give you something to enter your age in. Here we go."))
if age1<1   :
    print("Stop screwing around. What's your age.")
elif age1<14 :
    print ("Dude, you are a small child. Go ask your momma for a cookie.")
    time.sleep(2)
    print ("Dude.... bring me one, too!")
elif age1>99 :
    print ("Gee gramps, got some help from your grandkids for this?")
else:
    print ("Awesomesauce. Welcome to the prime of your life. Worry not, it'll soon pass you by.")
