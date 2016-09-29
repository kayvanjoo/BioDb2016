from __future__ import division
from sys import argv


def calcaulate_prob(k, m, n):
    t = k + m + n  # Total population
    prob = 1
    p_homozygous_rec_x2 = (n / t) * ((n - 1) / (t - 1))
    prob -= p_homozygous_rec_x2
    p_homozygous = (n / t)
    p_heterozygous_rec = (m / (t - 1)) * 0.5
    p_homozygous_heterozygous_rec = (p_homozygous * p_heterozygous_rec) * 2
    prob -= p_homozygous_heterozygous_rec
    p_heterozygous_rec_x2 = (m / t) * ((m - 1) / (t - 1)) * .25
    prob -= p_heterozygous_rec_x2

    return prob


def main():

    prob = calcaulate_prob(18, 27, 21)
    print(prob)



if __name__ == "__main__":
    main()