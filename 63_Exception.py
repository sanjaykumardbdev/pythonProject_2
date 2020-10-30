a = 5
b = 2

try:
    print("Resource Open")
    print(a/b)
    # to print err msg use "e", so that you can represent exception msg as e
    k = int(input("Enter number"))
    print(k)

#except Exception as e:
#    print("cannot divide by zero:---   ", e)

except ZeroDivisionError as e:
    print("cannot divide by zero:---   ", e)

except ValueError as e:
    print("value error:---   ", e)

except Exception as e:
    print("Something went wrong")


# either get exception or not it will execute
finally:
    print("Resource Closed")


print("Bye")
