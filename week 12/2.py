# a = {10}  # => {10, 20}
# def test():
#     a.add(20)
#     return None


# test()
# print(a)


# we want that in terminal, {10, 20}
# one is updation, {10}  -> {10, 20} # calling test will solve this problem
# we need to print the updated value of a -> which means to print a





# list = [1, 2, 3]




# while conditon:
#     # code you want to repeat


# i = 0
# while i < 6:
#     print("Hello")
#     i += 1


# for  i in range(1, 11):
#     print(i)

# def my_generator(n):
#     value = 0
#     while value < n:
#         yield value
#         value += 1


# temp = my_generator(3)

# print(next(temp))
# print(next(temp))
# print(next(temp))



gradebook = {
    "moosa":{
        "math":90,
        "science":79,
        "english":80
    },
    "abdullah":{
        "math":67,
        "science":40,
        "english":97
    },
    "jacob":{
        "math":40,
        "science":40,
        "english":20
    },
        "tyler":{
            "math":100,
        "science":100,
        "english":99
    },
        "mike":{
        "math":90,
        "science":85,
        "english":89
    }
}

# print(type(gradebook["abdullah"]))


print(gradebook["abdullah"].keys())
