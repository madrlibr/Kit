<p align="center">
  <img width="100" height="100" alt="1000190465" src="https://github.com/user-attachments/assets/580eb395-0852-488a-8b8c-2a23b7ac4a7e" />
</p>


# Kit: Git CLI Wrapper

Kit adalah wrapper Git berbasis Python yang dirancang untuk mempercepat manajemen repositori melalui terminal. Alat ini menyederhanakan perintah Git menjadi perintah singkat yang dilengkapi dengan output teks berwarna.

## Fitur

- Perintah singkat untuk operasi Git harian.
- Output terminal yang informatif menggunakan library Rich.
- Otomatisasi alur kerja (add, commit, dan push dalam satu perintah).
- Penanganan inisialisasi repositori dan remote secara cepat.

   
## Requirements
    Gitpython
    Rich


### Command tersedia:

* `kit gs`: Menampilkan status repositori saat ini dengan format teks berwarna (Git Status).
* `kit gaa`: Menambahkan seluruh perubahan file yang ada di direktori ke dalam staging area (Git Add All).
* `kit gc <pesan>`: Melakukan commit untuk perubahan yang telah di-staging dengan pesan tertentu (Git Commit).
* `kit gp`: Melakukan penarikan data terbaru dari remote repositori (Git Pull).
* `kit gpm`: Mengunggah perubahan yang telah di-commit langsung ke branch utama (Git Push Main).
* `kit acp <pesan>`: Menjalankan alur kerja otomatis: Add all, Commit, dan Push ke branch main sekaligus.
* `kit iap <url_remote>`: Melakukan inisialisasi repositori baru, setting remote, dan push pertama kali ke main.
* `kit ru`: Menampilkan alamat URL remote origin yang terhubung dengan repositori.
* `kit cb`: Menampilkan nama branch yang sedang aktif saat ini.
* `kit cd`: Menampilkan detail perbedaan atau perubahan kode yang belum di-commit (Git Diff).

## Installation

1. Clone repository:
```bash
git clone https://github.com/madrlibr/kit.git

```


2. Masuk ke direktori projek:
```bash
cd kit

```


3. Install library:
```bash
pip install -e .

```


## Contoh penggunaan:

Otomatisasi Push ke Main:
```bash
kit pam "memperbaiki bug"

```

Init dan Push pertama kali:
```bash
kit iap URL_REPO

```


## Footage:
<img width="1343" height="800" alt="Screenshot (1189)" src="https://github.com/user-attachments/assets/b81bca99-2b4b-4373-8977-043d3d29fcad" />




## License

Proyek ini menggunakan lisensi MIT. Silakan gunakan dan kembangkan sesuai kebutuhan Anda.


