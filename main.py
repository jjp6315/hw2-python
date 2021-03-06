# Author: Ji Woong Park jjp6315@psu.edu
# Section: 01-12
def getGradePoint(grade):
  if grade == "A":
    return 4.0  
  elif grade == "A-":
    return 3.67
  elif grade == "B+":
    return 3.33
  elif grade == "B":
    return 3.0 
  elif grade == "B-":
    return 2.67
  elif grade == "C+":
    return 2.33
  elif grade == "C":
    return 2.0 
  elif grade == "D":
    return 1.0 
  else:
    return 0.0

def run():
  grade = str(input("Enter your course 1 letter grade: "))
  credit1 = float(input("Enter your course 1 credit: "))
  print(f"Grade point for course 1 is: {getGradePoint (grade)}")
  GPA1 = {getGradePoint (grade)} * credit1

  grade = str(input("Enter your course 2 letter grade: "))
  credit2 = float(input("Enter your course 2 credit: "))
  print(f"Grade point for course 2 is: {getGradePoint (grade)}")
  GPA2 = {getGradePoint (grade)} * credit2

  grade = str(input("Enter your course 3 letter grade: "))
  credit3 = float(input("Enter your course 3 credit: "))
  print(f"Grade point for course 3 is: {getGradePoint (grade)}")
  GPA3 = {getGradePoint (grade)} * credit3

  GPA = (GPA1 + GPA2 + GPA3) / (credit1 + credit2 + credit3) 
  print(f"Your GPA is: {GPA}")

if __name__ == "__main__":
  run()