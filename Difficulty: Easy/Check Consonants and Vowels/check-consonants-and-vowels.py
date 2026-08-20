class Solution:
    def checkString(self, s):
        
        # Initializing vowel count
        # and consonant count to 0
        vowel_count = 0
        consonant_count = 0
        vowel = "aeiou"
        for ch in s:
            if ch in vowel:
                vowel_count += 1
            else:
                consonant_count += 1
        # code here
        if vowel_count > consonant_count:
            print("Yes")
        elif vowel_count < consonant_count:
            print("No")
        else:
            print("Same")