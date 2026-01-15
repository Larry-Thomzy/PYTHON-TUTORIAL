# Every function in Python receives a predefined number of arguments, if declared normally, like this:

# def myfunction(first, second, third):
    # do something with the 3 variables


# It is possible to declare functions which receive a variable number of arguments, using the following syntax:

def foo(first, second, third, *therest):
    print("First: %s" % first)
    print("Second: %s" % second)
    print("Third: %s" % third)
    print("And all the rest... %s" %list(therest))  # (therest,)--tuple or f string

foo(1,2,3,4,5,6,6,8,72,5,7,1)

# The *therest takes the extra arguments and store them as tuple

# Now this double ** takes the extra arguments and store them as a dictionary

def bar(first, second, third, **options):
    if options.get("action") == "sum":
        print("The sum is: %d" %(first + second + third))

    if options.get("number") == "first":
        return first

result = bar(1, 2, 3, action = "sum", number = "first")
print("Result: %d" %(result))




# 1.
# Finance — Calculate Total Price of Unlimited Products
# Write:
# def total_price(*prices):


# 2..
#  E-commerce — Generate Product Summary
# Write:
# def product_info(name, price, **extra):
# Where extra may include:
# brand="Nike"
# color="Black"
# in_stock=True
# discount=20



# Finance
# def total_price(*prices):
#     total = 0
#
#     for p in prices:
#         if isinstance(p, (int, float)):
#             total += p
#         else:
#             print(f"Skipping invalid price: {p}")
#
#     return total


# def product_info(name, price, **extra):
#     print(f"Product: {name}")
#     print(f"Price: ${price}")
#
#     if extra:
#         print("Extra Details:")
#         for key, value in extra.items():
#             print(f" - {key}: {value}")
#
#     if "discount" in extra:
#         discounted = price - (price * extra["discount"] / 100)
#         print(f"Discounted Price: ${discounted:.2f}")





