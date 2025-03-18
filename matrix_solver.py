import numpy as np

def get_matrix(rows,cols,name="matrix"):
  print(f"enter values {name}({rows}X{cols}) row-wise)")
  matrix = []
  for i in range(rows):
    while True:
      try:
        row = list(map(float,input(f"{i+1}: ").split()))
        if len(row) != cols:
          print("invalid! please enter {cols} value")
          continue
        matrix.append(row)
        break
      except ValueError:
        print("invalid! please enter positive integer")
  return np.array(matrix,dtype=float)

def perform_operation(A,B,choice):
  try:
    if choice == 1:
      return np.add(A,B)
    elif choice == 2:
      return np.subtract(A,B)
    elif choice == 3:
      if A.shape[1] != B.shape[0]:
        return("invalid! multiplication does not possible columns of a must match with rows of b")
      return np.matmul(A,B)
    elif choice == 4:
      return np.transpose(A)
    elif choice == 5:
      if A.shape[0] == A.shape[1]:
        return np.linalg.det(A)
      return "invalid! determinant must be a square"
    elif choice == 6:
      if A.shape[0] == A.shape[1] and np.linalg.det(A) != 0:
        return np.linalg.inv(A)
      return "inavlid! inverse does not exist matrix is singular or not a square"
    else:
      return "invalid choice!"
  except Exception as e:
    return f"error : {e}"

def matrix_operation():
  while True:
    try:
      rows,cols = map(int,input("entert matrix size(rows,cols): ").split())
      if rows <= 0 or cols <=0:
        print("invalid! rows and cols must be positive integer")
        continue
      break
    except ValueError:
      print("invalid input please two integer")
  A = get_matrix(rows,cols,"matrix A")
  B = get_matrix(rows,cols,"matrix B")
  while True:
      print("\noperations\n1.addition\n2.subtraction\n3.multiplication\n4.transpose\n5.determinant\n6.inverse\n7.exit")
      try:
        choice = int(input("enter the operation between 1 to 7: "))
        if choice == 7:
          print("exiting program")
          break
        result = perform_operation(A,B,choice)
        print("\nresult\n",result)
      except ValueError:
        print("invalid input enter a value between 1 to 7")
        continue
if __name__ == "__main__":
  matrix_operation()



    

  



      