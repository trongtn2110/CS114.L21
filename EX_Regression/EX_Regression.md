# Ex1: Dự đoán hướng đi của bão
>Input:   + hướng gió, vận tốc, áp suất : kiểu số thực tọa độ các ngày trước: ma trận 2x1
>
>Output:  + tọa độ bão các ngày sau: ma trận 2x1
>
>Cách thu thập: lấy dữ liệu từ các trung tâm dự báo khí tượng
>
>Xử lý dữ liệu:  loại bỏ những dữ liệu không cần thiết như nhiệt độ, độ ẩm,.. và quan tâm đến các yêu tố trong input, rồi thông kê tạo thành 1 file .csv
>
# Ex2: Dự đoán năng suất của cây 
>Input:   + lượng phân bón, lượng nước: kiểu số thực 
>         + năng suất trung bình của giống cây : kiểu số thực 
>         
>Output:  + năng suất cây trồng: kiểu số thực 
>
>Cách thu thập: lấy dữ liệu của các báo cáo khảo sát về năng suất từ các cánh đồng khác nhau 
>
>Xử lý dữ liệu: tạo một file CSV gồm các yếu tố như trong input qua 1 năm từ các cánh đồng.
>
# Ex3: Dự đoán mức thu nhập của sinh viên IT khi mới ra trường 
 >Input:  + Trình độ học vấn (kiểu số thực) 
 >        + Thành tựu đạt được trong quá trình học và thực tập (ta tạo bảng thành tựu và lựa chọn 0 và 1) 
 >        + Các kỹ năng giao tiếp (tạo bảng kỹ năng giao tiếp như ngoại ngữ, linh hoạt,.. và lựa chọn 0 và 1) 
 >        + Các chứng chỉ đạt được (dựa vào số điểm đạt được theo quy định của các trường đào tạo) 
 >        
 >Output: Mức lương trung bình khi được tuyển của sinh viên 
 >
 >Cách thu thập dữ liệu: thu thập dữ liệu từ các CV của sinh viên 
 >
 >Xử lý dữ liệu:  
 >        + Tạo một file CSV gồm các cột như trong input 
 >        + Nếu thông tin của một ô nào còn trống thì ta thay bằng NULL. 
