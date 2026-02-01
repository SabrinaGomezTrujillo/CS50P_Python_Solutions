import sys
from PIL import Image,ImageOps


def main():
    if len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    elif len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    input_f = sys.argv[1].lower()   #caseinsensitive
    output_f = sys.argv[2].lower()

    try:
        input_ext = input_f[input_f.rfind("."):]
        output_ext =output_f[output_f.rfind("."):]
        if not input_f.endswith ((".jpeg",".png",".jpg")):
            print("Invalid input")
            sys.exit(1)

        elif input_ext != output_ext:
            print("Input and output have different extensions")
            sys.exit(1)

        else:
            with Image.open(input_f,"r") as image, Image.open("shirt.png") as shirt:
                tamaño = shirt.size
                imageFit=ImageOps.fit(image, tamaño)#,Resampling.BICUBIC, 0.0,(0.5, 0.5)
                imageFit.paste(shirt,shirt)
                imageFit.save(output_f)
    except FileNotFoundError:
        print("Input does not exist")
        sys.exit(1)


if __name__ == "__main__":
    main()
