<h1 align="center">♜ 8-Rooks Visualizer with AI Algorithms</h1>

<div align="center">
  <p><b>Đồ án cá nhân Trí tuệ Nhân tạo</b><br>
  <b>Sinh viên thực hiện:</b> Trịnh Nhật Anh — <b>MSSV:</b> 23110074<br>
  <b>Giảng viên hướng dẫn:</b> TS. Phan Thị Huyền Trang</p>
</div>

<hr>

<h2> Mục lục</h2>
<ul>
  <li><a href="#giới-thiệu">Giới thiệu</a></li>
  <li><a href="#mục-tiêu">Mục tiêu</a></li>
  <li><a href="#nội-dung-dự-án">Nội dung dự án</a></li>
  <li><a href="#thuật-toán">Thuật toán</a>
    <ul>
      <li><a href="#31-tìm-kiếm-không-thông-tin-uninformed-search">3.1. Tìm kiếm không thông tin (Uninformed Search)</a></li>
      <li><a href="#32-tìm-kiếm-có-thông-tin-informed-search">3.2. Tìm kiếm có thông tin (Informed Search)</a></li>
      <li><a href="#33-tìm-kiếm-cục-bộ-local-search">3.3. Tìm kiếm cục bộ (Local Search)</a></li>
      <li><a href="#34-tìm-kiếm-trong-môi-trường-phức-tạp-complex-environment-search">3.4. Tìm kiếm trong môi trường phức tạp</a></li>
      <li><a href="#35-tìm-kiếm-có-điều-kiện-ràng-buộc-constraint-satisfaction-problem">3.5. Bài toán ràng buộc (CSP)</a></li>
    </ul>
  </li>
  <li><a href="#đánh-giá--so-sánh-hiệu-suất">Đánh giá & so sánh hiệu suất</a></li>
  <li><a href="#cấu-trúc-thư-mục">Cấu trúc thư mục</a></li>
  <li><a href="#giấy-phép--trích-dẫn">Giấy phép & trích dẫn</a></li>
</ul>

<hr>

<h2 id="giới-thiệu">Giới thiệu</h2>
<p>
<b>8-Rooks</b> là một bài toán yêu cầu đặt 8 quân Xe lên bàn cờ 8×8 sao cho
không có hai quân nào ăn nhau. Điều đó đồng nghĩa mỗi hàng và mỗi cột chỉ có duy nhất một quân Xe.
</p>

<hr>

<h2 id="mục-tiêu">Mục tiêu</h2>
<ul>
  <li><b>Triển khai đa thuật toán:</b> Bao gồm Uninformed, Informed, Local Search, Complex Environment và CSP – minh họa cách vận hành các phương pháp AI cổ điển.</li>
  <li><b>So sánh hiệu suất:</b> thời gian chạy (<code>elapsed_s</code>), số trạng thái duyệt (<code>nodes_visited</code>), bộ nhớ (<code>peak_mem_mb</code>), chi phí (<code>solution_cost</code>).</li>
  <li><b>Trực quan hoá:</b> giao diện đồ họa hiển thị trạng thái, tiến trình và thống kê.</li>
</ul>

<hr>

<h2 id="nội-dung-dự-án">Nội dung dự án</h2>
<p>Dự án tích hợp các nhóm thuật toán và chuẩn hóa giao diện đo lường:</p>
<ul>
  <li><b>Uninformed Search:</b> BFS, DFS, UCS, IDS.</li>
  <li><b>Informed Search:</b> Greedy Best-First, A*, IDA*.</li>
  <li><b>Local Search:</b> Hill Climbing, Simulated Annealing, Genetic, Beam Search.</li>
  <li><b>Complex Environment Search:</b> AND-OR Search, Partially Observable, No Observation.</li>
  <li><b>Constraint Satisfaction (CSP):</b> Backtracking, ForwardingChecking.</li>
</ul>
<p>Mỗi thuật toán kèm mô tả ngắn, ý tưởng, tham số, <b>ảnh GIF minh hoạ</b> (nếu có) và <b>chỉ số hiệu suất</b>.</p>

<hr>

<h2 id="thuật-toán">Thuật toán</h2>

<h3 id="31-tìm-kiếm-không-thông-tin-uninformed-search">3.1. Tìm kiếm không thông tin (Uninformed Search)</h3>

<h4>3.1.1. Thành phần bài toán</h4>
<ul>
  <li><b>Trạng thái:</b> mỗi trạng thái là danh sách (hoặc tuple) gồm các cặp (row, col) biểu diễn vị trí của các Xe.</li>
  <li><b>Hành động:</b> đặt thêm một Xe vào hàng kế tiếp ở cột hợp lệ.</li>
  <li><b>Mục tiêu:</b> đạt trạng thái có đủ n Xe, mỗi Xe ở hàng và cột khác nhau.</li>
  <li><b>Chi phí:</b> mỗi bước = 1 (không dùng heuristic).</li>
</ul>

<p>
<b>Lời giải</b> là chuỗi trạng thái và hành động từ gốc → đích.<br>
Kết quả gồm: <code>path</code>, <code>nodes_visited</code>, <code>solution_depth</code>, v.v.
</p>

<h2 align="center">🔹 Thuật toán BFS – Breadth-First Search</h2>

<p>
Thuật toán <b>BFS (Breadth-First Search)</b> là phương pháp duyệt theo chiều rộng, nghĩa là
khám phá tất cả các trạng thái ở cùng một mức độ sâu trước khi mở rộng sang mức kế tiếp.
Trong bài toán <b>8 quân Xe</b>, mỗi trạng thái biểu diễn một tập hợp vị trí hợp lệ của các Xe
(tránh trùng hàng và trùng cột). BFS bắt đầu từ trạng thái rỗng, sau đó lần lượt
đặt Xe theo từng hàng, đảm bảo tìm được lời giải ngắn nhất nếu tồn tại.
</p>

<ul>
  <li><b>Cấu trúc dữ liệu sử dụng:</b> Hàng đợi (<code>Queue</code>).</li>
  <li><b>Chiến lược tìm kiếm:</b> Duyệt tuần tự theo từng lớp độ sâu.</li>
  <li><b>Đặc điểm:</b> Hoàn chỉnh và cho lời giải tối ưu khi chi phí mỗi bước là như nhau.</li>
</ul>


<p align="center">
  🔗 <a href="https://www.geeksforgeeks.org/dsa/breadth-first-search-or-bfs-for-a-graph/" target="_blank">
  Tìm hiểu thêm về BFS trên GeeksforGeeks</a>
</p>

<hr>

<h4>📊 Phân tích nhanh</h4>
<ul>
  <li><b>Độ phức tạp thời gian:</b> O(b<sup>d</sup>), với b là số nhánh trung bình và d là độ sâu đích.</li>
  <li><b>Độ phức tạp bộ nhớ:</b> O(b<sup>d</sup>) – do cần lưu trữ toàn bộ hàng đợi.</li>
  <li><b>Ưu điểm:</b> Dễ cài đặt, đảm bảo tìm được lời giải tối ưu (nếu có).</li>
  <li><b>Nhược điểm:</b> Tốn nhiều bộ nhớ khi không gian trạng thái lớn.</li>
