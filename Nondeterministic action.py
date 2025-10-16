###### nhóm thuật toán trong môi trường phức tạp
# 1 hành động có thể sinh ra nhìu tt khác nhau, ko biết trc đc tt nào sẽ xảy ra
#vd: xác định đặt xe vào (0,0), nhưng bị run tay đặt nhầm vào (0,1) hoặc (1,0)
# đổi tên từ tt ban đầu thành tt niềm tin ban đầu
# học 2 thuật toán AND OR và
# tìm kiếm trong môi trường ko nhìn thấy( ko xác định)(đích và đầu đều đoán)
# # tt ban đầu: chỉ 1 có 1tt, action là 1 hành động, cho cố định hoặc random
# làm BFS, DFS cho dễ
# xây dựng hàm tính chi phí từ tập niềm tin ban đầu tới tập đang xét
# tt niềm tin là 1 tập hợp các tt có thể xảy ra, action là hợp của các hành động có thể xảy ra từ các tt trong tập hợp
# vd trước đây đưa 1 tt vào queue, bây giờ đưa 1 tập hợp các tt vào queue
# lấy tập các tt ra xét có là mục tiêu ko, là mục tiêu chỉ khi từng tt trong tập thuộc tập mục tiêu   

####Tìm kiếm trong môi trường nhìn thấy một phần ( có thể áp dụng BFS, DFS)
# đích và đầu đều đoán
# sẽ cho biết thông tin 1 trạng thái đặt 1 quân, sử dụng thông tin đó để xấy dựng tt niềm tin bắt đầu và mục tiêu, dễ đoán hơn và giảm bớt các tt sinh kế tiếp
# chỉ sinh ra tt mà thỏa mãn thông tin cho trước( cố định con đã cho trước), mỗi hành động đặt or di chuyển đều được giữ nguyên (nếu thực hiện hành động gây xung đột)
