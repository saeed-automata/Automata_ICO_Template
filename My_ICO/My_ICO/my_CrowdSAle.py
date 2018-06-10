from boa.builtins import concat
from My_ICO.my_token import *
from My_ICO.My_txio import get_asset_attachments
from boa.interop.Neo.Runtime import CheckWitness
from boa.interop.Neo.Action import RegisterAction
from boa.interop.Neo.Blockchain import GetHeight

OnKYCRegister = RegisterAction('kyc_registration', 'address')
OnTransfer = RegisterAction('transfer', 'addr_from', 'addr_to', 'amount')
OnRefund = RegisterAction('refund', 'addr_to', 'amount')


def kyc_register(ctx, args):
    if CheckWitness(TOKEN_OWNER):

        for address in args:
            if len(address) == 20: #WHY THIS
                key = concat(KYC_KEY, address)
                Put(ctx, key, True)
                return True
    return False

def kyc_status(ctx, args):

    if len(args) > 0:
        key = concat(KYC_KEY, args[0])
        return Get(ctx, key)
    return False

def perform_exchange(ctx):
    attachments = get_asset_attachments()

    exchange_possible = can_exchange(ctx, attachments, False)

    if not exchange_possible:
        if attachments[2] > 0:
            OnRefund(attachments[1], attachments[2])
        return False

    balance_of_sender = Get(ctx, attachments[1])
    balance_of_sender += attachments[2] * TOKENS_PER_NEO / 100000000

    Put(ctx, attachments[1],balance_of_sender)

    OnTransfer(attachments[0], attachments[1], balance_of_sender)

    return True

def can_exchange(ctx, attachments, verify_only):
    if attachments[2] == 0:
        return False

    if not get_kyc_status(ctx, attachments[1]):
        return False

    amount = attachments[2] * TOKENS_PER_NEO / 100000000

    return calculate_can_exchange(ctx, amount, attachments[1], verify_only)

def get_kyc_status(ctx, address):
    kyc_storage_key = concat(KYC_KEY, address)
    return Get(ctx, kyc_storage_key)

def calculate_can_exchange(ctx, amount, address, verify_only):
    height = GetHeight()

    if height < BLOCK_SALE_START:
        return False

    new_amount = get_circulation(ctx) + amount

    if new_amount > TOKEN_TOTAL_SUPPLY:
        return False

    if height > LIMITED_ROUND_END:
        return True

    if amount <= MAX_EXCHANGE_LIMITED_ROUND:
        key = concat(LIMITED_ROUND_KEY, address)
        participation_check = Get(ctx, key)

        if not participation_check:
            if not verify_only:
                Put(ctx, key, True)
            return True

        return False

    return False