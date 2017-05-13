# Goals
This  paper  introduces  a  new  technique(min/max approximation) for  searching  in  game  trees,  based  on the  idea  of  approximating  the  min  and  max  operators  with  generalized mean-value  operators.

# Techniques
## generalized mean values
![p-mean of a](http://i2.muimg.com/588926/cdb108d846085f93.png)

Base on the following two facts,we use $M_{p}(a)$ as approximation to min/max function in minimax algorithm.

![twofacts](http://i2.muimg.com/588926/338bb1aff7eb22ca.png)

$M_{p}(a)$,unlike max or min ,has continuous derivatives with respect to each variable.So they are more suitable for analysis.
## game trees searching
- game tree
    - consider a two-person zero-sum perfect information game
- searching a game tree
    - heuristic approximations
        -  For most interesting games the game tree is so large that heuristic approximations are needed.
        - Our proposed technique requires a single static evaluator
approximations are needed.
    - interactive deepening
        - Given a limit on timeout,one can successively compute the backed-up for depths,until one runs out of time,use the move determined by the last search completed.
- iteractive search heuristic details
    - The general process of partially exploring a game tree by an iterative heuristic:
![general process](http://i2.muimg.com/588926/70d71a018fb0aecb.png)
![formula9](http://i2.muimg.com/588926/60815f6c4fd6721f.png)
- penalty-based iterative search methods
    - the min/max approximation technique here is such a penalty-based scheme: to expand that tip node which has the least penalty.We add  the node's children to the tree,update the estimates,and update the  penalties on the edges.
- searching by min/max approximation
    - The  "min/max  approximation"  heuristic is special case of the  penalty-based search method,where the penalties are defined in terms  of the derivatives of the approximating functions $M_{p}(a)$.

# Results：min/max approximation is definitely superior.
- The number of distinct position considered by alpha-beta was
approximately three times larger than the number of distinct positions  considered by min/max when a timeout was in effect.
- Minimax search with alpha-beta pruning called the move operator approximately 3500 times/s,while the min/max heuristic called the move operator approximately 800 times/s.
# conclusion
This paper provides a novel approach to game tree searching,based  on approximating min/max functions by suitable generalized mean-value functions which outplays alpha-beta with iterative deepening.
