"""Tiny set-associative LRU cache trace model (CPU-only).

Address units are cache lines, not bytes. No latency or hardware timing.
Run: python set_associativity.py
"""
from collections import deque


def simulate(trace, num_sets, ways):
    if num_sets <= 0 or ways <= 0:
        raise ValueError("num_sets and ways must be positive")
    sets = [deque() for _ in range(num_sets)]
    hits = 0
    for line in trace:
        if line < 0:
            raise ValueError("cache-line IDs must be nonnegative")
        bucket = sets[line % num_sets]
        if line in bucket:
            hits += 1
            bucket.remove(line)
        elif len(bucket) == ways:
            bucket.popleft()
        bucket.append(line)
    return hits, len(trace) - hits


def main():
    # Lines 0 and 2 collide when there are two sets.
    trace = [0, 2] * 8
    direct = simulate(trace, num_sets=2, ways=1)
    two_way = simulate(trace, num_sets=2, ways=2)
    print(f"Direct-mapped (2 sets x 1 way): hits={direct[0]}, misses={direct[1]}")
    print(f"Two-way (2 sets x 2 ways): hits={two_way[0]}, misses={two_way[1]}")
    assert direct == (0, 16)
    assert two_way == (14, 2)


if __name__ == "__main__":
    main()
