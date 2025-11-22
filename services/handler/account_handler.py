from repository.account_repo import AccountRepository
from utils.response_builder import ok, fail

class AccountHandler:

    def get_balance(self, customer_id):
        repo = AccountRepository()
        acc = repo.get_account_by_customer(customer_id)

        if not acc:
            return fail("Account not found")

        return ok({
            "account_number": acc.account_number,
            "available_balance": float(acc.available_balance)
        })
