
from pathlib import Path
from PIL import Image
from reportlab.pdfgen import canvas

# Carpeta donde están las imágenes
carpeta = Path(__file__).parent
salida = carpeta / "esquema_completo.pdf"

# Formatos admitidos
extensiones = {".png", ".jpg", ".jpeg", ".webp", ".bmp", ".tif", ".tiff"}

imagenes = sorted(
    p for p in carpeta.iterdir()
    if p.suffix.lower() in extensiones
    and p.name != salida.name
)

if not imagenes:
    raise SystemExit("No se encontraron imágenes en la carpeta.")

# Crear un PDF con una página del tamaño de cada imagen
pdf = canvas.Canvas(str(salida), pageCompression=1)

for archivo in imagenes:
    with Image.open(archivo) as img:
        img = img.convert("RGB")
        ancho, alto = img.size

        pdf.setPageSize((ancho, alto))
        pdf.drawImage(
            str(archivo),
            0, 0,
            width=ancho,
            height=alto
        )
        pdf.showPage()

pdf.save()
print(f"PDF creado: {salida}")
print(f"Número de páginas: {len(imagenes)}")
