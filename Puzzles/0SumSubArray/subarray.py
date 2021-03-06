"""
Given an array of positive and negative numbers, find if there is a zero_sum_subseqeunce 
(of size at-least one) with 0 sum.

Hind:
If the sum of a sub-sequence is zero then this implies that cumulative sum until
the start of the sub-sequence and end of the sub-sequence is same. For example 
sum of sub-sequence 3 to 5 = 0

Index:  0  1  3   4  5  6
       [2, 2, 2, -3, 1, 6]
           ^  ^      ^
           |  <--0-->|           
        <->|         |
 total:    4         |
        <---(4 + 0)->|
                     4
                     
Algo: create a dict to store cumulative sum (from index 0 to index i) for each
      index. If cumulative sum is same for two index meas we have just cover
      a zero sum sub sequence array.
"""

def zero_sum_subseqeunce(array):
    if not array:
        return []
    if array[0] == 0:
        return [0]
    accumulate, total = {}, 0
    for index, number in enumerate(array):
        total += number
        if total in accumulate:
            start, end = accumulate[total] + 1, index
            return array[start: end + 1]
        accumulate[total] = index
    return []
    
def zero_sum_longest_subseqeunce(array):
    if not array:
        return []
    start, maxlen = 0, 0
    accumulate, total = {}, 0    
    for index, number in enumerate(array):
        total += number
        if total == 0:
            start, maxlen = 0, index
        elif total in accumulate:
            _start, _end = accumulate[total] + 1, index
            if maxlen < _end - _start + 1:
                start, maxlen = _start, _end - _start + 1
        else:
            accumulate[total] = index
    return array[start: start + maxlen]

if __name__ == '__main__':
    assert zero_sum_subseqeunce([0]) == [0]
    assert zero_sum_subseqeunce([]) == []
    assert zero_sum_subseqeunce([2, 2, 2, -3, 1, 6]) == [2, -3, 1]
    assert zero_sum_subseqeunce([4, 2, -3, 1, 6]) == [2, -3, 1]
    assert zero_sum_subseqeunce([4, 2, 0, 1, 6]) == [0]
    assert zero_sum_subseqeunce([-3, 2, 3, 1, 6]) == []
    assert zero_sum_longest_subseqeunce([15, -2, 2, -8, 1, 7, 10, 23]) ==\
                                            [-2, 2, -8, 1, 7]
    assert zero_sum_longest_subseqeunce([1, 2, 3]) == []
    assert zero_sum_longest_subseqeunce([1, 0, 3]) == [0]
    assert zero_sum_longest_subseqeunce([]) == []
    assert zero_sum_longest_subseqeunce([1, 2, 0, 3, 0, 0, -1, 2, -3, 2, 0, 3, 4, 2]) ==\
                                             [0, 0, -1, 2, -3, 2, 0]
