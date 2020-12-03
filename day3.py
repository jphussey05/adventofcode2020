def move(pos, width, right, down):
    x = pos[0] + right
    y = pos[1] + down

    if x > width:
        x = (x-1) % width

    return x, y

def slide_down(hill, right, down):
    height = len(hill)
    width = len(hill[0]) - 1
    tree_cnt = 0
    pos = 0,0

    while pos[1] < height:
        x,y = pos

        if hill[y][x] == '#':
            tree_cnt += 1
            
        pos = move(pos, width, right, down)
    
    return tree_cnt

if __name__ == "__main__":
    with open('day3.txt') as fin:
        contents = fin.readlines()

    hill = [line.strip() for line in contents]

    total_trees = slide_down(hill, 1, 1) * \
                  slide_down(hill, 3, 1) * \
                  slide_down(hill, 5, 1) * \
                  slide_down(hill, 7, 1) * \
                  slide_down(hill, 1, 2)
        
    print(total_trees)