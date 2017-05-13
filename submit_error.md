

H:\AIND\AIND-Isolation (master)
(aind) λ python tournament.py

This script evaluates the performance of the custom_score evaluation function
against the `ID_Improved` agent baseline. `ID_CustomScore` is an agent using
Iterative Deepening and the custom_score function defined in game_agent.py.

                        *************************
                             Playing Matches
                        *************************

 Match #   Opponent    AB_Improved   AB_Custom   AB_Custom_2  AB_Custom_3
                        Won | Lost   Won | Lost   Won | Lost   Won | Lost
    1       Random      188 |  12    191 |   9    191 |   9    189 |  11
    2       MM_Open     112 |  88    116 |  84    138 |  62    112 |  88
    3      MM_Center    140 |  60    141 |  59    155 |  45    149 |  51
    4     MM_Improved   108 |  92    102 |  98    120 |  80    112 |  88
    5       AB_Open     110 |  90    123 |  77    129 |  71    120 |  80
    6      AB_Center    149 |  51    155 |  45    151 |  49    142 |  58
    7     AB_Improved   105 |  95    88  |  112   131 |  69    96  |  104
--------------------------------------------------------------------------
           Win Rate:      65.1%        65.4%        72.5%        65.7%


H:\AIND\AIND-Isolation (master)
(aind) λ python tournament.py

This script evaluates the performance of the custom_score evaluation function
against the `ID_Improved` agent baseline. `ID_CustomScore` is an agent using
Iterative Deepening and the custom_score function defined in game_agent.py.

                        *************************
                             Playing Matches
                        *************************

 Match #   Opponent    AB_Improved   AB_Custom   AB_Custom_2  AB_Custom_3
                        Won | Lost   Won | Lost   Won | Lost   Won | Lost
    1       Random      185 |  15    192 |   8    185 |  15    186 |  14
    2       MM_Open     115 |  85    109 |  91    131 |  69    119 |  81
    3      MM_Center    143 |  57    153 |  47    153 |  47    149 |  51
    4     MM_Improved   88  |  112   111 |  89    123 |  77    105 |  95
    5       AB_Open     114 |  86    113 |  87    126 |  74    114 |  86
    6      AB_Center    144 |  56    145 |  55    160 |  40    139 |  61
    7     AB_Improved   100 |  100   94  |  106   122 |  78    92  |  108
--------------------------------------------------------------------------
           Win Rate:      63.5%        65.5%        71.4%        64.6%


H:\AIND\AIND-Isolation (master)
(aind) λ python tournament.py

This script evaluates the performance of the custom_score evaluation function
against the `ID_Improved` agent baseline. `ID_CustomScore` is an agent using
Iterative Deepening and the custom_score function defined in game_agent.py.

                        *************************
                             Playing Matches
                        *************************

 Match #   Opponent    AB_Improved   AB_Custom   AB_Custom_2  AB_Custom_3
                        Won | Lost   Won | Lost   Won | Lost   Won | Lost
    1       Random      183 |  17    185 |  15    182 |  18    189 |  11
    2       MM_Open     110 |  90    147 |  53    91  |  109   110 |  90
    3      MM_Center    141 |  59    157 |  43    134 |  66    152 |  48
    4     MM_Improved   109 |  91    139 |  61    74  |  126   97  |  103
    5       AB_Open     123 |  77    152 |  48    94  |  106   116 |  84
    6      AB_Center    153 |  47    145 |  55    141 |  59    152 |  48
    7     AB_Improved   91  |  109   127 |  73    105 |  95    101 |  99
--------------------------------------------------------------------------
           Win Rate:      65.0%        75.1%        58.6%        65.5%


H:\AIND\AIND-Isolation (master)
(aind) λ python tournament.py

This script evaluates the performance of the custom_score evaluation function
against the `ID_Improved` agent baseline. `ID_CustomScore` is an agent using
Iterative Deepening and the custom_score function defined in game_agent.py.

                        *************************
                             Playing Matches
                        *************************

 Match #   Opponent    AB_Improved   AB_Custom   AB_Custom_2  AB_Custom_3
                        Won | Lost   Won | Lost   Won | Lost   Won | Lost
    1       Random      190 |  10    186 |  14    183 |  17    187 |  13
    2       MM_Open     96  |  104   147 |  53    105 |  95    119 |  81
    3      MM_Center    148 |  52    168 |  32    139 |  61    147 |  53
    4     MM_Improved   99  |  101   130 |  70    94  |  106   114 |  86
    5       AB_Open     114 |  86    150 |  50    97  |  103   119 |  81
    6      AB_Center    141 |  59    156 |  44    141 |  59    165 |  35
    7     AB_Improved   101 |  99    134 |  66    85  |  115   102 |  98
