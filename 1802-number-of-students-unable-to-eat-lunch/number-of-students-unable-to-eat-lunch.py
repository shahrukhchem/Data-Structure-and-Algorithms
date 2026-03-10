from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        studentque=deque(students)
        sandichesstack=deque(sandwiches)
        def simulateonerun(student,sandiches):
            n=len(sandiches)
            count = 0

            while student and count<len(student):
                    if student[0]==sandiches[0]:
                        student.popleft()
                        sandiches.popleft()
                        count=0
                    elif  student[0]!=sandiches[0]:
                        x=student.popleft()
                        student.append(x)
                        count+=1
            return len(student)
        ac=simulateonerun( studentque,sandichesstack)
        return ac