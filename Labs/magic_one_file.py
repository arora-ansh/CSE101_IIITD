def find_magic_num(x,y,z):

    """ This function takes 3 numbers
And gives its magic number """
    m = (((x**2)+y)%z)**5
    return m

x = int(input())
y = int(input())
z = int(input())

print(find_magic_num(x,y,z))
