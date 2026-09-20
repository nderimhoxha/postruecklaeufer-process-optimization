import pandas as pd
import numpy as np


LOOKUP_COST_PER_CASE = 7.60       # EUR the bank pays per research, regardless of outcome
CLIENT_FEE_ON_SUCCESS = 25.00     # EUR charged to the client, only if a new address is found

ELIGIBLE_RATE = 0.80              # share of incoming letters that pass Girokonto/volljährig/address checks
ERROR_RATE_BEFORE = 0.08          # old process: chance a case's eligibility was mishandled
ERROR_RATE_AFTER = 0.02           # new process: same mistake, much rarer with the shared database
RESPONSE_RATE_AFTER = 0.40        # new process only: chance a client responds to the free message
SYNC_FAILURE_RATE_BEFORE = 0.10   # old process only: chance a ZEMA run was redundant (client already messaged in)

rng = np.random.default_rng(42)
