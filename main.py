# Author: Ji Woong Park jjp6315@psu.edu
 
def getGradePoint1(grade1):
  if grade1 == "A":
    g1 = 4.0  
  elif grade1 == "A-":
    g1 = 3.6
  elif grade1 == "B+":
    g1 = 3.3
  elif grade1 == "B":
    g1 = 3.0 
  elif grade1 == "B-":
    g1 = 2.6
  elif grade1 == "C+":
    g1 = 2.3
  elif grade1 == "C":
    g1 = 2.0 
  elif grade1 == "D":
    g1 = 1.0 
  else:
    g1 = 0.0
  return g1

def getGradePoint2(grade2):

  if grade2 == "A":
    g2 = 4.0  
  elif grade2 == "A-":
    g2 = 3.6
  elif grade2 == "B+":
    g2 = 3.3
  elif grade2 == "B":
    g2 = 3.0  
  elif grade2 == "B-":
    g2 = 2.6
  elif grade2 == "C+":
    g2 = 2.3
  elif grade2 == "C":
    g2 = 2.0  
  elif grade2 == "D":
    g2 = 1.0  
  else:
    g2 = 0.0 
  return g2

def getGradePoint3(grade3):

  if grade3 == "A":
    g3 = 4.0
  elif grade3 == "A-":
    g3 = 3.67
  elif grade3 == "B+":
    g3 = 3.3
  elif grade3 == "B":
    g3 = 3.0  
  elif grade3 == "B-":
    g3 = 2.6
  elif grade3 == "C+":
    g3 = 2.3
  elif grade3 == "C":
    g3 = 2.0  
  elif grade3 == "D":
    g3 = 1.0  
  else:
    g3 = 0.0
  return g3
  
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