"""Exact subset recourse and primary-failure hardening on small controller sets."""
from itertools import combinations
import numpy as np
from model import closure, denied_edges


def subset_deliveries(lp, nominal):
    """Enumerate every primary-failure set, caching identical dispatch denials."""
    U = lp.network['controllers']; values = np.empty(2 ** U)
    cache = {tuple(): nominal.delivery}; rows = []
    for mask in range(2 ** U):
        failures = [u for u in range(U) if mask & (1 << u)]
        lost = tuple(sorted(denied_edges(lp.network, failures)))
        if lost not in cache:
            cache[lost] = lp.solve(failures).delivery
        values[mask] = cache[lost]
        closed = closure(lp.network, failures)
        rows.append(dict(mask=mask, closure_mask=sum(1 << u for u in closed),
                         delivery=values[mask], AVI=(nominal.delivery - values[mask]) / nominal.delivery))
    return values, rows


def expected_service(deliveries, controllers, protected, failure_probability):
    """Protect against primary failure only; prerequisite-induced denial still applies."""
    protected_mask = sum(1 << u for u in protected)
    exposed = controllers - len(protected); total = 0.
    for mask, delivery in enumerate(deliveries):
        if mask & protected_mask:
            continue
        count = mask.bit_count()
        probability = failure_probability ** count * (1 - failure_probability) ** (exposed - count)
        total += probability * delivery
    return float(total)


def hardening_comparison(deliveries, controllers, probability=.2, budget=2):
    """Compare actual greedy marginal service benefit against every feasible set."""
    empty = expected_service(deliveries, controllers, (), probability)
    candidates = list(combinations(range(controllers), budget))
    benefits = {c: expected_service(deliveries, controllers, c, probability) - empty for c in candidates}
    best = max(benefits, key=lambda c: (benefits[c], tuple(-u for u in c)))
    greedy = []
    for _ in range(budget):
        greedy.append(max((u for u in range(controllers) if u not in greedy),
                          key=lambda u: (expected_service(deliveries, controllers, (*greedy, u), probability), -u)))
    greedy = tuple(sorted(greedy))
    gain = benefits[greedy]; optimum = benefits[best]
    return dict(probability=probability, budget=budget, unprotected_expected_service=empty,
                greedy_set=' '.join(map(str, greedy)), optimal_set=' '.join(map(str, best)),
                greedy_gain=gain, optimal_gain=optimum,
                gain_ratio=gain / optimum if optimum > 1e-10 else 1.,
                greedy_optimal=int(abs(gain - optimum) <= 1e-8))
