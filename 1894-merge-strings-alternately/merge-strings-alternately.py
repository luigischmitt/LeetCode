class Solution(object):
    def mergeAlternately(self, word1, word2):
        word1 = list(word1)
        word2 = list(word2)

        resposta = []

        tamanho1 = len(word1)
        tamanho2 = len(word2)
        
        if tamanho1 >= tamanho2:
            maior = word1
            menor = word2
        else:
            maior = word2
            menor = word1

        for i in range(len(maior)):
            if maior == word2:
                if i <= len(menor)-1:
                    resposta.append(word1[i])
                resposta.append(word2[i])
            else:    
                resposta.append(maior[i])
                if i <= len(menor)-1:
                    resposta.append(menor[i])

        return "".join(resposta)
        