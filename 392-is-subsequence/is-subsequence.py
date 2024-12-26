class Solution(object):
    def isSubsequence(self, s, t):
        resposta = []
        s = list(s)
        t = list(t)

        i, j = 0, 0 

        while j < len(t):  
            if i < len(s) and s[i] == t[j]:
                resposta.append(s[i])
                i += 1
            j += 1

        return resposta == s
