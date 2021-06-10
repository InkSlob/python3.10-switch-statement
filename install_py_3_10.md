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

