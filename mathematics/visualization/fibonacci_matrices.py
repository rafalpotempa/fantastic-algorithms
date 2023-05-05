def visualize(function):
    def wrapper(n):
        print(', '.join([str(function(i)) for i in range(n)]))
    return wrapper
