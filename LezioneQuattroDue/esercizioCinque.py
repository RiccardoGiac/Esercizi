"""
Data una lista di numeri interi, spostare gli zeri alla fine di questa lista
mantenendo l'ordine originale dei numeri che non sono gli zeri

Esempio:
nums = [0,1,0,3,12] -> modificare lista in [1,3,12,0,0]
"""

def move_zeroes(nums:list[int]):
    for i in range(len(nums)):
        if nums[i] == 0:
            nums.append(nums.pop(i))
    print(nums)

list: list = [0,5,4,2,0,1,2]
move_zeroes(list)


