import signal

def timeout(seconds):
    def decorator(function):
        def wrapper(*args, **kwargs):
            def handler(signum, frame):
                raise Exception('\nTimeout')
            signal.signal(signal.SIGALRM, handler)
            signal.alarm(seconds)
            result = function(*args, **kwargs)
            signal.alarm(0)
            return result
        return wrapper
    return decorator

@timeout(seconds=5)
def read_user_name():
    name = input('Qual é o seu nome? ')
    print('Seja bem-vindo,', name)

try:
    read_user_name()
except Exception as e:
    print(e)