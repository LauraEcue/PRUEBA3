class fibonacci:
    def fibonacci(self, n):
        if n == 1:
            return 1
        elif n == 0:
            return 0

        else:
            return self.fibonacci(n-1) + self.fibonacci(n-2)


f1 = fibonacci()
print (f1.fibonacci(5))