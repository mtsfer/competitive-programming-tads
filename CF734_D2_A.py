numberOfChessGamePlayed: int = int(input())
outcomeOfGames: str = input()
antonWins: int = outcomeOfGames.count('A')
danikWins: int = numberOfChessGamePlayed - antonWins

if antonWins == danikWins:
    print("Friendship")
elif antonWins > danikWins:
    print("Anton")
else:
    print("Danik")
