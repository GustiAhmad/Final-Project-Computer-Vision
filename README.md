SIFT Image Stitching: Dokumentasi Panorama Posko KKN
Proyek ini merupakan implementasi algoritma Scale-Invariant Feature Transform (SIFT) untuk menggabungkan dua citra digital (image stitching) menjadi satu foto panorama yang utuh. Proyek ini dikembangkan sebagai bagian dari Tugas Akhir mata kuliah Visi Komputer.

📝 Deskripsi Singkat
Proyek ini bertujuan untuk menciptakan citra panorama secara manual menggunakan pemrograman Python. Sistem menerima dua gambar dengan area tumpang tindih (overlap), mendeteksi fitur unik di dalamnya, mencocokkannya, dan melakukan transformasi perspektif untuk menyatukan kedua gambar tersebut menjadi satu kesatuan yang koheren secara geometris.

📖 Latar Belakang
Dalam pengambilan foto secara manual (tanpa tripod), sering kali terjadi pergeseran skala, rotasi, maupun sudut pandang antar foto. Algoritma SIFT dipilih karena memiliki ketangguhan (robustness) yang sangat baik terhadap perubahan-perubahan tersebut dibandingkan algoritma deteksi fitur lainnya. Hal ini memungkinkan proses penyatuan gambar tetap akurat meskipun foto diambil dalam kondisi lapangan yang dinamis (seperti dokumentasi di lokasi KKN).

✨ Fitur Utama Sistem
- Feature Detection: Mendeteksi ribuan titik kunci (keypoints) unik pada citra.
- Feature Matching: Mencocokkan fitur antar dua citra menggunakan Brute-Force Matcher.
- Outlier Removal: Menggunakan Lowe's Ratio Test dan RANSAC untuk membuang kecocokan fitur yang salah.
- Perspective Warping: Mentransformasi citra menggunakan matriks Homografi.
- Image Stitching: Menggabungkan citra ke dalam satu kanvas panorama yang luas.

📂 Struktur Folder Proyek
.
├── dataset/                   # Folder berisi citra masukan (posko1.jpg, posko2.jpg)
├── output/                    # Folder hasil proses (matching, keypoints, panorama)
├── src/                       # Folder berisi kode sumber Python
│   ├── deteksi_keypoint.py    # Deteksi Keypoint Awal
│   ├── feature_matching.py    # Visualisasi feature matching
│   └── buat_panorama.py       # Proses utama stitching panorama
└── README.md                  # Dokumentasi proyek


⚙️ Requirement / Dependency
- Python: Versi 3.8 atau lebih tinggi.
- Library:
  - opencv-python (Pengolahan citra utama)
  - numpy (Komputasi matriks)
  - matplotlib (Visualisasi hasil)

🛠️ Cara Instalasi dan Setup
1. Clone repositori ini:
git clone [https://github.com/username/sift-panorama-kkn.git](https://github.com/username/sift-panorama-kkn.git)
cd sift-panorama-kkn

2. Buat Virtual Environment (Opsional namun disarankan):
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

3. Instal library yang dibutuhkan:
pip install opencv-python numpy matplotlib

🚀 Cara Menjalankan Program
1. Pastikan file gambar Anda sudah berada di folder dataset/.
2. Untuk melihat hasil pencocokan fitur (garis penghubung):
    python src/deteksi_keypoint.py
3. Untuk menghasilkan citra panorama utuh:
    python src/panorama.py


📊 Contoh Output
Sistem akan menghasilkan output berupa:
  1. Visualisasi Matching: Menampilkan garis-garis yang menghubungkan titik identik antara dua foto.
  2. Hasil Panorama: Satu gambar lebar yang menyatukan kedua sisi bangunan posko tanpa adanya patahan struktur.

🔄 Alur Kerja Sistem
1. Preprocessing: Mengubah citra ke grayscale.
2. Ekstraksi Fitur: Mendeteksi keypoints dan menghitung descriptors dengan SIFT.
3. Matching: Mencari pasangan titik yang mirip antar citra.
4. Homografi: Menghitung matriks transformasi koordinat menggunakan RANSAC.
5. Warping & Merging: Melenturkan citra dan menempelkannya ke kanvas utama.
   
🚀 Pengembangan Lanjutan
- Integrasi teknik Multi-band Blending untuk menghilangkan garis sambungan (seam).
- Implementasi penggabungan lebih dari dua citra secara otomatis.
- Eksperimen perbandingan performa waktu antara SIFT dengan ORB untuk perangkat mobile.
  
👤 Identitas Pembuat
- Nama: Gusti Ahmad Muttahid Bilhaq
- NIM: 442023611097
- Mata Kuliah: Visi Komputer
- Institusi: Universitas Darussalam Gontor
- Tahun: 2026
