def minimax(self, game, depth):
    '''
    return a tuple (x, y): x, y int in [1, 7]
    or (-1, -1) if no legal moves
    '''
    if self.time_left() < self.TIMER_THRESHOLD:
        raise SearchTimeout()

    def terminal_test(game, depth):
        return depth == 0 or game.is_winner(self) or game.is_loser(self)

    def min_value(game, depth):
        if terminal_test(game, depth):
            return self.score(game, self) # score函数恰好有三类结过
        # 只要没有输赢，moves 就不会是空的
        moves = game.get_legal_moves()

        # 选取最佳move对应的分数；
        # 每个move的分数都决定于depth之后的状态得分（提前结束返回正负无穷）
        # v的初值怎么赋：不影响正常值，在去极限是，也能正确返回,初值是最坏的选择
        v = float('inf')
        for move in moves:
            newgame = game.forecast_move(move)
            score = max_value(newgame, depth - 1) # 交替进行
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
            v = max(v, score)
        return v

    # 从min开始，其实就是min_value跑一遍，但是哟啊返回move
    if terminal_test(game, depth):
        return (-1, -1)

    best_score = float('-inf')
    best_action = (-1, -1)
    if terminal_test(game, depth):
        return best_action

    moves = game.get_legal_moves()

    for move in moves:
        newgame = game.forecast_move(move)
        v = min_value(newgame, depth)
        if v >= best_score:
            best_score = v
            best_action = move

    return best_action


def alphabeta(self, game, depth ,alpha=float('-inf'), beta=float('inf')):
    if self.time_left() < self.TIMER_THRESHOLD:
        raise SearchTimeout()

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
