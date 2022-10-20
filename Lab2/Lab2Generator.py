#wszystko ze slowkiem kluczowym yield to generator, to troche taki return
def yolo():
    yield 'Hello'
    yield 'World'
    yield '!'

for w in yolo():
    print(w)

print(type(yolo()))

def my_range(maxv):
    index =0
    while index < maxv:
        yield index, 'Hakuna matata'
        index += 1

for w in my_range(3):
    print(w)