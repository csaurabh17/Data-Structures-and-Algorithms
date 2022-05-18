class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def __hash(self, key):
        hash_key = 0
        for letter in key:
            hash_key = (hash_key + ord(letter) * 17) % len(self.data_map)
        return hash_key

    def print_hashtable(self):
        for i, val in enumerate(self.data_map):
            print(i, ":", val)

    def set_item(self, key, value):
        index = self.__hash(key)
        lst = [key, value]
        if self.data_map[index] is None:
            self.data_map[index] = [lst]
        else:
            self.data_map[index].append(lst)
        return True

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is None:
            return None
        else:
            for i in self.data_map[index]:
                if i[0] == key:
                    return i[1]
            return None

    def keys(self):
        keys_arr = []
        for i, val in enumerate(self.data_map):
            if self.data_map[i] is not None:
                for elem in self.data_map[i]:
                    keys_arr.append(elem[0])
        return keys_arr


# Instantiating Hashtable
hash_table = HashTable()
# hash_table.print_hashtable()

# Setting item
hash_table.set_item('Saurabh', 1)
# hash_table.print_hashtable()
hash_table.set_item('Choudhary', 2)
# hash_table.print_hashtable()

# Getting item
print(hash_table.get_item('Saurabh'))
print(hash_table.get_item('Choudhary'))
print(hash_table.get_item('Paris'))

# printing keys
print(hash_table.keys())