#   ############### This is a python program to print a person's profile page ######################


str1 = input("Enter your First Name: ")
str2 = input("Enter your Last Name: ")
str3 = input("Enter the month in which you were born: ")
str4 = input("Enter the day of the month you were born: ")
str5 = input("Enter the year in which you were born: ")
str6 = input("Enter your Gender: ")
str7 = input("Enter a password: ")
str8 = input("Enter your Email: ")

p = "PHOTO"
n = "NAME"
b = "BIRTHDAY"
g = "GENDER"
pwd = "PASSWORD"
e = "EMAIL"

# ##############Printing the output####################################################
print("\n\n\n\nProfile\n")
print("Some info may be visible to other people using Google services. Learn more\n\n\n")
print(p.ljust(30, " "), "Add a photo to personalize your account\n")
print(n.ljust(30, " "), "{} {}\n".format(str1.capitalize(), str2.capitalize()))
# print(b.ljust(30, " "), "{} {}, {}\n".format(str3.capitalize(), str4, str5))
print("{} {} {}, {}\n".format(b.ljust(30, " "), str3.capitalize(), str4, str5))
print("{} {}\n".format(g.ljust(30, " "), str6.capitalize()))
print("%s %s\n\n\n" % (pwd.ljust(30, " "), str7))
print("Contact info\n")
print(e.ljust(30, " "), "%s\n" % str8)
