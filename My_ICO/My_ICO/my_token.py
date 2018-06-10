from boa.interop.Neo.Storage import *
# from boa.interop.Neo.Runtime import CheckWitness


TOKEN_NAME = 'AUTOMATON'

TOKEN_SYMBOL = 'AUTO'

TOKEN_DECIMALS = 8

TOKEN_OWNER = b'#\xba\'\x03\xc52c\xe8\xd6\xe5"\xdc2 39\xdc\xd8\xee\xe9'

TOKEN_CIRC_KEY = b'in_circulation'

TOKEN_TOTAL_SUPPLY = 10000000 * 100000000

TOKEN_INITIAL_AMOUNT = 2500000 * 100000000

TOKENS_PER_NEO = 40 * 100000000

TOKENS_PER_GAS = 20 * 100000000

MAX_EXCHANGE_LIMITED_ROUND = 500 * 40 * 100000000

BLOCK_SALE_START = 1

LIMITED_ROUND_END = 1 + 10000

KYC_KEY = b'kyc_ok'

LIMITED_ROUND_KEY = b'r1'



def get_circulation(ctx):
    return Get(ctx, TOKEN_CIRC_KEY)

def crowdsale_available_amount(ctx):
    amount_in_circulation = Get(ctx, TOKEN_CIRC_KEY)
    return TOKEN_TOTAL_SUPPLY - amount_in_circulation

def add_to_circulation(ctx, amount):
    amount_in_circulation = Get(ctx, TOKEN_CIRC_KEY)
    amount_in_circulation += amount
    Put(ctx, amount_in_circulation)
    return True
