'''

Implement the following functions based on the question. Retain the name of the functions, and parameters as is in the question. 

=================


1. construct_card(name_list, address_list, phone_list) --> 30% 
Get the names, addresses, phone of 10 different people as a list and return a list of dictionaries. 

Input:
name_list = ['Joe', 'Max' ...]
address_list = ['Addr 1', 'Addr 2' ..]
phone_list = ['4041234567', '6161234567'..]

Output:
result_list = [
    {'name': "Joe", 
    'address':"Addr 1",
    'phone': "40412334567"},
    {'name': "Max", 
    'address':"Addr 2",
    'phone': "61612334567"},
    .... 10 entries
]

------------------------------------------------

2. remove_empty_values(sample_dict) --> 40%
 
Write a function to remove all the None values from a dictionary in Python. Use get_dict_with_none() function in util file for sample dictionary. 
Input:
sample_dict = {'c1': 'A', 'c2': 'B', 'c3': None}
Output:
return_dict = {'c1': 'A', 'c2': 'B'}

----------------------------------------------------------------

3. search_for_key(sample_dict, sample_student) --> 30% 

Write a function that takes in a sample dictionary and student name. (Use fn: get_dict_student() from util)
Student name is of the format stu_{x} where x is in the range 1 to 100. 
Check if sample student is present in the sample dict, if yes return the list of students with same value as the sample_student:
If student not found, return empty list.

Input 1:
sample_dict = {'stu_1':10, 'stu_2':20, 'stu_3':10}
sample_student = stu_1

Output 1:
[stu_1, stu_3]


Input 2:
sample_dict = {'stu_1':10, 'stu_2':20, 'stu_3':10}
sample_student = stu_4

Output 2:
[]


'''