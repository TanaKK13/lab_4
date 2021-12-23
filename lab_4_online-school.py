import random

class Webium:
    def speach(self):
        print('Я из Вебиума!')

class teachers(Webium):
    
    def __init__(self):
        self.time = 50
        self.money = 100000
        self.mood = 80
        
    def web(self):
        answer = random.randrange(1, 10, 1)
        if answer > 7:
            web_condition = 'Вебинар прошёл хорошо'
            self.mood += 10
            print('*Настроение препода повысилось*')
        else:
            web_condition = 'Вебинар сегодня не удался'
            self.mood -= 10
            print('*Настроение препода понизилось*')
        return web_condition

    def skript(self):
         print ('Препод: Я сделал скрипт!')
         self.time -= 20
         self.mood += 10

    def course(self):
        self.money += 500
        print ('+1 студент, которого я подготовлю на нужный ему балл!')
         
class students(Webium):
    
    def __init__(self):
        self.time = 100
        self.money = 5000
        self.mood = 40

    def homework(self):
        print('Студент: Я сделал домашку!')

    def course(self):
        self.money -= 3000
        print ('Студент: Я купил курс')

class marketing(Webium):
    
    def __init__(self):
        self.time = 60
        self.money = 10000000
        self.mood = 70
        
    def give_work(self):
        print ('Маркетинг: Нам нужен макет для анонса нового курса!')
        time = random.randrange(1, 100, 1)
        return time
    
    def course(self):
        self.money += 500
        print ('Студент купил курс!')

class designers(Webium):
    
    def __init__(self):
        self.time = 10
        self.money = 40000
        self.mood = 80
        
    def get_work(self, time_work):
        self.time -= time_work
        return ('Дизайнер: Я сделал работу!')
        
    def course(self):
        self.money += 500
        print ('О! Деньги от продажи')

class sales(Webium):
    
    def __init__(self):
        self.time = 20
        self.money = 9000000
        self.mood = 51
        
    def purchase(self):
        
        if self.mood > 50:
            purchase_condition = 'Отдел продаж: Студент купил курс'
        else:
            purchase_condition = 'Отдел продаж: Студент ещё не купил курс'
        return purchase_condition
            
    def course(self):
        self.money += 500
        print ('О! Деньги от продажи')
        
        
student = students()
teacher = teachers()
designer = designers()
people_from_marketing = marketing()
people_from_sales = sales()


condition_web = teacher.web()

print(condition_web)
if condition_web == 'Вебинар сегодня не удался':
    student.mood -= 20
    print ('*Настроение студентов понизилось*')
    print ('//----//')
else:
    student.mood += 20
    print ('*Настроение студентов повысилось*')
    print ('//----//')

if student.money >= 3000:
    
    print ('Счёт студента:', student.money)
    webium = [student, teacher, designer, people_from_marketing, people_from_sales]
    for person in webium:
        person.course()
    print ('Счёт студента:', student.money)
    print ('//----//')
    
time_work = people_from_marketing.give_work()
designer.get_work(time_work)
print ('Дизайнер: Время, которое уйдёт:', time_work)
print (designer.get_work(time_work))
print ('//----//')

print (people_from_sales.purchase())
print ('//----//')

for person in webium:
    person.speach()
