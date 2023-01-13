import random as rd

def handle_response(message) -> str:

    if message.lower() == 'hello':
        return "Hi There!"
    
    if message.lower()[:3] == 'add' and message.lower()[4] in ['0','1','2','3','4','5','6','7','8','9'] and message.lower()[6] in ['0','1','2','3','4','5','6','7','8','9']:
        return f"Ans: {str(int(message.lower()[4]) + int(message.lower()[6]))}"

    if message.lower() == 'dice':
        val = rd.randint(1, 20)
        if val == 13:
            return f"Dice Roll: {val} -> Spooky!"
        else:
            return f"Dice Roll: {val}"

    if message.lower() == 'randomstr':
        letters = ['a', 'e', 'i', 'o', 'u']
        new_str = ''
        while len(new_str) != 5:
            rand_ind = rd.randint(0, len(letters) - 1)
            new_str += letters[rand_ind]
        return new_str 
    
    if message.lower() == 'test':
        pass


    if message.lower() == '!help':
        return f'''dice - rolls random number from 1 - 20
randomstr - gives you a random str
add x+y - returns result of addition
'''

