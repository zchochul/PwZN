import rich
from rich.progress import track
import rich.traceback #do lapania wyjatkow
import time

rich.traceback.install()
#3/0
rich.get_console().clear()
rich.get_console().rule('Lab1 zabawa :blush:')
rich.print('Siema :smiley:')

for i in track(range(10)):
    time.sleep(1)

#do histagramowania słowniki, słowa + ilość wystąpień, później posortować i wyświetlić