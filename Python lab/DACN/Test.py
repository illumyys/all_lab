import cv2
import numpy as np
from random import choice

def getColor():
    lstColor = [[255,64,64],[255,165,0],[255,244,79],[102,255,0],[172,229,238],[148,87,235],[148,87,235],[241,156,187]]
    return choice(lstColor)

def getInfo(piece):
    if piece == "":
        coords = np.array([[0, 0]])
    elif piece == "I":
        coords = np.array([[0, 3], [0, 4], [0, 5], [0, 6]])
    elif piece == "T":
        coords = np.array([[1, 3], [1, 4], [1, 5], [0, 4]])
    elif piece == "L":
        coords = np.array([[1, 3], [1, 4], [1, 5], [0, 5]])
    elif piece == "J":
        coords = np.array([[1, 3], [1, 4], [1, 5], [0, 3]])
    elif piece == "S":
        coords = np.array([[1, 5], [1, 4], [0, 3], [0, 4]])
    elif piece == "Z":
        coords = np.array([[1, 3], [1, 4], [0, 4], [0, 5]])
    else:
        coords = np.array([[0, 4], [0, 5], [1, 4], [1, 5]])
    
    return coords, getColor()

def display(board, coords, color, next_info, held_info, score, SPEED):
    # Tạo màn hình hiển thị
    
    border = np.uint8(127 - np.zeros([20, 1, 3]))
    border_ = np.uint8(127 - np.zeros([1, 23, 3]))
    
    dummy = board.copy()
    dummy[coords[:,0], coords[:,1]] = color
    
    right = np.uint8(np.zeros([20, 10, 3]))
    right[next_info[0][:,0] + 2, next_info[0][:,1]] = next_info[1]
    
    dummy = np.concatenate(( border, dummy, border, right, border), 1)
    dummy = np.concatenate((border_, dummy, border_), 0)
    dummy = dummy.repeat(20, 0).repeat(20, 1)
    dummy = cv2.putText(dummy, str(score), (325, 150), cv2.FONT_HERSHEY_DUPLEX, 1, [0, 0, 255], 2)
    
    # Hướng dẫn cho người chơi
    index_pos = 300
    x_index_pos = 300
    dummy = cv2.putText(dummy, "A - left", (x_index_pos, index_pos), cv2.FONT_HERSHEY_DUPLEX, 0.6, [0, 0, 234])
    dummy = cv2.putText(dummy, "D - right", (x_index_pos, index_pos+25), cv2.FONT_HERSHEY_DUPLEX, 0.6, [0, 0, 234])
    dummy = cv2.putText(dummy, "S - drain", (x_index_pos, index_pos+50), cv2.FONT_HERSHEY_DUPLEX, 0.6, [0, 0, 234])
    dummy = cv2.putText(dummy, "W - rotate", (x_index_pos, index_pos+75), cv2.FONT_HERSHEY_DUPLEX, 0.6, [0, 0, 234])
    
    cv2.imshow("Tetris", dummy)
    key = cv2.waitKey(int(1000/SPEED))
    
    return key

def getNextPiece():
    next_piece = choice(["O", "I", "S", "Z", "L", "J", "T"])

    return next_piece

SPEED = 1 # Kiểm soát tốc độ của các mảnh tetris

# Làm một bảng

board = np.uint8(np.zeros([20, 10, 3]))

# Khởi tạo một số biến

quit = False
place = False
drop = False
switch = False
held_piece = ""
flag = 0
score = 0
next_piece =""
current_piece = ""
# Tất cả các mảnh tetris



