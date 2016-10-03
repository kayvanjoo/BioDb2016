
# coding: utf-8

# In[ ]:

#perm

def perm(seq):
    #print 'SEQ: ', seq
    if len(seq) <= 1:
        yield seq
    else:
        for p in perm(seq[1:]):
            for i in range(len(seq) + 1):
                yield p[:i] + seq[0:1] + p[i:]


def main():
    num = int(6)
    seq = []
    for i in range(num):
        seq.append(i + 1)

    all_seqs = []
    perms = list(perm(seq))
    for x in perms:
        if x not in all_seqs:
            all_seqs.append(x)

    print (len(all_seqs))
    for y in all_seqs:
        print (' '.join(map(str, y)))

if __name__ == "__main__":
    main()

