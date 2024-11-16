import string, random

class Codec:
    BASE_URL = 'https://tinyurl.com/'
    
    encodeMap = dict()
    decodeMap = dict()

    @staticmethod
    def _generate_uuid() -> str:
        letters = string.ascii_letters + string.digits
        return ''.join(random.choice(letters) for _ in range(6))

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl in Codec.encodeMap:
            return Codec.encodeMap[longUrl]
        
        generated_url = Codec.BASE_URL + self._generate_uuid()
        Codec.encodeMap[longUrl] = generated_url
        Codec.decodeMap[generated_url] = longUrl
        
        return generated_url

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return Codec.decodeMap[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))