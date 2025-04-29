import math

def minimax(current, node, maxTHTurn, scores, target, path=[]):
    if current == target:
        return scores[node], path
    if maxTHTurn:
        l_score, l_path = minimax(current+1, node*2, False, scores, target, path+[node*2])
        r_score, r_path = minimax(current+1, node*2+1, False, scores, target, path+[node*2+1])
        if l_score > r_score:
            return l_score, l_path
        else:
            return r_score, r_path
    else: #min turn
        l_score, l_path = minimax(current+1, node*2, True, scores, target, path+[node*2])
        r_score, r_path = minimax(current+1, node*2+1, True, scores, target, path+[node*2+1])
        if l_score < r_score:
            return l_score, l_path
        else:
            return r_score, r_path
scores = [12, 3, 10, 13, 1, 8, 6,5, 7, 4, 9, 12, 11, 14, 15, 0]
treeDepth = int(math.log(len(scores), 2))
optimal_value, path = minimax(0, 0, True, scores, treeDepth)
print("\nOptimal value:", optimal_value)
print("Path:", path)
