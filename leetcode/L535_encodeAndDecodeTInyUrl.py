
"""TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and 
it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. 
You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL"""


class Codec:
    
    import string
    import random
    
    dic = {} 
    
    def encode(self, longUrl): # complexity is O(1)
        """Encodes a URL to a shortened URL.
        :type longUrl: str
        :rtype: str
        """
        if longUrl not in self.dic:
            x = "".join(random.choice(string.ascii_letters + string.digits) for i in range(7))
            self.dic[x]=longUrl
            return x
            
    def decode(self, shortUrl): # complexity is O(1)
        """Decodes a shortened URL to its original URL.
        :type shortUrl: str
        :rtype: str
        """
        return self.dic[shortUrl]
        #12:43
        #12 :51
        #1:48

# Your Codec object will be instantiated and called as such:
# codec = Codec()
#codec.decode(codec.encode(url))

"""NotesToMe:

Previously you used this code.
for encode  self.dic[longUrl]=x and for decode you used iteritems() to search for the shortUrl and then returned longUrl. But this increased 
complexity to O(N) for decode. You the above code you decresed the complexity to O(1) just by swapping key-pair values in encode."""
            
