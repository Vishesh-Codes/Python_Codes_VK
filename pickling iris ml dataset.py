#-------------------------------
# pickling iris (an ML dataset)
#-------------------------------
"""
Keyword for searching on web:   uci ml repository
Source of data: https://archive.ics.uci.edu/

In this exercise, I have obtained list of lists of dataset of iris by using zipfile module because the downloadable file is provided in zip format. So, without extracting the zip file, I have read the data from that and made list of lists.
Then used 'pickle' module for pickling and unpickling
"""
# importing built-in modules zipfile and pickle
import zipfile
import pickle

# reading file from the zip file without unzipping
with zipfile.ZipFile(r"D:\New folder\iris.zip") as z:

    # reading data from the file iris.data 
    with z.open("iris.data", "r") as f:

        # iterating over each line in iris.data
        list1 = [line.decode('utf-8').strip() for line in f]

        # iterating over each item of above list
        final_list = [item.split(",") for item in list1 if len(item) != 0]

# using pickle.dumps() for pickling
pickled_list_of_lists = pickle.dumps(final_list)

# using pickle.dump() for pickling
with open("z_pickled_list.pkl", "wb") as file:
    pickle.dump(final_list, file)

# unpickling by pickle.loads()
unpickled_list = pickle.loads(pickled_list_of_lists)
print(unpickled_list)

# unpickling by pickle.load()
with open("z_pickled_list.pkl", "rb") as file:
    unpickled_list2 = pickle.load(file)
    # print(unpickled_list2)

