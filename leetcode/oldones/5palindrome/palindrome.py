# brute force 
# moving windows start - end (pair)
# 0,0 -> is palindrome
# 0,1 -> is it palindrome?
# 0,2 -> is it palindrome?
# then check lengtht of palindrome and save if it is bigger

# memoization - remember each palindrome check
# check if this start_end is in dict if it is assume it is palindrome

class Solution(object):
    def __init__(self):
        self.counter = 0
        self.cache = {}

    def longestPalindrome(self, s):
        if len(s) <= 1:
            return s

        longest = ""

        for x in range(len(s)):
            for y in range(len(s) + 1):
                start_end = s[x:y]
                if start_end in self.cache:
                    continue
                if self.is_palindrome(start_end):
                    self.cache[start_end] = True
                    if len(start_end) > len(longest):
                        longest = start_end
                else:
                    self.cache[start_end] = False


        if longest == "":
            return None
        else:
            return longest

    def is_palindrome(self, s):
        self.counter += 1
        if len(s) <= 1:
            return True

        start = 0
        end = len(s) - 1

        if s[start] != s[end]:
            return False
        else:
            sub = s[1:end]
            if sub in self.cache and self.cache[sub]:
                return True
            if self.is_palindrome(sub):
                self.cache[sub] = True
                return True
            else:
                self.cache[sub] = False
                return False

if __name__ == "__main__":
    t = Solution()
    print(t.longestPalindrome("klvxwqyzugrdoaccdafdfrvxiowkcuedfhoixzipxrkzbvpusslsgfjocvidnpsnkqdfnnzzawzsslwnvvjyoignsfbxkgrokzyusxikxumrxlzzrnbtrixxfioormoyyejashrowjqqzifacecvoruwkuessttlexvdptuvodoavsjaepvrfvbdhumtuvxufzzyowiswokioyjtzzmevttheeyjqcldllxvjraeyflthntsmipaoyjixygbtbvbnnrmlwwkeikhnnmlfspjgmcxwbjyhomfjdcnogqjviggklplpznfwjydkxzjkoskvqvnxfzdrsmooyciwulvtlmvnjbbmffureoilszlonibbcwfsjzguxqrjwypwrskhrttvnqoqisdfuifqnabzbvyzgbxfvmcomneykfmycevnrcsyqclamfxskmsxreptpxqxqidvjbuduktnwwoztvkuebfdigmjqfuolqzvjincchlmbrxpqgguwuyhrdtwqkdlqidlxzqktgzktihvlwsbysjeykiwokyqaskjjngovbagspyspeghutyoeahhgynzsyaszlirmlekpboywqdliumihwnsnwjc"))
    print(t.counter)
