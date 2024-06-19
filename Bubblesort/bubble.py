def bubble_sort(x: list[float]):
    for i in range (len(x)):
        swap: bool = False
        for j in range(len(x)-i-1):
            if x[j] > x[j+1]:
                temp: float = x[j+1]
                swap = True
                x[j+1] = x[j]
                x[j] = temp
        if not swap:
            break


def merge_sort(ls:list[int])->list[int]:

    if len(ls) == 1:

        return ls

    mid_point: int = len(ls) // 2

    list_1: list[int] = merge_sort(ls=ls[:mid_point])
    list_2: list[int] = merge_sort(ls=ls[mid_point:])

    return merge(list_1, list_2)


def merge(list_1: list[int], list_2: list[int]) -> list[int]:
    
    i,j = 0,0
    result: list[int] = [None for _ in range(len(list_1 + list_2))]
    #oppure -> result: list[int] = []

    for k in range(len(result)):

        if list_1[i] > list_2[j]:

            result[k] = list_2[j]
            j += 1
            
            if j == len(list_2):

                return result[:k+1] + list_1[i:]
        
        else:
            result[k] = list[i]
            i += 1

            if i == len(list_1):

                return result[:k+1] + list_1[j:]


    return result












if __name__ == "__main__":

    input_list: list[int] = [0,1,2,3,4,5,6,7]

    merge_sort(ls=input_list)


    
        
        

