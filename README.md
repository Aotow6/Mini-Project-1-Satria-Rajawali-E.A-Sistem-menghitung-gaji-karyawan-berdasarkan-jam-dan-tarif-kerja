Disini saya akan menjelaskan program saya :

usn_benar = "satria"
nim_benar = "067"
session = "off"  

  
untuk baris 1 - 2 saya membuat dan memberi nilai variable yang akan digunakan untuk login atau kek bikin akun gitu
di baris 3 ada variable session yang akan di gunakan untuk mengkondisikan looping while dan untuk di baris 3 ini saya set value nya "off"
____________________________________________________________________________________________________________________________________________________________________________________________________


while session == "off":
    print("------- Login --------")
    usn = input("Masukkan nama anda: ")
    nim = input("Masukkan NIM anda: ")
    if usn == usn_benar and nim == nim_benar:
        print(f"Login berhasil Selamat datang, {usn}.")
        session = "in"  
    else:
        print("Login error")

        
di baris 5-13  ada looping while nah karena dimana jika variable session bernilai "off" maka kita akan disuru mengisi input untuk login yaitu 
input nama dan nim lalu kalau benar maka nilai variable session akan berubah menjadi "on" dan kita bisa memakai fitur untuk menghitung gaji tetapi jika salah maka kita looping lagi ke input nama dan nim dan nilai dalam var session tidak berubah 
____________________________________________________________________________________________________________________________________________________________________________________________________


while session == "in":
    try:
        print("------- Input Data --------")
        tarif_kerja = int(input("Masukkan gaji per jam (Rp): "))
        jam_kerja = int(input("Masukkan jumlah jam kerja: "))
        if tarif_kerja <= 0 or jam_kerja <= 0:
            print("Hanya menerima angka dan nilai positif")
            continue
    except ValueError:
        print("Input tidak valid, Hanya menerima angka dan nilai positif")
        continue

        
di baris 15-25 nah karena var session kita udah "on" karena kita sudah login kita bisa mulai menghitung gaji dengan menginput tarif kerja dan jam kerja dan disini saya udah pasang security agar hanya menerima inputan berupa angka dan bilangan positif
dan jika kita tidak menepati maka kita akan disuru mengisi ulang atau looping untuk meng input lagi 
____________________________________________________________________________________________________________________________________________________________________________________________________


    total_gaji = tarif_kerja * jam_kerja
    if jam_kerja >= 160:
        print("------- Gaji --------")
        bonus = total_gaji * 0.10
        total_gajinew = total_gaji + bonus
        print(f"Total Gaji: Rp. {total_gaji:}")
        print(f"Bonus yang diperoleh: Rp. {bonus:}")
        print(f"Total Gaji dengan bonus: Rp. {total_gajinew:}")
    else:
        print("------- Gaji --------")
        print(f"Total Gaji: Rp. {total_gaji:} (Tidak ada bonus, Lebih semangat lagi kerjanya LOL)")

        
baris 27-37 nah disini kita akan mengeluaran output gaji berdasarkan tarif dan jam kerja yang di input pada bari 5-13 dan disini ada deklarasi variable total_gaji yaitu tarif kerja X jam kerja untuk menghitung gaji dari karyawan  nah terus di lanjut dengan perkondisian  (pemakaian print(f"") atau f string digunakan agar saya bisa menyisipkan variable dalam print string)
if dan else. jadi if jam_kerja sama atau leboh dari 160 jam maka karyawan akan menerima bonus sebesar 10% dari total gaji nya dan else nya ya berati kayawan tidak menerima bonus karna jam kerja dibawah 160
____________________________________________________________________________________________________________________________________________________________________________________________________

    print("------- opsi --------")
    pilihan = input("Lanjut menghitung gaji? (y/n): ")
    if pilihan != 'y':
        print("Makasih dah pake program ini jangan lupa beri laiks dan subrek ")
        logged = "off"  
        break

        
39-44 disini merupakan bagian terakhir yaitu bagian opsi jika kita ingin menghitung gaji lagi atau mengsudahi. jika kita input "y" maka kita akan bisa menghitung gaji lagi langsung ke input tidak perlu login dan jika input "n"  maka program akan berakhir karena baris break yang menghentikan/keluar dari looping 
____________________________________________________________________________________________________________________________________________________________________________________________________


sekian dari laporan saya mengenai progam ini terimakasih.

--------------------------ScreenShot Output Program-----------------------
![Screenshot 2024-09-30 193939](https://github.com/user-attachments/assets/8359f3c7-4ce9-4542-bdb7-c4e5dff3ad79)
![Screenshot 2024-09-30 193728](https://github.com/user-attachments/assets/d88b8ef0-5249-4aab-8d2b-b769446e6e3c)
![Screenshot 2024-09-30 193800](https://github.com/user-attachments/assets/5e3c4087-4813-4bcb-bdc8-102385091af2)



--------------------------Flow chart-----------------------------------------
![gg drawio](https://github.com/user-attachments/assets/8011c581-aec8-49a0-a046-6191e88588bc)