if __name__ == "__main__":
    next_piece = getNextPiece()
    while not quit:
        # Kiểm tra xem người dùng có muốn trao đổi các phần được giữ và hiện tại không
        if switch:
           # Trao đổi tổ chức và mảnh hiện tại
            held_piece, current_piece = current_piece, held_piece
            switch = False
        else:
            # Tạo phần tiếp theo và cập nhật phần hiện tại
            current_piece = next_piece
            next_piece = getNextPiece()

        if flag > 0:
            flag -= 1

        # Xác định màu sắc và vị trí của các mảnh hiện tại, tiếp theo và được giữ
        
        held_info = getInfo(held_piece)
        next_info = getInfo(next_piece)
        coords, color = getInfo(current_piece)
        if current_piece == "I":
            top_left = [-2, 3]

        if not np.all(board[coords[:,0], coords[:,1]] == 0):
            break

        while True:
            # Hiển thị bảng và nhấn phím
            key = display(board, coords, color, next_info, held_info, score, SPEED)
            # Tạo một bản sao của vị trí
            dummy = coords.copy()
            print("speed ",SPEED, "key ",key," ", ord("s"))

            if key == ord("s"):
                drop = True

            elif key == ord("a"):
                # Di chuyển mảnh sang trái nếu nó không dựa vào bức tường bên trái
                if np.min(coords[:,1]) > 0:
                    coords[:,1] -= 1
                if current_piece == "I":
                    top_left[1] -= 1
            elif key == ord("d"):
                # Di chuyển mảnh sang phải nếu nó không dựa vào bức tường bên phải
                if np.max(coords[:,1]) < 9:
                    coords[:,1] += 1
                    if current_piece == "I":
                        top_left[1] += 1
            
            elif key == ord("w"):
                        # Cơ chế quay
                
                if current_piece != "I" and current_piece != "O":
                    if coords[1,1] > 0 and coords[1,1] < 9:
                        arr = coords[1] - 1 + np.array([[[x, y] for y in range(3)] for x in range(3)])
                        pov = coords - coords[1] + 1
                        
                elif current_piece == "I":
                    # Đoạn thẳng có mảng 4x4 nên cần code riêng
                    
                    arr = top_left + np.array([[[x, y] for y in range(4)] for x in range(4)])
                    pov = np.array([np.where(np.logical_and(arr[:,:,0] == pos[0], arr[:,:,1] == pos[1])) for pos in coords])
                    pov = np.array([k[0] for k in np.swapaxes(pov, 1, 2)])
                
                # Xoay mảng và định vị lại phần đó về vị trí hiện tại
                
                if current_piece != "O":
                    if key == ord("j"):
                        arr = np.rot90(arr, -1)
                    else:
                        arr = np.rot90(arr)
                    coords = arr[pov[:,0], pov[:,1]]
                # Hard drop set to true
                # drop = True
            elif key == ord("i"):
                # Thoát khỏi vòng lặp và yêu cầu chương trình chuyển đổi các phần được giữ và phần hiện tại
                if flag == 0:
                    if held_piece == "":
                        held_piece = current_piece
                    else:
                        switch = True
                    flag = 2
                    break
            elif key == 8 or key == 27:
                quit = True
                break

            # Kiểm tra xem quân cờ có chồng lên các quân cờ khác hay nằm ngoài bàn cờ hay không và nếu có, hãy thay đổi vị trí về vị trí trước khi có điều gì đó xảy ra
            
            if np.max(coords[:,0]) < 20 and np.min(coords[:,0]) >= 0:
                if not (current_piece == "I" and (np.max(coords[:,1]) >= 10 or np.min(coords[:,1]) < 0)):
                    if not np.all(board[coords[:,0], coords[:,1]] == 0):
                        coords = dummy.copy()
                else:
                    coords = dummy.copy()
            else:
                coords = dummy.copy()
            
            if drop:
            # Mỗi lần lặp của vòng lặp sẽ di chuyển mảnh xuống 1 và nếu mảnh đó nằm trên mặt đất hoặc mảnh khác thì nó dừng lại và đặt nó vào vị trí
                while not place:
                    if np.max(coords[:,0]) != 19:
                        # Kiểm tra xem mảnh có nằm trên thứ gì không
                        for pos in coords:
                            if not np.array_equal(board[pos[0] + 1, pos[1]], [0, 0, 0]):
                                place = True
                                break
                    else:
                        # Nếu vị trí của mảnh nằm ở mặt đất thì nó đặt
                        place = True
                    
                    if place:
                        break
                    
                    # Tiếp tục đi xuống và kiểm tra khi nào mảnh cần được đặt
                    
                    coords[:,0] += 1
                    
                    if current_piece == "I":
                        top_left[0] += 1
                        
                drop = False

            else:
                # Kiểm tra xem mảnh có cần được đặt không
                if np.max(coords[:,0]) != 19:
                    for pos in coords:
                        if not np.array_equal(board[pos[0] + 1, pos[1]], [0, 0, 0]):
                            place = True
                            break
                else:
                    place = True
                
            if place:
                # Đặt mảnh vào vị trí của nó trên bảng
                for pos in coords:
                    board[tuple(pos)] = color
                    
                # Đặt lại vị trí thành Sai
                place = False
                break

            # Giảm xuống 1

            coords[:,0] += 1
            if current_piece == "I":
                top_left[0] += 1

        # Xóa các dòng và cũng đếm xem có bao nhiêu dòng đã bị xóa và cập nhật điểm
        
        lines = 0
                
        for line in range(20):
            if np.all([np.any(pos != 0) for pos in board[line]]):
                lines += 1
                board[1:line+1] = board[:line]
                        
        
        score += lines*10