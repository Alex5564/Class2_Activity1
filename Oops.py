class Employee:
    def __init__(self):
        print('Employ Created')

        def __del__(self):
            print('Employee Destroyed')

def Create_obj():
   
      print('Making Object...')
      obj = Employee()
      print('Function end...')  
      return obj


print('Calling Create obj() function...')
obj = Create_obj()
print('Program End...')



        