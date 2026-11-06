import pandas as pd
import numpy as np


LOOKUP_COST_PER_CASE = 7.60       # EUR the bank pays per research, regardless of outcome
CLIENT_FEE_ON_SUCCESS = 25.00     # EUR charged to the client, only if a new address is found

ELIGIBLE_RATE = 0.80              # share of incoming letters that pass Girokonto/volljährig/address checks
ERROR_RATE_BEFORE = 0.08          # old process: chance a case's eligibility was mishandled
ERROR_RATE_AFTER = 0.02           # new process: same mistake, much rarer with the shared database
RESPONSE_RATE_AFTER = 0.40        # new process only: chance a client responds to the free message
SYNC_FAILURE_RATE_BEFORE = 0.10   # old process only: chance a Lookup run was redundant (client already messaged in)

rng = np.random.default_rng(42)

def lookup_outcome():
     roll = rng.random()
     if roll < 0.15:
        return "new_address"
     elif roll < 0.60:
        return "same_address"
     elif roll < 0.90:
        return "not_found"
     else:
        return "moved_abroad"
     

def process_case_before():
    eligible = rng.random() < ELIGIBLE_RATE
    mistake = rng.random() < ERROR_RATE_BEFORE

    if mistake:
        effective_eligible = not eligible
    else:
        effective_eligible = eligible

    if effective_eligible:
        cost = LOOKUP_COST_PER_CASE
        outcome = lookup_outcome()
        redundant = rng.random() < SYNC_FAILURE_RATE_BEFORE

        if outcome == "new_address":
            fee = CLIENT_FEE_ON_SUCCESS
        else:
            fee = 0
    else:
        cost = 0
        outcome = "not_eligible"
        fee = 0
        redundant = False

    return {
        "eligible": effective_eligible,
        "outcome": outcome,
        "cost": cost,
        "fee": fee,
        "redundant": redundant,
    }

def process_case_after():
    eligible = rng.random() < ELIGIBLE_RATE
    mistake = rng.random() < ERROR_RATE_AFTER

    if mistake:
        effective_eligible = not eligible
    else:
        effective_eligible = eligible

    if effective_eligible:
        responded = rng.random() < RESPONSE_RATE_AFTER

        if responded:
            cost = 0
            fee = 0
            outcome = "resolved_free"
        else:
            cost = LOOKUP_COST_PER_CASE
            outcome = lookup_outcome()
            if outcome == "new_address":
                fee = CLIENT_FEE_ON_SUCCESS
            else:
                fee = 0
    else:
        cost = 0
        fee = 0
        outcome = "not_eligible"

    return {
        "eligible": effective_eligible,
        "outcome": outcome,
        "cost": cost,
        "fee": fee,
    }

def run_month(process_function, n_cases):
    results = []

    for i in range(n_cases):
        case = process_function()
        results.append(case)

    return results

cases = run_month(process_case_after, 1000)
print(len(cases))
print(cases[0])



     

