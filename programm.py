# импорт модулей
from tkinter import *
import random
import os
import time
import threading
#делаем холст
tk=Tk()
tk.wm_attributes('-topmost',1)
tk.title('Дорожные знаки')
tk.update()
canvas=Canvas(tk,width=1000,height=800)
canvas.pack()
#делаем всякие переменные
score=0
completed=0
sign_to_show=None
image=None
button1=None
button2=None
button3=None
image_id=0
all_signs=[]
max_score=0
sign_to_show_id=0
#функция для вывода результатов в конце
def print_results():
    canvas.create_text(500,300,text=f'Счёт - {score} из {max_score}.',font=('Calibri',30))
#функция, которая говорит что делать если нажата правильная кнопка
def right_button_press():
    global score
    #удаляем существующие кнопки
    button1.destroy()
    button2.destroy()
    button3.destroy()
    #удаляем картинку
    canvas.delete(image_id)
    #увеличиваем счёт
    score+=1
    #удаляем использованный знак из списка
    del signs[sign_to_show_id]
    #смотрим, остались ли ещё знаки. Если да - берём следующий, если нет - выводим результат
    if len(signs)>0:
        main()
    else:
        print_results()
#функция, которая говорит что делать если нажата неправильная кнопка
def wrong_button_press():
    #удаляем существующие кнопки
    button1.destroy()
    button2.destroy()
    button3.destroy()
    #удаляем картинку
    canvas.delete(image_id)
    #удаляем использованный знак из списка
    del signs[sign_to_show_id]
    #смотрим, остались ли ещё знаки. Если да - берём следующий, если нет - выводим результат
    if len(signs)>0:
        main()
    else:
        print_results()
#узнаем, какие знаки есть в папке со знаками
signs=os.listdir('images')
#делаем список, из которого ничего не удаляется(для неправильных кнопок)
        

all_signs=signs
#устанавливаем максимальное кол-во очков
max_score=len(all_signs)
#главная функция
def main():
    #делаем кучу переменных глобальными
    global button1
    global button2
    global button3
    global image
    global image_id
    global sign_to_show
    global sign_to_show_id
    #определяем, какой знак будет показан
    sign_to_show_id=random.randint(0,len(signs)-1)
    sign_to_show=signs[sign_to_show_id]
    #выводим знак
    image=PhotoImage(file=f'images\\{sign_to_show}')
    image_id=canvas.create_image(500,300,image=image)
    #определяем правильную кнопку
    right_button=random.randint(1,3)
    #удаляем .gif из имени изображения(для показа на кнопках
    right_text=sign_to_show.replace('.gif','')
    #создаем кнопки
    if right_button==1:
        #если строка примерно такая, то здесь делаем правильной кнопке правильный текст
        button1=Button(text=right_text,command=right_button_press)
        #если строка примерно такая, то здесь делаем неправильной кнопке 1 неправильный текст, и смотрим, не совпадает ли он с правильным
        while True:
            random_text1=all_signs[random.randint(0,len(signs)-1)]
            if random_text1==right_text:
                pass
            else:
                random_text1=random_text1.replace('.gif','')
                break
        button2=Button(text=random_text1,command=wrong_button_press)
        #если строка примерно такая, то здесь делаем неправильной кнопке 1 неправильный текст, и смотрим, не совпадает ли он с правильным и не совпадает ли он с первым неправильным
        while True:
            random_text2=all_signs[random.randint(0,len(signs)-1)]
            if random_text2==right_text or random_text2==random_text1:
                pass
            else:
                random_text2=random_text2.replace('.gif','')
                break
        button3=Button(text=random_text2,command=wrong_button_press)
        button1.pack()
        button2.pack()
        button3.pack()
    elif right_button==2:
        while True:
            random_text1=all_signs[random.randint(0,len(signs)-1)]
            if random_text1==right_text:
                pass
            else:
                random_text1=random_text1.replace('.gif','')
                break
        button1=Button(text=random_text1,command=wrong_button_press)
        
        button2=Button(text=right_text,command=right_button_press)
        while True:
            random_text2=all_signs[random.randint(0,len(signs)-1)]
            if random_text2==right_text or random_text2==random_text1:
                pass
            else:
                random_text2=random_text2.replace('.gif','')
                break
        button3=Button(text=random_text2,command=wrong_button_press)
        button1.pack()
        button2.pack()
        button3.pack()
    elif right_button==3:
        while True:
            random_text1=all_signs[random.randint(0,len(signs)-1)]
            if random_text1==right_text:
                pass
            else:
                random_text1=random_text1.replace('.gif','')
                break
        button1=Button(text=random_text1,command=wrong_button_press)
        while True:
            random_text2=all_signs[random.randint(0,len(signs)-1)]
            if random_text2==right_text or random_text2==random_text1:
                pass
            else:
                random_text2=random_text2.replace('.gif','')
                break
        button2=Button(text=random_text2,command=wrong_button_press)
        
        button3=Button(text=right_text,command=right_button_press)
        button1.pack()
        button2.pack()
        button3.pack()
canvas.mainloop()
#Запускаем!
main()
