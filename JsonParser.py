import json
from JsonBlob import User
from JsonBlob import Sites
from JsonBlob import JsonBlob

class JsonParser():
    def parseFile(self, jsonObject):
        """
            Read the decrypted blob file into a JsonBlob object
        """
        blob = JsonBlob(**json.loads(jsonObject))
        return blob

    def updateJson(self, jsonBlob :JsonBlob):
        """
            Serialize theJsonBlob object
        """
        enc = json.dumps(jsonBlob, default=lambda o: o.__dict__, indent=4)
        return enc
        
