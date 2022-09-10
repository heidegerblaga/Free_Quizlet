from random import randint
from model import dic
from Quiz import Quiz
from model import (Base, session,
                    Lern, engine)

if __name__ == '__main__':

    print(dic[1].point)
    Quiz(dic)