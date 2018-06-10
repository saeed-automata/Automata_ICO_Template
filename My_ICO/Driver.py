from boa.interop.Neo.Runtime import GetTrigger, CheckWitness
from boa.interop.Neo.TriggerType import Application, Verification
from My_ICO.my_nep5 import *
from My_ICO.my_CrowdSAle import *
from My_ICO.my_token import *
from My_ICO.My_txio import get_asset_attachments
from boa.interop.Neo.Storage import *


NEP5_METHODS = ['name', 'symbol', 'decimals', 'totalSupply', 'balanceOf', 'transfer']

ctx = GetContext()
# 0xd390a99b339669dada5e25a112a2d929ee3bcc05
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
            deploy()

        if operation == 'circulation':
            get_circulation(ctx)

        if operation == 'mintTokens':
            pass

        if operation == 'crowdsale_register ':
            kyc_register(ctx, args)

        if operation == 'crowdsale_status ':
            kyc_status(ctx, args)

        if operation == 'crowdsale_avaiable ':
            crowdsale_available_amount(ctx)

        if operation == 'get_attachements ':
            get_asset_attachments()

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
