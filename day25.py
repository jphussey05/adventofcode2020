def transform(sub_num, pub_key):
    value = 1
    loop_size = 0
    while value != pub_key:
        value = (value * sub_num) % 20201227
        loop_size += 1
    
    return loop_size

def encrypt(sub_num, loops):
    value = 1
    for _ in range(loops):
        value = (value * sub_num) % 20201227

    return value

if __name__ == "__main__":
    card_pub = 15335876
    door_pub = 15086442

    card_loop = transform(7, card_pub)
    print(f'Card loop size is {card_loop}')
    door_loop = transform(7, door_pub)
    print(f'Door loop size is {door_loop}')

    key = encrypt(card_pub, door_loop)
    print(f'Encryption key is {key}')