class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        my_hash  = {}
        ans = 0
        lenth = len(s)
        i=0 
        j=0
        while j<lenth:
            char = s[j]
            if char in my_hash:
                if my_hash[char]>i:
                    i =  my_hash[char]
            if ans<(j-i+1):
                ans = (j - i + 1)
            j = j + 1
            my_hash[char] = j
        return ans

def stringToString(input):
    import json

    return json.loads(input)

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            s = stringToString(line);
            
            ret = Solution().lengthOfLongestSubstring(s)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
