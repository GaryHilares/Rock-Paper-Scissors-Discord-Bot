import random
from discord.ext import commands

@commands.command(name='play', brief='Play a rock-paper-scissors game.')
async def rock_paper_scissors(ctx, *args):
    moves = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
    if len(args) != 1:
        await ctx.channel.send('Invalid arguments. Please just send 1 option.')
        return
    player_move = args[0].lower()
    legal_moves = list(moves.keys())
    if player_move not in legal_moves:
        await ctx.channel.send(f'{player_move} is not a valid option. Valid options are {legal_moves}.')
        return
    bot_move = random.choice(legal_moves)
    winner = ''
    if player_move == moves[bot_move]:
        winner = 'The bot'
    elif bot_move == moves[player_move]:
        winner = 'The player'
    else:
        winner = 'No one'
    await ctx.channel.send(f'Bot played {bot_move}. {winner} won.')