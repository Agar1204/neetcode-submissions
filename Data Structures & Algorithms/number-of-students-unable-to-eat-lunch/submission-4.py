class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        studentSum = sum(students)
        studentPreferences = [len(students) - studentSum, studentSum]

        for i in range(len(sandwiches)):
            if studentPreferences[sandwiches[i]] == 0:
                return len(sandwiches) - i
            studentPreferences[sandwiches[i]] -= 1
        return 0
        


            

        