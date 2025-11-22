from services.business.customer_business import authenticate_customer, fetch_profile
from app.utils.jwt_utils import create_token

def login_customer(username, pin):
    user = authenticate_customer(username, pin)
    if not user:
        return None
    token = create_token(user["id"])
    return token

def get_customer_profile(customer_id):
    return fetch_profile(customer_id)

def get_accounts_by_customer(customer_id):
    from services.business.account_business import list_accounts
    return list_accounts(customer_id)
