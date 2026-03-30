# def my_function(*input arguments):
#     pass

def my_decorator(func):
    def wrapper(*args, **kwargs):
        # check position argument
        if not isinstance(args[0], int):
            raise ValueError("First input argument is not Integer")
        if not isinstance(args[1], int):
            raise ValueError("Second input argument is not Integer")
        
        # assign default value to kwargs
        if len(kwargs) > 0:
            for each_key in kwargs.keys():
                if not isinstance(kwargs[each_key], int):
                    raise ValueError("Second input argument is not Integer")
        else:
            kwargs.setdefault('c', 0)
            kwargs.setdefault('d', 0)
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def addition(first_num, second_num, **user_inputs):
    third_num = user_inputs['c']
    fourth_num = user_inputs['d']
    sum = first_num + second_num + third_num + fourth_num
    return sum

