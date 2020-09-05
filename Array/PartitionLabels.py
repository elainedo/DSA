# A string S of lowercase English letters is given. We want to partition this string into 
# as many parts as possible so that each letter appears in at most one part, and return
# a list of integers representing the size of these parts.

def partition_labels(S):
    last_index_dict = {c: i for i, c in enumerate(S)}
    part_last_index = 0
    count = 0
    result = []
    for i, c in enumerate(S):
        part_last_index = max(part_last_index, last_index_dict[c])
        count += 1
        if i == part_last_index:
            result.append(count)
            count = 0
    return result

print(partition_labels("ababcbacadefegdehijhklij"))