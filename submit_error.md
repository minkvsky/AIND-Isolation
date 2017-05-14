
Details are available in isolation-result-18935.json.

If you would like this version of the project to be reviewed,
submit isolation-18935.zip to the reviews website.


H:\AIND\AIND-Isolation (master)
H:\AIND\AIND-Isolation (master)
(aind) λ udacity submit isolation
Submission includes the following files:
    game_agent.py
    heuristic_analysis.pdf
    research_review.pdf

Uploading submission...
[=========================== 100% ===========================] 352003/352003

Waiting for results...Done!

Results:
--------

************************************************************************
                         Test Failure Feedback
************************************************************************

Failed Test: 2. Test functionality of MinimaxPlayer.minimax()
----------------------------------------------------------------------
AssertionError: False is not true : Your MinimaxAgent.minimax function did not visit every node in the game tree as player 1.  First check for off-by-one errors in your handling of the depth limiting. Then, especially if the number of nodes explored by your agent is too low, check everywhere you call to game.get_legal_moves() to make sure you are getting the legal moves for the appropriate player at each level of the game tree.  Finally, you may be using non-standard search optimizations that are not supported by the test cases.  The range of expansions accepted will vary slightly within the range indicated based on your termination condition.

Expected number of visited nodes -- min: 7 max: 7
Number of nodes your agent explored: 37

Test Case Details:
------------------
Heuristic: open_move_score
Depth limit: 1
Initial Board State:
     0   1   2   3   4   5   6   7   8
0  |   |   |   |   |   |   |   |   |   |
1  |   |   |   |   |   |   |   |   |   |
2  |   |   |   | - |   | - |   |   |   |
3  |   |   |   |   |   | - |   |   |   |
4  |   |   |   | - | - | - | 1 |   |   |
5  |   |   |   |   |   | 2 |   |   |   |
6  |   |   |   |   | - |   | - |   |   |
7  |   |   |   |   |   |   |   |   |   |
8  |   |   |   |   |   |   |   |   |   |

game._board_state:
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50, 58]



Failed Test: 7. Test functionality of AlphaBetaPlayer.alphabeta()
----------------------------------------------------------------------
AssertionError: False is not true : Your AlphaBetaAgent.alphabeta function did not call the heuristic evaluation function in all of the expected set of leaf nodes configurations in the game tree as player 1. Make sure that you are using the self.score() method to evaluate the board (not calling one of your heuristic functions directly) and verify your stopping conditions. Leaf nodes are shown as (player_1, player_2) location pairs. Optional nodes may or may not be visited depending on your termination test.

Expected leaf nodes:
{((5, 8), (2, 3)), ((1, 6), (2, 3)), ((1, 8), (2, 3)), ((2, 5), (2, 3))}
Optional leaf nodes:
set()
Leaf nodes your agent evaluated:
{((1, 6), (0, 4)), ((2, 5), (0, 4)), ((2, 5), (1, 7)), ((2, 5), (1, 3)), ((1, 8), (0, 6)), ((2, 5), (3, 3)), ((2, 5), (4, 6)), ((1, 6), (2, 8)), ((2, 5), (0, 6)), ((5, 8), (4, 6)), ((1, 6), (0, 8))}
Skipped nodes:
{((5, 8), (2, 3)), ((1, 6), (2, 3)), ((1, 8), (2, 3)), ((2, 5), (2, 3))}
Extra nodes:
{((1, 6), (0, 4)), ((2, 5), (0, 4)), ((2, 5), (1, 7)), ((2, 5), (1, 3)), ((1, 8), (0, 6)), ((2, 5), (3, 3)), ((2, 5), (4, 6)), ((1, 6), (2, 8)), ((2, 5), (0, 6)), ((5, 8), (4, 6)), ((1, 6), (0, 8))}

Test Case Details:
------------------
Heuristic: open_move_score
Depth limit: 1
Initial Board State:
     0   1   2   3   4   5   6   7   8
0  |   |   |   |   |   |   |   |   |   |
1  |   |   |   |   |   |   |   |   |   |
2  |   |   | - | 2 | - |   |   |   |   |
3  |   |   |   |   | - | - |   | 1 |   |
4  |   |   | - | - | - | - |   |   |   |
5  |   |   | - | - | - |   | - |   |   |
6  |   |   |   | - | - |   |   |   |   |
7  |   |   |   |   |   |   |   |   |   |
8  |   |   |   |   |   |   |   |   |   |

game._board_state:
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 29, 66]



************************************************************************
                          Test Result Summary
************************************************************************

1. Test output interface of MinimaxPlayer.minimax():                   .
2. Test functionality of MinimaxPlayer.minimax():                      F
3. Test that minimax() raises SearchTimeout when the timer expires:    .
4. Test that MinimaxPlayer successfully plays a full game:             .
5. Test interface of AlphaBetaPlayer.alphabeta():                      .
6. Test the interface of AlphaBetaPlayer.get_move():                   .
7. Test functionality of AlphaBetaPlayer.alphabeta():                  F
8. Test that alphabeta() raises SearchTimeout when the timer expires:  .
9. Test iterative deepening in AlphaBetaPlayer.get_move():             .
10. Test that AlphaBetaPlayer successfully plays a full game:          .
11. Test output interface of custom_score():                           .
12. Test output interface of custom_score_2():                         .
13. Test output interface of custom_score_3():                         .
14. Submission includes heuristic_analysis.pdf:                        .
15. Submission includes research_review.pdf:                           .

------------------------------------------------------------------------
            . - Test Passed    F - Test Failed    E - Error



Details are available in isolation-result-18943.json.

If you would like this version of the project to be reviewed,
submit isolation-18943.zip to the reviews website.


H:\AIND\AIND-Isolation (master)
(aind) λ
