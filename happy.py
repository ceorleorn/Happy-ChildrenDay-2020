import time
print('')
print('作品开源在https://github.com/snbck/Happy-ChildrenDay-2020')
print('作品遵循MIT开源协议')

print('')

def tab(n):
    stab = ''
    for i in range(0,n):
        stab = stab + ' '
    return stab

def fill(n):
    stab = ''
    for i in range(0,n):
        stab = stab + '■'
    return stab


def PaintCandle():
    #TEXT7
    renderPaintText = tab(8)
    for i in range(0,7):
        renderPaintText = renderPaintText + tab(5) + fill(1) + tab(5)
        time.sleep(0.1)
    for i in range(0,5):
        print(renderPaintText)
        time.sleep(0.1)

def PaintBody():
    #画逐层
    for i in range(0,16,2):
        overTabNumber = tab(13 - i)
        renderPaintText = overTabNumber + fill(38 + i)
        print(renderPaintText)
        for b in range(0,6,2):
            print(tab(13 - i) + fill(1) + tab(72 + i + i) + fill(1))
            time.sleep(0.1)
        
    



PaintCandle()
PaintBody()