from services.business.transaction_business import transfer_internal as svc_internal, transfer_interbank as svc_interbank, list_transactions_for_customer

def transfer_internal(user_id, from_acc, to_acc, amount, desc):
    return svc_internal(user_id, from_acc, to_acc, amount, desc)

def transfer_interbank(user_id, from_acc, to_acc, bank_code, amount, desc):
    return svc_interbank(user_id, from_acc, to_acc, bank_code, amount, desc)

def get_transactions_by_customer(user_id):
    return list_transactions_for_customer(user_id)
