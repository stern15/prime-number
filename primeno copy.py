class Main():
    def prime():
    	UserIn=int(input("Is this number a prime number:"))
    	if (UserIn>1):
    	    for i in range(2,UserIn):
    	        if (UserIn % i==0):
    	            print("false")
    	            break
    	        else:
    	            print("true")
    	            break
    	elif(UserIn==1):
    		("true")
    	else:
    		print("please input a number equal or greater than 1")
    prime()
if __name__=="__main__":Main()