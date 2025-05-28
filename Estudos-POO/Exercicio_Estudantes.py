class Students():
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
    
    def __str__(self):
        return f"{self.name} \n{self.grades}"
        
    def average():
        return f"{sum(grades) / len(grades)}"
    
name = "john"
grades = [6,6,6,6]

student = Students(name, grades)
print(f"{student} \n{Students.average()}")