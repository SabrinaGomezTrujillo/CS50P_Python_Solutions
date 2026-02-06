from fpdf import FPDF
import sys

class PDF(FPDF):
    def header(self):


        self.set_font("Times", style="B", size=30)
        self.cell(0, 40, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")
        self.ln(10)

    def create_shirtificate(self, name):


        box_width = 160
        box_height = 180

        page_usable_width = self.w - 2 * self.l_margin

        x_pos = (page_usable_width - box_width) / 2 + self.l_margin
        y_pos = 70

        self.image(
            "shirtificate.png",
            x=x_pos,
            y=y_pos,
            w=box_width,
            keep_aspect_ratio=True,
        )


        self.set_font("Times", style="B", size=20)

        self.set_text_color(255, 255, 255)

        texto = f"{name} took CS50"
        texto_ancho = self.get_string_width(texto)
        texto_y = y_pos + box_height * 0.3
        texto_x = x_pos + (box_width / 2) - (texto_ancho / 2)
        self.text(texto_x, texto_y, texto)
        self.text(texto_x, texto_y, f"{name} took CS50")


def valid_name():
        while True:
            try:
                 name = input("Name: ")
                 if not name:
                    print("Missing name")
                    continue
                 elif len(name) > 15:
                    print("Name too long")
                    continue
                 else:
                    return name
            except EOFError:
                sys.exit(1)

def main():
    name = valid_name()
    if name:
            pdf = PDF()
            pdf.add_page()
            pdf.create_shirtificate(name.capitalize())
            pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
