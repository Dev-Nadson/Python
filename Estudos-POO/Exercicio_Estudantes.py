class Students:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
    
    def __str__(self):
        return f"Name: {self.name} \nGrades: {self.grades}"
        
    def average(self):
        return sum(self.grades) / len(self.grades)
    
name = "john"
grades = [6,6,7.89,6]

student = Students(name, grades)
print(f"{student} \nAverage: {student.average():.2f}") 