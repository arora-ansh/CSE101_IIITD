# magic_module.py

"""This function takes 3 numbers
And gives its Magic Number"""

def find_magic_num(x,y,z):
    m = (((x**2)+y)%z)**5
    return m
