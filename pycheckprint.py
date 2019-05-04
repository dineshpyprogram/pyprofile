
x = input("Enter your first_name: ")
y = input("Enter your last_name: ")
a = input("Enter the month of birth: ")
b = input("Enter the day of the month you were born: ")
c = input("Enter the year of birth: ")
pwd = input("Enter your password: ")
email = input("Enter your email: ")

print("Your name is: ".ljust(30, " "), "%s %s" % (x.capitalize().ljust(0, " "), y.capitalize()))
print("Your Birthday is: ".ljust(30, " "), "%s %s, %s" % (a.capitalize().ljust(0, " "), b, c))
print("Your password is: ".ljust(30, " "), "%s" % (pwd.ljust(0, " ")))
print("Your email is: ".ljust(30, " "), "%s" % (email.ljust(0, " ")))

