from hash_table import*
from records import*

def default_reader(keys, ht):
    '''default_reader(list, HashTable)
    Inserts Records into the HashTable, ignores duplicates.'''
    for n in keys:
        n = Record(n)
        #ignores duplicates
        if ht.retrieve(n) is None:
            ht.insert(n)

def word_reader(file, ht):
    '''word_reader(str, HashTable)
    Reads in a file and inserts Word_Records into the HashTable.'''
    in_file = open(r"{}".format(file))
    
    for line in in_file:
        line = line.strip()
        words = line.split(" ")
        
        for n in words:
            n = Word_Record(n)
            record = ht.retrieve(n)
            #checks if record is in hashtable
            if record is None:
                ht.insert(n)
            else:
                record.add_one()

def ip_reader(file, ht):
    '''ip_reader(str, HashTable)
    Reads in a file and inserts IP_Records into the HashTable.'''
    in_file = open(r"{}".format(file))
    
    for line in in_file:
        line = line.strip()
        line = line.split(": ")
        
        n = IP_Record(line[0])
        
        record = ht.retrieve(n)
        if record is None:
            ht.insert(n)
            n.add_page(line[1])
        else:
            record.add_page(line[1])

#TESTING:
def main():
    
    ht = HashTable(11000, True)
    word_reader("wordy_file.txt", ht)
    print(ht)
    print(ht.condensed_str())
    '''
    ht = HashTable(1, True)
    ip_reader("ip_clicks.txt", ht)
    print(ht)
    print(ht.condensed_str())'''
    '''
    ht = HashTable(4, False)
    stuff = ['aaa', 'bbb', 'ccc', 'ddd', 'EEE', 'fff', 'aaa', 'xyz', '987', '000']
    default_reader(stuff, ht)
    print(ht.condensed_str())
    print(ht)'''
    
if __name__ == "__main__":
    main()