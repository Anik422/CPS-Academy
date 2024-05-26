class Solution:
    def compressedString(self, word: str) -> str:
        ans = ''
        con = 1
        for i in range(1, len(word)):
            if word[i-1] == word[i]:
                con += 1
            else:
                ans += f'{con}' + word[i-1]
                con = 1
        return ans

obj = Solution()
print(obj.compressedString('aaabbcc'))  # 3a2b2c