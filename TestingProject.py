#https://www.youtube.com/watch?v=6SVT4DipubQ

def minimum_index(seq):
    if len(seq) == 0:
        raise ValueError("Cannot get the minimym value index from an empty seq")
    min_idx = 0
    for i in range(1, len(seq)):
        if a[i] < a[min_idx]:
            min_idx = i
    return min_idx

#return empty array 
class TestDataEmptyArray(object):
    @staticmethod
    def get_array():
        return []

class TestDataUniqueValues(object):
    @staticmethod
    def get_array():
        return [3,4,5]

    @staticmethod
    def get_expected_result():
        return 0

class TestDataExactlyTwoDifferentMinimums(object):

    @staticmethod
    def get_array():
        a = [3, 1, 1]
        return a

    @staticmethod
    def get_expected_result():
        return 1