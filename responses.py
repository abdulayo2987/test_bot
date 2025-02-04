from random import choice, randint



def get_response(user_inputs: str)-> str:
    lowered: str = user_inputs.lower()

    if lowered == '':
        return 'Well your quiet'
    elif 'hello' in lowered:
        return 'Hello there'
    else:
        return 'message'