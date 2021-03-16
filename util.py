import random
import pandas as pd
import json

def get_player_scores():
    
    sample_dict = [
        {'name': 'Alice', 'r_1': 96, 'r_2': 89, 'r_3': 80, 'r_4': 98, 'r_5': 71}, 
        {'name': 'Bob', 'r_1': 62, 'r_2': 91, 'r_3': 64, 'r_4': 82, 'r_5': 79}, 
        {'name': 'John', 'r_1': 87, 'r_2': 77, 'r_3': 75, 'r_4': 84, 'r_5': 83}, 
        {'name': 'Joe', 'r_1': 90, 'r_2': 70, 'r_3': 83, 'r_4': 86, 'r_5': 68}, 
        {'name': 'Park', 'r_1': 96, 'r_2': 62, 'r_3': 62, 'r_4': 78, 'r_5': 89},
        {'name': 'Pat', 'r_1': 60, 'r_2': 93, 'r_3': 86, 'r_4': 76, 'r_5': 75}, 
        {'name': 'Laney', 'r_1': 73, 'r_2': 91, 'r_3': 68, 'r_4': 89, 'r_5': 88}
        ]
    return sample_dict

def get_dict_with_none():

    random.seed(20)
    index_list = set()
    for i in range(10):
        index_list.add(random.randint(0,49))
    
    sample_dict = dict()
    for i in range(50):
        key = f"key_{i}"
        if i in index_list:
            sample_dict[key] = None
        else:
            sample_dict[key] = random.randint(1,100)

    return sample_dict


def get_dict_student():
    random.seed(1000)
    index_list = set()
    for i in range(70):
        index_list.add(random.randint(1,100))

    print(len(index_list))
    sample_dict = dict()
    for i in index_list:
        key = f"stu_{i}"
        sample_dict[key] = random.randint(1,10)
    return sample_dict


def get_netflix_files():
    json_fd = open("netflix.json", 'r')
    dataset = json.load(json_fd)
    return dataset

if __name__ == "__main__":
    print(get_netflix_files())

