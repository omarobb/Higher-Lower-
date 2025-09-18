from logging.config import stopListening

import art
import random
import game_data
i = int(random.randint(0, 50))
score = 0


stop=True
while stop:
    stop2=True
    j = int(random.randint(0, 50))
    num = j
    while  stop2:
            print(art.logo)
            if score>0:

                print(f"You're right! Current score {score}")

            def stop_game():
                """description for stop the game  """
                print("\n" * 100)
                print(art.logo)
                print(f"Sorry, that's wrong. Final score: {score}.")


            def random_data_for_a():
                """random data for a"""
                rn_data=(game_data.data[i]["name"])
                rd_data=(game_data.data[i]["description"])
                rc_data=(game_data.data[i]["country"])

                print(f"Compare A: {rn_data + ", "}{rd_data + ", "}{rc_data}")

            rfa_data = (game_data.data[i]["follower_count"])

            def random_data_for_b():
                """random data for b"""
                rn_data = (game_data.data[j]["name"])
                rd_data = (game_data.data[j]["description"])
                rc_data = (game_data.data[j]["country"])

                print(f"Compare B: {rn_data + ", "}{rd_data + ", "}{rc_data}")

            rfb_data = (game_data.data[j]["follower_count"])

            random_data_for_a()

            print(art.vs)

            random_data_for_b()

            choice=input("Who has more followers? Type 'A' or 'B': ").lower()

            if choice=='a':

                if rfa_data>rfb_data:
                    score+=1
                    print("\n"*100)
                    i=num
                    stop2=False
                else:
                    stop_game()
                    stop2 = False
                    stop = False
            elif choice=='b':

                if rfb_data>rfa_data:
                    score += 1
                    print("\n" * 100)
                    i=num
                    stop2 = False
                else:
                    stop_game()
                    stop2 = False
                    stop = False
            else:
                stop_game()
                stop2 = False
                stop = False