--------------------------------------------------------------------------
           Win Rate:      63.5%        76.5%        60.3%        68.1%


H:\AIND\AIND-Isolation (master)
(aind) λ udacity submit
Traceback (most recent call last):
  File "c:\users\chuan\anaconda3\envs\aind\lib\runpy.py", line 193, in _run_module_as_main
    "__main__", mod_spec)
  File "c:\users\chuan\anaconda3\envs\aind\lib\runpy.py", line 85, in _run_code
    exec(code, run_globals)
  File "C:\Users\chuan\Anaconda3\envs\aind\Scripts\udacity.exe\__main__.py", line 9, in <module>
  File "c:\users\chuan\anaconda3\envs\aind\lib\site-packages\udacity_pa\projectassistant.py", line 166, in main_func
    main(args, projects.nanodegree)
  File "c:\users\chuan\anaconda3\envs\aind\lib\site-packages\udacity_pa\projectassistant.py", line 140, in main
    return SubmitHelper(args).act()
  File "c:\users\chuan\anaconda3\envs\aind\lib\site-packages\udacity_pa\projectassistant.py", line 132, in act
    projects.submit(self.args)
  File "H:\AIND\AIND-Isolation\.udacity-pa\projects.py", line 76, in submit
    raise RuntimeError("You must specifiy 'isolation' or 'isolation-pvp' after 'udacity submit'.")
RuntimeError: You must specifiy 'isolation' or 'isolation-pvp' after 'udacity submit'.

H:\AIND\AIND-Isolation (master)
(aind) λ udacity submit isolation
Submission includes the following files:
    game_agent.py
    heuristic_analysis.pdf
    research_review.pdf

Uploading submission...
[=========================== 100% ===========================] 351499/351499

Waiting for results...Done!

Results:
--------

************************************************************************
                         Test Failure Feedback
************************************************************************

Failed Test: 1. Test output interface of MinimaxPlayer.minimax()
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/vmuser_ncdylpsk/workspace/game_agent.py", line 302, in minimax
    v = min_value(newgame, depth)
  File "/home/vmuser_ncdylpsk/workspace/game_agent.py", line 275, in min_value
    score = max_value(newgame, depth - 1)

                     ...lines elided for space...

  File "/home/vmuser_ncdylpsk/workspace/game_agent.py", line 275, in min_value
    score = max_value(newgame, depth - 1)
  File "/home/vmuser_ncdylpsk/workspace/game_agent.py", line 289, in max_value
    score = min_value(newgame, depth - 1)
  File "/home/vmuser_ncdylpsk/workspace/game_agent.py", line 275, in min_value
    score = max_value(newgame, depth - 1)
  File "/home/vmuser_ncdylpsk/workspace/game_agent.py", line 289, in max_value
    score = min_value(newgame, depth - 1)
  File "/home/vmuser_ncdylpsk/workspace/game_agent.py", line 275, in min_value
    score = max_value(newgame, depth - 1)
  File "/home/vmuser_ncdylpsk/workspace/game_agent.py", line 289, in max_value
    score = min_value(newgame, depth - 1)
  File "/home/vmuser_ncdylpsk/workspace/game_agent.py", line 275, in min_value
    score = max_value(newgame, depth - 1)
  File "/home/vmuser_ncdylpsk/workspace/game_agent.py", line 289, in max_value
    score = min_value(newgame, depth - 1)
  File "/home/vmuser_ncdylpsk/workspace/game_agent.py", line 275, in min_value
    score = max_value(newgame, depth - 1)
  File "/home/vmuser_ncdylpsk/workspace/game_agent.py", line 289, in max_value
    score = min_value(newgame, depth - 1)
  File "/home/vmuser_ncdylpsk/workspace/game_agent.py", line 275, in min_value
    score = max_value(newgame, depth - 1)
  File "/home/vmuser_ncdylpsk/workspace/game_agent.py", line 289, in max_value
    score = min_value(newgame, depth - 1)
  File "/home/vmuser_ncdylpsk/workspace/game_agent.py", line 268, in min_value
    return self.score(game, self)
  File "/home/vmuser_ncdylpsk/testcases.py", line 540, in score
    "each call to avoid timeout.").format(search_name)
RuntimeError: Your minimax agent called the score_fn after the timer fell below 0 milliseconds remaining.  If you call any helper functions in your minimax search, then you need to check the timer inside each call to avoid timeout.


Failed Test: 2. Test functionality of MinimaxPlayer.minimax()
----------------------------------------------------------------------
AssertionError: False is not true : Your MinimaxAgent.minimax function did not visit every node in the game tree as player 1.  First check for off-by-one errors in your handling of the depth limiting. Then, especially if the number of nodes explored by your agent is too low, check everywhere you call to game.get_legal_moves() to make sure you are getting the legal moves for the appropriate player at each level of the game tree.  Finally, you may be using non-standard search optimizations that are not supported by the test cases.  The range of expansions accepted will vary slightly within the range indicated based on your termination condition.

