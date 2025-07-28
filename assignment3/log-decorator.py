def clear_log():
    with open('./decorator.log', 'w') as log:
        print('Log cleared.')

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        with open('./decorator.log', 'a') as log:
            log.write(f'''
function: {func.__name__}
positional parameters: {args}
keyword parameters: {kwargs}
return: {func(*args, **kwargs)}
''')
    return wrapper

@logger_decorator
def hello():
    print("Hello, World!")

@logger_decorator
def truth(a, b, c):
    return True

def main():
    clear_log()
    hello()
    truth(1, 2, 3)
    truth(c=1,b=2,a=3)
main()
