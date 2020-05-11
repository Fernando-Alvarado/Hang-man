import random

dibujo = [
        '''            +------------------+ 
            |                  |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
        ============================''',
        '''            +------------------+
            |                  |
            0                  |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
        ============================''',
        '''            +------------------+
            |                  |
            0                  |
            |                  |
            -                  |
            |                  |
                               |
                               |
                               |
                               |
        ============================''',
        '''            +------------------+
            |                  |
            0                  |
            |                  |
            -                  |
            |                  |
             \                 |
              \                |
                               |
                               |
        ============================''',
        '''            +------------------+
            |                  |
            0                  |
            |                  |
            -                  |
            |                  |
           / \                 |
          /   \                |
                               |
                               |
        ============================''',
        '''            +------------------+
            |                  |
            0                  |
            |                  |
         -------               |
            |                  |
           / \                 |
          /   \                |
                               |
                               |
        ============================''',
        '''            +------------------+
            |                  |
            0                  |
            |                  |
         -------               |
            |                  |
           / \                 |
          /   \                |
                               |
                               |
        ============================
        U r dead!!!!!!              ''',
]#7
palabras = ['perro', 'gato', 'bodega', 'matriz', 'fernando', 'programacion', 'rapero', 'sultan', 'comiendo', 'vino', 'videojuegos',
'toro', 'computadora', 'cubeta', 'escorpion', 'arco', 'flecha', 'espada', 'microbio', 'brujula', 'heineken', 'spivak', 'leeman']
#22
def PrintHangWord(string):
    question = []
    for i in range(0, len(list(string))):
        question.append('.-.')
    return question
        
def CompareHangManWord(string, letter):
    number = string.find(letter)
    if number != -1:
        delate = list(string)
        del delate[number]
        return [number, ''.join(delate)]
    else:
        return False
    
#def Repeat(word, letter):
#       
#    if CompareHangManWord(word, letter) != False:
#        var = PrintHangWord(word)
#        array = var[CompareHangManWord(word, letter)[0]]= letter
#        return Repeat(''.join(array), letter)
#    else: 
#        return word  

def hangManMain():
    tries = 0
    print(dibujo[tries])
    word = palabras[random.randint(0,22)]
    completeAnswer = PrintHangWord(word)
    print(completeAnswer)
    state = False
    print(tries != 6)
    print(state != True)
    while tries != 6 and state != True:
        answer = input('Dime una letras  ')
        if CompareHangManWord(word, answer) != False:
             completeAnswer[CompareHangManWord(word, answer)[0]] = answer
             word = CompareHangManWord(word, answer)[1]
             print(dibujo[tries])
             print(completeAnswer)
        else:
            tries += 1
            print(dibujo[tries])
            print(completeAnswer)
            if tries == 6:
                print(dibujo[6])
                input('presione cualquier tecla para salir')
                exit()

if __name__ == '__main__':
    hangManMain()