</ul>


<h2 align="center">🔹 Thuật toán DFS – Depth-First Search</h2>

<p>
Thuật toán <b>DFS (Depth-First Search)</b> tìm kiếm theo <b>chiều sâu</b>, nghĩa là
ưu tiên mở rộng trạng thái sâu nhất trong cây tìm kiếm trước.  
Trong bài toán <b>8 quân Xe</b>, DFS sẽ đặt Xe ở hàng đầu tiên còn trống, sau đó tiếp tục
đi sâu xuống hàng kế tiếp cho đến khi không còn vị trí hợp lệ thì mới quay lui.
</p>

<p>
Thuật toán trong dự án được triển khai bằng cấu trúc dữ liệu <b>ngăn xếp (stack)</b>,
mỗi phần tử trong stack là một bàn cờ (<code>numpy.ndarray</code>) biểu diễn trạng thái hiện tại.
Mỗi lần rút ra phần tử trên đỉnh stack để mở rộng, chương trình:
</p>

<ol>
  <li>Tìm hàng đầu tiên chưa có Xe.</li>
  <li>Thử đặt Xe vào từng cột còn trống của hàng đó.</li>
  <li>Nếu hợp lệ (không trùng cột), sinh ra trạng thái mới và đẩy vào stack.</li>
</ol>

<p>
Quá trình tiếp tục cho đến khi gặp trạng thái đích hoặc stack rỗng.
DFS thích hợp để khảo sát nhanh nghiệm sâu, nhưng không đảm bảo tìm được lời giải ngắn nhất.
</p>

<ul>
  <li><b>Cấu trúc dữ liệu:</b> Ngăn xếp (<code>Stack</code>).</li>
  <li><b>Chiến lược mở rộng:</b> Ưu tiên đi sâu nhất, quay lui khi không còn hướng đi.</li>
  <li><b>Đặc tính:</b> Bộ nhớ nhỏ, dễ cài đặt, nhưng không đảm bảo tối ưu.</li>
</ul>



<p align="center">
  🔗 <a href="https://www.geeksforgeeks.org/dsa/depth-first-search-or-dfs-for-a-graph/" target="_blank">
  Tìm hiểu thêm về DFS trên GeeksforGeeks</a>
</p>

<hr>

<h4>📊 Phân tích nhanh</h4>
<ul>
  <li><b>Độ phức tạp thời gian:</b> O(b<sup>m</sup>) – b: số nhánh trung bình, m: độ sâu tối đa.</li>
  <li><b>Độ phức tạp bộ nhớ:</b> O(bm) – chỉ lưu đường đi hiện tại.</li>
  <li><b>Ưu điểm:</b> Gọn nhẹ, tiết kiệm bộ nhớ, cài đặt trực tiếp bằng stack hoặc đệ quy.</li>
  <li><b>Nhược điểm:</b> Không tối ưu, có thể rơi vào vòng lặp hoặc bỏ qua nghiệm nông hơn.</li>
</ul>



<h2 align="center">🔹 Thuật toán UCS – Uniform Cost Search</h2>

<p>
Thuật toán <b>UCS (Uniform Cost Search)</b> là phiên bản tổng quát của BFS, trong đó
mỗi hành động có thể có <b>chi phí khác nhau</b>.
Thay vì duyệt theo độ sâu, UCS luôn chọn trạng thái có <b>tổng chi phí g(n)</b> nhỏ nhất để mở rộng,
đảm bảo tìm được đường đi tối ưu nếu <code>step_cost ≥ 0</code>.
</p>

<p>
Trong bài toán <b>8 quân Xe</b>, mỗi khi đặt một Xe mới vào ô <code>(row, col)</code>,
hàm <code>tinh_cost(row, col)</code> được gọi để tính <b>chi phí bước đi</b> dựa trên khoảng cách
so với vị trí Xe ở bàn đích. Tổng chi phí đến trạng thái hiện tại được lưu trong biến <code>g</code>.
Thuật toán dùng <b>hàng đợi ưu tiên (min-heap)</b> để bật ra trạng thái có <code>g</code> nhỏ nhất.
</p>

<p>Chiến lược mở rộng trong code thực hiện như sau:</p>

<ol>
  <li>Khởi tạo heap với trạng thái gốc có chi phí <code>0</code>.</li>
  <li>Luôn bật ra trạng thái có <code>g</code> nhỏ nhất từ heap.</li>
  <li>Chọn hàng đầu tiên chưa có Xe, thử đặt Xe vào từng cột trống.</li>
  <li>Tính <code>step_cost</code> bằng hàm <code>tinh_cost()</code> và cộng dồn vào <code>new_cost = g + step_cost</code>.</li>
  <li>Nếu <code>new_cost</code> nhỏ hơn chi phí cũ của trạng thái này, cập nhật và đẩy vào heap.</li>
</ol>

<p>
Cấu trúc dữ liệu <code>best_cost</code> được dùng để tránh mở rộng lại các trạng thái đã có chi phí thấp hơn,
giúp UCS tiết kiệm thời gian và bộ nhớ.
</p>

<ul>
  <li><b>Cấu trúc dữ liệu:</b> Hàng đợi ưu tiên (<code>heapq</code> theo giá trị <code>g</code>).</li>
  <li><b>Chiến lược mở rộng:</b> Ưu tiên trạng thái có tổng chi phí nhỏ nhất.</li>
  <li><b>Kiểm soát trùng lặp:</b> Từ điển <code>best_cost</code> lưu chi phí tối ưu đã biết cho mỗi trạng thái.</li>
  <li><b>Kết quả:</b> Khi gặp bàn cờ đích, thuật toán trả về <code>path</code> và <code>solution_cost = g*</code>.</li>
</ul>


<p align="center">
  🔗 <a href="https://www.geeksforgeeks.org/artificial-intelligence/uniform-cost-search-ucs-in-ai/" target="_blank">
  Tìm hiểu thêm về Uniform Cost Search (GeeksforGeeks)</a>
</p>

<hr>

<h4>📊 Phân tích nhanh</h4>
<ul>
  <li><b>Hoàn chỉnh:</b> ✅ nếu mọi <code>step_cost ≥ 0</code>.</li>
  <li><b>Tối ưu:</b> ✅ trả về lời giải có tổng chi phí nhỏ nhất.</li>
  <li><b>Độ phức tạp thời gian:</b> Tỷ lệ với số trạng thái có <code>g ≤ g*</code> (thường là hàm mũ theo độ sâu).</li>
  <li><b>Độ phức tạp bộ nhớ:</b> Phụ thuộc vào kích thước hàng đợi ưu tiên (tăng theo số nút đã sinh).</li>
  <li><b>Ưu điểm:</b> Tối ưu theo chi phí thực, phù hợp khi chi phí các bước khác nhau.</li>
  <li><b>Nhược điểm:</b> Chạy chậm hơn BFS nếu tất cả bước có chi phí bằng nhau; tốn bộ nhớ khi nhiều trạng thái đồng chi phí.</li>
