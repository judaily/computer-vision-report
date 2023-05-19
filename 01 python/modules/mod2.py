# mod2.py
PI = 3.141592

class Math:
    def solv(self, r): # method
        return PI * (r**2)
    
def sum(a, b): # function
    return a + b

def main():
    print(PI)
    a = Math()
    print(a.solv(2))
    print(sum(PI,4.4))

if __name__=='__main__':
    main()