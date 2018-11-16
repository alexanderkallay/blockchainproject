# Initializing our (empty) blockchain list
genesis_block: {
    'previous_hash': '',
    'index': 0,
    'transactions': []
}
blockchain = []
open_transactions = []
owner = 'Alexander'


def get_last_blockchain_value():
    """ Return the last value of the current blockchain, """
    if len(blockchain) < 1:
        return None
    # no need to write "else". It is an implicit "else" case.
    return blockchain[-1]

# This function accepts two arguments.
# One required one (transaction_amount) and one optional one (last_transaction).
# The optional one is optional because it has a default value --> [1].


# always mention arguments with a default variable at the end when there are also arguments without one.
def add_transaction(recipient, sender=owner, amount=1.0):
    """ Append a new value as well as the last blockchain value to the blockchain

    Arguments:
        :sender: The sender of the coins.
        :recipient: The recipient of the coins.
        :amount: The amount of coins sent with the trnsaction (default = 1.0).
    """
    transaction = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }
    open_transactions.append(transaction)


def mine_block():
    last_block = blockchain[-1]
    block = {
        'previous hash': 'XYZ',
        'index': len(blockchain),
        'transacitons': open_transactions
    }
    blockchain.append(block)


def get_transaction_value():
    """ Return the input of the user (a new transaction amount) as a float. """
    return float(input('Your transaction amount please: '))


def get_user_choice():
    tx_recipient = input('Enter the recipient of the transaction: ')
    tx_amount = input('Your choice: ')
    # create tuple (an iterable)
    return tx_recipient, tx_amount


def print_blockchain_elements():
    # Output the blockchain list to the console
    for block in blockchain:
        print('Outputting block')
        print(block)


def verify_chain():
    is_valid = True
    for block_index in range(len(blockchain)):
        if block_index == 0:
            continue
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False


waiting_for_input = True

while waiting_for_input:
    print('\nPlease choose')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    print('h: Manipulate the chain')
    print('q: Quit\n')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        # unpack tuple
        recipient, amount = tx_data
        add_transaction(recipient, amount=amount)
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Input was invalid, please pick a value from the list!')
    if not verify_chain():
        print_blockchain_elements()
        print('Invalid blockchain!')
        break
