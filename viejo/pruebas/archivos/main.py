from fastapi import FastAPI, HTTPException, Query
from PIL import Image
from io import BytesIO
from starlette.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# Montar la carpeta "static"
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/images/{image_name}")
async def view_image(
    image_name: str,
    crop: str = Query(..., description="Parámetros de recorte en formato 'x1,y1,x2,y2'")
):
    try:
        # Construir la ruta completa de la imagen original
        image_path = f"static/images/{image_name}"

        # Verificar si la imagen existe
        try:
            im = Image.open(image_path)
        except Exception:
            raise HTTPException(status_code=404, detail="La imagen especificada no existe.")

        # Realizar el recorte
        x1, y1, x2, y2 = map(int, crop.split(','))
        box = (x1, y1, x2, y2)
        region = im.crop(box)

        # Crear un buffer de Bytes para almacenar la imagen recortada
        output = BytesIO()
        region.save(output, format="PNG")
        output.seek(0)

        # Guardar la imagen recortada en la carpeta 'editadas'
        edited_image_name = f"editadas/{image_name}"
        edited_image_path = f"static/{edited_image_name}"
        region.save(edited_image_path, format="PNG")

        # Devolver la URI para acceder a la imagen recortada
        edited_image_uri = f"https://localhost:8000/static/{edited_image_name}"

        return {"message": "Imagen recortada guardada en:", "edited_image_uri": edited_image_uri}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error al procesar la imagen: " + str(e))
