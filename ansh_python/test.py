print("hello fatty baby", 1 ," love uuuuuuu", sep = ' $ ')
print(''' i am in love with mt fatty baby and overaction 
of my fatty baby ''')
print("hello 'fatty'she is mabbu ")

# ÷backslah is used to tell this is not a character 
print('hello \'fatty\' this is cutie')

# fstring 


# variiables 
x,y,z = 10,40,40
print(x+y+z)


add = 10+40+50\
    +50

print(add)

# explicit typecasting
a = 10
a_new = str(a)
print(type(a))


# implicit typecasting
a = 10 
b = 10.5
print(type(b))
c = a+ b 
print(c) 
#  here impliit typecasting is done to add difff datatypes which are both similar datatypes 


# array
x = "fattybaby"
# this can be taken as array and count starts from 0 
print(x[0])



#  splicing 
#  [n:n+1}

print(x[0:6])
print(x[:])
#  if nothing is given we eill get 0 as default and n as default where n is lenngth

# ÷functionss in built 
# .upper()
# .lower()
# capitalize() first charcter upper 
# .replace("a","b")
v = "fattybaby"
print(v.upper())
print(v.replace("at","bt"))


# remove the delimiterss

k = "love you fatty baby"
print(k.split(" "))
# split always gives list example ['love', 'you', 'fatty', 'baby']

# endswith() and startswith()
#  htis is used like reading a csv file ... os to check if the file ends with .csv we can use this inside if condition 
test_file = "my_data.csv"
if (test_file.endswith(".csv")):
    print("yes")

# similary startwith()
if (test_file.startswith("my")):
    print("nooooo")

# count() a particular words 

statement = "hey fatty baby what are you doing , hey i am near you but your not seeing "
# we will check number of words/word count
#  here lets check for "you"
print(statement.count("yukk")) 
# if nothing is there we get 0 

#  to know if string has numbers or not isnumeric() .. output boolean
n = "10"
print(n.isnumeric())


#  conditionals 

# if 

x = 11

if(x == 10 ):
    print("x is 10")
elif(x>100):
    print("x is too big")
    if((x > 200) & (x < 200)):
        print("between 100 & 200")
    else:
        ("greater than 200")
else:
    print("x is not 10")


# iterations loops 


