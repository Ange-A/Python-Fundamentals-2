#queen Attack

#check if two queens are attacking each other on the chessboard.

def is_queen_attack(queen1, queen2):
    
    #check if the queens are in the same row or column
   if queen1[0] == queen2[0] or queen1[1]  == queen2[1]:
     return True
   
   #check if the queens are in the same diagonal
   
   if abs(queen1[0] - queen2[0]) == abs(queen1[1]- queen2[1]):
      return True
    
   else:
       return False


queen1 = (2, 3)
queen2 = (5, 6)
print(is_queen_attack(queen1, queen2))  

queen3 = (4, 1)
queen4 = (2, 3)
print(is_queen_attack(queen3, queen4))  
queen5 = (1, 1)
queen6 = (6, 7)
print(is_queen_attack(queen5, queen6)) 

