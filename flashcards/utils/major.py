class Major:
    def __init__(self, key):
        self.key = key.upper()
        # self.email = first + "."+ last + "@email.com" 

    @property
    def key(self):
        """The Key property"""
        print("The key is: ")
        return self._key
    
    @key.setter
    def key(self, new_key):
        self._key = new_key.upper()
        print(f"The key was set to: {self._key}")

    @key.deleter
    def key(self):
        print(f"the key of {self._key} was deleted")
        del self._key
        
    @property
    def scale(self):
        """The notes generated based on the key"""
        print("The notes on the scale are:")
        return self.key