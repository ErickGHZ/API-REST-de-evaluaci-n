from fastapi import FastAPI, status, UploadFile, File, Form
from fastapi.staticfiles import StaticFiles
from PIL import Image
import os
from typing import List
from io import BytesIO
from fastapi.responses import HTMLResponse

app = FastAPI()

# Ruta de la carpeta de imágenes
images_folder = "static/images"
os.makedirs(images_folder, exist_ok=True)

# Monta la carpeta "static" para servir archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")
upload_folder = "static/images"

@app.post("/subir_imagen", status_code=status.HTTP_201_CREATED, summary="Endpoint para subir imágenes")
async def crear_imagen(
    imagenes: List[UploadFile] = File(...),
    cortar: str = Form(None),
    rotar: str = Form(None),
    redimensionar: str = Form(None)
):
    print(f"cortar: {cortar}")
    print(f"rotar: {rotar}")
    print(f"redimensionar: {redimensionar}")

    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)

    for archivo in imagenes:
        image = Image.open(BytesIO(archivo.file.read()))

        if cortar:
            izquierda, arriba, derecha, abajo = map(int, cortar.split(","))
            image = image.crop((izquierda, arriba, derecha, abajo))

        if rotar:
            angulo = int(rotar)
            image = image.rotate(angulo)

        if redimensionar:
            ancho, alto = map(int, redimensionar.split(","))
            image = image.resize((ancho, alto))

        image.save(os.path.join(upload_folder, archivo.filename))

    return {"message": "Archivos subidos y editados correctamente"}

@app.get("/", response_class=HTMLResponse)
async def main():
    content = """
    <!DOCTYPE html>
    <body>
        <h1>Subir y Editar Imágenes</h1>
        <form action="/subir_imagen" method="post" enctype="multipart/form-data">
            <label for="imagenes">Selecciona una imagen:</label>
            <input type="file" id="imagenes" name="imagenes" accept="image/*">
            <br>
            <h2>Editar Imagen:</h2>
            <label for="cortar">Cortar (izquierda, arriba, derecha, abajo):</label>
            <input type="text" id="cortar" name="cortar" placeholder="100,100,300,300">
            <br>
            <label for="rotar">Rotar (grados):</label>
            <input type="text" id="rotar" name="rotar" placeholder="45">
            <br>
            <label for "redimensionar">Redimensionar (ancho, alto):</label>
            <input type="text" id="redimensionar" name="redimensionar" placeholder="800,600">
            <br>
            <input type="submit" value="Subir y Editar Imagen">
        </form>
    </body>
    """
    return content
