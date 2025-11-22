from repository.account_repo import AccountRepository
from repository.transaction_repo import TransactionRepository
from utils.response_builder import ok, fail

class TransactionHandler:

    def transfer(self, customer_id, from_acc, to_acc, amount):

        acc_repo = AccountRepository()
        trx_repo = TransactionRepository()

        source = acc_repo.get_account_by_customer(customer_id)

        if not source:
            return fail("Source account not found")

        if float(source.available_balance) < amount:
            return fail("Insufficient balance")

        # proses pengurangan saldo
        new_balance = float(source.available_balance) - amount
        acc_repo.update_balance(from_acc, new_balance)

        # catat transaksi
        trx = trx_repo.insert_transaction({
            "customer_id": customer_id,
            "from": from_acc,
            "to": to_acc,
            "amount": amount,
            "status": "SUCCESS",
            "description": "Internal transfer"
        })

        return ok({"reference": trx.id, "balance_after": new_balance})
