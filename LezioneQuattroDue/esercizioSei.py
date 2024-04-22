"""
Fare intersezione di due liste senza utilizzare i set
"""
def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    nums1:set[int] = set(nums1)
    nums2:set[int] = set(nums2)
    elementiInComune: list[int] = []
    for num in nums1:
        if num in nums2:
            elementiInComune.append(num)
    return elementiInComune
            
            
