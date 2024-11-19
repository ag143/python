#The try block will generate an error, because x is not defined:

try:
  print(x)
except:
  print("An exception occurred")
############################
#The try block will generate a NameError, because x is not defined:

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

#######################
#The try block does not raise any errors, so the else block is executed:

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

##################################
#The finally block gets executed no matter if the try block raises any errors or not:

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

#####################################
f = open("demofile.txt", "r")

print(f.read())

######################################
f = open("demofile.txt", "r")

print(f.read(5))

#####################################
f = open("demofile.txt", "r")

print(f.readline())

#######################################
f = open("demofile.txt", "r")
for x in f:
  print(x)

