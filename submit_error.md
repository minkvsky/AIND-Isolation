

************************************************************************
                         Test Failure Feedback
************************************************************************

Failed Test: 7. Test functionality of AlphaBetaPlayer.alphabeta()
----------------------------------------------------------------------
AssertionError: Failed to cut off search -- expanded too many nodes. (i.e., your agent did not prune at this node, but a correct alpha beta search did prune at this node when following the same expansion order that your agent followed.)
Alpha: 5.0
Beta: 5.0
Game tree evaluation order:
[(1, 4), (1, 6), (2, 7), (4, 7), (5, 4), (5, 6)]
[(5, 7), (7, 3), (7, 7)]

Nodes are shown with each layer sorted in the order the nodes were expanded
during search.  All nodes in each successive layer are children of the
furthest-right node in the parent layer above it.

Test Case Details:
------------------
Heuristic: open_move_score
Depth limit: 2
Initial Board State:
     0   1   2   3   4   5   6   7   8
0  |   |   |   |   |   |   |   |   |   |
1  |   |   |   |   |   |   |   |   |   |
2  |   |   |   | - |   | - | - |   |   |
3  |   |   | - |   | - | 1 | - |   |   |
4  |   |   | - | - | - | - | - |   |   |
5  |   |   |   | - |   | - |   |   |   |
6  |   |   | - |   |   | 2 |   |   |   |
7  |   |   |   |   |   |   |   |   |   |
8  |   |   |   |   |   |   |   |   |   |

game._board_state:
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 51, 48]



************************************************************************
                          Test Result Summary
************************************************************************

1. Test output interface of MinimaxPlayer.minimax():                   .
2. Test functionality of MinimaxPlayer.minimax():                      .
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



Details are available in isolation-result-19357.json.

If you would like this version of the project to be reviewed,
submit isolation-19357.zip to the reviews website.


H:\AIND\AIND-Isolation (master)
(aind) λ
