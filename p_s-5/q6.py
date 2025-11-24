''' create an empty dictionary . allow 4 frinds to enter their favorite langauge as value
  and key was their name . assume that their name are unique'''

di = {

}
for i in range(4):
 fr = input("enter your name: ")
 lg = input("enter your favorite langauge: ")
 di.update({fr:lg})
 print(di)
# get input data from users and print data
