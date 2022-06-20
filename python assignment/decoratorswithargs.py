Import functools  
  
def repeat(num):  
  
#Creating and returning a wrapper function  
    def decorator_repeat(func):  
        @functools.wraps(func)  
        def wrapper(*args,**kwargs):  
            for _ in range(num):  
                value = func(*args,**kwargs)  
             return value  
          return wrapper  
    return decorator_repeat  
  
#Here we are passing num as an argument which repeats the print function  
@repeat(num=5)  
def function1(name):  
     print(f"{name}")  