</ul>

<h2 align="center">🔹 Thuật toán DLS – Depth-Limited Search</h2>

<p>
<b>DLS (Depth-Limited Search)</b> là biến thể của DFS, trong đó ta giới hạn độ sâu tối đa 
<code>limit</code> để tránh việc đi quá xa trong không gian tìm kiếm vô hạn. 
Thuật toán hoạt động giống DFS nhưng sẽ <b>dừng lại khi đạt tới giới hạn độ sâu</b>.
Nếu không tìm thấy nghiệm trong phạm vi đó, ta có thể tăng giới hạn để thử lại (chính là ý tưởng của IDS).
</p>

<ul>
  <li><b>Cấu trúc dữ liệu:</b> Ngăn xếp (<code>stack</code>), lưu trạng thái và độ sâu hiện tại.</li>
  <li><b>Chiến lược:</b> Mở rộng các nút theo chiều sâu nhưng chỉ khi <code>depth ≤ limit</code>.</li>
  <li><b>Kiểm soát vòng lặp:</b> Mỗi trạng thái được lưu trong <code>explored</code> để tránh duyệt lại.</li>
  <li><b>Kết quả:</b> Trả về <code>path</code> nếu tìm thấy nghiệm trong phạm vi giới hạn; nếu không thì None.</li>
</ul>


<p align="center">
  🔗 <a href="https://www.geeksforgeeks.org/depth-limited-search-dls-in-ai/" target="_blank">
  Tìm hiểu thêm về Depth-Limited Search (Geeksforgeeks)</a>
</p>

<hr>

<h4>📊 Phân tích nhanh</h4>
<ul>
  <li><b>Hoàn chỉnh:</b> ❌ nếu giới hạn <code>limit</code> nhỏ hơn độ sâu nghiệm; ✅ nếu đủ lớn.</li>
  <li><b>Tối ưu:</b> ❌ (vì không mở rộng đều như BFS).</li>
  <li><b>Độ phức tạp:</b> Thời gian <code>O(b^l)</code>, bộ nhớ <code>O(b·l)</code> (với <code>l</code> là giới hạn độ sâu).</li>
  <li><b>Ưu điểm:</b> Giới hạn được độ sâu, tránh vòng lặp vô hạn; tiết kiệm bộ nhớ.</li>
  <li><b>Nhược điểm:</b> Có thể bỏ lỡ nghiệm nếu giới hạn chưa đủ lớn.</li>
</ul>

<h2 align="center">🔹 Thuật toán IDS – Iterative Deepening Search</h2>

<p>
<b>IDS (Iterative Deepening Search)</b> lặp lại <b>DFS giới hạn độ sâu (DLS)</b> với
ngưỡng <code>limit</code> tăng dần: 0, 1, 2, … cho đến khi gặp nghiệm.
Cách làm này <b>kết hợp</b> ưu điểm của <b>BFS</b> (tối ưu theo số bước khi chi phí đồng nhất)
và <b>DFS</b> (bộ nhớ nhỏ), rất phù hợp khi <b>không biết trước độ sâu nghiệm</b>.
</p>

<ul>
  <li><b>Cấu trúc dữ liệu:</b> Gọi đệ quy theo phong cách DFS với tham số <code>limit</code>.</li>
  <li><b>Chiến lược:</b> Mỗi vòng chạy <code>DLS(root, limit)</code>; nếu chưa thấy nghiệm thì tăng <code>limit</code>.</li>
  <li><b>Kết quả:</b> Trả về <code>path</code> ngay khi một vòng DLS chạm mục tiêu.</li>
</ul>


<p align="center">
  🔗 <a href="https://www.geeksforgeeks.org/artificial-intelligence/iterative-deepening-search-ids-in-ai/" target="_blank">
  Tìm hiểu thêm về Iterative Deepening Depth-First Search (Geeksforgeeks)</a>
</p>

<hr>

<h4>📊 Phân tích nhanh</h4>
<ul>
  <li><b>Tối ưu & Hoàn chỉnh:</b> ✅ (khi chi phí bước bằng nhau; tìm được nghiệm nông nhất).</li>
  <li><b>Độ phức tạp:</b> Thời gian xấp xỉ <code>O(b^d)</code>; Bộ nhớ <code>O(b·d)</code> (tương tự DFS, rất tiết kiệm).</li>
  <li><b>Ưu điểm:</b> Không cần biết trước độ sâu nghiệm; dùng ít bộ nhớ.</li>
  <li><b>Nhược điểm:</b> Lặp lại mở rộng các nút ở tầng nông (nhưng chi phí dư này thường nhỏ).</li>
</ul>


<h3 id="#32-tìm-kiếm-có-thông-tin-informed-search">3.2. Tìm kiếm có thông tin (Informed Search)</h3>

<p>
  Trong tìm kiếm có thông tin, thuật toán sử dụng thêm <b>hàm heuristic</b> để ước lượng 
  khoảng cách hoặc chi phí còn lại đến đích, giúp thu hẹp không gian tìm kiếm và tăng tốc độ giải.  
  Phần này giới thiệu hai thuật toán tiêu biểu: <b>Greedy Best-First Search</b> và <b>A*</b>.
</p>

<ul>
  <li>
    <b>Thuật toán Greedy Best-First Search:</b>  
    Luôn chọn mở rộng nút có giá trị heuristic nhỏ nhất &rarr; hướng về đích nhanh nhất, 
    nhưng không đảm bảo tìm được lời giải tối ưu.
  </li>

  <li>
    <b>Thuật toán A* (A-star):</b>  
    Kết hợp chi phí thực tế <code>g(n)</code> và ước lượng còn lại <code>h(n)</code> 
    thông qua công thức <code>f(n) = g(n) + h(n)</code>.  
    A* đảm bảo tìm được lời giải tối ưu nếu <code>h(n)</code> là <i>heuristic chấp nhận được</i> 
    (không đánh giá thấp hơn thực tế).
  </li>
</ul>

<h4>Hàm heuristic và chi phí sử dụng trong bài toán 8 Rooks</h4>

<p>Dưới đây là hai hàm được sử dụng để hỗ trợ hai thuật toán trên:</p>

<pre><code class="language-python">
def heuristic(board):
    used_rows = set()
    used_cols = set()
    n = board.shape[0]

    # Đếm số hàng và cột đã được đặt quân Xe
    for r in range(n):
        for c in range(n):
            if board[r, c] == 1:
                used_rows.add(r)
                used_cols.add(c)

    # Heuristic = số hàng và cột còn trống (chưa đặt Xe)
    return (8 - len(used_rows)) + (8 - len(used_cols))


