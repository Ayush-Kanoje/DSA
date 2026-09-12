class Solution:
    def mergeTwoLists(self, list1, list2: list[int]):
        list1.extend(list2)

        final_list = sorted(list1)

        return final_list

