# KMP is a search algorithm 


def _compute_LPS_array(pat, M, lps):
    len_longest_prefix =0 
    i=1
    while i< M:
        if pat[i] == pat[len_longest_prefix]:
            len_longest_prefix+=1
            lps[i]=len_longest_prefix
            i+=1
        else:
            if len_longest_prefix!=0:
                len_longest_prefix = lps[len_longest_prefix-1]
            else:
                lps[i] = 0
                i+=1

def KMP_search(txt, pat):
    M = len(pat)
    N = len(txt)

    
    lps = [0] * M # that will hold the longest prefix suffix
    j = 0 # index for pat[]

    _compute_LPS_array(pat, M, lps)

    results=[]
    i=0
    while i < N:
        if pat[j] == txt[i]:
            i+=1
            j+=1
        if j ==M:
            results.append(i-j)
            print("Found patter at index"+str(i-j))
            j = lps[j-1]
        # mismatch after j matches
        elif i <N and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters, they will match anyway
            if j != 0:
                j = lps[j-1]
            else:
                i+=1
    return results

txt = "asdasdasdasdasdasdasdasdasd"
pat = "dasd"

print(KMP_search(txt, pat))