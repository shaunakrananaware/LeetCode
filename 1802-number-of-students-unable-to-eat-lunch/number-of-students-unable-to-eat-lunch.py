class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        sandwich_ptr = 0
        while sandwich_ptr < len(sandwiches) and sandwiches[sandwich_ptr] in students:
            for idx in range(len(students)):
                if students[idx] != sandwiches[sandwich_ptr]:
                    continue
                students.pop(idx)
                sandwich_ptr += 1
                break
        return len(sandwiches) - sandwich_ptr