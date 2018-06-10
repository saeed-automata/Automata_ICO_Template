from boa.interop.Neo.Runtime import GetTrigger, CheckWitness
from boa.interop.Neo.TriggerType import Application, Verification
from My_ICO.my_nep5 import *
from My_ICO.my_CrowdSAle import *
from My_ICO.my_token import *
from My_ICO.My_txio import get_asset_attachments
from boa.interop.Neo.Storage import *


NEP5_METHODS = ['name', 'symbol', 'decimals', 'totalSupply', 'balanceOf', 'transfer']

ctx = GetContext()
# 0xe70e27cf705e33de9f42bd4b89781a6e71c6ed06
def Main(operation , args):

    trigger = GetTrigger()

    if trigger == Verification():

        if CheckWitness(TOKEN_OWNER):
            return True

        attachments = get_asset_attachments()
        return can_exchange(ctx, attachments, True)

    elif trigger == Application():

        for op in NEP5_METHODS:
            if operation == op:
                return handle_nep51(ctx, operation, args)

        if operation == 'deploy':
            return deploy()

        if operation == 'circulation':
            return get_circulation(ctx)

        if operation == 'mintTokens':
            return perform_exchange(ctx)

        if operation == 'crowdsale_register ':
            return kyc_register(ctx, args)

        if operation == 'crowdsale_status ':
            return kyc_status(ctx, args)

        if operation == 'crowdsale_avaiable ':
            return crowdsale_available_amount(ctx)

        if operation == 'get_attachements ':
            return get_asset_attachments()

        return 'Unknown operation'

    return False

def deploy():
    if not CheckWitness(TOKEN_OWNER):
        return False

    if not Get(ctx, 'initialized'):
        Put(ctx, 'initialized', 1)
        Put(ctx, TOKEN_OWNER, TOKEN_INITIAL_AMOUNT)
        return add_to_circulation(ctx, TOKEN_INITIAL_AMOUNT)

    return False
