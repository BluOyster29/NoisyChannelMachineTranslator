from tqdm import tqdm
from nltk.util import bigrams,trigrams

class LanguageModel:

    def __init__(self, language_data):
        self.language_data = language_data
        self.unigram_counts, self.bigram_counts, self.trigram_counts ,self.bis, self.tris = self.build_model()
        self.bi_mle = self.bigram_mle()
        self.tri_mmle = self.trigram_mle()

    def build_model(self):

        unigram_counts, bigram_counts, trigram_counts = {},{},{}
        bis, tris = [], []

        print('Counting Ngrams')
        for i in tqdm(self.language_data):

         
            tokens = i
            tokens.insert(0, 0)
            tokens.append(1)
            tokens.insert(0, 0)
            tokens.append(1)
         
            '''
            tokens = i
            tokens.insert(0, '<s>')
            tokens.append('<e>')
            tokens.insert(0, '<s>')
            tokens.append('<e>')
            '''
            
            bis.append(list(bigrams(tokens)))
            tris.append(list(trigrams(tokens)))

            for unigram in tokens:
                unigram_counts = self.update_dic(unigram,unigram_counts)

            for bi in bigrams(tokens):
                bigram_counts = self.update_dic(bi,bigram_counts)

            for tri in trigrams(tokens):
                trigram_counts = self.update_dic(tri,trigram_counts)

        return unigram_counts, bigram_counts, trigram_counts, bis, tris

    def bigram_mle(self):

        bigram_mle = {}
        print('Calculating Bigram MLE')
        for sents in tqdm(self.bis):

            for bi in sents:

                wn_1_wn = self.bigram_counts[bi]
                wn = self.unigram_counts[bi[0]]

                bigram_prb = self.mle(wn_1_wn, wn)

                bigram_mle[bi] = bigram_prb

        return bigram_mle

    def trigram_mle(self):
        trigram_mle = {}
        print('Calculating Triigram MLE')
        for sents in tqdm(self.tris):

            for tri in sents:

                wn_1_wn = self.trigram_counts[tri]
                wn = self.bigram_counts[tri[0:2]]

                trigram_prb = self.mle(wn_1_wn, wn)

                trigram_mle[tri] = trigram_prb

        return trigram_mle

    def most_likely(self, ngram, n, start_word):

        if start_word == True:
            startword = ngram[1:3]
        else:
            startword=ngram

        choices = {}
        for tri, probs in self.tri_mmle.items():


            if tri[0:2] == startword:

                choices[tri] = probs


        try:
            max_choice = sorted(choices.items(), key=lambda x:-x[1])[:n]
            return max_choice
        except:
            None

    def update_dic(self, x, dic):

        if x not in dic:
            dic[x] = 1
        else:
            dic[x] += 1

        return dic

    def mle(self, count_wn_1_wn, count_wn_1):

        return count_wn_1_wn /count_wn_1

    def gen_tweet(self, start_gram,n):
    
    
        possible_starts = self.most_likely(start_gram,n, True)
        tweets = []
        for i in possible_starts:
        
            start_gram = i[0]

            sent = [start_gram[0],start_gram[1]]
            next_word = start_gram


            for x in range(0,20):

                try:
                    next_word=self.most_likely(next_word, 1, True)[0][0]
                    
                    if type(next_word[1]) == int:
                        continue
                    
                    elif next_word == 'amp':
                        next_word = 'and'
                    else:
                        sent.append(next_word[1])
                except:
                    continue

            tweets.append(sent)
        return tweets
    
            
           
