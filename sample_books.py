import os
import json

def read_json_data(directory):
    data_list = []

    for subdir in os.listdir(directory):
        file_path = os.path.join(directory, subdir, 'metadata.json')
        if os.path.isfile(file_path):
            with open(file_path, 'r') as f:
                data = json.load(f)
                data_list.append(data)
    return data_list

def write_list_to_file(list_data, file_name):
    with open(file_name, 'w') as f:
        for item in list_data:
            f.write("%s\n" % item)

# Usage
directory = 'all_chapterized_books'
data_list = read_json_data(directory)
print("Total books:" + str(len(data_list)))
file_name = 'books.txt'
write_list_to_file(data_list, file_name)

import random
random.seed(42)
sample = random.sample(list(range(1, 158)), 20)
sampled_book_metadata = []
for i in sample:
    sampled_book_metadata.append(data_list[i])
write_list_to_file(sampled_book_metadata, "sampled-books.txt")