# Author: Ji Woong Park jjp6315@psu.edu
 
def getGradePoint1(grade1):
  if grade1 == "A":
    return float(4.0)
  elif grade1 == "A-":
    return float(3.67)
  elif grade1 == "B+":
    return float(3.33)
  elif grade1 == "B":
    return float(3.0)  
  elif grade1 == "B-":
    return float(2.67)
  elif grade1 == "C+":
    return float(2.33)
  elif grade1 == "C":
    return float(2.0)  
  elif grade1 == "D":
    return float(1.0)  
  else:
    return float(0.0)


def getGradePoint2(grade2):

  if grade2 == "A":
    return float(4.0)
  elif grade2 == "A-":
    return float(3.67)
  elif grade2 == "B+":
    return float(3.33)
  elif grade2 == "B":
    return float(3.0)
  elif grade2 == "B-":
    return float(2.67)
  elif grade2 == "C+":
    return float(2.33)
  elif grade2 == "C":
    return float(2.0)
  elif grade2 == "D":
    return float(1.0)
  else:
    return float(0.0)
 

def getGradePoint3(grade3):

  if grade3 == "A":
    return float(4.0)
  elif grade3 == "A-":
    return (3.67)
  elif grade3 == "B+":
    return (3.33)
  elif grade3 == "B":
    return float(3.0)
  elif grade3 == "B-":
    return (2.67)
  elif grade3 == "C+":
    return (2.33)
  elif grade3 == "C":
    return float(2.0)
  elif grade3 == "D":
    return float(1.0)
  else:
    return float(0.0)

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
  
  GPA = ({getGradePoint1 (grade1)} * credit1 + {getGradePoint2 (grade2)} * credit2 + {getGradePoint3 (grade3)} * credit3) / (credit1 + credit2 + credit3) 
  print(f"Your GPA is: {GPA}")

if __name__ == "__main__":
  run()