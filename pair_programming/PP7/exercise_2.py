# PP7 Exercise 2
# Group member: Thee Ngamsangrat, Kaiwen Li, Yingchen Liu
def my_pow(x, r):
    """ Calculate f(x) = x^r and f'(x) where
    x: int
    r: int
    """

    ret = []
    ret_val = x**r
    ret_der = r*(x**(r-1))

    ret.append(ret_val)
    ret.append(ret_der)

    return ret

if __name__ == "__main__":
    print(my_pow(3, 4))