Expected number of visited nodes -- min: 5 max: 5
Number of nodes your agent explored: 25

Test Case Details:
------------------
Heuristic: open_move_score
Depth limit: 1
Initial Board State:
     0   1   2   3   4   5   6   7   8
0  |   |   |   |   |   |   |   |   |   |
1  |   |   |   |   |   |   |   |   |   |
2  |   |   |   |   | - |   |   |   |   |
3  |   |   | - |   | - | - | - |   |   |
4  |   |   | - |   | - |   | - | 1 |   |
5  |   | 2 | - | - |   |   | - |   |   |
6  |   |   |   | - | - | - |   |   |   |
7  |   |   |   |   |   |   |   |   |   |
8  |   |   |   |   |   |   |   |   |   |

game._board_state:
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 14, 67]



Failed Test: 4. Test that MinimaxPlayer successfully plays a full game
----------------------------------------------------------------------
Traceback (most recent call last):
RuntimeError: Timeout: 1652.6605ms exceeds 25ms limit

During handling of the above exception, another exception occurred:

AssertionError: Your agent raised an error while attempting to play a complete game against another agent.  Make sure that your agent can play an entire game -- including selecting initial moves on an empty board.
Exception: Timeout: 1652.6605ms exceeds 25ms limit


Failed Test: 7. Test functionality of AlphaBetaPlayer.alphabeta()
----------------------------------------------------------------------
AssertionError: False is not true : Your AlphaBetaAgent.alphabeta function did not call the heuristic evaluation function in all of the expected set of leaf nodes configurations in the game tree as player 1. Make sure that you are using the self.score() method to evaluate the board (not calling one of your heuristic functions directly) and verify your stopping conditions. Leaf nodes are shown as (player_1, player_2) location pairs. Optional nodes may or may not be visited depending on your termination test.

Expected leaf nodes:
{((4, 7), (6, 2)), ((7, 8), (6, 2)), ((8, 7), (6, 2)), ((4, 5), (6, 2)), ((5, 8), (6, 2)), ((8, 5), (6, 2))}
Optional leaf nodes:
set()
Leaf nodes your agent evaluated:
{((4, 5), (8, 3)), ((4, 7), (4, 1)), ((4, 5), (4, 3)), ((4, 5), (5, 0)), ((4, 7), (8, 1)), ((4, 7), (8, 3)), ((7, 8), (4, 1)), ((8, 5), (4, 1)), ((5, 8), (4, 1)), ((4, 5), (8, 1)), ((4, 7), (4, 3)), ((4, 7), (5, 0)), ((4, 5), (4, 1)), ((8, 7), (4, 1)), ((4, 7), (7, 0)), ((4, 5), (7, 0))}
Skipped nodes:
{((4, 7), (6, 2)), ((8, 5), (6, 2)), ((8, 7), (6, 2)), ((4, 5), (6, 2)), ((5, 8), (6, 2)), ((7, 8), (6, 2))}
Extra nodes:
{((4, 7), (4, 1)), ((4, 5), (8, 3)), ((4, 5), (4, 3)), ((4, 5), (5, 0)), ((4, 7), (8, 1)), ((7, 8), (4, 1)), ((8, 5), (4, 1)), ((5, 8), (4, 1)), ((4, 5), (8, 1)), ((4, 7), (4, 3)), ((4, 7), (5, 0)), ((4, 5), (4, 1)), ((4, 7), (8, 3)), ((8, 7), (4, 1)), ((4, 7), (7, 0)), ((4, 5), (7, 0))}

Test Case Details:
------------------
Heuristic: open_move_score
Depth limit: 1
Initial Board State:
     0   1   2   3   4   5   6   7   8
0  |   |   |   |   |   |   |   |   |   |
1  |   |   |   |   |   |   |   |   |   |
2  |   |   |   | - | - |   |   |   |   |
3  |   |   | - | - |   | - | - |   |   |
4  |   |   | - |   |   |   | - |   |   |
5  |   |   | - | - | - | - | - |   |   |
6  |   |   | 2 | - | - | - | 1 | - |   |
7  |   |   |   |   | - | - |   |   |   |
8  |   |   |   |   |   |   | - |   |   |

game._board_state:
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 60]



