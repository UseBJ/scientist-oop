class Scientist:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty
        self.energy = 100
        self.task_done = 0
        self.is_alive = True

    def rest(self):
        self.energy = 100
        print(f"{self.name} отдыхает...")
        print(f"{self.name} энергия восстановлена: 100")
    
    def work(self, task):
        if self.energy >0:
            self.energy -= 10
            self.task_done += 1
            print(f"{self.name} работает над {task}...")
            print(f"{self.name} энергия: {self.energy}")
        else:
            print(f"{self.name} слишком устал, чтобы работать.")

    def status(self):
        print(f"Имя: {self.name}")
        print(f"Специализация: {self.specialty}")
        print(f"Энергия: {self.energy}")
        print(f"Задачи выполнены: {self.task_done}")
        print(f"Живой: {'Да' if self.is_alive else 'Нет'}")

class Engineer(Scientist):
    def __init__(self, name):
        super().__init__(name, "engineering") 
    
    def build(self, item):
        if self.energy < 20: 
            print(f"{self.name} не может строить.")
        else:
            self.energy -= 20
            print(f"{self.name} строит {item}...")
            print(f"Энергия: {self.energy}")

# Пример использования класса Scientist
if __name__ == "__main__":
    Senku = Scientist("Senku Ishigami", "everything")
    Chrome = Scientist("Chrome", "geology")

    Senku.status()
    Senku.work("rocket fuel")
    Senku.work("electricity")
    Senku.status()

    Chrome.work("mining")
    Chrome.rest()
    Chrome.status() 

    #check Engineer class
    chrome = Engineer("Chrome")
    chrome.status()       # должен показать specialty: engineering
    chrome.build("car")   # тратит 20 энергии
    chrome.work("task")   # тратит 10 энергии
    chrome.status()       # энергия должна быть 70
