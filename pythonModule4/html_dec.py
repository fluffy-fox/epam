def italic(func):
   def func_wrapper(*args, **kwargs):
       return "<i>" + func(*args, **kwargs) + "</i>"
   return func_wrapper

def bold(func):
   def func_wrapper(*args, **kwargs):
       return "<b>" + func(*args, **kwargs) + "</b>"
   return func_wrapper

def underline(func):
   def func_wrapper(*args, **kwargs):
       return "<u>" + func(*args, **kwargs) + "</u>"
   return func_wrapper

@italic
def hello(test):
    return test

