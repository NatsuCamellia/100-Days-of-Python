from time import sleep
import os

class Clock:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def run(self):
        self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute += 1
            if self.minute == 60:
                self.minute = 0
                self.hour += 1
                if self.hour == 24:
                    self.hour = 0

    def display(self):
        print("It's %02d:%02d:%02d now" % (self.hour, self.minute, self.second))

def main():
    clock = Clock()
    while True:
        os.system('clear')
        clock.run()
        clock.display()
        sleep(1)


if __name__ == '__main__':
    main()