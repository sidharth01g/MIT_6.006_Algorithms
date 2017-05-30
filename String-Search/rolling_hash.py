# Not working - Check hash rolling
import math


class RollingHash(object):
    def __init__(self, prime_number, base=256, intitial_string):
        self.prime_number = prime_number
        self.base = base
        self.intitial_string = intitial_string

        self.current_word = intitial_string
        self.current_hash = self.initial_hash

    @property
    def window_size(self):
        return len(self.intitial_string)

    @property
    def initial_hash(self):
        """
        digits_list = [
            ord(self.intitial_string[i]) * math.pow(self.base, i) for i in range(
                self.window_size)
        ]
        N = sum(digits_list)
        """
        N = string_to_number(intitial_string, self.base)
        hash = N
        return hash

    def string_to_number(self, string, base=256):
        power = 0
        sum = 0
        for character in string[::-1]:
            ascii_value = ord(character)
            sum += ascii_value * (base ** power)
            power += 1
        return sum




    def roll(self, in_char):
        if type(in_char) is not str or len(in_char) != 1:
            raise TypeError("Rolling needs an input character")
        nr = ord(in_char)
        nl = ord(self.current_word[0])

        old_hash = self.current_hash
        base = self.base
        k = self.window_size
        p = self.prime_number

        print(old_hash, base, k, p)
        new_hash = ((old_hash * base) - (nl * math.pow(base, k)) + nr)

        self.current_hash = new_hash
        self.current_word += in_char
        self.current_word = self.current_word[1:]


def main():
    text = "The Eisenhower dollar is a one-dollar coin issued from 1971 to 1978 by the United States Mint. Authorized by law on December 31, 1970, it was the first US dollar coin minted since 1935, the last year of the Peace dollar. Designed by Frank Gasparro, the coin's obverse depicts President Dwight D. Eisenhower, who died in March 1969."
    search_keyword = "he Eisenho"
    prime_number = 19
    base = 256
    search_keyword_hash = RollingHash(prime_number, base, search_keyword)
    print("Search for: " + search_keyword)
    print("Search keyword hash: %s" % str(search_keyword_hash.current_hash))

    text_rolling_hash = RollingHash(
        prime_number, base, text[0: len(search_keyword)])

    for i in range(len(search_keyword), len(text)):
        # print(i, end= " ")
        print(i, text_rolling_hash.current_word, text_rolling_hash.current_hash)

        if text_rolling_hash.current_hash == search_keyword_hash.current_hash:
            print("-------------------Potential match")

        text_rolling_hash.roll(text[i])




if __name__ == "__main__":
    main()
