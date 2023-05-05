# TODO
def visualize(function):
    def wrapper(result, rows):
        result, rows = function(result, rows)
        
        def ok(x):
            if x%2 != 0: return "+"
            return ""
        
        for x, y in rows:
            print(f"{x:6} {y:6} {ok(x)}")
        print("-" * 15)
        print(f"{result:13}")
    return wrapper