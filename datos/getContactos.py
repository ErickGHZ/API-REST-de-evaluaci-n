@app.get("/contactos", summary="Endpoint para obtener todos los contactos")
def obtener_contactos():
    """
    # Endpoint para obtener todos los contactos.
    ## Status Code
    * 200 OK: Lista de contactos encontrados.
    * 430 Not Found: Si no se encuentran contactos en la base de datos.
    * 500 Internal Server Error: En caso de un error interno del servidor.
    """
    contactos = []
    try:
        # Intentar abrir y leer el archivo CSV de contactos
        with open('contactos.csv', 'r', newline='') as archivo_csv:
            lector_csv = csv.DictReader(archivo_csv)
            for fila in lector_csv:
                contactos.append(fila)
    except Exception as e:
        # Si hay un error al leer el archivo, lanzar una excepción de servidor interno
        raise HTTPException(status_code=500, detail=f"Error en el servidor: {str(e)}")
    
    if not contactos:
        raise HTTPException(status_code=430, detail="No se encontraron contactos")
    
    return contactos
