def lower_half(rows):
    return rows[:len(rows)//2]

def upper_half(rows):
    return rows[len(rows)//2:]

def get_seat_id(boarding_pass):

    rows = list(range(128))
    seats = list(range(8))

    for c in boarding_pass[:7]:
        rows = lower_half(rows) if  c == 'F' else upper_half(rows)

    for s in boarding_pass[7:]:
        seats = lower_half(seats) if s == 'L' else upper_half(seats)

    return rows[0] * 8 + seats[0]

if __name__ == "__main__":
    with open('day5.txt') as fin:
        passes = [line.strip() for line in fin.readlines()]

    seat_ids = [get_seat_id(boarding_pass) for boarding_pass in passes]
    
    print(max(seat_ids))
    seat_ids.sort()
    for idx, seat in enumerate(seat_ids):
        try:
            if seat != seat_ids[idx-1] + 1:
                print(seat_ids[idx-1], seat_ids[idx], seat_ids[idx+1])
        except IndexError:
            continue