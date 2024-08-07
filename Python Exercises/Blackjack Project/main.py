import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_hands = []
computer_hands = []
player_sum = 0
computer_sum = 0
game_input = player_input = ''


def draw_a_card():
    return random.choice(cards)


def deck_init():
    global computer_hands, player_hands
    computer_hands = []
    player_hands = []
    player_hands.append(draw_a_card())
    computer_hands.append(draw_a_card())
    player_hands.append(draw_a_card())


def play_game(game_state):
    global game_input, player_input
    if game_state == 'new':
        deck_init()
        game_input = input('Do you want to play a game of Blackjack? Type \'y\' or \'n\':').lower()
    elif game_state == 'draw':
        player_input = input('Type \'y\' to get another card, type \'n\' to pass: ').lower()


print(logo)
play_game('new')
deck_init()

while game_input == 'y':
    print(f'Your cards: {player_hands}, current score: {sum(player_hands)}')
    print(f'Computer\'s first card: {computer_hands}')
    play_game('draw')

    if sum(player_hands) == 21:
        print('You got a blackjack! Auto win')
        play_game('new')

    if player_input == 'y':
        player_hands.append(draw_a_card())
        player_sum = sum(player_hands)
        if player_sum > 21:
            print(f'Your final hand: {player_hands}, final score: {player_sum}')
            print(f'Computer final hand: {computer_hands}, final score: {sum(computer_hands)}')
            print('You went over. You lose')
            play_game('new')

    if player_input == 'n':
        player_sum = sum(player_hands)
        comp_draws = True
        while comp_draws:
            computer_hands.append((draw_a_card()))
            computer_sum = sum(computer_hands)
            if computer_sum > 16:
                print(f'Your final hand: {player_hands}, final score: {player_sum}')
                print(f'Computer final hand: {computer_hands}, final score: {computer_sum}')
                if player_sum < computer_sum < 22:
                    print('You Lose')
                    comp_draws = False
                    play_game('new')
                elif computer_sum == player_sum:
                    print('You Tied')
                    comp_draws = False
                    play_game('new')
                else:
                    print('Computer went over, You Win!')
                    comp_draws = False
                    play_game('new')

if game_input == 'n':
    exit()
