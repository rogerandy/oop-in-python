import random
from turtle import Turtle, Screen
from game import data
is_correct=True
paper = '''
            -------------
                        )
                        )
                        )
                        )
            ___________ _)
        '''

scissors = '''
        ---------------
                        )
            ________   _ )
            ____ )
            _____)
            )
                        
        '''

rock = '''
        --------)
                )
                )
                )
        ------- )
    '''

class TurtleRace:
    def play(self):
        is_race_on = False
        screen = Screen()
        screen.setup(width=500, height=400)
        user_bet = screen.textinput(title="Make your bet", prompt="which turtle will win the race?")
        y_pos = [-100, -50, 0, 50, 100]
        colors = ["orange", "red", "yellow", "blue", "purple"]
        all_turtles = []

        for turtle_index in range(0, 5):
            new_turtle = Turtle(shape="turtle")
            new_turtle.color(colors[turtle_index])
            new_turtle.penup()
            new_turtle.goto(x=-230, y=y_pos[turtle_index])
            all_turtles.append(new_turtle)

        if user_bet:
            is_race_on = True

        while is_race_on:
            for turtle in all_turtles:
                if turtle.xcor() > 220:
                    is_race_on = False
                    winning_color = turtle.pencolor()
                    if winning_color == user_bet:
                        print(f"You've won! The {winning_color} turtle is the winner")
                    else:
                        print(f"You've lost! The {winning_color} turtle is the winner")

                speed = random.randint(0, 10)
                turtle.forward(speed)

        screen.exitonclick()

class RockPaperScissors:
    def play(self):
        game_image = [rock, paper, scissors]

        user = int(input("你要出什麼,0=rock,1=paper,2=sissors: "))
        if user >= 3 or user < 0:
            print("....")
        else:
            print(game_image[user])
            computer = random.randint(0, 2)
            print(f"電腦出:{computer}")
            print(game_image[computer])

            if user == 0 and computer == 2:
                print("you win")
            elif user == 0 and computer == 1:
                print("you are lose")
            elif user == computer:
                print("it is a draw!")
            elif user == 1 and computer == 0:
                print("you win")
            elif user == 1 and computer == 2:
                print("you are lose")
            elif user == 2 and computer == 1:
                print("you win")
            elif user == 2 and computer == 0:
                print("you are lose")

class FollowerComparison:
    def play(self):
        pass  # Add the follower comparison game logic here
        
        score=0
        roger_is_handsome=True
        account_b=random.choice(data)

        while roger_is_handsome:
            def compare(account):
                account_name=account['name']
                account_description=account['description']
                account_country=account['country']
                return f"{account_name},{account_description}  form  {account_country}"

            def check_answer(guess,a_followers,b_followers):
                if a_followers>b_followers:
                    if guess == "a":
                        return "a"
                    else:
                        return "b"



            account_a=account_b
            account_b=random.choice(data)

            while account_a==account_b:
                account_b=random.choice(data)

            print(f"compare A {compare(account_a)}")
            print("-----------")
            print("vs")
            print("-----------")
            print(f"against B {compare(account_b)}")

            guess=input("what is your answer??'a','b'")

            a_followers=account_a['follower_count']
            b_followers=account_b['follower_count']

            is_correct=check_answer(guess,a_followers,b_followers)





            if is_correct :
                score+=1
                print(f"you are right   {score}")
            else:
                print(f"yor are wrong,  {score}")
                break


class GameManager:
    def __init__(self):
        self.games = {
            "1": TurtleRace(),
            "2": RockPaperScissors(),
            "3": FollowerComparison()
        }

    def start(self):
        while True:
            print("Choose a game to play:")
            print("1. Turtle Race")
            print("2. Rock-Paper-Scissors")
            print("3. Follower Comparison")
            print("4. Quit")
            choice = input("Enter your choice: ")

            if choice == "4":
                break
            if choice in self.games:
                self.games[choice].play()
            else:
                print("Invalid choice. Please select a valid game.")
                


if __name__ == "__main__":
    game_manager = GameManager()
    game_manager.start()