def num_analyzer():
      while True:
          try:
        
       
        
    
      
            a = int(input("Enter a number "))
            print("Analyzing "f"{a}")
            
            if a > 0 and a % 2==0:
                print("Positive Even Number")
        
            elif a < 0 and a % 2==0:
                print("Negative Even Number")
    
            elif a > 0 and a % 2 != 0:
                print("Positive Odd Number")
    
            elif a < 0 and a % 2 != 0:
                print("Negative Odd Number")
      
            else:
                print("Zero")
                break
                
        
          except ValueError:
            print("Enter a valid integer")
            continue
              
              
   
          finally:
            print("Current Session Finished")
        
        
        
    
 
num_analyzer()
