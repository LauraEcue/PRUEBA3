class fact:
    def factorial(self,n):

        f = 1

        while n >= 1:
            f = f*n
            n -=1
        return f

class fact_R:
    def factorial_R(self,n):
        if n == 1:
            return 1
        else:
            return n*self.factorial_R(n-1)

f1 = fact ()
f2 = fact_R ()

print (f1.factorial(5))
print (f2.factorial_R(5))



