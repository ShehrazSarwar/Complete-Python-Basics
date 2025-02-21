def print_list(list_,idx=0):
    if idx == len(list_):
        return
    print(list_[idx])
    print_list(list_,idx+1)

fruits = ["Orange","Banana","Lichi","Apple"]
print_list(fruits)