class Solution(object):
    def isAnagram(self, s, t):
        s_dict = Counter(s)
        t_dict = Counter(t)

        return s_dict == t_dict
        