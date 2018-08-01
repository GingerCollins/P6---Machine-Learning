predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]
print "predictions:", len(predictions)
print "true_labels:", len(true_labels)

# true positives, true negatives, false positives, false negatives
true_positives = 0
true_negatives = 0
false_positives = 0
false_negatives = 0
for i in range(len(predictions)):
    if predictions[i] == true_labels[i]:
        if predictions[i] > 0:
            true_positives += 1
        else:
            true_negatives += 1
    else:
        if predictions[i] > 0:
            false_positives += 1
        else:
            false_negatives += 1


print "true positives:", true_positives
print "true negatives:", true_negatives
print "false positives:", false_positives
print "false negatives:", false_negatives


precision = true_positives/float(true_positives + false_positives)
print "precision:", precision
recall = true_positives/float(true_positives + false_negatives)
print "recall:", recall