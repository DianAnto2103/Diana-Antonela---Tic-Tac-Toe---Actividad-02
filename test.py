import tictactoe as ttt

board = ttt.initial_state()
print("1. initial_state:", board)

# 2.Probar player (X empieza)
print("2. player (tablero vacío):", ttt.player(board))  

# 3.Probar actions (9 movimientos)
print("3. actions (vacio):", len(ttt.actions(board))) 

# 4.Probar result
board2 = ttt.result(board, (0, 0))
print("4. result (mover a 0,0):", board2)

# 5.Probar winner (sin ganador)
print("5. winner (sin ganador):", ttt.winner(board2)) 

# 6.Probar terminal
print("6. terminal (no terminó):", ttt.terminal(board2))  

# 7.Probar utility
print("7. utility:", "No aplica")

# 8.Probar minimax
print("8. minimax (primer movimiento):", ttt.minimax(board))
