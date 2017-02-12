from time import sleep
print "Hello!"
print "I am a bit sleepy so i might stop"
sleep (3)
print "talking."
print "How are you to"
sleep (2)
while 1:
    a = raw_input("How are you today? Great or bad?")
    if a == "great":
        print "great"
        break
    elif a == "bad":
        print "Oh well this will be fun!"
        break
    else:
        continue

while 1:
    password = "i am jerry hi"
    ans = raw_input("Password please:   ")
    if ans == password :
        print "You entered the secret club!"
        break
    else:
        print "This is not the correct password, please try again."
        continue

while 1:
    command = raw_input("Please input what you want the computer to do. c+ for addition c- for minus c* for multiplication c/ for division q for quit                                                                                                                     ")
    if command == "q":
        break 
