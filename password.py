cases = int(input())

for case in range(cases):
    n = int(input())
    used = [int(x) for x in input().split()]
    differs = 10 - len(used)
 
    factn = 1
    for nums in range(1, 10+1):
        factn = factn*nums
    down = 10 - 4
    factr = 1
    for nums in range(1, down+1):
        factr = factr*nums
    
        
    
    print(factn // down)
 
    
        
    
    
    
    
    
    

    
                

    
        
            

    
    

    
    