# How to Install a Beta Version of Python

Python 3.10.0b2 - Released May 31, 2021

## Overview of Procedure

1. Ubuntu Server 20.04 LTS
2. Install required libraries
```$ sudo apt-get install libssl-dev openssl make gcc```
3. Copy url for specific Python version desired
```https://www.python.org/ftp/python/3.10.0/Python-3.10.0b2.tgz```
4. Go to /opt directory and download Python to here
```
$ cd /opt
$ wget https://www.python.org/ftp/python/3.10.0/Python-3.10.0b2.tgz
```
5. Extract the archive
```$ tar xzvf Python-3.10.0b2.tgz```
6. Drop into the new Python directory
```$ cd Python-3.10.0b2```
7. Compile the new version - each of these take awhile
```
$ ./Configure
$ make
$ sudo install
```
8. Make this version of Python usable anywhere
```sudo ln -fs /opt/Python-3.10.0b2/Python /usr/bin/python3.10```
9. Check your Python Version now
```$ python3 --version```
success looks like:
```Python 3.10.0b2```

## In Python 

### A Basic Usage

```python3
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
```

OUTPUT:
```
Bad request
Bad request
Not found
Bad request
I'm a teapot
Not found
I'm a teapot
Something's wrong with the Internet
```

Note the last block: the variable name, _, acts as a wildcard and insures the subject will always match. The use of _ is optional.

Removing the Wildcard will result in:

```Python3
def http_error2(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
```
OUTPUT:
```
Bad request
Bad request
Not found
Bad request
I'm a teapot
Not found
I'm a teapot
None
```

### Guard

We can add an if clause to a pattern, known as a “guard”. If the guard is false, match goes on to try the next case block. Note that value capture happens before the guard is evaluated:

```Python3
def use_a_guard(x,y):
    match x,y:
        case x, y if x == y:
            print(f"The point is located on the diagonal Y=X at {x}.")
        case x, y:
            print(f"Point is not on the diagonal.")
```
OUTPUT:
```
The point is located on the diagonal Y=X at 1.
None
Point is not on the diagonal.
None
The point is located on the diagonal Y=X at 3.
None
```

## FULL CODE

```Python3
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
```

# References

- [PEP 634: Structural Pattern Matching](https://docs.python.org/3.10/whatsnew/3.10.html#pep-634-structural-pattern-matching)
- [Python 3.10.0b2](https://www.python.org/downloads/release/python-3100b2/)
- [How to install a specific Python version on Ubuntu?](https://www.digitalocean.com/community/questions/how-to-install-a-specific-python-version-on-ubuntu)
- [GitHub Code for this Report](https://github.com/InkSlob/python3.10-switch-statement/blob/main/install_py_3_10.md)