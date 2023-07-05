""" 
numbers.py
"""

class NumberSamples:


    def getNumberTypes(self):
        # Display number types
        print("\n---Get number types---")
        self.getType(1.2)
        self.getType(1000)
        self.getComplexType(1+2j)

    def getType(self, number):
        
        message = '{0} {1} {2}'.format(number, 'is of type ', type(number))
        print(message)

    def getComplexType(self, number):
        message = '{0} {1} {2}'.format(number, 'is of type complex? ', 
                isinstance(1+2j,complex))
        print(message)
        
    def fib(self, f, N) : 
        # Implementation for 
        # Fibonacci triangle 
        # function to fill Fibonacci 
        # Numbers in f[] 
        # 1st and 2nd number of 
        # the series are 1 and 1 
        f[1] = 1
        f[2] = 1
        for i in range(3, N + 1) : 
            # Add the previous 2 numbers 
            # in the series and store it 
            f[i] = f[i - 1] + f[i - 2] 

    def fiboTriangle(self, n) : 
        # Fill Fibonacci numbers in 
        # f[] using fib(). We need 
        # N = n*(n + 1)/2 Fibonacci 
        # numbers to make a triangle 
        # of height n 
        N = n * (n + 1) // 2
        f =[0] * (N + 1) 
        self.fib(f, N) 
        
        # To store next Fibonacci 
        # Number to print 
        fiboNum = 1

        # for loop to keep track of 
        # number of lines 
        for i in range(1, n + 1) : 
            # For loop to keep track of 
            # numbers in each line 
            for j in range( 1, i + 1) : 
                
                if (fiboNum<=len(f)-2):
                    fiboNum = fiboNum + 1 
                print(f[fiboNum], " ", end = "") 
                
            print() 
