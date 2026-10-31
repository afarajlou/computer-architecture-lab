"""Fully associative LRU cache trace model; not real hardware measurement."""
from collections import OrderedDict


def simulate(trace, capacity):
    if not isinstance(capacity, int) or capacity <= 0:
        raise ValueError("capacity must be a positive integer")
    cache = OrderedDict()
    hits = 0
    for address in trace:
        if address in cache:
            hits += 1
            cache.move_to_end(address)
        else:
            if len(cache) == capacity:
                cache.popitem(last=False)
            cache[address] = None
    return hits, len(trace) - hits


def main():
    for name, trace in (
        ("working set of 4, repeated", list(range(4)) * 4),
        ("scan of 8, repeated", list(range(8)) * 2),
    ):
        hits, misses = simulate(trace, capacity=4)
        print(f"{name}: hits={hits}, misses={misses}, hit rate={hits / len(trace):.1%}")
    print("Simplified trace model; no block size, prefetching, or latency.")


if __name__ == "__main__":
    main()