def tinh_cost(ma_tran, row, col, vi_tri_dich):
    cost = 1
    # Nếu trùng hàng với vị trí đích thì cộng thêm khoảng cách cột
    for r, c in vi_tri_dich:
        if r == row:
            cost += abs(col - c)
            break
    return cost
</code></pre>

<p>
  <b>Giải thích:</b><br>
  - <code>heuristic(board)</code>: Ước lượng số lượng quân Xe còn cần đặt sao cho đủ 8 hàng và 8 cột.<br>
  - <code>tinh_cost(...)</code>: Tính chi phí đặt Xe tại vị trí <code>(row, col)</code> dựa trên 
  khoảng cách so với vị trí đích, dùng trong tính <code>g(n)</code> và <code>f(n)</code> của A*.
</p>


<hr>

<h4>📊 Phân tích nhanh</h4>
<ul>
  <li><b>Tối ưu:</b> ❌ – không đảm bảo tìm được nghiệm chi phí thấp nhất.</li>
  <li><b>Hoàn chỉnh:</b> ✅ nếu chi phí bước dương và không gian trạng thái hữu hạn.</li>
  <li><b>Thời gian:</b> phụ thuộc vào độ chính xác của heuristic (xấu nhất vẫn là <code>O(b^d)</code>).</li>
  <li><b>Bộ nhớ:</b> cần lưu toàn bộ hàng đợi ưu tiên – tương đối lớn.</li>
  <li><b>Ưu điểm:</b> Rất nhanh khi heuristic tốt, giảm đáng kể số nút mở rộng.</li>
  <li><b>Nhược điểm:</b> Có thể bị “lạc hướng” nếu heuristic đánh giá sai.</li>
</ul>



<h2 align="center">🔹 Thuật toán A* – A Star Search</h2>

<p>
Thuật toán <b>A*</b> kết hợp ưu điểm của <b>Uniform Cost Search</b> và <b>Greedy Best-First Search</b>
thông qua công thức <code>f(n) = g(n) + h(n)</code>, trong đó:
</p>

<ul>
  <li><code>g(n)</code>: Tổng chi phí thực tế đã đi được (cost từ trạng thái gốc đến n).</li>
  <li><code>h(n)</code>: Ước lượng chi phí còn lại đến đích (heuristic function).</li>
</ul>

<p>
A* mở rộng nút có <b>giá trị f nhỏ nhất</b> trong hàng đợi ưu tiên, đảm bảo tìm được nghiệm
<b>tối ưu</b> nếu <code>h(n)</code> là heuristic chấp nhận được (admissible).
Trong bài toán <b>8 Rooks</b>, ta sử dụng:
</p>

<ul>
  <li><b>Heuristic:</b> Số hàng và cột còn trống (chưa đặt Xe) – thể hiện số bước tối thiểu cần đi tiếp.</li>
  <li><b>Chi phí g(n):</b> Tính bằng tổng chi phí di chuyển của mỗi quân Xe đã đặt,
      trong đó hàm <code>tinh_cost()</code> tăng chi phí khi đặt xa vị trí đích.</li>
</ul>

<pre><code class="language-python">
def heuristic(board):
    used_rows = set()
    used_cols = set()
    n = board.shape[0]
    for r in range(n):
        for c in range(n):
            if board[r, c] == 1:
                used_rows.add(r)
                used_cols.add(c)
    # Heuristic: số hàng + số cột còn trống
    return (8 - len(used_rows)) + (8 - len(used_cols))


def tinh_cost(ma_tran, row, col, vi_tri_dich):
    cost = 1
    # Nếu cùng hàng với vị trí đích, cộng thêm khoảng cách cột
    for r, c in vi_tri_dich:
        if r == row:
            cost += abs(col - c)
            break
    return cost
</code></pre>

<p>Quy trình A*:</p>
<ol>
  <li>Khởi tạo <b>priority queue</b> với trạng thái ban đầu, có f = g + h.</li>
  <li>Lặp: lấy ra trạng thái có f nhỏ nhất.</li>
  <li>Nếu là trạng thái đích → trả kết quả.</li>
  <li>Ngược lại, sinh các trạng thái con hợp lệ (đặt Xe vào hàng tiếp theo).</li>
  <li>Tính lại g, h, f cho mỗi con và thêm vào hàng đợi nếu tốt hơn.</li>
</ol>

<pre><code class="language-python">
def A_star(start, Ma_Tran_Dich, vi_tri_dich):
    pq = []
    counter = 0
    h_start = heuristic(start)
    heapq.heappush(pq, (0 + h_start, 0, counter, start.copy()))
    parent = {start.tobytes(): None}
    best_g = {start.tobytes(): 0}
    node_count = 0

    print("Bắt đầu A* SEARCH")
    print(f"Trạng thái ban đầu (g=0, h={h_start}, f={h_start}):")
    print(start)

    while pq:
        f, g, _, state = heapq.heappop(pq)
        key = state.tobytes()
        node_count += 1

        if best_g.get(key, float('inf')) < g:
            continue

        print(f"\nNode #{node_count}: g={g}, h={heuristic(state)}, f={f}")
        print("Trạng thái hiện tại:")
        print(state)

        if np.array_equal(state, Ma_Tran_Dich):
            print(f"\nTÌM THẤY ĐÍCH sau {node_count} node!")
            print(f"Tổng chi phí g cuối: {g}, h=0, f={f}")
            return state, parent, best_g, g

        rows_empty = np.where(np.sum(state, axis=1) == 0)[0]
        if len(rows_empty) == 0:
            continue
        row = rows_empty[0]

        for col in range(state.shape[1]):
            if state[:, col].sum() != 0:
                continue
            child = state.copy()
            child[row, col] = 1
            step_cost = tinh_cost(child, row, col, vi_tri_dich)
            new_g = g + step_cost
            new_h = heuristic(child)
            new_f = new_g + new_h

            child_key = child.tobytes()
            if new_g < best_g.get(child_key, float('inf')):
                best_g[child_key] = new_g
                parent[child_key] = state
                counter += 1
                heapq.heappush(pq, (new_f, new_g, counter, child))
                print(f"  Sinh trạng thái con: đặt xe tại ({row}, {col}), step_cost={step_cost}, g={new_g}, h={new_h}, f={new_f}")
    return None, parent, best_g, None
</code></pre>

<p>
Khi kết thúc, nếu tìm được đích, ta dùng hàm <code>truy_vet_A_star()</code> để dựng lại đường đi tối ưu:
</p>

<pre><code class="language-python">
def truy_vet_A_star(parent, trang_thai_cuoi):
    if trang_thai_cuoi is None:
        return []
    duong_di = []
    dtype, shape = trang_thai_cuoi.dtype, trang_thai_cuoi.shape
    key = trang_thai_cuoi.tobytes()
    while key is not None:
        mang_1c = np.frombuffer(key, dtype=dtype)
        mang_2c = mang_1c.reshape(shape).copy()
        duong_di.append(mang_2c)
        cha = parent.get(key, None)
        key = cha.tobytes() if cha is not None else None
    return duong_di[::-1]
