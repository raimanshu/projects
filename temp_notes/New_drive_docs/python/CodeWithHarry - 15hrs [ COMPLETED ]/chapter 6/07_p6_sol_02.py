sub1 = int(input("Enter marks of subject 1 : \n"))
sub2 = int(input("Enter marks of subject 2 : \n"))
sub3 = int(input("Enter marks of subject 3 : \n"))

if(sub1 < 33 or sub2 < 33 or sub3 < 33):
    print("You are failed because any subject has less than 33 marks")
elif(sub1 + sub2 + sub3)/3 < 40:
    print("You are failed because total marks is les than 40")
else:
    print("Congratulations ! You are passed")