# Exc. 1
print("---Exc. 1---")
#--------------------
def sum_num(*args):
    """
    gets a list of number add return its total
    :param args:
    :return:
    """
    res = 0
    for i in args:
        res += i
    print(res)
#--------------------
sum_num(1,2,3,4)
print()

# Exc. 2
print("---Exc. 2---")
#--------------------
def print_user_info(**kwargs):
    """
    gets several dictionary items and prints them
    :param kwargs:
    :return:
    """
    for key, value in kwargs.items():
        print(f"{key}:{value}", end= ", ")
    print()
#--------------------
print_user_info(name="Dana", age=30, city="Tel Aviv")
print()

# Exc. 3
print("---Exc. 3---")
#--------------------
def combine_values(*args, **kwargs):
    """
    gets a list of number add return its total
    gets several dictionary items and prints them
    :param args:
    :param kwargs:
    :return:
    """
    res = 0
    for i in args:
        res += i
    print(res)

    for key, value in kwargs.items():
        print(f"{key}:{value}")
#--------------------
combine_values(2, 4, 6, name="Tom", job="Dev")
print()

# Exc. 4
print("--Exc. 4--")
#--------------------
def greet_user(**kwargs):
    """
    get a user name and greet him
    if not greet user
    :param kwargs:
    :return:
    """
    if not kwargs:
        print ("Hello guest")
    else:
        for key, value in kwargs.items():
            print(f"Hello {value}")
#--------------------
greet_user(name="Lior")
greet_user()