# TIC TAC TEC GAME BASE SCRIPT 
## COMAND LINE

Tic-tac-toe (American English), noughts and crosses (Commonwealth English), or Xs and Os (Canadian or Irish English) is a paper-and-pencil game for two players who take turns marking the spaces in a three-by-three grid with X or O. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is the winner. It is a solved game, with a forced draw assuming best play from both players.
Gameplay

Tic-tac-toe is played on a three-by-three grid by two players, who alternately place the marks X and O in one of the nine spaces in the grid.

In the following example, the first player (X) wins the game in seven steps:
Game of Tic-tac-toe, won by X

There is no universally-agreed rule as to who plays first, but in this article the convention that X plays first is used.

Players soon discover that the best play from both parties leads to a draw. Hence, tic-tac-toe is often played by young children who may not have discovered the optimal strategy.

Because of the simplicity of tic-tac-toe, it is often used as a pedagogical tool for teaching the concepts of good sportsmanship and the branch of artificial intelligence that deals with the searching of game trees. It is straightforward to write a computer program to play tic-tac-toe perfectly or to enumerate the 765 essentially different positions (the state space complexity) or the 26,830 possible games up to rotations and reflections (the game tree complexity) on this space.[1] If played optimally by both players, the game always ends in a draw, making tic-tac-toe a futile game.[2]
Incidence structure for tic-tac-toe

The game can be generalized to an m,n,k-game, in which two players alternate placing stones of their own color on an m-by-n board with the goal of getting k of their own color in a row. Tic-tac-toe is the 3,3,3-game.[3] Harary's generalized tic-tac-toe is an even broader generalization of tic-tac-toe. It can also be generalized as an nd game, specifically one in which n equals 3 and d equals 2.[4] It can be generalised even further by playing on an arbitrary incidence structure, where rows are lines and cells are points. Tic-tac-toe's incidence structure consists of nine points, three horizontal lines, three vertical lines, and two diagonal lines, with each line consisting of at least three points.
History

Games played on three-in-a-row boards can be traced back to ancient Egypt,[5] where such game boards have been found on roofing tiles dating from around 1300 BC.[6]

An early variation of tic-tac-toe was played in the Roman Empire, around the first century BC. It was called terni lapilli (three pebbles at a time) and instead of having any number of pieces, each player had only three; thus, they had to move them around to empty spaces to keep playing.[7] The game's grid markings have been found chalked all over Rome. Another closely related ancient game is three men's morris which is also played on a simple grid and requires three pieces in a row to finish,[8] and Picaria, a game of the Puebloans.

The different names of the game are more recent. The first print reference to "noughts and crosses" (nought being an alternative word for 'zero'), the British name, appeared in 1858, in an issue of Notes and Queries.[9] The first print reference to a game called "tick-tack-toe" occurred in 1884, but referred to "a children's game played on a slate, consisting of trying with the eyes shut to bring the pencil down on one of the numbers of a set, the number hit being scored".[This quote needs a citation] "Tic-tac-toe" may also derive from "tick-tack", the name of an old version of backgammon first described in 1558. The US renaming of "noughts and crosses" to "tic-tac-toe" occurred in the 20th century.[10]

In 1952, OXO (or Noughts and Crosses), developed by British computer scientist Sandy Douglas for the EDSAC computer at the University of Cambridge, became one of the first known video games.[11][12] The computer player could play perfect games of tic-tac-toe against a human opponent.[11]

In 1975, tic-tac-toe was also used by MIT students to demonstrate the computational power of Tinkertoy elements. The Tinkertoy computer, made out of (almost) only Tinkertoys, is able to play tic-tac-toe perfectly.[13] It is currently on display at the Museum of Science, Boston.
Combinatorics

When considering only the state of the board, and after taking into account board symmetries (i.e. rotations and reflections), there are only 138 terminal board positions. A combinatorics study of the game shows that when "X" makes the first move every time, the game outcomes are as follows:[14]

    91 distinct positions are won by (X)
    44 distinct positions are won by (O)
    3 distinct positions are drawn (often called a "cat's game"[15])

