class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students)
        std_count = Counter(students)

        for sandwich in sandwiches:
            if not std_count[sandwich]:
                break
            res -= 1
            std_count[sandwich] -= 1

        return res