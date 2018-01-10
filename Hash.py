'''
hashTable = [0]*10 #intialized a 10 index array for hashtable

#initalize a 10index array of arrays in case multiple values have same key
hashTable2 = [[] for _ in range(10)] 

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

def insert2(table, key, value):
	table[hashFunct(key)].append(value)

print(hashFunct("hello"))
insert(hashTable, "hello", 24601)
print(hashTable)
print(hashTable2)
insert2(hashTable2, "hello", 24601)
print(hashTable2)
insert2(hashTable2, "hello", 10029)
print(hashTable2)
'''
class Hash():

	def __init__(self, size):
		self.size = size
		self.list = [[]for _ in range(size)]

	def hashFunct(self, string):
		hash_value = 0
		for c in string:
			hash_value = hash_value + ord(c)
		return hash_value%len(self.list)

	def insert(self, key, value):
		self.list[hashFunct(key)].append(value)