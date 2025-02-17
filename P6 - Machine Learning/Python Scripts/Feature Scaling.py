""" quiz materials for feature scaling clustering """

### FYI, the most straightforward implementation might
### throw a divide-by-zero error, if the min and max
### values are the same
### but think about this for a second--that means that every
### data point has the same value for that feature!
### why would you rescale it?  Or even use it at all?
def featureScaling(arr):
    answer = []
    if max(arr) == min(arr):
        return 0.5
    else:
        for i in arr:
            value = (i - min(arr))/float((max(arr) - min(arr)))
            answer.append(value)
    return answer

# tests of your feature scaler--line below is input data
data = [115, 140, 175]
print featureScaling(data)

data = [3285, 200000, 34348384]
print "stock:", featureScaling(data)

data = [477, 1000000, 1111258]
print "salary:", featureScaling(data)