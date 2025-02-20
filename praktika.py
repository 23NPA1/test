def dobavlenie(shopping_list, item):
    if item not in shopping_list:  
        shopping_list.append(item) 
    else:
        print('Товар уже в корзине')
    return shopping_list

def delete(shopping_list, item):
    if item in shopping_list:
        shopping_list.remove(item)
    else:
        print('Продукта нет в корзине')    
    return shopping_list
     
    
def view(shopping_list):
    if shopping_list:  
        print("Текущий список покупок:")
        for item in shopping_list:
            print(f"- {item}")  
    else:
        print('Список покупок пуст.')  
    return shopping_list

def check(shopping_list, item):
    if item in shopping_list:  
        print('Товар на месте, бро!')
    else:
        print('Проебался, друг.')  
    return shopping_list















shopping_list = ['яблоко', 'молоко', 'хлеб', 'овсянка']
print(shopping_list)
print(dobavlenie(shopping_list, 'жопа'))
print(delete(shopping_list,'хлеб'))
view(shopping_list)
print(check(shopping_list, 'жопа'))

#Условия:
#Создайте пустой список shopping_list, который будет хранить названия товаров.

#Реализуйте функции для следующих операций:

#Добавление нового товара в список. (Если такой есть, то не добавлять)
#Удаление товара из списка по его названию.
#Отображение текущего списка покупок.
#Поиск товара в списке и отображение сообщения, есть он или нет.
#Пример работы программы:
#Добавить товар "Хлеб" в список.
#Добавить товар "Молоко" в список.
#Удалить товар "Хлеб" из списка.
#Отобразить текущий список. - должен отобразиться только Молоко, тк Хлеб удалилю.
#Проверить наличие товара "Молоко" в списке — программа должна сообщить, что товар найден.

#Комментарий:
#У тебя задача написать 4 функции - добавить/удалить/посмотреть/найти
#Они простые, просто на базу работы со списками