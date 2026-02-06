from fpdf import FPDF
import sys

class PDF(FPDF):
    def header(self):

        # Configura la fuente: helvetica negrita, tamaño 30
        self.set_font("helvetica", style="B", size=30)
        self.cell(0, 40, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")
        # Salto de línea de 10mm (espacio después del título)
        self.ln(10)

    def create_shirtificate(self, name):

        # 1. DEFINIR DIMENSIONES DEL "CUADRO" PARA LA IMAGEN
        box_width = 160  # Ancho deseado para la imagen (en milímetros)
        box_height = 180  # Alto deseado para el área (en milímetros)

        # 2. CALCULAR POSICIÓN CENTRADA HORIZONTALMENTE
        # self.w = ancho total de la página (210mm para A4)
        # self.l_margin = margen izquierdo (por defecto 10mm)
        # page_usable_width = ancho útil de la página (ancho total - 2 márgenes)
        page_usable_width = self.w - 2 * self.l_margin

        # x_pos = posición X donde empezará la imagen, centrada horizontalmente:
        # (ancho útil - ancho de imagen) / 2 + margen izquierdo
        x_pos = (page_usable_width - box_width) / 2 + self.l_margin

        # 3. POSICIÓN VERTICAL DESPUÉS DEL TÍTULO
        # 70mm desde el borde superior (título ocupa ~50mm + espacio)
        y_pos = 70

        # 4. INSERTAR IMAGEN ESCALADA
        # self.image() inserta una imagen con las siguientes propiedades:
        # - img_path: ruta del archivo de imagen
        # - x: posición horizontal desde el borde izquierdo
        # - y: posición vertical desde el borde superior
        # - w: ancho deseado (la imagen se escalará proporcionalmente)
        # - keep_aspect_ratio=True: mantiene las proporciones originales
        #   (el alto se calculará automáticamente)
        self.image(
            "/home/sabri/Escritorio/PYTHON/oop/shirtificate.png",
            x=x_pos,
            y=y_pos,
            w=box_width,
            keep_aspect_ratio=True,
        )

        # Configurar fuente para el texto
        self.set_font("helvetica", style="B", size=20)
        # Color del texto: blanco (RGB: 255, 255, 255)
        self.set_text_color(255, 255, 255)

        texto = f"{name} took CS50"
        texto_ancho = self.get_string_width(texto)
        texto_y = y_pos + box_height * 0.3  # Posición vertical del texto
        texto_x = x_pos + (box_width / 2) - (texto_ancho / 2)
        self.text(texto_x, texto_y, texto)
        # Insertar texto en la posición calculada
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
