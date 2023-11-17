def test_func(arg1, arg2, arg3):
    print(arg1 + arg2 + arg3)

args = {}
args["arg1"] = 1
args["arg2"] = 2
args["arg3"] = 3

test_func(*args) #arg1arg2arg3

test_func(**args) #6
