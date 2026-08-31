class Solution:
    def getTriangle(self, arr):
        triangle = []
        row = arr[:]
        triangle.append(row)
        while len(row) > 1:
            new_row = []
            for i in range(len(row) - 1):
                new_row.append(row[i] + row[i + 1])
            row = new_row
            triangle.append(row)
        triangle.reverse()
        result = []
        for row in triangle:
            result.extend(row)
        return result
