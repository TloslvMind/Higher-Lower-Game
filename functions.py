def format_data(account):
    """Format the account data and returns the printable format."""
    account_name = account['name']
    account_descr = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_descr}, from {account_country}."


def check_answer(user_guess, a_followers, b_followers):
    """Takes a user's guess and the follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return user_guess == 'a'
    else:
        return user_guess == 'b'

