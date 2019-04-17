class Node:
    def __init__(self, value, turn):
        self.value = value
        self.left = None
        self.right = None
        self.turn = turn

        self.fill()

    def fill(self):
        if self.value<10:
            self.right = Node(self.value+1,  self.turn+1)
            self.left = Node(self.value+2,  self.turn+1)


def count_wins(node, count, turn):
    # if value is 10 on turn
    if node.value > 9:
        if node.turn % 2 == turn:
            return count
        else:
            return count + 1
    else:
        count = count_wins(node.right, count, turn)
        count = count_wins(node.left, count, turn)
        return count


test = Node(0, 0)
run = True
computer_num = 0
last_holder = 0

while run:
    usernum = int(input("What's your number? (you may increase by 1 or 2): "))
    if usernum > 9:
        print("Computer wins")
        run = False
    else:
        if usernum-computer_num == 2:
            test = test.left
        else:
            test = test.right
        count = count_wins(test.right, 0, 0)
        countL = count_wins(test.left, 0, 0)
        if count > countL:
            computer_num = usernum+1
            test = test.right
            print("The computer plays: " + str(computer_num))
        else:
            computer_num = usernum+2
            test = test.left
            print("The computer plays: " + str(computer_num))

        if computer_num>9:
            print("You win")
            run = False
    user_holder = usernum