</code></pre>



<p align="center">
  🔗 <a href="https://en.wikipedia.org/wiki/A*_search_algorithm" target="_blank">
  Tìm hiểu thêm về A* (Wikipedia)</a>
</p>

<hr>

<h4>📊 Phân tích nhanh</h4>
<ul>
  <li><b>Tối ưu & Hoàn chỉnh:</b> ✅ Nếu heuristic admissible.</li>
  <li><b>Thời gian:</b> O(b<sup>d</sup>) trong trường hợp xấu nhất.</li>
  <li><b>Bộ nhớ:</b> O(b<sup>d</sup>) (lưu toàn bộ hàng đợi ưu tiên).</li>
  <li><b>Ưu điểm:</b> Tối ưu, hội tụ nhanh khi có heuristic tốt.</li>
  <li><b>Nhược điểm:</b> Tiêu tốn nhiều bộ nhớ với không gian lớn.</li>
</ul>


<h3 id="33-tìm-kiếm-cục-bộ-local-search">3.3. Tìm kiếm cục bộ (Local Search)</h3>

<h4>3.3.1. Thành phần bài toán</h4>
<ul>
  <li><b>Trạng thái:</b> một danh sách gồm các cặp <code>(row, col)</code> biểu diễn vị trí của 8 quân Xe
      (có thể trùng cột ở trạng thái ban đầu).</li>
  <li><b>Hành động:</b> di chuyển một Xe sang cột khác trong cùng hàng để tạo láng giềng mới.</li>
  <li><b>Hàm đánh giá (fitness):</b> số lượng cột duy nhất (tức là số Xe không tấn công nhau).</li>
  <li><b>Mục tiêu:</b> đạt trạng thái có 8 Xe trên 8 cột khác nhau (không xung đột).</li>
</ul>

<p>
<b>Lời giải</b> là cấu hình tốt nhất tìm được trong không gian trạng thái cục bộ.<br>
Thuật toán dừng khi không còn láng giềng nào tốt hơn hoặc đạt trạng thái mục tiêu.
</p>

<h2 align="center">🔹 Thuật toán Hill Climbing</h2>

<p>
<b>Hill Climbing</b> trong bài toán này bắt đầu từ <b>một ma trận khởi tạo ngẫu nhiên</b> có các Xe được đặt ngẫu nhiên trên bàn cờ.
Ở mỗi bước, thuật toán sinh ra <b>tập láng giềng</b> bằng cách <b>di chuyển một Xe sang hàng hoặc cột khác</b> (nếu ô đó trống),
sau đó chọn ra trạng thái có <b>heuristic nhỏ nhất</b> (tức là gần đích hơn) để thay thế trạng thái hiện tại.
Quá trình lặp lại cho đến khi <i>không còn láng giềng nào tốt hơn</i> hoặc đạt được ma trận đích.
</p>

<ul>
  <li><b>Trạng thái ban đầu:</b> Ma trận <code>start</code> được khởi tạo ngẫu nhiên, mỗi hàng có thể có nhiều Xe.</li>
  <li><b>Láng giềng:</b> Sinh ra bằng cách di chuyển từng Xe sang vị trí trống khác cùng hàng hoặc cùng cột.</li>
  <li><b>Hàm heuristic:</b> <code>heuristic(state)</code> đánh giá mức độ “xa đích” của trạng thái 
      (giá trị càng nhỏ nghĩa là càng gần ma trận đích).</li>
  <li><b>Chiến lược lựa chọn:</b> duyệt toàn bộ láng giềng, chọn <b>trạng thái có heuristic nhỏ nhất</b> 
      nếu nó tốt hơn trạng thái hiện tại.</li>
  <li><b>Điều kiện dừng:</b> nếu không có láng giềng nào tốt hơn hoặc trạng thái hiện tại bằng <code>Ma_Tran_Dich</code>.</li>
  <li><b>Đường đi:</b> lưu lại toàn bộ các ma trận đã duyệt trong danh sách <code>path</code> để mô phỏng quá trình leo đồi.</li>
</ul>


<p align="center">
  🔗 <a href="https://en.wikipedia.org/wiki/Hill_climbing" target="_blank">
  Tìm hiểu thêm về Hill Climbing (Wikipedia)</a>
</p>

<hr>

<h4>📊 Phân tích nhanh</h4>
<ul>
  <li><b>Tốc độ & Bộ nhớ:</b> nhanh, vì chỉ lưu trạng thái hiện tại và tập láng giềng.</li>
  <li><b>Tối ưu:</b> ❌ không đảm bảo nghiệm toàn cục – dễ bị kẹt tại cực trị cục bộ hoặc cao nguyên.</li>
  <li><b>Hiệu quả:</b> phụ thuộc vào cách sinh láng giềng và hàm heuristic.</li>
  <li><b>Giải pháp cải thiện:</b> dùng <i>Random Restart</i> hoặc <i>Simulated Annealing</i> để thoát khỏi kẹt cục bộ.</li>
</ul>


<h2 align="center">🔹 Thuật toán Genetic – Genetic Algorithm (GA)</h2>

<p>
<b>Genetic Algorithm (GA)</b> mô phỏng quá trình tiến hóa tự nhiên để tìm lời giải tối ưu. 
Thuật toán bắt đầu bằng cách <b>khởi tạo một quần thể cá thể ngẫu nhiên</b>, 
mỗi cá thể biểu diễn cách sắp xếp các Xe trên bàn cờ (một gene = cột của Xe trên hàng tương ứng). 
Sau đó, GA lặp lại các bước <b>chọn lọc → lai ghép → đột biến</b> để tạo ra thế hệ mới,
dần cải thiện chất lượng lời giải cho đến khi đạt được cấu hình đích (8 Xe ở 8 cột khác nhau) hoặc hết số thế hệ cho phép.
</p>

