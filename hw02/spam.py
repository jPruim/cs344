"""
Creating a spam filter in python
For CS344
At Calvin University.
Jason Pruim
Spring 2020
"""

spam_corpus = [["I", "am", "spam", "spam", "I", "am"], ["I", "do", "not", "like", "that", "spamiam"]]
ham_corpus = [["do", "i", "like", "green", "eggs", "and", "ham"], ["i", "do"]]
good = {}
bad = {}

def computeWordworth(word):
    num_bad = 2
    num_good = 2
    if word in good:
        g = 2 * good[word]    #is there a reason for the 2* in the algorithm?
    else:
        g = 0
    if word in bad:
        b = bad[word]
    else:
        b = 0
    if (b+g)>1:
        return max(.01, min(.99, min(1, b/num_bad) / (min(1, g/num_good) + min( 1, b/num_bad)) ))
    return 0

if __name__ == "__main__":
    for email in spam_corpus:
        for word in email:
            if word in bad:
                bad[word] +=1
            else:
                bad[word] = 1

    for email in ham_corpus:
        for word in email:
            if word in good:
                good[word] +=1
            else:
                good[word] = 1
    email_list = [["I", "am", "spam", "spam", "I", "am"], ["I", "do", "not", "like", "that", "spamiam"],["do", "i", "like", "green", "eggs", "and", "ham"], ["i", "do"]]
    print("Word ---- Probability of spam being email")
    for email in email_list:
        for word in email:
            print(word + "----" + str(computeWordworth(word)))
