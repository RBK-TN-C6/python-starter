# BEFORE YOU START

# Javascript uses curly brackets {} to delimit code blocks
# Python, however, uses indentation to delimit code blocks

# Let's consider this Javascript code 

# if(hungry) {
# eat();
# } else { dont_eat();
# }


# Notice that the above code does not care about indentation.
# In Python, we NEED to write it this way 

# if(hungry):
#     eat()
# else:
#     dont_eat()

# IMPORTANT : Indentation in a python should have the same size
# Either use 4 spaces or tabs for each indent
# With that information in mind, happy hacking :)

#########
# INSERT YOUR CODE BELOW THIS LINE
#########
res=[]
for num in range(2000, 3200):
    if (num%7 ==0) and (num%5 !=0):
        res.append(str(num))
print (res)

