
def find_first_bad(n, start, end):
    if end<start:
        return -1
    else:
        
        mid = (end+start)/2
        # print 'start', start, 'mid', mid, 'end', end
        if isBadVersion(mid):
            if mid-1 >=0:
                if isBadVersion(mid-1):
                    return find_first_bad(n, start, mid-1)
                else:
                    return mid
            else:
                return mid
        else:
            return find_first_bad(n, mid+1, end)

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return find_first_bad(n, 1, n)
        