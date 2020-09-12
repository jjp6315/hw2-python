# Author: Ji Woong Park jjp6315@psu.edu

def run():
  grade1 = str(input("Enter your course 1 letter grade: "))
  credit1 = float(input("Enter your course 1 credit: "))
  print(f"Grade point for course 1 is: {getGradePoint1 (grade1)}.")
  
  grade2 = str(input("Enter your course 2 letter grade: "))
  credit2 = float(input("Enter your course 2 credit: "))
  print(f"Grade point for course 2 is: {getGradePoint2 (grade2)}.")
  
  grade3 = str(input("Enter your course 3 letter grade: "))
  credit3 = float(input("Enter your course 3 credit: "))
  print(f"Grade point for course 3 is: {getGradePoint3 (grade3)}.")
  
  GPA = float(gradenum1 * credit1 + gradenum2 * credit2 + gradenum3 * credit3) / (credit1 + credit2 + credit3) 
  print(f"GPA is {GPA}.")



  
def getGradePoint1(grade1):

  if grade1 == "A":
    gradenum1 = 4.0
    return "4.0"
  elif grade1 == "A-":
    gradenum1 = 3.67
    return "3.67"
  elif grade1 == "B+":
    gradenum1 = 3.33
    return "3.33"
  elif grade1 == "B":
    gradenum1 = 3.0
    return "3.0"
  elif grade1 == "B-":
    gradenum1 = 2.67
    return "2.67"
  elif grade1 == "C+":
    gradenum1 = 2.33
    return "2.33"
  elif grade1 == "C":
    gradenum1 = 2.0
    return "2.0"
  elif grade1 == "D":
    gradenum1 = 1.0
    return "1.0"
  elif grade1 == "F":
    gradenum1 = 0.0
    return "0.0"
  else:
    return "Invalid Letter Grade"


def getGradePoint2(grade2):

  if grade2 == "A":
    gradenum2 = 4.0
    return "4.0"
  elif grade2 == "A-":
    gradenum2 = 3.67
    return "3.67"
  elif grade2 == "B+":
    gradenum2 = 3.33
    return "3.33"
  elif grade2 == "B":
    gradenum2 = 3.0
    return "3.0"
  elif grade2 == "B-":
    gradenum2 = 2.67
    return "2.67"
  elif grade2 == "C+":
    gradenum2 = 2.33
    return "2.33"
  elif grade2 == "C":
    gradenum2 = 2.0
    return "2.0"
  elif grade2 == "D":
    gradenum2 = 1.0
    return "1.0"
  elif grade2 == "F":
    gradenum2 = 0.0
    return "0.0"
  else:
    return "Invalid Letter Grade"


def getGradePoint3(grade3):

  if grade3 == "A":
    gradenum3 = 4.0
    return "4.0"
  elif grade3 == "A-":
    gradenum3 = 3.67
    return "3.67"
  elif grade3 == "B+":
    gradenum3 = 3.33
    return "3.33"
  elif grade3 == "B":
    gradenum3 = 3.0
    return "3.0"
  elif grade3 == "B-":
    gradenum3 = 2.67
    return "2.67"
  elif grade3 == "C+":
    gradenum3 = 2.33
    return "2.33"
  elif grade3 == "C":
    gradenum3 = 2.0
    return "2.0"
  elif grade3 == "D":
    gradenum3 = 1.0
    return "1.0"
  elif grade3 == "F":
    gradenum3 = 0.0
    return "0.0"
  else:
    return "Invalid Letter Grade"




if __name__ == "__main__":
  run()