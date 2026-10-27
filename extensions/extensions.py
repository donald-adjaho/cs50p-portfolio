# # CS50P Week 1 - Extensions.py
# # This program takes a file name as input and returns
# the corresponding MIME type.
# # The program checks the file extension and maps it to a MIME type.
# # If the file extension is not recognized, it
# returns "application/octet-stream".

def main() -> None:
    file_name = input("File name: ")
    print(map_file_extenions(file_name))


def map_file_extenions(file_name: str) -> str:
    if "." not in file_name:
        return "application/octet-stream"
    name, extensions = file_name.lower().strip().rsplit(".", 1)
    if file_name.strip().lower().endswith((".gif", ".png")):
        return f"image/{extensions}"
    if file_name.strip().lower().endswith((".jpg", ".jpeg")):
        return "image/jpeg"
    elif file_name.strip().lower().endswith((".pdf", ".zip")):
        return f"application/{extensions}"
    elif file_name.strip().lower().endswith(".txt"):
        return f"text/{name}"
    return "application/octet-stream"


if __name__ == "__main__":
    main()
