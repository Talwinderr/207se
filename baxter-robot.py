userArray = []    #Array where the instructions will be appended to
Mv = ("left", "right", "forward", "backward", "stop")
Tm = ["1second", "2seconds", "5seconds", "unlimited"]
Ob = ["orange", "apple", "car", "bus", "diamond"]    #Defining the correct inputs user should make
Ac = ["recongise", "eat", "see", "lift", "drop", "fetch"]
Si = ["small", "big", "little", "massive"]
Loc = ["door", "kitchen", "table"]

#Definng the syntax instructions here and have created array above to store in

SyntaxRules1 = ["Object", "Action", "Time"]
SyntaxRules2 = ["Object", "Size", "Action"]
SyntaxRules3 = ["Move", "Time"]
SyntaxRules4 = ["Move", "Time", "Move", "Time"]
SyntaxRules5 = ["Location", "Action", "Object"]   #These are basically defined rules


print(" ")
print("~~~~~~~~~~//  BAXTER ROBOT PROGRAM  \\~~~~~~~~~~")   #Creating a title page!
print(" ")
print("Instructions for Object; 'orange', 'apple', 'car', 'bus', 'diamond'")  
print("Instructions for Move; 'left', 'right', 'forward', 'backward', 'stop'")  
print("Instructions for Location; 'door', 'kitchen', 'table'")  #All printed for the user's benefit
print("Instructions for Size; 'small', 'big', 'little', 'massive'")
print("Instructions for Action; 'recognise', 'eat', 'see', 'lift', 'drop', 'fetch'")
print("Instructions for Time; '1second, '2seconds', '5seconds', 'unlimited'")
print(" ")
print(" ")
print("Syntax Method 1: 'Object', 'Action', 'Time'")
print("Syntax Method 2: 'Object', 'Size', 'Action'")
print("Syntax Method 3: 'Move', 'Time'")  #This all appears as title info page
print("Syntax Method 4: 'Move', 'Time', 'Move', 'Time'")
print("Syntax Method 5: 'Location', 'Action', 'Time'")
print(" ")
print(" ")  #Spaces for readablity and nice look



txt = str(input("Type a / object \ instruction for the baxter robot or press enter to skip: "))
if txt == Ob[0] or txt == Ob[1] or txt == Ob[2] or txt == Ob[3] or txt == Ob[4]:
  print(" ")
  print("Success!")
  print("The entered instruction has been recognised by the baxter robot.")
  userArray.append("Object")
else:
  print(" ")         #If user inputs right instruction, append string to empty array created at top
  print("Error!")
  print("This instruction is unrecognised.")


txt = str(input("Type a / movement \ instruction for the baxter robot or press enter to skip: "))
if txt == Mv[0] or txt == Mv[1] or txt == Mv[2] or txt == Mv[3] or txt == Mv[4]:
  print(" ")
  print("Success!")
  print("The entered instruction has been recognised by the baxter robot.")
  userArray.append("Move")
else:
  print(" ")        #Its the same thing for the rest of these
  print("Error!")
  print("This instruction is unrecognised.")


txt = str(input("Type a / location \ instruction for the baxter robot or press enter to skip: "))
if txt == Loc[0] or txt == Loc[1] or txt == Loc[2]:
  print(" ")
  print("Success!")
  print("The entered instruction has been recognised by the baxter robot.")
  userArray.append("Location")
else:
  print(" ")
  print("Error!")
  print("This instruction is unrecognised.")


txt = str(input("Type a / size \ instruction for the baxter robot or press enter to skip: "))
if txt == Si[0] or txt == Si[1] or txt == Si[2] or txt == Si[3]:
  print(" ")
  print("Success!")
  print("The entered instruction has been recognised by the baxter robot.")
  userArray.append("Size")
else:
  print(" ")
  print("Error!")
  print("This instruction is unrecognised.")


txt = str(input("Type a / action \ instruction for the baxter robot or press enter to skip: "))
if txt == Ac[0] or txt == Ac[1] or txt == Ac[2] or txt == Ac[3] or txt == Ac[4] or txt == Ac[5]:
  print(" ")
  print("Success!")
  print("The entered instruction has been recognised by the baxter robot.")
  userArray.append("Action")
else:
  print(" ")
  print("Error!")
  print("This instruction is unrecognised.")


txt = str(input("Type a / time \ instruction for the baxter robot or press enter to skip: "))
if txt == Tm[0] or txt == Tm[1] or txt == Tm[2] or txt == Tm[3]:
  print(" ")
  print("Success!")
  print("The entered instruction has been recognised by the baxter robot.")
  userArray.append("Time")
else:
  print(" ")
  print("Error!")
  print("This instruction is unrecognised.")


txt = str(input("Type another / movement \ instruction for the baxter robot or press enter to skip: "))
if txt == Mv[0] or txt == Mv[1] or txt == Mv[2] or txt == Mv[3] or txt == Mv[4]:
  print(" ")
  print("Success!")
  print("The entered instruction has been recognised by the baxter robot.")
  userArray.append("Move")
else:                      #Movement and time are repeated, in order to achieve one defined syntax rule
  print(" ")
  print("Error!")
  print("This instruction is unrecognised.")


txt = str(input("Type another / time \ instruction for the baxter robot or press enter to skip: "))
if txt == Tm[0] or txt == Tm[1] or txt == Tm[2] or txt == Tm[3]:
  print(" ")
  print("Success!")
  print("The entered instruction has been recognised by the baxter robot.")
  userArray.append("Time")
else:
  print(" ")
  print("Error!")   #Remember, if user inputs wrong thing, they program doesn't like it
  print("This instruction is unrecognised.")



##################################################################################################
#if txt in Tm:
  #userArray.append("Time")
#if txt in Ob:
  #userArray.append("Object")
#if txt in Ac:
  #userArray.append("Action")         #Just a simple plan I made, ignore this
#if txt in Si:
  #userArray.append("Size")
#if txt in Loc:
  #userArray.append("Location")

#if userArray in [SyntaxRules1, SyntaxRules2, SyntaxRules3, SyntaxRules4, SyntaxRules5]:
  #print("Success! The baxter robot will follow the instructions of", + userArray)
#else:
  #print("ERROR!")
##################################################################################################  

print(" ")
print(userArray)   #Prints the user array at the end and display what user has appended inside
print(" ")


if userArray == SyntaxRules1:
    print("Well done! The baxter robot will follow your verified instructions!")
elif userArray == SyntaxRules2:
    print("Well done! The baxter robot will follow your verified instructions!")
elif userArray == SyntaxRules3:
    print("Well done! The baxter robot will follow your verified instructions!") #Checks which syntax rules matches array
elif userArray == SyntaxRules4:
    print("Well done! The baxter robot will follow your verified instructions!")
elif userArray == SyntaxRules5:
    print("Well done! The baxter robot will follow your verified instructions!")
else:
    print("~/  Your instructions as a result didn't match the baxter robot syntax rules! Please refer to the top and try again.  \~")  

print(" ")   #If array doesn't match, program explains why
