# HƯỚNG DẪN

## Giới thiệu
- Kết nối từ key trong một câu hỏi đến câu trả lời (Phần 1)
- Từ câu trả lời phát thành file âm thanh (Phần 2)

## Phần 1
### Mô tả:

- Mô tả

    - Mục đích: Từ một tập hợp key của câu hỏi ban đầu trả về câu trả lời
    - Class nằm trong thư mục mapping_folder
    - Các file liên quan:
       + **mapping_key.py** : chứa thông tin về class
       + **ans_room.csv** : chứa thông tin về câu trả lời liên quan đến các phòng theo ID của các phòng
       + **key_name_other.csv**: bao gồm thông tin tên gọi của các phòng liên quan đến ID của các phòng đó
       + **key_room.txt**: chứa thông tin về ID của các phòng hiện có
       + **key_to_room.csv**: chứa thông tin về ID và tên phòng theo ID đó
       + **name_other.txt**: chứa tên gọi của các phòng
       + **target.csv**: chứa yêu cầu của người dùng kết nối ID
            
            
            
### Trong file **mapping_key.py** chứa các hàm:


- Thông tin các hàm

    - **adding_name_room**:
        + Mục đích: bổ sung thêm các tên gọi khác của phòng
        + Đầu vào: Gồm hai tham số. Tham số thứ nhất là tên gọi của phòng, tham số thứ 2 là ID của phòng
        + Đầu ra: Không có
    - **adding_target_room**:
        + Mục đích: bổ sung thêm những yêu cầu của người dùng có thể hỏi liên quan đến mục đích
        + Đầu vào: Gồm hai tham số. Tham số thứ nhất là yêu cầu mới, tham số thứ 2 là ID liên quan đến phòng xử  lý yêu cầu đó
        + Đầu ra: Không có
    - **is_room**:
        + Mục đích: Kiểm tra xem liệu key đó có phải là phòng hay là yêu cầu
        + Đầu vào: Key để kiểm tra xem liệu đó là phòng hay không
        + Đầu ra: là phòng học hoặc 
    - **target_room**:
        + Mục đích: Kiểm tra xem key thuộc theo yêu cầu nào và đưa về ID liên quan đến yêu cầu 
        + Đầu vào: Key chứa yêu cầu
        + Đầu ra: ID của phòng xử lý yêu cầu
    - **return_key**:
        + Mục đích: Trả về tập câu trả lời liên quan đến câu hỏi
        + Đầu vào: Tập key được lấy ra từ câu hỏi
        + Đầu ra: Tập câu trả lời
        
## Demo
- Hàm **return_key**


```python
from mapping_key import mapping
x = mapping()
key = ['tài vụ','hành chính']
x.return_key(key)
```




    [['phòng', 'tài vụ', 'nằm tại tầng 1 dãy nhà a tòa nhà học'],
     ['phòng', 'hành chính', 'nằm tại tầng 1 dãy nhà a tòa nhà học']]



## Phần 2
### Mô tả:
- Thông tin:

    - Mục đích: Từ một tập hợp câu trả lời ban đầu trả về đường dẫn file âm thanh hoặc phát file âm thanh
    - Class nằm trong thư mục mapping_ans_to_speech
    - Các file liên quan:
       + **ans_to_speech.py** : chứa thông tin về class
       + **key_speech.csv** : chứa thông tin về câu trả lời kết đến file âm thanh
       + **name_speech.txt**: chứa thông tin về các câu trả lời
       + **folder_record**: thư mục chứa các file âm thanh
       
### Trong file **ans_to_speech.py** chứa các hàm:

- Thông tin các hàm:
    - **return_speech**:
        + Mục đích: Trả về danh sách đường dẫn của câu trả lời
        + Đầu vào: Tập các câu trả lời
        + Đầu ra: Đường dẫn file âm thanh của các câu trả lời đó
    - **play_sound_from_ans_room**:
        + Mục đích: Phát file âm thanh từ danh sách câu trả lời
        + Đầu vào: Tập các câu trả lời
        + Đầu ra: Danh sách đường dẫn file âm thanh của các câu trả lời đó
    - **play_sound_with_path**:
        + Mục đích: Phát file âm thanh từ danh sách đường dẫn
        + Đầu vào: Danh sách đường dẫn file âm thanh của các câu trả lời
        + Đầu ra: Không có
    - **return_ans**:
        + Mục đích: Trả về danh sách đường dẫn đến các câu trả lời từ key của các câu hỏi
        + Đầu vào: key được trích xuất ra từ câu hỏi
        + Đầu ra: Danh sách đường dẫn đến các file âm thanh của câu trả lời

## Demo
- Sử dụng từ key phát sáng file âm thanh


```python
import sys
sys.path.insert(1, './mapping_ans_to_speech')
from ans_to_speech import answer_to_speech
k = answer_to_speech('./mapping_ans_to_speech/')
key_ask = ['đào tạo','quan hệ công chúng','ăn uống']
list_speech=k.return_ans(key_ask)
k.play_sound_with_path(list_speech)
```

    phòng
    đào tạo
    nằm tại tầng 1 dãy nhà a tòa nhà học
    phòng
    quan hệ công chúng
    nằm tại tầng 2 tòa nhà giảng đường và hội trường
    bạn có thể  đến
    căn tin
    nằm bên phải cổng phụ đi vào và đối diện cửa ra vào dãy nhà b tòa nhà học
