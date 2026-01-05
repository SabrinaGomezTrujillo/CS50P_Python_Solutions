file=input("Name of the file: ")
extension=file.rsplit(".", 1)[-1].lower()

if file.startswith('.') or ' .' in file or file == "" or '.' not in file:
    print("application/octet-stream")
else: extension


match extension:
        case "gif":
            print("image/gif")
        case "jpg" | "jpeg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "pdf":
            print("application/pdf")
        case "txt":
            print("text/plain")
        case "zip":
            print("application/zip")
        case _:
            print("application/octet-stream")


