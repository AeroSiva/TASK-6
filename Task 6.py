#Q1. You have been given a python list [10,501,22,37,100,999,87,351] your task is to create two list one which have 
# all the Even numbers and another list which have all the Odd numbers i it ?
def odd_even_lst(lst):
    even_lst = []
    odd_lst = []
    odd_even_dict = {}

    for num in lst:
        if num % 2 == 0:
            even_lst.append(num)
        else:
            odd_lst.append(num)
    
    odd_even_dict["odd_list"] = odd_lst
    odd_even_dict["even_list"] = even_lst
    
    return odd_even_dict

lst = [10, 501, 22, 37, 100, 999, 87, 351]
result = odd_even_lst(lst)

print("Even list:", result["even_list"])
print("Odd list:", result["odd_list"])




#Q2. Given a python list[10,501,22,37,100,999,87,351] 
# your task is to count ll the Prime Numbers and create a new python list which will contain all the Prime Numbers in it ?

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def prime_num_lst(lst) :
    prime_numbers_list = [num for num in lst if is_prime(num)]
    return prime_numbers_list
lst = [10, 501, 22, 37, 100, 999, 87, 351]
print(prime_num_lst(lst))




#Q3.Given a python list[10,501,22,37,100,999,87,351].
# Find out how many numbers are thre in the given Python List which are Happy Numbers ?

def is_happy_num(lst) :
    happy_num = []
    for num in lst:
        temp_dig_sq = set()
        dig_sq = 0
        while num not in temp_dig_sq and dig_sq not in temp_dig_sq and num !=1 and dig_sq != 1:
            temp_dig_sq.add(num)
            dig_sq = sum(int(dig)**2 for dig in str(num))
            if dig_sq == 1 :
                happy_num.append(num)
    return happy_num
lst = [10, 501, 22, 37, 100, 999, 87, 351]
result = is_happy_num(lst)
print(result)




#Q4. Write a python program to find the sum of the first and last digit of an integer ?
def sum_1st_last (num) :
    sum = int(num[0]) + int(num[-1])
    return sum
num = input("Enter the integer : ")
result = sum_1st_last(num)
print(result)





#Q5.You have been given list of N integerhich represents the number of Mangoes in a bag.
#Each bag has a variable number of Mangoes.There are M students in a Guvi class, your task is to distribute the Mangoes 
# in such a way that each student gets one Bag. The difference between the number of Mangoes in a bag with maximum Mangoes
#and minimum Mangoes given to the student is minimum ?

def dis_mangoes(lst,M) :
    sorted_lst = sorted(lst)
    distri_to_stu = []
    N = len(lst)
    if N < M :
        return ("Cannot distribute to all students")
    else :
        for i in range(M) :
            distri_to_stu.append(sorted_lst[i])
        return distri_to_stu
lst = list(input("Enter the list of number of mangoes in bag seperated by space : ").split())
M = int(input("Enter the number of students : "))
result = " ".join(map(str,dis_mangoes(lst,M)))
print("The distributed bags are : ",result)




#Q6. You have been given three lists. Your task is to find the duplicates in the thre lists. Wite a python program for the same
#  You can use your own python lists?
def dup_ele(lst_1,lst_2,lst_3) :
    max_len = max(len(lst_1),len(lst_2),len(lst_3))
    dup = set()
    for i in lst_1 :
        if i in lst_2 or i in lst_3 :
            dup.add(i)
    print (dup)
    for j in lst_2 :
        if j in lst_3 :
            dup.add(j)
    print(dup)
    return dup
lst_1 = list(input("Enter list 1 elements seperated by space : ").split())
lst_2 = list(input("Enter list 2 elements seperated by space : ").split())
lst_3 = list(input("Enter list 3 elements seperated by space : ").split())
result = " ".join(dup_ele(lst_1,lst_2,lst_3))
print("The duplicate elements in three lists are : ", result)





#Q7. Write a python program to find th efirst nion- repeating elements in a given list of integers ?

def first_non_rep(lst) :
    count_dict = {}
    for num in lst :
        if num not in count_dict :
            count_dict[num] = 1
        else:
            count_dict[num] += 1
    for num1 in lst:
        if count_dict[num1] == 1 :
            return num1
    return ("No repeating elements")

lst = [10,20,30,10,30,40,50,60]
result = first_non_rep(lst)
print("First non repeating element is : ",result)






#Q8.Write a python program to find the minimum element in a rated and sorted list ?

def find_min_ele (lst) :
    sorted_lst = sorted(lst)
    return sorted_lst[0]
lst = [50,40,20,30,60,40,70]
result = find_min_ele(lst)
print("minimum element is : ",result)





#Q9. You have been given a python list[10,20,30,9] and a value of 59.
# Write a python program to find the triplet in the list whose sum is equal to the given value ?

def find_triplets(lst, triplet_sum):
    n = len(lst)
    triplets = []

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if lst[i] + lst[j] + lst[k] == triplet_sum:
                    triplets.append([lst[i], lst[j], lst[k]])

    return triplets

lst = [10, 20, 30, 9]
triplet_sum = 59

triplets = find_triplets(lst, triplet_sum)

if triplets:
    print("Triplets are :")
    for triplet in triplets:
        print(triplet)
else:
    print("There are no triplets ")







#Q10. Given a list [4,2,-3,1,6].Write a python program to find if there is a sub-list with sum equal to zero ?

def is_sub_lst_sum_zero (lst) :
    sublists = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            sublists.append(lst[i:j])
    for k in sublists :
        if sum(k) == 0 :
            return ("Yes, the list has a sub-list with sum equal to zero for example ",k )
    return ("No, the list has no sub-list with sum equal to zero ")

lst = [4,2,-3,1,6]
result = is_sub_lst_sum_zero(lst)
print(result)