import nltk
from nltk import word_tokenize
class IOB2Annotator:
    def __init__(self,X,y):
        self.X = X
        self.y = y
        self.result = []
    
    def annotate(self):
        '''
        This funciton helps us to tag the sentence using IOB2 tagging structure.
        '''
        for i,j in zip(self.X,self.y):
            temp =[]
            if len(j.strip().split()) > 1:
                for k in nltk.pos_tag(word_tokenize(i)):
                    if k[0].lower() == j.strip().split()[0].lower():
                        temp.append(k + ('B-Event',))
                    elif k[0].lower() in j.strip().lower().split()[1:]:
                        temp.append(k + ('I-Event',))
                    else:
                        temp.append(k + ('O',))

            else:
                for k in nltk.pos_tag(word_tokenize(i)):
                    if k[0].lower() == j.lower():
                        temp.append(k + ('B-Event',))
                    else:
                        temp.append(k + ('O',))
            self.result.append(temp)
        return self.result

def main():
    X = ['He was having heart attack','He was hospitalized']
    y = ['Heart Attack','hospitalized']
    result = IOB2Annotator(X,y).annotate()
    print(result)

if __name__ == "__main__":
    main()
