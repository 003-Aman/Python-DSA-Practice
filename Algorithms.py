#an algorithm is basically a set of instructions given to the computer to perform a task or to complete the program

#BINARY SEARCH needs a sorted list to perform and takes log2n steps at max

def binary_search(arr,item):
    low =0 # esma chai indices start from 0 tei vayers
    high = len(arr)-1 # tara esma chai becuase length function will directly give you length tara were looking for the index so -1

    while low<=high:#which means as long as its in asending order
        mid =(low +high)//2
        guess = arr[mid]
        if guess == item:
            return mid
        elif guess< item:
            low = mid+1
        else:
            high =mid-1

    return None

my_list =[1,3,5,7,9]

print(binary_search(my_list, 5))
print(binary_search(my_list, 5))




