
Max_Number = 100
prime_lst = [2]

def prime_number():
    for i in range(3,Max_Number):
        state = True
        for p in prime_lst:
            #checking if the number is divisible by any of the primes smaller than it
            if i% p == 0:
                state = False
                break
        
        if state == True:
            prime_lst.append(i)    
        
prime_number()
print(prime_lst)