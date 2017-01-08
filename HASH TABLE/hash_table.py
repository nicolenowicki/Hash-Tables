from linked_list import*
from records import*

class HashTable(object):
    '''Models a hashtable, with a list of 'buckets' that are linkedlists.'''
    
    def __init__(self, size, scalable):
        '''HashTable(int, bool)
        Construct a HashTable with number of buckets and the ability to scale to size.'''
        self.__size = size
        self.__scalable = scalable
        self.__list = []
        self.__amount = 0
        
        for n in range(0, self.__size):
            self.__list.append(LinkedList())
    
    #METHODS:
    
    def __str__(self):
        '''H.__str__() or str(H) --> str
        Returns a string representation of this HashTable in the format [bucket #]|: {LinkedList}'''
        out = ""
        counter = 0
        for n in self.__list:
            out += "[{:_>5}]{}\n".format(counter, str(n))
            counter += 1
        return out
    
    def hashing(self, key):
        '''H.hashing(str) --> int
        Returns a int that represents the str value of key. Takes the ordinal value of each character, adds them as strings, multiplies the int version of the string by its length, integer divides it by 2, and then subtracts the value of the original first number to the power of the last number.'''
        val = ""
        #takes ordinal value of each character
        for n in key:
            val += str(ord(n))
            
        num = int(val)
        #multiplying the num by the legnth of its original string (val) will produce varied results because, if val=0011 therefore num=11 which could correspond to different key's num. However, multiplying it by its orginal length will make its num 44 and the other num 22. Therefore, the line below helps in cases such as these.
        num *= len(val)
        
        num = num//2
        num -= int(val[0]) ** int(val[1])
    
        return int(num)%self.__size
        
    def insert(self, record):
        '''H.insert(Record)
        Inserts a Record into this HashTable based on its hash value'''
        self.__amount += 1 
        
        num = hash(record.get_key()) % self.__size
        #num = self.hashing(record.get_key())
        
        pos = self.__list[num]
        pos.insert(record)
        
        #scalable factor
        if self.load_factor() > 0.75 and self.__scalable == True:
            new = []
            for n in self.__list:
                #loop through linked list and add to new list
                current = n.get_first()
                while current != None:
                    new.append(current.get_data())
                    current = current.get_next()
            
            #reset hashtable and double size     
            self.__list = []   
            self.__size *= 2
            self.__amount = 0
            
            for n in range(0, self.__size):
                self.__list.append(LinkedList())  
            
            #re-insert records
            for n in new:
                self.__amount += 1 
        
                num = hash(n.get_key())%self.__size
                #num = self.hashing(n.get_key())
        
                pos = self.__list[num]
                pos.insert(n)

    def delete(self, record):
        '''H.delete(Record)
        Removes the Record if it is present in this HashTable'''
        num = hash(record.get_key()) % self.__size
        #num = self.hashing(record.get_key())
        
        pos = self.__list[num]
        if pos.contains(record) == True:
            pos.delete(record)
    
    def get_num_records(self):
        '''H.get_num_records() --> int
        Returns the number of Records within this HashTable'''
        return self.__amount
    
    def load_factor(self):
        '''H.load_factor() --> float
        Return the load factor of this HashTable which represents the number of records over the number of buckets'''
        load = self.__amount/self.__size
        return load
    
    def num_empty(self):
        '''H.num_empty() --> int
        Returns the number of empty buckets in this HashTable'''
        total = 0
        for n in self.__list:
            if n.is_empty():
                total += 1
        return total
    
    def largest_bucket(self):
        '''H.largest_bucket() --> int
        Returns the size of the largest bucket in this HashTable'''
        max_b = 0
        for n in self.__list:
            if n.size() > max_b:
                max_b = n.size()
        return max_b
    
    def retrieve(self, record):
        '''H.retrieve(Record) --> Record
        Returns a reference to Record or None if Record doesn't exist in this HashTable'''
        pos = hash(record.get_key())%self.__size
        #pos = self.hashing(record.get_key())%self.__size
        n = self.__list[pos]
        
        #to check if in linked list
        if n.contains(record) == True:
            out = n.retrieve(record)
        else:
            out = None
        return out
    
    def condensed_str(self):
        '''H.condensed_str() --> str
        Return a condensed string representation of this HashTable, where each value in the HashTable is represented by #'''
        out = ""
        out += "Size={}  Records={}  LF={}".format(self.__size, self.__amount, self.load_factor())
        for n in self.__list:
            out += "\n:"
            for n in range(0, n.size()):
                out += "#"
        return out

#TESTING:    
def main():
    '''
    ht = HashTable(8, False)
    n = Record('123')
    ht.insert(n)
    ht.insert(Record('sdfsa'))
    ht.insert(Record('asdfg'))
    ht.insert(Record('kjhgfd'))
    print(ht.condensed_str())
    print(ht)
    print(ht.retrieve(Record('123'))) 
    print(ht.largest_bucket())
    print(ht.num_empty())
    print(ht.get_num_records())
    ht.delete(Record('123'))
    ht.delete(Record('a'))
    print(ht)'''
if __name__ == "__main__":
    main()