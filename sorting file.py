import os
import shutil

# UBAH PATH SESUAI KOMPUTER KAMU

folder_path = "D:/fuji pcc"


file_types = {
    "images": [".jpg", ".jpeg", ".png"],
    "documents": [".pdf", ".docx", ".txt"],
    "videos": [".mp4", ".mkv"],
    "music": [".mp3"]
}


def organize_files():
    for file in os.listdir(folder_path):

        file_path = os.path.join(folder_path, file)

        # skip folder
        if os.path.isdir(file_path):
            continue

        # ambil ekstensi
        ext = os.path.splitext(file)[1].lower()

        moved = False

        # cek kategori
        for folder, extensions in file_types.items():
            if ext in extensions:

                target_folder = os.path.join(folder_path, folder)
                os.makedirs(target_folder, exist_ok=True)

                move_file(file_path, target_folder, file)
                print(f"Moved: {file} → {folder}")

                moved = True
                break

        # jika tidak masuk kategori
        if not moved:
            other_folder = os.path.join(folder_path, "others")
            os.makedirs(other_folder, exist_ok=True)

            move_file(file_path, other_folder, file)
            print(f"Moved: {file} → others")


# FUNCTION UNTUK HANDLE DUPLIKAT

def move_file(src, dest_folder, filename):

    dest_path = os.path.join(dest_folder, filename)

    # kalau file sudah ada → rename
    if os.path.exists(dest_path):
        name, ext = os.path.splitext(filename)
        counter = 1

        while True:
            new_name = f"{name}_{counter}{ext}"
            new_path = os.path.join(dest_folder, new_name)

            if not os.path.exists(new_path):
                dest_path = new_path
                break

            counter += 1

    shutil.move(src, dest_path)


# PROGRAM EXCUSION

if __name__ == "__main__":
    try:
        organize_files()
        print("\nSelesai!")
    except Exception as e:
        print("Terjadi error:", e)
