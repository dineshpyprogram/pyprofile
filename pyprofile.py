#   ############### This is a python program to print a person's profile page ######################

<<<<<<< HEAD
first_name = input("Enter your First Name: ")
last_name = input("Enter your Last Name: ")
birth_month = input("Enter the month in which you were born: ")
birth_day = input("Enter the day of the month you were born: ")
birth_year = input("Enter the year in which you were born: ")
gender = input("Enter your Gender: ")
password = input("Enter a password: ")
email = input("Enter your Email: ")

=======

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
>>>>>>> 32526c72de4dac2fae7371a40c8630c493672d6d

# ##############Printing the output####################################################
print("\n\n\n\nProfile\n")
print("Some info may be visible to other people using Google services. Learn more\n\n\n")
<<<<<<< HEAD
print("Your name is: ".ljust(30, " "), "{} {}\n".format(first_name.capitalize().ljust(0, " "), last_name.capitalize()))
print("Your birthday is: ".ljust(30, " "), "%s %s, %s\n" % (birth_month.capitalize().ljust(0, " "), birth_day, birth_year))
print("Your gender is: ".ljust(30, " "), "%s\n" % (gender.capitalize().ljust(0, " ")))
print("Your password is: ".ljust(30, " "), "{}\n\n\n".format(password.ljust(0, " ")))
print("Contact info\n")
print("Your email is: ".ljust(30, " "), "{}".format(email.ljust(0, " ")))
=======
print(p.ljust(30, " "), "Add a photo to personalize your account\n")
print(n.ljust(30, " "), "{} {}\n".format(str1.capitalize(), str2.capitalize()))
# print(b.ljust(30, " "), "{} {}, {}\n".format(str3.capitalize(), str4, str5))
print("{} {} {}, {}\n".format(b.ljust(30, " "), str3.capitalize(), str4, str5))
print("{} {}\n".format(g.ljust(30, " "), str6.capitalize()))
print("%s %s\n\n\n" % (pwd.ljust(30, " "), str7))
print("Contact info\n")
print(e.ljust(30, " "), "%s\n" % str8)
>>>>>>> 32526c72de4dac2fae7371a40c8630c493672d6d