Strategy
Optimal strategy for player X if starting in middle. In each grid, the shaded red X denotes the optimal move, and the location of O's next move gives the next subgrid to examine. Note that only two sequences of moves by O (both starting with the center, top-right, left-mid) lead to a draw, with the remaining sequences leading to wins from X.
Optimal strategy for player O. Player O can only force a win or draw by playing in the center first.

A player can play a perfect game of tic-tac-toe (to win or at least draw) if, each time it is their turn to play, they choose the first available move from the following list, as used in Newell and Simon's 1972 tic-tac-toe program.[16]

    Win: If the player has two in a row, they can place a third to get three in a row.
    Block: If the opponent has two in a row, the player must play the third themselves to block the opponent.
    Fork: Cause a scenario where the player has two ways to win (two non-blocked lines of 2).
    Blocking an opponent's fork: If there is only one possible fork for the opponent, the player should block it. Otherwise, the player should block all forks in any way that simultaneously allows them to make two in a row. Otherwise, the player should make a two in a row to force the opponent into defending, as long as it does not result in them producing a fork. For example, if "X" has two opposite corners and "O" has the center, "O" must not play a corner move to win. (Playing a corner move in this scenario produces a fork for "X" to win.)
    Center: A player marks the center. (If it is the first move of the game, playing a corner move gives the second player more opportunities to make a mistake and may therefore be the better choice; however, it makes no difference between perfect players.)
    Opposite corner: If the opponent is in the corner, the player plays the opposite corner.
    Empty corner: The player plays in a corner square.
    Empty side: The player plays in a middle square on any of the four sides.

The first player, who shall be designated "X", has three possible strategically distinct positions to mark during the first turn. Superficially, it might seem that there are nine possible positions, corresponding to the nine squares in the grid. However, by rotating the board, we will find that, in the first turn, every corner mark is strategically equivalent to every other corner mark. The same is true of every edge (side middle) mark. From a strategic point of view, there are therefore only three possible first marks: corner, edge, or center. Player X can win or force a draw from any of these starting marks; however, playing the corner gives the opponent the smallest choice of squares which must be played to avoid losing.[17] This might suggest that the corner is the best opening move for X, however another study[18] shows that if the players are not perfect, an opening move in the center is best for X.

The second player, who shall be designated "O", must respond to X's opening mark in such a way as to avoid the forced win. Player O must always respond to a corner opening with a center mark, and to a center opening with a corner mark. An edge opening must be answered either with a center mark, a corner mark next to the X, or an edge mark opposite the X. Any other responses will allow X to force the win. Once the opening is completed, O's task is to follow the above list of priorities in order to force the draw, or else to gain a win if X makes a weak play.

More detailed, to guarantee a draw, O should adopt the following strategies:

    If X plays a corner opening move, O should take center, and then an edge, forcing X to block in the next move. This will stop any forks from happening. When both X and O are perfect players and X chooses to start by marking a corner, O takes the center, and X takes the corner opposite the original. In that case, O is free to choose any edge as its second move. However, if X is not a perfect player and has played a corner and then an edge, O should not play the opposite edge as its second move, because then X is not forced to block in the next move and can fork.
    If X plays edge opening move, O should take center or one of the corners adjacent to X, and then follow the above list of priorities, mainly paying attention to block forks.
    If X plays the center opening move, O should take a corner, and then follow the above list of priorities, mainly paying attention to block forks.

When X plays corner first, and O is not a perfect player, the following may happen:

    If O responds with a center mark (best move for them), a perfect X player will take the corner opposite the original. Then O should play an edge. However, if O plays a corner as its second move, a perfect X player will mark the remaining corner, blocking O's 3-in-a-row and making their own fork.
    If O responds with a corner mark, X is guaranteed to win, by simply taking any of the other two corners and then the last, a fork. (since when X takes the third corner, O can only take the position between the two Xs. Then X can take the only remaining corner to win)
    If O responds with an edge mark, X is guaranteed to win, by taking center, then O can only take the corner opposite the corner which X plays first. Finally, X can take a corner to create a fork, and then X will win on the next move.

