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
    array = list(string)
    try:
        numero = array.index(letter)
        array[numero] = '*'
        return [numero, ''.join(array)]
    except ValueError:
        return False
    
def Repeat(word, letter, array): 
    if CompareHangManWord(word, letter) != False:
        Response_Array = CompareHangManWord(word, letter)
        array.append( Response_Array[0])  
        return Repeat( Response_Array[1], letter, array)
    else: 
        if len(array)!=0:
            return array  
        else:
            return False

def ImagePrint(dibujo, tries, PrintWord):
    print(dibujo[tries])
    print(PrintWord)

def message(mensaje):
    input(mensaje)
    exit()

def hangManMain():
    tries = 0 #fallo que he cometido
    word = palabras[random.randint(0, len(dibujo)-1)]#palabra que saco al azar
    AnswersGotten = len(word)#saber cuendo gane
    PrintWord = PrintHangWord(word) #lo necesito para luego imprimir la palabra del ahorcado
    ImagePrint(dibujo, tries, PrintWord)
    while tries != 6:
        answer = input('Dime una letra  ')
        if Repeat(word, answer, []) != False:
            for i in Repeat(word, answer, []):
                PrintWord[i] = answer
            ImagePrint(dibujo, tries, PrintWord)
            AnswersGotten -= len(Repeat(word, answer, []))
            if AnswersGotten == 0:
                print(PrintWord)
                message('Felicidades Ganaste')
        else:
            tries += 1
            ImagePrint(dibujo, tries, PrintWord)
            if tries == 6:
                print(dibujo[6])
                message('Repampanos Perdiste')

if __name__ == '__main__':
    hangManMain()