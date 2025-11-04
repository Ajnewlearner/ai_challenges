class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows
        currentRow = 0
        down = False

        for char in s:
            rows[currentRow] += char
            if currentRow == 0 or currentRow == numRows - 1:
                down = not down
            if down:
                currentRow += 1         
            else:
                currentRow -= 1    
        return ''.join(rows)        

s = Solution()
print(s.convert('paypal',3))    
# p  a
# a p l
# y