class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.health = 100
        print('*****************')
        print('To make your learning procedure more colorful, here is the puppy for you! It will accompnay you in your English learning journey! \n 为了让你的英语学习之路更加丰富，这里是陪伴你学习英语的小狗，請查收!')
        print('*****************')
        print('- Today is your first day to start your English words memorizing journey, please give your puppy a name! \n  今天是你第一次记单词，也是你和小狗狗第一次见面，给它取个好听的名字吧：' + self.name)


    def display(self):
        print('-------------------')
        print('- Puppy\'s name：' + self.name)
        print('- Puppy\s hair color： ' + self.color)
        print('- Puppy\'s current health level：' + str(self.health))
        print('--------------------')

    def setcolor(self, color):
        self.color = color
        print('- Puppy just became more fashionable! It dyed the hair into: ' + self.color)

    def setname(self, name):
        self.name = name
        print('- Thank you for this name, I love it! From now on, my name is: ' + name + '. I love it!')

    def starve(self):
        self.health -= 10
        print('- Oh no, it seems like you didn\'t accomplish your goal for some time, now the puppy is starving... ')
        if self.health <= 0:
            print('- Your puppy [\' + self.name +\'] is so hungry that we have to send it to the hospital... Please learn more vocabularies to get it back!')
    def eat(self, statue):
        if statue == 'finish':
            self.health += 5
            print('- Oh, you just fed the puppy with your hard-work, now the puppy is more healthy!')
        else:
            self.health -= 10
            print('- Oh oh, are you sure you wanna skip the learning procedure today? The puppy will be hungry...')

if __name__ == "__main__":
    mydog = Dog("Robin", "red")
    mydog.display()
    mydog.setcolor('gold')
    mydog.setname('Bambina')
    mydog.starve()
    mydog.eat('finish')
    for x in range(1,10):
        mydog.starve()


