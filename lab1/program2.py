a = [10, 20, 4, 45, 99]
max1 = max2 = float('-inf')

# Loop through each number in list
for n in a:
  
   
    if n > max1:
      
        # Update second largest to the previous largest
        max2 = max1  
        
        # Update largest to the current number
        max1 = n     
        
    elif n > max2 and n != max1:
      
        # Update second largest to current number
        max2 = n  

print(max2)
