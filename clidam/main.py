import itertools
import curses


# https://stackoverflow.com/a/22045226
def chunk(it, size):
    it = iter(it)
    return iter(lambda: tuple(itertools.islice(it, size)), ())


def curses_func(stdscr):

    stdscr.scrollok(True)
    # Clear screen
    stdscr.clear()

    height, width = stdscr.getmaxyx()
    stdscr.addstr(f"Max X, Y: {width}, {height}")

    stdscr.addstr(f"Colors: {curses.COLORS}\n")
    stdscr.addstr(f"Color Pairs: {curses.COLOR_PAIRS}\n")
    stdscr.addstr(f"RED: {curses.color_content(curses.COLOR_RED)}\n")

    stdscr.addstr(f"Has Colors: {curses.has_colors()}\n")
    stdscr.addstr(f"Can Change Color: {curses.can_change_color()}\n")

    stdscr.refresh()
    stdscr.getkey()

    colors = range(curses.COLORS)
    pairs = range(1, curses.COLOR_PAIRS)
    cgrps = chunk(colors, len(pairs))
    colorgroups = (zip(pairs, cgrp) for cgrp in cgrps)
    for grp in colorgroups:
        stdscr.clear()
        for p, c in grp:
            curses.init_pair(p, c, curses.COLOR_WHITE)
            x, y = divmod(p, width)
            stdscr.addstr(x, y, str(c % 10), curses.color_pair(p))
        stdscr.refresh()
        stdscr.getkey()


def main():
    # curses.wrapper(curses_func)
    stdscr = curses.initscr()
    curses.start_color()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    curses_func(stdscr)


if __name__ == "__main__":
    main()
