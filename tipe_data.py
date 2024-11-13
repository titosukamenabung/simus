# Program untuk menyimpan informasi tentang buku

 
def input_buku():

    judul = input("Masukkan judul buku: ")
    
    # Menginput tahun terbit (integer)
    tahun_terbit = int(input("Masukkan tahun terbit: "))
    
     
    harga = float(input("Masukkan harga buku: "))
    
     
    penulis = input("Masukkan nama penulis: ")
    

    genre = input("Masukkan genre buku (pisahkan dengan koma): ").split(',')
    genre = [g.strip() for g in genre]   
     
    tersedia = input("Apakah buku ini tersedia? (ya/tidak): ").strip().lower() == 'ya'
    

    return {
        "judul": judul,
        "tahun_terbit": tahun_terbit,
        "harga": harga,
        "penulis": penulis,
        "genre": genre,
        "tersedia": tersedia
    }


def main():
     
    daftar_buku = []
    
    while True:
        print("\n--- Input Data Buku ---")
        buku = input_buku()
        
         
        daftar_buku.append(buku)
        
         
        lagi = input("Apakah Anda ingin menambah buku lain? (ya/tidak): ").strip().lower()
        if lagi != 'ya':
            break
    
     
    print("\n--- Daftar Buku ---")
    for b in daftar_buku:
        print(f"Judul: {b['judul']}, Tahun Terbit: {b['tahun_terbit']}, Harga: {b['harga']}, Penulis: {b['penulis']}, Genre: {', '.join(b['genre'])}, Tersedia: {'Ya' if b['tersedia'] else 'Tidak'}")

 
if __name__ == "__main__":
    main()