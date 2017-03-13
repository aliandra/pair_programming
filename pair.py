from __future__ import division


def j(a, b):
    # jaccard distance
    intersection = set(a).intersection(set(b))
    union = set(a).union(set(b))
    return len(intersection) / len(union)
