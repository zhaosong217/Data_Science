class Solution:
    def areAlmostEqual(self, s1, s2):
        i, j, cnt = -1, -1, 0
        for k in range(len(s1)):
            if s1[k] != s2[k]:
                cnt += 1
                if i == -1:
                    i = k
                elif j == -1:
                    j = k
        if cnt == 0:
            return True
        elif cnt == 2 and s1[i] == s2[j] and s1[j] == s2[i]:
            return True
        return False
    
if __name__ == '__main__':
    s1 = "siyolsdcjthwsiplccjbuceoxmpjgrauocx"
    s2 = "siyolsdcjthwsiplccpbuceoxmjjgrauocx"
    s = Solution()
    print(s.areAlmostEqual(s1, s2))