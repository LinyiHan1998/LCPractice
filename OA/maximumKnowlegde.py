import re

from sortedcontainers import SortedDict, SortedSet


def maximum_knowledge(s, e, a, d, k):
    n = len(s)
    all_events = SortedDict()

    for i in range(n):
        if s[i] not in all_events:
            all_events[s[i]] = []
        all_events[s[i]].append(i + 1)

        if e[i] + 1 not in all_events:
            all_events[e[i] + 1] = []
        all_events[e[i] + 1].append(-i - 1)

    # Add this key if not exist.
    if d + 1 not in all_events:
        all_events[d + 1] = []

    selected = SortedSet()
    unselected = SortedSet()
    sum_val = 0
    r = 0

    for time, events in all_events.items():
        r = max(r, sum_val)

        for x in events:
            if x >= 0:
                unselected.add((-a[x - 1], x))

                if len(selected) < k or selected[0][0] < -unselected[0][0]:
                    selected.add((-unselected[0][0], unselected[0][1]))
                    sum_val -= unselected[0][0]
                    unselected.remove(unselected[0])

                    if len(selected) > k:
                        unselected.add((-selected[0][0], selected[0][1]))
                        sum_val -= selected[0][0]
                        selected.remove(selected[0])
            else:
                x = -x
                unselected.discard((-a[x - 1], x))

                if (-a[x - 1], x) in selected:
                    sum_val -= a[x - 1]
                    selected.discard((-a[x - 1], x))

                    if unselected:
                        selected.add((-unselected[0][0], unselected[0][1]))
                        sum_val -= unselected[0][0]
                        unselected.remove(unselected[0])

        if time == d + 1:
            break

    return r