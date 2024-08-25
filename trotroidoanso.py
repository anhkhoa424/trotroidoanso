# Trong code này, nhập vào một số
# Kiểm tra xem số âm hay dương
# hay bằng không và hiển thị
# number = float(input("Nhập một số: "))
# if number >= 0:
#    if number == 0:
#        print("Số Không")
#    else:
#        print("Số dương")
# else:
#    print("Số âm")
# sotuoi = float(input("mời bạn nhập số tuổi:"))
# if sotuoi <=15:
#     print("tuổi trẻ em")
# elif sotuoi <=18:
#     print('tuổi thiếu niên')
# elif sotuoi <=50:
#     print('tuổi lao động')
# elif sotuoi <=70:
#     print('tuổi trung niên')
# elif sotuoi >70:
#     print('tuổi già')
# else:
#     print('không hợp lệ')
import random
    
number = random.randint(1, 10)
đoán = None
    
while  đoán != number:
    đoán = input('hãy nhập một số từ 1 đến 10')
    
    if đoán  == number:
        print("Xin chúc mừng Bạn đã thắng")
        break
    else:
        print("không xin lỗi. Hãy thử lại")
