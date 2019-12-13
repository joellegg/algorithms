# Overview
# Python hash table implementation that utilizes open addressing
# where the table is maintained as an array of elements (not buckets).
# Collisions are resolved by appending the item to the element
    # could change to use linked list or doubly linked list
    # could use next bucket

# Questions
# Should the # of buckets be a large prime or
# do we multiply the hash by a large prime when # of buckets becomes large?
class HashTable(object):
    def __init__(self, size=10):
        self.tableSize = size
        self.table = [[] for i in range(size)]

    def hashIt(self, key):
        return key % self.tableSize

    def insert(self, key, value):
        # can also use the built in hash function but wanted to implement my own simple version
        hashKey = self.hashIt(key)
        bucket = self.table[hashKey]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                bucket[i] = ((key, value))
                return 'Key {} overwritten'.format(key)
        bucket.append((key, value))
        return 'Key {} added'.format(key)

    def search(self, key):
        hashKey = self.hashIt(key)
        bucket = self.table[hashKey]
        for i, kv in enumerate(bucket):
            k, v = kv
            if (k == key):
                return v
        return 'Key {} not found'.format(key)

    def delete(self, key):
        hashKey = self.hashIt(key)
        bucket = self.table[hashKey]
        for i, kv in enumerate(bucket):
            k, v = kv
            if (k == key):
                del bucket[i]
                return 'Key {} deleted'.format(key)
        return 'Key {} not found'.format(key)


hashTable = HashTable(11)
print(hashTable.table)
print(hashTable.insert(0, 'Joel'))
print(hashTable.insert(10, 'John'))
print(hashTable.insert(0, 'Billy'))
print(hashTable.insert(7, 'Marty'))
print(hashTable.table)

print(hashTable.search(0))
print(hashTable.search(1))

print(hashTable.delete(2))
print(hashTable.delete(3))
