characters = 'abcdefghiklmnopqrstuvwyzABCDEFGHIJLKMNOPQRSTUVWYZ0123456789'

class Codec:
    def __init__(self):
        self.encoded = {}
        self.decoded = {}

    def toShortUrl(self, longUrl):
        shortUrl = []

        for i in range(6):
            randomIndex = random.randrange(len(characters))
            shortUrl.append(characters[randomIndex])

        "".join(shortUrl)


    def encode(self, longUrl):
        if longUrl not in self.encoded:
            shortUrl = self.toShortUrl(longUrl)
            self.encoded[longUrl] = shortUrl
            self.decoded[shortUrl] = longUrl

        return self.encoded[longUrl]


        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        

    def decode(self, shortUrl):
        if shortUrl in self.decoded:
            return self.decoded[shortUrl]
        return None
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))