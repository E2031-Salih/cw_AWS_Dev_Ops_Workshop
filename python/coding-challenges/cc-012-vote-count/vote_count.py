def majority_vote(vote_list):
    result_dict = {}
    for i in set(vote_list):
        result_dict[i] = vote_list.count(i)
    return max(result_dict, key = lambda k : result_dict[k])

print(majority_vote(["A", "A", "A", "B", "C", "A", "C", "C", "C", "C"]))