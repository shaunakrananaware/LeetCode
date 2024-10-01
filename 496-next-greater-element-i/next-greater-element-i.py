class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []

        for idx in range(len(nums1)):
            for jdx in range(len(nums2)):
                if nums1[idx] != nums2[jdx]: continue 

                for kdx in range(jdx, len(nums2)):
                    if nums2[jdx] >= nums2[kdx]:
                        if kdx == len(nums2)-1:
                            output.append(-1)
                        continue
                    
                    output.append(nums2[kdx])
                    break

        return output