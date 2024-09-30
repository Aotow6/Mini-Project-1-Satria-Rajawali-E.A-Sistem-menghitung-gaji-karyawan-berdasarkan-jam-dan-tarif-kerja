usn_benar = "satria"
nim_benar = "067"
session = "off"  

while session == "off":
    print("------- Login --------")
    usn = input("Masukkan nama anda: ")
    nim = input("Masukkan NIM anda: ")
    if usn == usn_benar and nim == nim_benar:
        print(f"Login berhasil Selamat datang, {usn}.")
        session = "in"  
    else:
        print("Login error")

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

    print("------- opsi --------")
    pilihan = input("Lanjut menghitung gaji? (y/n): ")
    if pilihan != 'y':
        print("Makasih dah pake program ini jangan lupa beri laiks dan subrek ")
        logged = "off"  
        break