Further details

Consider a board with the nine positions numbered as follows:
 1  	 2  	 3 
 4  	 5  	 6 
 7  	 8  	 9 

When X plays 1 as their opening move, then O should take 5. Then X takes 9 (in this situation, O should not take 3 or 7, O should take 2, 4, 6 or 8):

    X1 → O5 → X9 → O2 → X8 → O7 → X3 → O6 → X4, this game will be a draw.

or 6 (in this situation, O should not take 4 or 7, O should take 2, 3, 8 or 9. In fact, taking 9 is the best move, since a non-perfect player X may take 4, then O can take 7 to win).

    X1 → O5 → X6 → O2 → X8, then O should not take 3, or X can take 7 to win, and O should not take 4, or X can take 9 to win, O should take 7 or 9.
        X1 → O5 → X6 → O2 → X8 → O7 → X3 → O9 → X4, this game will be a draw.
        X1 → O5 → X6 → O2 → X8 → O9 → X4 (7) → O7 (4) → X3, this game will be a draw.
    X1 → O5 → X6 → O3 → X7 → O4 → X8 (9) → O9 (8) → X2, this game will be a draw.
    X1 → O5 → X6 → O8 → X2 → O3 → X7 → O4 → X9, this game will be a draw.
    X1 → O5 → X6 → O9, then X should not take 4, or O can take 7 to win, X should take 2, 3, 7 or 8.
        X1 → O5 → X6 → O9 → X2 → O3 → X7 → O4 → X8, this game will be a draw.
        X1 → O5 → X6 → O9 → X3 → O2 → X8 → O4 (7) → X7 (4), this game will be a draw.
        X1 → O5 → X6 → O9 → X7 → O4 → X2 (3) → O3 (2) → X8, this game will be a draw.
        X1 → O5 → X6 → O9 → X8 → O2 (3, 4, 7) → X4/7 (4/7, 2/3, 2/3) → O7/4 (7/4, 3/2, 3/2) → X3 (2, 7, 4), this game will be a draw.

In both of these situations (X takes 9 or 6 as the second move), X has a 1/3 property to win.

If X is not a perfect player, X may take 2 or 3 as a second move. Then this game will be a draw, X cannot win.

    X1 → O5 → X2 → O3 → X7 → O4 → X6 → O8 (9) → X9 (8), this game will be a draw.
    X1 → O5 → X3 → O2 → X8 → O4 (6) → X6 (4) → O9 (7) → X7 (9), this game will be a draw.

If X plays 1 opening move, and O is not a perfect player, the following may happen:

Although O takes the only good position (5) as the first move, O takes a bad position as the second move:

    X1 → O5 → X9 → O3 → X7, then X can take 4 or 8 to win.
    X1 → O5 → X6 → O4 → X3, then X can take 7 or 9 to win.
    X1 → O5 → X6 → O7 → X3, then X can take 2 or 9 to win.

Although O takes good positions in the first two moves, O takes a bad position in the third move:

    X1 → O5 → X6 → O2 → X8 → O3 → X7, then X can take 4 or 9 to win.
    X1 → O5 → X6 → O2 → X8 → O4 → X9, then X can take 3 or 7 to win.

O takes a bad position as first move (except of 5, all other positions are bad):

    X1 → O3 → X7 → O4 → X9, then X can take 5 or 8 to win.
    X1 → O9 → X3 → O2 → X7, then X can take 4 or 5 to win.
    X1 → O2 → X5 → O9 → X7, then X can take 3 or 4 to win.
    X1 → O6 → X5 → O9 → X3, then X can take 2 or 7 to win.