#/usr/bin/python
def element_at(my_list, idx):
    if idx < 0 and idx > len(my_list):
        print("None")
    else:
        print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
