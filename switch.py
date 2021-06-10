

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


def main():
    statuses = [400,400,404,400,418,404,418,'']
    for status in statuses:
        print(http_error(status))
        

if __name__ == "__main__":
    main()