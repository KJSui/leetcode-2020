class Solution:
    def seat(self):
        if not self.students:
            student = 0

        else:
            dist,student = students[0], 0
            for i, s in enumerate(self.students):
                if i:
                    prev = self.students[i]
                    d = (s-prev)//2
                    if d > dist:
                        dist = d
                        student = prev + d
            d = self.N -1 - self.students[-1]
            if d > dist:
                student = self.N-1

        bisect.insert(self.students, student)
        return student

        


