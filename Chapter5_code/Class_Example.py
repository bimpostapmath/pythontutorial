# Use object, not Object
class student(object):
    def __init__ (self, age, name, grade, gender):
        self.name  = name
        self.age   = age
        self.grade =grade
        self.gender=gender
    def announcement(self):
        if (self.grade==11):
            print("Junior")
        elif (self.grade==12):
            print("Senior")
        elif (self.grade==10):
            print("Sophomore")
        elif (self.grade==9):
            print("Freshmen")
        elif (self.grade>6):
            print("Middle Schooler")
        else:
            print("Young kid")

leolin=student(12,"Leo Lin", 11, "Preferred not to tell")
leolin.announcement()
