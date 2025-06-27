#max hillyer 4/28/25

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        strnum = ""
        newlist = []
        for i in digits:
            strnum += str(i)
        strnum = int(strnum)
        strnum += 1
        for i in str(strnum):
            newlist.append(int(i))
        return newlist
