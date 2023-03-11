from collections import deque

""" Поиск в ширину """

# передаем функции поиска словарь и ключ
def serch(graf, name):
    # создаем структуру данных двухсторонняя очередь "дека"
    serch_queue = deque()
    # добавляем в нее соседей первого уровня
    serch_queue += graf[name]
    # Создаем список, куда будем помещать уже проверенные узлы
    serched = []

    # запускаем цикл пока не закончятся все узлы
    while serch_queue:
        # берем первый узел для проверки
        person = serch_queue.popleft() 
        # Проверям чтобы узел не был в списке проверенных узлов
        if person not in serched:
            # Проверяем соответсвует ли узел критерию поиска
            if person_is_saller(person):
                print(f'person {person} is seller')
                return True
            # Иначе добавляем все связи проверенного узла в очерель
            else:
                try:
                    serch_queue += graf[person]
                except:
                    print(Exception)
                # Добалвяем узел в список проверенных
                serched.append(person)

    return False

def person_is_saller(person):
    return True if len(person) > 6 else False

graf = {}
graf['ko'] = ['mike', 'alex', 'sanar']
graf['alex'] = ['adertas', 'kf',]
serch(graf, 'ko')