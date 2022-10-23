line1 = input().strip()
line2 = input().strip()
line3 = input().strip()
line4 = input().strip()
line5 = input().strip()

num_knights = line1.count("k") +line2.count("k") + line3.count("k") + line4.count("k") + line5.count("k")
valid = True

board = [list(line1), list(line2), list(line3), list(line4), list(line5)]

if num_knights == 9:
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == 'k':
                if x + 1 in range(0, len(board) - 1) and y + 2 in range(0, len(board) - 1):
                    if board[x + 1][y + 2] == 'k':
                        valid = False
                if x - 1 in range(0, len(board) - 1) and y + 2 in range(0, len(board) - 1):
                    if board[x - 1][y + 2] == 'k':
                        valid = False  
                if x + 1 in range(0, len(board) - 1) and y - 2 in range(0, len(board) - 1):
                    if board[x + 1][y - 2] == 'k':
                        valid = False
                if x - 1 in range(0, len(board) - 1) and y - 2 in range(0, len(board) - 1):
                    if board[x - 1][y - 2] == 'k':
                        valid = False
                if x + 2 in range(0, len(board) - 1) and y + 1 in range(0, len(board) - 1):
                    if board[x + 2][y + 1] == 'k':
                        valid = False
                if x + 2 in range(0, len(board) - 1) and y - 1 in range(0, len(board) - 1):
                    if board[x + 2][y - 1] == 'k':
                        valid = False
                if x - 2 in range(0, len(board) - 1) and y + 1 in range(0, len(board) - 1):
                    if board[x - 2][y + 1] == 'k':
                        valid = False
                if x - 2 in range(0, len(board) - 1) and y - 1 in range(0, len(board) - 1):
                    if board[x - 2][y - 1] == 'k':
                        valid = False
else:
    valid = False
    
if valid:
    print('valid')
else:
    print('invalid')
    