def calculate_score(input_tuple):
    score_sheet = {'X':1, 'Y':2, 'Z':3}
    pair_score = {'X':{'A':3,'B':0,'C':6}, 'Y':{'A':6,'B':3,'C':0}, 'Z':{'A':0,'B':6,'C':3}}
    p1, p2 = input_tuple
    score = pair_score[p2][p1] + score_sheet[p2]
    return score

if __name__ == "__main__":
   fp = open("input2", 'r')
   input = fp.read().split('\n')
   input_tuples = [x.split(' ') for x in input]
   input_tuples = input_tuples[:-1]
   for input_tuple in input_tuples:
       print(input_tuple) 
   scores = [calculate_score(input_tuple) for input_tuple in input_tuples]
   net_score = sum(scores)
   print(net_score)

   
