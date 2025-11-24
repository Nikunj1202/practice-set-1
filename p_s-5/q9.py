# can we change the value inside a list which is contained in set ?
s = {1,3,4,"nikunj",[1,2]}
s[4][1] = 9
print(s)
# get error because cant chage the value of list