<ul>
  <li><b>Biểu diễn cá thể:</b> <code>list[int]</code> độ dài <code>n</code>, trong đó <code>gene[i]</code> là vị trí cột của Xe ở hàng <code>i</code>.</li>
  <li><b>Fitness:</b> số Xe được đặt đúng vị trí trong <code>Ma_Tran_Dich</code>. 
      <br>Cụ thể: <code>tinh_fitness(ca_the, Ma_Tran_Dich)</code> đếm số Xe trùng cột với ma trận đích.</li>
  <li><b>Khởi tạo quần thể:</b> <code>so_ca_the</code> cá thể ngẫu nhiên, mỗi cá thể chọn cột ngẫu nhiên cho từng hàng.</li>
  <li><b>Chọn lọc:</b> xác suất chọn tỉ lệ thuận với <code>fitness</code> – cá thể tốt có cơ hội sinh con cao hơn.</li>
  <li><b>Lai ghép (Crossover):</b> chọn ngẫu nhiên một <code>điểm cắt</code>, 
      trộn gene của bố và mẹ để sinh 2 con lai (<code>one-point crossover</code>).</li>
  <li><b>Đột biến (Mutation):</b> với xác suất <code>xac_suat_dot_bien</code>, 
      chọn ngẫu nhiên 1 gene và thay đổi nó thành giá trị cột khác (0→N-1).</li>
  <li><b>Điều kiện dừng:</b> khi cá thể có <code>fitness == N</code> (tức là đạt ma trận đích) 
      hoặc đạt <code>max_the_he</code> thế hệ.</li>
  <li><b>Lịch sử tiến hóa:</b> lưu lại cá thể tốt nhất mỗi thế hệ trong danh sách <code>lich_su</code> để theo dõi quá trình hội tụ.</li>
</ul>


<p align="center">
  🔗 <a href="https://en.wikipedia.org/wiki/Genetic_algorithm" target="_blank">
  Tìm hiểu thêm về Genetic Algorithm (Wikipedia)</a>
</p>

<hr>

<h4>📊 Phân tích nhanh</h4>
<ul>
  <li><b>Tốc độ & Bộ nhớ:</b> phụ thuộc vào <code>so_ca_the</code> và <code>max_the_he</code>; có thể song song hóa tốt.</li>
  <li><b>Tối ưu:</b> ❌ không đảm bảo nghiệm toàn cục, nhưng thường tìm nghiệm tốt trong không gian tìm kiếm lớn.</li>
  <li><b>Ưu điểm:</b> Khám phá đa hướng, tránh kẹt tại cực trị cục bộ; dễ mở rộng với nhiều chiến lược GA khác nhau.</li>
  <li><b>Nhược điểm:</b> Nhạy với tham số (quy mô quần thể, xác suất đột biến, số thế hệ...); cần tinh chỉnh để đạt hiệu quả tốt nhất.</li>
</ul>


<h2 align="center">🔹 Thuật toán Simulated Annealing (SA)</h2>

<p>
<b>Simulated Annealing (SA)</b> bắt đầu từ <b>một trạng thái đầy đủ ngẫu nhiên</b>, sau đó lặp lại việc
đề xuất láng giềng và <b>chấp nhận có xác suất</b> những bước <i>xấu hơn</i> khi nhiệt độ còn cao, giúp thoát kẹt cực trị cục bộ.
Nhiệt độ giảm dần theo lịch <code>T_k = T0 · α^k</code>.
</p>

<ul>
  <li><b>Trạng thái:</b> danh sách <code>[(row, col)]</code> đủ <code>n</code> Xe (có thể trùng cột ban đầu).</li>
  <li><b>Năng lượng (Energy):</b> <code>E(state) = n - số cột khác nhau</code> (tối ưu khi <code>E=0</code>).</li>
  <li><b>Láng giềng:</b> chọn ngẫu nhiên một hàng và đổi sang một cột khác (<code>generate_neighbors</code>).</li>
  <li><b>Quy tắc chấp nhận:</b> nếu <code>ΔE ≤ 0</code> thì nhận; nếu <code>ΔE &gt; 0</code> thì nhận với xác suất <code>exp(-ΔE/T)</code>.</li>
  <li><b>Lịch nhiệt:</b> <code>T ← T · α</code> mỗi bước (mặc định <code>T0=2.5</code>, <code>α=0.98</code>, <code>steps=5000</code>).</li>
  <li><b>Điều kiện dừng:</b> đạt nghiệm <code>E=0</code> hoặc hết số bước.</li>
</ul>


<p align="center">
  🔗 <a href="https://en.wikipedia.org/wiki/Simulated_annealing" target="_blank">
  Tìm hiểu thêm về Simulated Annealing (Wikipedia)</a>
</p>

<hr>

<h4>📊 Phân tích nhanh</h4>
<ul>
  <li><b>Tốc độ & Bộ nhớ:</b> nhẹ; chỉ lưu trạng thái hiện tại và một láng giềng.</li>
  <li><b>Tối ưu:</b> ❌ không bảo đảm nghiệm toàn cục, nhưng <i>thường</i> tốt hơn Hill Climbing nhờ bước nhận xấu có kiểm soát.</li>
  <li><b>Nhạy tham số:</b> cần điều chỉnh <code>T0</code>, <code>α</code>, <code>steps</code> theo kích thước bài toán.</li>
</ul>

<h2 align="center">🔹 Thuật toán Beam Search</h2>

<p>
<b>Beam Search</b> mở rộng theo <b>tầng (theo hàng)</b> và chỉ giữ lại tối đa <b>k</b> trạng thái tốt nhất ở mỗi tầng.
Cách này giảm mạnh nhánh cần duyệt so với BFS, nhưng <i>không đảm bảo tối ưu</i> do cắt tỉa sớm.
</p>

<ul>
  <li><b>Thước đo (score):</b> <code>(distinct_cols, depth)</code> &rarr; ưu tiên <b>số cột khác nhau</b> trước, sau đó ưu tiên trạng thái <b>sâu hơn</b>.</li>
  <li><b>Beam size:</b> <code>k</code> (mặc định 3) – số trạng thái tối đa được giữ lại sau khi mở rộng một tầng.</li>
  <li><b>Fallback an toàn:</b> khi đã đặt đến hàng <code>n-1</code> và còn đúng <b>1 cột</b> trống, tự động điền nốt để hoàn tất nghiệm.</li>
</ul>


<p align="center">
  🔗 <a href="https://en.wikipedia.org/wiki/Beam_search" target="_blank">Tìm hiểu thêm về Beam Search (Wikipedia)</a>
</p>

<hr>

<h4>📊 Phân tích nhanh</h4>
<ul>
  <li><b>Tốc độ & Bộ nhớ:</b> kiểm soát tốt nhờ tham số <code>k</code> (nhỏ hơn BFS rất nhiều).</li>
  <li><b>Tối ưu:</b> ❌ không đảm bảo, có thể loại bỏ nhánh dẫn đến nghiệm tối ưu.</li>
  <li><b>Ưu điểm:</b> Hiệu quả thực nghiệm, dễ điều chỉnh bằng <code>beam_size</code>.</li>
  <li><b>Nhược điểm:</b> Nhạy với thước đo <code>score</code>; cắt tỉa quá sớm có thể bỏ lỡ nghiệm.</li>
</ul>

<h3 id="34-tìm-kiếm-trong-môi-trường-phức-tạp-complex-environment-search">3.4. Tìm kiếm trong môi trường phức tạp</h3>
<p>
Trong phần này, bài toán <b>Eight Rooks</b> được mở rộng sang các biến thể phức tạp hơn, nơi môi trường có thể
<b>không xác định (Non-deterministic)</b> hoặc <b>quan sát không đầy đủ (Partially Observable)</b>.
Các thuật toán trong nhóm này thường được dùng trong trí tuệ nhân tạo khi tác nhân
phải ra quyết định mà không có thông tin hoàn hảo về trạng thái của thế giới.
</p>

