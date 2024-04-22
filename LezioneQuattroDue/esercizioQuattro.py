"""
Data una lista nums di n elementi, restituire l'elemento che compare più di n/2 volte.

Esempio:
nums = [3,2,3 -> restituire 3

Esempio 2:
nums = [2,2,1,1,1,2] -> restituire None
"""

def majority_element(nums: list[int]) -> int:
    
    max: int = 0
    conta: int = 0
    nummax: int = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] == nums[j]:
             conta += 1
            if conta > max:
                max = conta
                nummax = nums[i]

        conta = 0
    if max > len(nums)//2:
        return nummax
    
lista: list = [2,4,6,6,5,6]
print(majority_element(lista))

