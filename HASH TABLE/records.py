from hash_table import*

class Record(object):
    '''Models a Record which is a str value that is meant to be stored in a HashTable.'''
    
    def __init__(self, key):
        '''Record(str)
        Construct a Record with a key value'''
        self.__key = key
    
    def get_key(self):
        '''R.get_key() --> str
        Returns the str value of this Record'''
        return self.__key
    
    def __eq__(self, other):
        '''R.__eq__(Record) or R == Record --> bool'''
        return self.__key == other.get_key()
    
    def __str__(self):
        '''R.__str__() or str(R) --> str
        Returns a string representation of this Record.'''
        return "{}".format(self.__key)
    
class Word_Record(Record):
    '''A class that is a Record object and models a record of a word with properties for its key, and count(number of times it occurs in a HashTable).'''
    
    def __init__(self, key):
        '''Word_Record(str)
        Construct a Word_Record that is a Record with a key value, and a count value of one'''
        Record.__init__(self, key)
        self.__count = 1
    
    def add_one(self):
        '''W.add_one()
        Add one to this Word_Record's count property.'''
        self.__count += 1
    
    def __str__(self):
        '''W.__str__() or str(W) --> str
        Return a string representation of this Word_Record in the format {key}:{count}.'''
        return "{}:{}".format(self.get_key(), self.__count)
    
class IP_Record(Record):
    '''A class that is a Record object and models a record of an IP address with properties for its key(IP address), and pages visited.'''
    
    def __init__(self, key):
        '''IP_Record(str)
        Construct an IP_Record that is a record with properties for its key(IP address) and pages visited.'''
        Record.__init__(self, key)
        self.__pages = []
    
    def add_page(self, url):
        '''I.add_page(str)
        Adds a url to this IP_Record.'''
        self.__pages.append(url)

    def __str__(self):
        '''I.__str__() or str(I) --> str
        Returns a string representation of this IP_Record, in the format {key}:{pages}.'''
        return "{}:{}".format(self.get_key(), self.__pages)