<h4> Thành phần chính của bài toán</h4>
<ul>
  <li><b>Trạng thái:</b>
    Là danh sách các cặp <code>(row, col)</code> như trước, nhưng trong môi trường phức tạp,
    mỗi trạng thái có thể đại diện cho <b>một tập hợp các khả năng</b> (gọi là <i>belief state</i>),
    tức là <b>phân phối xác suất</b> trên các trạng thái vật lý thật.
  </li>
  <li><b>Hành động:</b>
    Đặt hoặc di chuyển một quân Xe, nhưng do tính không chắc chắn, một hành động có thể dẫn đến
    <b>nhiều kết quả khả dĩ</b> thay vì chỉ một trạng thái duy nhất.
  </li>
  <li><b>Kiểm tra mục tiêu:</b>
    Xác định xem trạng thái hiện tại (hoặc tập hợp trạng thái) có chứa <b>ít nhất một cấu hình hợp lệ</b>
    trong đó 8 quân Xe không tấn công nhau.
    Trong mô hình xác suất, ta chọn trạng thái có <b>xác suất cao nhất</b> đạt mục tiêu.
  </li>
  <li><b>Đặc điểm:</b>
    <ul>
      <li>Môi trường có thể <b>không xác định</b>: cùng một hành động, kết quả có thể khác nhau.</li>
      <li><b>Quan sát hạn chế:</b> tác nhân không thể biết chính xác trạng thái thật,
          chỉ ước lượng dựa trên tập hợp các khả năng (belief states).</li>
      <li>Cần duy trì và cập nhật một <b>tập trạng thái</b> thay vì một trạng thái duy nhất.</li>
    </ul>
  </li>
</ul>


<h2 align="center">🔹 Thuật toán AND–OR Search</h2>

<p>
<b>AND–OR Search</b> biểu diễn quá trình lập kế hoạch bằng <b>cây AND–OR</b>:
các <b>nút OR</b> là lựa chọn hành động; các <b>nút AND</b> gom <i>mọi kết quả có thể xảy ra</i> của một hành động.
Với Eight Rooks phiên bản <i>deterministic</i> trong code, mỗi hành động sinh đúng <b>một</b> kết quả,
vì vậy nút AND quy về việc gọi lại OR trên trạng thái con duy nhất.
</p>

<ul>
  <li><b>OR-node:</b> chọn một hành động <i>đặt thêm 1 Xe vào hàng kế tiếp</i> (cột hợp lệ) rồi chuyển sang AND.</li>
  <li><b>AND-node:</b> yêu cầu <b>tất cả</b> kết quả của hành động đều thành công. Với bản deterministic hiện tại, chỉ có 1 kết quả → gọi lại OR.</li>
  <li><b>Chống lặp:</b> dùng khóa <code>tuple(cols)</code> để phát hiện vòng lặp khi quay lui.</li>
  <li><b>Kết quả:</b> trả về <code>path</code> (chuỗi trạng thái–hành động) khi đặt đủ <code>n</code> Xe hợp lệ.</li>
</ul>


<p align="center">
  🔗 <a href="https://en.wikipedia.org/wiki/AND%E2%80%93OR_tree" target="_blank">Tìm hiểu thêm về AND–OR Search (Wikipedia)</a>
</p>

<hr>

<h4>📊 Phân tích độ phức tạp</h4>
<ul>
  <li><b>Trường hợp deterministic (code hiện tại):</b>
    <ul>
      <li><b>Thời gian:</b> tệ nhất tương đương duyệt cây tìm kiếm một nhánh/tiền thứ tự, xấp xỉ <code>O(b^d)</code>
          (b: số cột hợp lệ trung bình mỗi hàng, d ≈ n).</li>
      <li><b>Bộ nhớ:</b> <code>O(b·d)</code> đến <code>O(d)</code> tuỳ cách hiện thực (gần DFS do quay lui theo nhánh).</li>
    </ul>
  </li>
  <li><b>Ưu điểm:</b> Diễn đạt tự nhiên các bài toán có rẽ nhánh kết quả và lập kế hoạch có điều kiện; mở rộng được cho sensing.</li>
  <li><b>Nhược điểm:</b> Dễ bùng nổ tổ hợp khi có nhiều kết quả/quan sát; cần chống lặp tốt để khả thi.</li>
</ul>


<h2 align="center">🔹 Partially Observable Search (Belief State Search)</h2>

<p>
Thuật toán <b>Partially Observable Search</b> làm việc trên <b>belief state</b> (miền giá trị có thể)
thay vì một trạng thái duy nhất. Với Eight Rooks, mỗi hàng <code>r</code> có miền cột khả dĩ
<code>domains[r] ⊆ {0..n−1}</code>. Ta có cảm biến (sensor) <code>observe_equal(r, c)</code> trả lời
<b>True/False</b> (hoặc <i>None</i> nếu không quan sát được), được dùng để <b>cắt tỉa</b> miền trước khi gán.
</p>

<ul>
  <li><b>Belief (Domains):</b> <code>list[ set[int] ]</code> – mỗi phần tử là miền cột còn lại cho một hàng.
      Khởi tạo bằng <code>_init_domains()</code> và cập nhật ràng buộc hàng–cột qua <code>_apply_commits()</code>.</li>
  <li><b>Chọn biến:</b> <code>_select_row()</code> dùng <b>MRV</b> (Minimum Remaining Values) nếu bật
      <code>use_mrv=True</code> để ưu tiên hàng có miền nhỏ nhất.</li>
  <li><b>Quan sát (Sensor):</b> <code>_observe_equal(row, col)</code> – nếu <code>hidden_solution</code> tồn tại,
      có thể hỏi tối đa <code>max_sense_per_row</code> lần mỗi hàng để loại nhanh giá trị sai.</li>
  <li><b>Forward Checking:</b> <code>_forward_check(domains, row, col)</code> khóa <code>row={col}</code>
      và xóa <code>col</code> khỏi miền các hàng chưa gán; trả <i>None</i> nếu sinh miền rỗng.</li>
  <li><b>Tìm kiếm:</b> <code>set_up_PartialDFS()</code> – DFS trên belief; thứ tự thử giá trị có thể
      <b>xáo trộn</b> (<code>shuffle_values=True</code>) hoặc <b>sắp xếp</b>.</li>
  <li><b>Mục tiêu:</b> gán đủ <code>n</code> hàng sao cho các cột là duy nhất (<code>is_goal_full</code> tương đương <code>distinct == n</code>).</li>
</ul>


<p align="center">
  🔗 <a href="https://en.wikipedia.org/wiki/Partially_observable_Markov_decision_process" target="_blank">
  Tìm hiểu thêm: Partially Observable (POMDP) & belief states</a>
