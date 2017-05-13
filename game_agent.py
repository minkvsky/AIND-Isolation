"""Finish all TODO items in this file to complete the isolation project, then
test your agent's strength against a set of known agents using tournament.py
and include the results in your report.
"""
import random


class SearchTimeout(Exception):
    """Subclass base exception for code clarity. """
    pass


def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    This should be the best heuristic function for your project submission.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # TODO: finish this function!
    # raise NotImplementedError
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    own_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))
    return float(own_moves - 2 * opp_moves + 8)



def custom_score_2(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    This should be the best heuristic function for your project submission.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # TODO: finish this function!
    # raise NotImplementedError
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    # opp_moves = len(game.get_legal_moves(game.get_opponent(player)))
    # blank_moves = len(game.get_blank_spaces())
    #
    # return float(blank_moves - opp_moves)
    own_location = game.get_player_location(player)
    opp_location = game.get_player_location(game.get_opponent(player))
    distance = abs(own_location[0]-opp_location[0]) + abs(own_location[1]-opp_location[1])
    return float(distance)


def custom_score_3(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called    from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # TODO: finish this function!
    # raise NotImplementedError
    # if game.is_loser(player):
    #     return float("-inf")
    #
    # if game.is_winner(player):
    #     return float("inf")
    #
    # own_moves = len(game.get_legal_moves(player))
    # blank_moves = len(game.get_blank_spaces())
    #
    # return float(own_moves) / float(blank_moves)
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    def in_bounds(game, row, col):
        return 0 <= row < game.height and 0 <= col < game.width

    bonus = 0.

    center = (int(game.width/2), int(game.height/2))
    r, c = center
    directions = [(-1, -2), (-1, 2), (1, -2), (1, 2),
                  (2, -1), (2, 1), (-2, -1), (-2, 1)]

    off_center = [(r + dr, c + dc) for dr, dc in directions if in_bounds(game, r + dr, c + dc)]
    player_location = game.get_player_location(player)
    if player_location == center:
        bonus = 1.5
    elif player_location in off_center:
            bonus = 0.5
    own_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))
    return float(own_moves - opp_moves) + bonus


class IsolationPlayer:
    """Base class for minimax and alphabeta agents -- this class is never
    constructed or tested directly.

    ********************  DO NOT MODIFY THIS CLASS  ********************

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """
    def __init__(self, search_depth=3, score_fn=custom_score, timeout=10.):
        self.search_depth = search_depth
        self.score = score_fn
        self.time_left = None
        self.TIMER_THRESHOLD = timeout


class MinimaxPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using depth-limited minimax
    search. You must finish and test this player to make sure it properly uses
    minimax to return a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        **************  YOU DO NOT NEED TO MODIFY THIS FUNCTION  *************

        For fixed-depth search, this function simply wraps the call to the
        minimax method, but this method provides a common interface for all
        Isolation agents, and you will replace it in the AlphaBetaPlayer with
        iterative deepening search.

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_move = (-1, -1)

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            # print('get move:{}'.format(self.minimax(game, self.search_depth)))
            return self.minimax(game, self.search_depth)

        except SearchTimeout:
            pass  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        # print('get move:{}'.format(best_move)) # if you get this wrong in minimax
        return best_move

    def minimax(self, game, depth):
        """Implement depth-limited minimax search algorithm as described in
        the lectures.

        This should be a modified version of MINIMAX-DECISION in the AIMA text.
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Minimax-Decision.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        # # TODO: finish this function!
        def terminal_test(game, depth):
            # some problem here
            return depth == 0 or game.is_winner(self) or game.is_loser(self)

        def min_value(game, depth):
            if terminal_test(game, depth):
                return self.score(game, self)

            moves = game.get_legal_moves()

            v = float('inf')
            for move in moves:
                newgame = game.forecast_move(move)
                score = max_value(newgame, depth - 1)
                # print('min_value:score:{}'.format(score))
                v = min(v,score)

            return v

        def max_value(game, depth):
            if terminal_test(game, depth):
                return self.score(game, self)

            moves = game.get_legal_moves()

            v = float('-inf')
            for move in moves:
                newgame = game.forecast_move(move)
                score = min_value(newgame, depth - 1)
                # print('max_value:score:{}'.format(score))
                v = max(v,score)

            return v
        # raise NotImplementedError
        # player = game.active_player()
        # return argmax(moves,
        #               key=lambda move: min_value(game.forecast_move(move), depth))

        best_score = float('-inf')
        best_action = (-1, -1)
        if terminal_test(game, depth):
            return best_action
        moves = game.get_legal_moves()
        # if not moves:
        #     return (-1, -1)

        for move in moves:
            newgame = game.forecast_move(move)
            v = min_value(newgame, depth)
            if v >= best_score:
                best_score = v
                best_action = move
            # print(best_score)
            # print(best_action)
        # print(best_action)
        # print('once_minimax')
        return best_action


class AlphaBetaPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using iterative deepening minimax
    search with alpha-beta pruning. You must finish and test this player to
    make sure it returns a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        Modify the get_move() method from the MinimaxPlayer class to implement
        iterative deepening search instead of fixed-depth search.

        **********************************************************************
        NOTE: If time_left() < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # TODO: finish this function!
        # raise NotImplementedError

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_move = (-1, -1)

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            return self.alphabeta(game, self.search_depth)

        except SearchTimeout:
            pass  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return best_move

    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf")):
        """Implement depth-limited minimax search with alpha-beta pruning as
        described in the lectures.

        This should be a modified version of ALPHA-BETA-SEARCH in the AIMA text
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Alpha-Beta-Search.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()


        # # TODO: finish this function!
        def terminal_test(game, depth):
            return depth == 0 or game.is_winner(self) or game.is_loser(self)

        def min_value(game, alpha, beta, depth):
            if terminal_test(game, depth):
                return self.score(game, self)

            moves = game.get_legal_moves()
            best_score = float('inf')
            for move in moves:
                newgame = game.forecast_move(move)
                score = max_value(newgame, alpha, beta, depth - 1)
                best_score = min(best_score, score)
                if best_score < alpha:
                    # return best_score
                    break
                beta = min(beta, best_score)
            return best_score

        def max_value(game, alpha, beta, depth):
            if terminal_test(game, depth):
                return self.score(game, self)

            moves = game.get_legal_moves()
            best_score = float('-inf')
            for move in moves:
                newgame = game.forecast_move(move)
                score = min_value(newgame, alpha, beta, depth - 1)
                best_score = max(best_score, score)
                if best_score > beta:
                    # return best_score
                    break
                alpha = max(alpha, best_score)
            return best_score

        best_action = (-1, -1)
        if terminal_test(game, depth):
            return best_action
        moves = game.get_legal_moves()
        best_score = float('-inf')
        for move in moves:
            newgame = game.forecast_move(move)
            score = min_value(newgame, alpha, beta, depth)
            # best_score = max(best_score, score)
            if best_score <= score:
                best_score = score
                best_action = move
            if best_score > beta:
                # return best_score
                break
            alpha = max(alpha, best_score)

        return best_action
