# 3 agentplayer
### Random agent
It is an agent that choses randomly. As it does not uses heuristic,it is not executed with any.
### Minimax Agent (MM)
It is an agent that implements a fixed-depth minimax search
algorithm.It is excuted by all following heuristic functions.
### Alpha-Beta agent (AB)
It is an agent that implements the fixed-depth Alpha-Beta pruning search algorithm.It is excuted by all following heuristic functions.

# Different heuristic functions in `sample_players.py`
- open_move_score
    - how many legal moves are there for player.With this score, player will only consider itself.
- center_score
    - the square of the distance between the center of the board and the location of the active player.
    - this will let the player move away from the center.
    - this doesn't consider the situation of the opponent.
- improved_score
    - the difference between own moves and opponent's moves.With this score, player will consider both.Since legal moves will be less and less with the game going,the difference will generally be less and less too.When the difference is possitive,the ative player gets a better situation than the other.

# Different heuristic functions in `game_agent.py`
- custom_score
    - difference of the sum of available moves for each legal move of the two players.
    - this consider situation of both players and more precisely than the improved_score.In some meaning,this seems like to add the depth by 1.
    - this will block the opponent.
    - this will outplay the improved_score.
- custom_score_2
    - some kind of distance of two players' loactions:the sum of absolute difference of each element of the location tuple.
    - this will let the active player away from the other.
    - the improved_score will outplay this score.
- custom_score_3
    - linear commbination of own_moves(number of own legal moves) and opp_moves(number of oppoent's legal moves):own_moves - 1.5 * opp_moves
    - this almost gets a tie with the improved_score.

# Result picture
Here is the result of 400 matches.AB_Custom gets the best winning probability.

![result of 400 matches](http://i1.piimg.com/588926/2785c1f19ef2ff6e.png)

# Conclution
My best score is the difference of the sum of available moves for each legal move of the two players which can outplay improved_score.
I recommend custom_score(the difference of the sum of available moves for each legal move of the two players) as my final heuristic base on the three following reason:
- this score performs better and outplays improved_score.
- only addition and subtraction appear in this score,so this heuristic is easy.
- althougth this score is more complex than others,it will not go shallower than others because it is not slower to calculate.