</p>


<hr>

<h4>📊 Phân tích độ phức tạp</h4>
<ul>
  <li><b>Có sensor (quan sát một phần):</b>
    <ul>
      <li><b>Thời gian:</b> biên trên vẫn theo thứ tự gán, nhưng kỳ vọng <b>giảm mạnh</b> do mỗi hàng chỉ cần thử
          tối đa <code>max_sense_per_row</code> giá trị trước khi cắt tỉa; mỗi bước đánh giá và FC là
          <code>O(n)</code>–<code>O(n²)</code> tùy hiện thực set.</li>
      <li><b>Bộ nhớ:</b> tương tự trường hợp trên; thêm log/steps không ảnh hưởng tới bản chất độ phức tạp.</li>
    </ul>
  </li>
  <li><b>Ưu điểm:</b> Khai thác quan sát để <b>cắt tỉa sớm</b>, MRV giảm nhánh, forward checking ngăn mâu thuẫn lan truyền.</li>
  <li><b>Nhược điểm:</b> Hiệu quả phụ thuộc chất lượng sensor và thứ tự thử giá trị; vẫn có thể backtrack sâu khi miền rộng.</li>
</ul>

<hr>

<hr>

<h3 id="35-tìm-kiếm-có-điều-kiện-ràng-buộc-constraint-satisfaction-problem">3.5. Bài toán ràng buộc (CSP)</h3>

<p><b>Thành phần chính của bài toán:</b></p>

<ul>
  <li><b>Trạng thái (State):</b> Gồm 8 biến từ <code>X₁</code> đến <code>X₈</code>, tương ứng với vị trí của 8 quân Xe trên bàn cờ 8×8.  
  Mỗi biến <code>Xᵢ</code> đại diện cho hàng của quân Xe thứ <code>i</code>.</li>

  <li><b>Miền giá trị (Domains):</b> Mỗi biến <code>Xᵢ</code> có thể nhận một giá trị trong khoảng <code>{0, 1, 2, ..., 7}</code>, tương ứng với 8 cột có thể đặt quân Xe.  
  Mỗi Xe phải nằm trên một cột duy nhất, nên các giá trị của các biến không được trùng nhau.</li>

  <li><b>Ràng buộc (Constraints):</b>
    <ul>
      <li><b>Ràng buộc không trùng cột:</b> Hai quân Xe bất kỳ không được nằm trên cùng một cột:  
      <code>Xᵢ ≠ Xⱼ</code> với mọi <code>i ≠ j</code>.</li>
    </ul>
  </li>
</ul>

<p><b>Lời giải:</b></p>
Lời giải là một bộ gán giá trị cho 8 biến <code>{X₁, X₂, ..., X₈}</code> sao cho thỏa mãn tất cả các ràng buộc — tức là mỗi hàng và mỗi cột chỉ có một quân Xe duy nhất.  
Thuật toán CSP (Constraint Satisfaction Problem) như <b>Backtracking</b>, <b>MRV</b>, hoặc <b>Forward Checking</b> có thể được sử dụng để tìm lời giải hợp lệ này.
</p>

<h2 align="center">🔹 Thuật toán Backtracking</h2>

<p>
<b>Backtracking</b> thử lần lượt các cột <b>chưa dùng</b> cho từng hàng; nếu bế tắc thì <b>quay lui</b> về hàng trước và thử cột khác. Mục tiêu là đặt đủ <code>n</code> Xe sao cho không trùng cột.
</p>

<ul>
  <li><b>Trạng thái:</b> danh sách <code>(row, col)</code> của các Xe đã đặt.</li>
  <li><b>Hành động:</b> đặt Xe vào hàng hiện tại tại một cột chưa dùng.</li>
  <li><b>Chiến lược:</b> đệ quy theo hàng; push khi thử, pop khi quay lui.</li>
  <li><b>Kết thúc:</b> khi <code>len(state) = n</code> → trả <code>path</code> nghiệm đầu tiên.</li>
</ul>


<h4>📊 Độ phức tạp & đặc tính</h4>
<ul>
  <li><b>Thời gian (xấu nhất):</b> ~<code>O(n!)</code> (thử hoán vị cột).</li>
  <li><b>Bộ nhớ:</b> <code>O(n)</code> (ngăn xếp đệ quy).</li>
  <li><b>Ưu:</b> đơn giản, tìm nghiệm đầu tiên nhanh khi thứ tự cột tốt.</li>
  <li><b>Nhược:</b> có thể quay lui sâu nếu thứ tự thử không thuận lợi.</li>
</ul>

<p align="center">
  🔗 <a href="https://en.wikipedia.org/wiki/Backtracking" target="_blank">Backtracking (Wikipedia)</a>
</p>

<h2 align="center">🔹 Backtracking + Forward Checking (BT+FC)</h2>

<p>
<b>Backtracking + Forward Checking</b> mở rộng Backtracking bằng bước <b>kiểm tra trước</b>:
mỗi khi gán <code>row → col</code>, ta <b>xóa ngay</b> <code>col</code> khỏi miền các hàng chưa gán.
Nếu miền nào rỗng, <b>quay lui</b> tức thì → cắt tỉa mạnh các nhánh vô vọng.
</p>

<ul>
  <li><b>Trạng thái:</b> danh sách <code>(row, col)</code> các Xe đã đặt.</li>
  <li><b>Miền ban đầu:</b> mỗi hàng có miền <code>{0..n−1}</code>.</li>
  <li><b>Hành động:</b> gán <code>(row, col)</code> theo miền hiện tại (có thể <i>shuffle</i> thứ tự cột).</li>
  <li><b>Forward Checking:</b> khóa <code>row={col}</code>, xóa <code>col</code> khỏi miền hàng sau; nếu có miền rỗng ⇒ <i>prune</i>.</li>
  <li><b>Kết thúc:</b> khi <code>len(state)=n</code> (đặt đủ n Xe, không trùng cột) ⇒ trả <code>path</code>.</li>
</ul>



<h4>📊 Độ phức tạp & đặc tính</h4>
<ul>
  <li><b>Thời gian (xấu nhất):</b> ~<code>O(n!)</code>, nhưng <b>FC</b> thường giảm mạnh số nhánh phải thử.</li>
  <li><b>Bộ nhớ:</b> <code>O(n²)</code> cho các miền + <code>O(n)</code> ngăn xếp đệ quy.</li>
  <li><b>Ưu:</b> Đơn giản, hiệu quả hơn Backtracking thuần; phát hiện sớm ngõ cụt.</li>
  <li><b>Nhược:</b> Vẫn có thể quay lui sâu khi miền rộng hoặc thứ tự thử kém.</li>
</ul>

<p align="center">
  🔗 <a href="https://en.wikipedia.org/wiki/Constraint_satisfaction_problem#Solving_CSPs" target="_blank">
  Forward Checking & CSP (Wikipedia)</a>
</p>



