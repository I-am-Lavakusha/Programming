def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        no=len(nums1)
        for i in range(n-1, n-m, -1):
            if nums1[i]==0:
                nums1.remove(nums1[i])

        nums1.extend(nums2)
        nums1.sort()
