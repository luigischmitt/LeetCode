class Solution(object):
    def summaryRanges(self, nums):
        if nums == []:
            return nums

        i, j = 0, 1
        lista, resposta = [], []
        
        resposta.append(nums[i])
        while j < len(nums):
            if nums[j] == nums[i] + 1:
                resposta.append(nums[j])
                i = j
                j += 1
            else:
                lista.append(resposta)
                resposta = []
                resposta.append(nums[j])
                i = j
                j += 1

        if resposta != []:
            lista.append(resposta)

        array = []

        for lista in lista:
            if len(lista) > 1:
                lista = str(lista[0]) + "->" + str(lista[len(lista)-1])
            else:
                lista = str(lista[0])
            array.append(lista)

        return array
        