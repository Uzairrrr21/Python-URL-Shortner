import string
import random

class URLShortener:
    def __init__(self, base_url):
        self.base_url = base_url
        self.url_map = {}

    def _generate_short_code(self):
        """Creating a random 6-character string"""
        return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

    def shorten_url(self, long_url):
        """Shortens a long URL"""
        while True:
            short_code = self._generate_short_code()
            if short_code not in self.url_map:
                self.url_map[short_code] = long_url
                return f"{self.base_url}/{short_code}"

    def expand_url(self, short_code):
        """Retrieves the original URL"""
        return self.url_map.get(short_code)

# Example usage
shortener = URLShortener("https://bit.ly")
short_url = shortener.shorten_url("http://careers.netsolpk.com/")
original_url = shortener.expand_url(short_url.split("/")[-1])

print(f"Shortened URL: {short_url}")
print(f"Original URL: {original_url}")
