#primera for

class fact:
    def factorial(self,n):

        f = 1

        while n >= 1:
            f = f*n
            n -=1
        return f

#segunda forma

class fact_R:
    def factorial_R(self,n):
        if n == 1:
            return 1
        else:
            return n*self.factorial_R(n-1)

f1 = fact ()  #1
f2 = fact_R ()  #2

print (f1.factorial(5))
print (f2.factorial_R(5))