Failed Test: 8. Test that alphabeta() raises SearchTimeout when the timer expires
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/vmuser_ncdylpsk/workspace/game_agent.py", line 456, in alphabeta
    score = min_value(newgame, alpha, beta, depth)
  File "/home/vmuser_ncdylpsk/workspace/game_agent.py", line 427, in min_value
    score = max_value(newgame, alpha, beta, depth - 1)

                     ...lines elided for space...

  File "/home/vmuser_ncdylpsk/workspace/game_agent.py", line 427, in min_value
    score = max_value(newgame, alpha, beta, depth - 1)
  File "/home/vmuser_ncdylpsk/workspace/game_agent.py", line 442, in max_value
    score = min_value(newgame, alpha, beta, depth - 1)
  File "/home/vmuser_ncdylpsk/workspace/game_agent.py", line 427, in min_value
    score = max_value(newgame, alpha, beta, depth - 1)
  File "/home/vmuser_ncdylpsk/workspace/game_agent.py", line 442, in max_value
    score = min_value(newgame, alpha, beta, depth - 1)
  File "/home/vmuser_ncdylpsk/workspace/game_agent.py", line 427, in min_value
    score = max_value(newgame, alpha, beta, depth - 1)
  File "/home/vmuser_ncdylpsk/workspace/game_agent.py", line 442, in max_value
    score = min_value(newgame, alpha, beta, depth - 1)
  File "/home/vmuser_ncdylpsk/workspace/game_agent.py", line 427, in min_value
    score = max_value(newgame, alpha, beta, depth - 1)
  File "/home/vmuser_ncdylpsk/workspace/game_agent.py", line 442, in max_value
    score = min_value(newgame, alpha, beta, depth - 1)
  File "/home/vmuser_ncdylpsk/workspace/game_agent.py", line 427, in min_value
    score = max_value(newgame, alpha, beta, depth - 1)
  File "/home/vmuser_ncdylpsk/workspace/game_agent.py", line 442, in max_value
    score = min_value(newgame, alpha, beta, depth - 1)
  File "/home/vmuser_ncdylpsk/workspace/game_agent.py", line 427, in min_value
    score = max_value(newgame, alpha, beta, depth - 1)
  File "/home/vmuser_ncdylpsk/workspace/game_agent.py", line 442, in max_value
    score = min_value(newgame, alpha, beta, depth - 1)
  File "/home/vmuser_ncdylpsk/workspace/game_agent.py", line 421, in min_value
    return self.score(game, self)
  File "/home/vmuser_ncdylpsk/testcases.py", line 540, in score
    "each call to avoid timeout.").format(search_name)
RuntimeError: Your alphabeta agent called the score_fn after the timer fell below 0 milliseconds remaining.  If you call any helper functions in your alphabeta search, then you need to check the timer inside each call to avoid timeout.


Failed Test: 9. Test iterative deepening in AlphaBetaPlayer.get_move()
----------------------------------------------------------------------
AssertionError: False is not true : Your agent did not call the search function self.alphabeta() the expected number of times.  Iterative deepening should call the search function with sequential values until SearchTimeout is raised. SearchTimeout was set to be raised after 24 moves, and your agent called the search function 1 times.


Failed Test: 10. Test that AlphaBetaPlayer successfully plays a full game
----------------------------------------------------------------------
Traceback (most recent call last):
RuntimeError: Timeout: 663.4549ms exceeds 25ms limit

During handling of the above exception, another exception occurred:

AssertionError: Your agent raised an error while attempting to play a complete game against another agent.  Make sure that your agent can play an entire game -- including selecting initial moves on an empty board.
Exception: Timeout: 663.4549ms exceeds 25ms limit


************************************************************************
                          Test Result Summary
************************************************************************

1. Test output interface of MinimaxPlayer.minimax():                   E
2. Test functionality of MinimaxPlayer.minimax():                      F
3. Test that minimax() raises SearchTimeout when the timer expires:    .
4. Test that MinimaxPlayer successfully plays a full game:             F
5. Test interface of AlphaBetaPlayer.alphabeta():                      .
6. Test the interface of AlphaBetaPlayer.get_move():                   .
7. Test functionality of AlphaBetaPlayer.alphabeta():                  F
8. Test that alphabeta() raises SearchTimeout when the timer expires:  E
9. Test iterative deepening in AlphaBetaPlayer.get_move():             F
10. Test that AlphaBetaPlayer successfully plays a full game:          F
11. Test output interface of custom_score():                           .
12. Test output interface of custom_score_2():                         .
13. Test output interface of custom_score_3():                         .
14. Submission includes heuristic_analysis.pdf:                        .
15. Submission includes research_review.pdf:                           .

------------------------------------------------------------------------
            . - Test Passed    F - Test Failed    E - Error



Details are available in isolation-result-18806.json.

If you would like this version of the project to be reviewed,
submit isolation-18806.zip to the reviews website.


H:\AIND\AIND-Isolation (master)
(aind) λ
