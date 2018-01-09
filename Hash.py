hashTable = [0]*10 #intialized a 10 index array for hashtable

print(hashTable)

def hashFunct(string):
	#hash = []
	hash_value = 0
	for c in string:
		hash_value = hash_value + ord(c)
		#hash.append(ord(c))
	return hash_value%len(hashTable)

def insert(table, key, value):
	table[hashFunct(key)] = value


print(hashFunct("hello"))
insert(hashTable, "hello", 24601)
print(hashTable)