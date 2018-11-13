blockchain = []

def get_last_blockchain_value():
    """ Returns the value of the current blochcain. """
    return blockchain[-1]

def add_value(transaction_amount, last_transaction=[1]):
    """ Append a new value as well as the last blockchain to the blockchain 

    Arguments:
        :transaction_amount: The amount that should be added to the blockchain.
        :last_transaction: The last blockchain transaction (default[1])
    """

    blockchain.append([last_transaction, transaction_amount])
    
def get_user_input():
    """Return the input of the user (a new transaction)"""
    return float(input("Your transaction amount please "))


tx_amount = get_user_input()

tx_amount = get_user_input()
add_value(tx_amount)

tx_amount = get_user_input()
add_value(transaction_amount= tx_amount, last_transaction=get_last_blockchain_value())

tx_amount = get_user_input
add_value(tx_amount, get_last_blockchain_value())

print(blockchain)