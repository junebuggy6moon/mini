#1. Create a Class Student and sub-classes `FT_Student` and `PT_Student`
#   * Each should have a Class variable credits
#		For `FT_Student`: `credits = 60`
#			For `PT_Student`: `credits = 30`

# Create instances
#			`FT_Student`: `Joe ` & ` Mary`
#			PT_Student: Ann ` & ` Fred`

# Change the value of credits for `PT_Student` to 203
# * Does this change for `Ann ` & ` Fred`?

class Student:
    pass
class FT(Student):
    credits = 60

class PT(Student):
    credits = 30

Joe = FT()
Mary = FT()
Ann = PT()
Fred = PT()

PT.credits = 20

print(Ann.credits)
print(Fred.credits)