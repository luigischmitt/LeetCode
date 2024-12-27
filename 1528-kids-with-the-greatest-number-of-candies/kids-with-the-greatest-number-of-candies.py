class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maior = max(candies)
        resposta = []
        for candy in candies:
            if candy + extraCandies >= maior:
                resposta.append(True)
            else:
                resposta.append(False)

        return resposta
        