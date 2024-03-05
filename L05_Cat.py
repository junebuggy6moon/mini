#### Exercise#
# 1** Create a new class called Cat with:
 # Instance variables
  #- name
  # fav_food
  # staff
 # Class variables
  # disposition =  ‘Not as nice as dogs’
  # cat_count = 0
 # Methods
   # \_\_init\_\_
   # add_staff

#**2** Fix add\_staff so that if won't add someone who is already staff
#**3** Fix \_\_init\_\_ so that it updates cat_count each time a cat is created
class Cat:
    disposition = "Not as nice as dogs"
    cat_count = 0

    def __init__(self, name, fav_food, staff):
        self.name = name
        self.fav_food = fav_food
        self.staff = staff
        self.staff = []
        Cat.cat_count += 1

    def add_staff(self, new_staff):
        if new_staff not in self.staff:
            self.staff.append(new_staff)
            print(f"{new_staff} has {self.name}.")
        else:
            print(f"{new_staff} has {self.name}.")

cat1 = Cat("cat1", "fish", "June")
cat2 = Cat("cat2", "rat", [])

cat1.add_staff("June")
cat2.add_staff("July")

print("Total:", Cat.cat_count)
