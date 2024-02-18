start_num = input("Please enter the start number of the range: ")
end_num = input("Please enter the end number of the range: ")

int_start = int(start_num)
int_end = int(end_num)

print("Prime numbers between", int_start, "and", int_end, "are:")

for each_num in range(int_start, int_end + 1): # to include the end number itself.
    if each_num > 1:
        for i in range(2, each_num):
            if each_num % i == 0:
                break
        else:
            print(each_num)





