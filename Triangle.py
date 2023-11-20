
def triangle_type(a,b,c):
    if a == b == c:
       return "equilateral Triangle"
     
    elif a == b or b == c:
         return "Isosceles Triangle"
       
    else:
         "Scalene Triangle"
         



print(triangle_type(5, 5, 5))  
print(triangle_type(5, 5, 6))  
print(triangle_type(3, 4, 5)) 
