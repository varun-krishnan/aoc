def calculate_score(input_tuple):
    pair_score = {'X':{'A':3,'B':1,'C':2}, 'Y':{'A':4,'B':5,'C':6}, 'Z':{'A':8,'B':9,'C':7}}
    p1, p2 = input_tuple
    score = pair_score[p2][p1]
    return score

if __name__ == "__main__":
   fp = open("input2", 'r')
   input = fp.read().split('\n')
   input_tuples = [x.split(' ') for x in input]
   input_tuples = input_tuples[:-1]
   scores = [calculate_score(input_tuple) for input_tuple in input_tuples]
   net_score = sum(scores)
   print(net_score)

   
