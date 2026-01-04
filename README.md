
<div align="center">
	<img src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python" alt="Python">
	<img src="https://img.shields.io/badge/PyOpenGL-3.1.7-green?logo=opengl" alt="PyOpenGL">
	<img src="https://img.shields.io/badge/Status-Active-brightgreen" alt="Status">
</div>

# 🏠 Bedroom Showcase

<p align="center">
	<img src="assets/textures/preview.jpg" alt="Bedroom Showcase Preview" width="600"/>
</p>

<p align="center"><b>Visualisasi 3D interaktif kamar tidur dengan Python & PyOpenGL</b></p>


---

## ✨ Deskripsi
"Bedroom Showcase" adalah aplikasi grafika komputer yang menampilkan kamar tidur 3D lengkap dengan berbagai furnitur, pencahayaan dinamis, dan kontrol kamera first-person. Cocok untuk pembelajaran, demo, atau tugas besar grafika komputer.


## 🚀 Fitur Utama
<ul>
	<li><b>Visualisasi 3D kamar tidur:</b> Bed, desk, chair, drawer, lamp, clock, HUD</li>
	<li><b>Kamera first-person:</b> Navigasi bebas & smooth</li>
	<li><b>Pencahayaan dinamis:</b> Mode siang/malam, lampu interaktif</li>
	<li><b>Texture mapping:</b> Objek dengan tekstur realistis</li>
	<li><b>Animasi objek:</b> Drawer, jam, dan lainnya</li>
	<li><b>Auto tour:</b> Kamera berkeliling otomatis</li>
</ul>


## 🗂️ Struktur Proyek
<details>
	<summary>Klik untuk melihat struktur</summary>

	- <b>main.py</b> : Entry point aplikasi
	- <b>src/</b> : Source code utama
		- <b>app.py</b> : Inisialisasi & loop aplikasi
		- <b>camera.py</b> : Kontrol kamera
		- <b>lighting.py</b> : Sistem pencahayaan
		- <b>renderer.py</b> : Rendering scene
		- <b>textures.py</b> : Manajemen tekstur
		- <b>scene/bedroom_scene.py</b> : Scene utama kamar tidur
		- <b>entities/</b> : Definisi objek 3D (bed, desk, dll)
	- <b>assets/textures/</b> : File tekstur gambar
	- <b>requirements.txt</b> : Daftar dependensi Python
</details>


## ⚡ Instalasi
1. <b>Clone repository</b>
	```bash
	git clone <repo-url>
	cd bedroomshowcase
	```
2. <b>Install dependencies</b>
	```bash
	pip install -r requirements.txt
	```
3. <b>Pastikan folder <code>assets/textures/</code> berisi file tekstur yang diperlukan</b>


## ▶️ Menjalankan Aplikasi
```bash
python main.py
```


## 🎮 Kontrol Keyboard & Mouse
| Tombol         | Fungsi                        |
| -------------- | ----------------------------- |
| W/A/S/D        | Gerak maju/kiri/mundur/kanan  |
| Mouse          | Putar/pindah kamera           |
| H              | Tampilkan/sembunyikan HUD     |
| N              | Toggle mode siang/malam       |
| L              | Nyalakan/matikan lampu        |
| T              | Aktifkan auto tour            |
| O              | Buka/tutup drawer             |
| 1/2/3          | Fokus ke objek (bed/desk/drawer) |
| 0              | Reset fokus kamera            |


## 👨‍💻 Tim Pengembang
Lihat detail anggota di file <b>LAPORAN_TUBES.md</b>


## 📄 Lisensi
Proyek ini dibuat untuk keperluan pembelajaran dan tugas besar mata kuliah Grafika Komputer.

---

<div align="center">
	<sub>Copyright © 2026 Bedroom Showcase Team</sub>
</div>
