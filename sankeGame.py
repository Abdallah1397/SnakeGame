import random
import curses

# initialized curses
scr=curses.initscr()
# hidden 0 , 1 normal , 2 very visiable 
curses.curs_set(0)


# Hight,Width => return y,x of my scr
scrHight,scrWidth=scr.getmaxyx()

# define window and start from
window=curses.newwin(scrHight,scrWidth,0,0)
# keypad => true
window.keypad(1)
# refersh after 100 ms
# window.timeout(100)

snake_x=scrWidth//4
snake_y=scrHight//2

snake=[
    [snake_y,snake_x],
    [snake_y,snake_x-1],
    [snake_y,snake_x-2 ]
]

# Food
food=[scrHight//2,scrWidth//2]

window.addch(food[0],food[1],curses.ACS_PLUS)

# define the Movment

key=curses.KEY_RIGHT

while True:
    next_key=window.getch()
    key=key if next_key ==-1 else next_key

    if snake[0][0] in [0,scrHight] or snake[0][1] in [0,scrWidth] or snake[0] in snake[1:]:
        curses.endwin()
        quit()

    new_head=[snake[0][0],snake[0][1]]

    if key== curses.KEY_DOWN:
        new_head[0] +=1
    elif key == curses.KEY_UP:
        new_head[0] -=1
    elif key == curses.KEY_RIGHT:
        new_head[1] -=1
    elif key == curses.KEY_LEFT:
        new_head[1] +=1
    
    snake.insert(0,new_head)


    if snake[0]==food:
        food=None
        while food is None:
            newFood=[
                random.randint(1,scrHight-1),
                random.randint(1,scrWidth-1)
            ]
            
            food =newFood if newFood not in snake else None
        window.addch(food[0],food[1],curses.ACS_PLUS)
    # else:
    #     tail=snake.pop()
    #     window.addch(tail[0],tail[1],'')

    window.addch(snake[0][0],snake[0][1],curses.ACS_CKBOARD)




