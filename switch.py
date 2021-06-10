


def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the Internet"


def http_error2(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"


def use_a_guard(x,y):
    match x,y:
        case x, y if x == y:
            print(f"The point is located on the diagonal Y=X at {x}.")
        case x, y:
            print(f"Point is not on the diagonal.")
        

def main():
    
    # BASIC SWITCH
    statuses = [400,400,404,400,418,404,418,'']
    for status in statuses:
        print(http_error(status))
    # No Wildcard
    for status in statuses:
        print(http_error2(status))
        
    # USING GUARD
    points = [[1,1], [1,2], [3,3]]
    for point in points:
        x = point[0]
        y = point[1]
        print(use_a_guard(x,y))
        
        

if __name__ == "__main__":
    main()