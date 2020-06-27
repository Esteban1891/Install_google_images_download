***<span id="Instalargoogle_images_download" data-mce-mark="1"> </span>_google_images_download_***

Como se puede observar, es simplemente una función que recibe una serie de parámetros.

Los parámetros que obligatoriamente debemos pasarle a la función son los siguientes:

*   <span id="Instalargoogle_images_download">_query:_ </span>consulta que queremos realizar para buscar las imágenes. Es de tipo cadena y solo se puede pasar una única cadena.
*   _<span id="Instalargoogle_images_download">image_format: </span>_formato en el cual queremos descargar las imágenes, por ejemplo png, jpg.
*   <span id="Instalargoogle_images_download">_limit: _</span>número máximo de imágenes que queremos descargar.

Además de los parámetros obligatorios, también se pueden especificar otros dos parámetros, aunque éstos no son obligatorios porque tienen un valor por defecto:

*   <span id="Instalargoogle_images_download">_size:_ </span>especifica el tamaño de la imagen. Los valores que se pueden introducir son _large, medium, icon._
*   <span id="Instalargoogle_images_download">_ratio:_</span>relación de aspecto de la imagen, que puede tomar los valores _tall, square, wide, panoramic._

En la función simplemente realizaremos una petición de descarga con los parámetros que hayamos introducido especificados en un diccionario.

Si no se ha producido ninguna [excepción](https://mapecode.com/excepciones-en-python/) durante la descarga las imágenes se habrán guardado en una carpeta llamada _downloads, _localizada en el mismo directorio donde hayamos ejecutado el script.

### <span id="Instalargoogle_images_download">Ejemplos de uso</span>

Ahora os voy a mostrar dos ejemplos de uso del script para descargar imágenes de google con Python:

*   Descargar imágenes de python en formato icono:

<div class="EnlighterJSWrapper gitEnlighterJSWrapper">

1.  <span id="Instalargoogle_images_download">download_images</span><span id="Instalargoogle_images_download">(</span><span id="Instalargoogle_images_download">'python'</span><span id="Instalargoogle_images_download">,</span> <span id="Instalargoogle_images_download">'jpg'</span><span id="Instalargoogle_images_download">,</span> <span id="Instalargoogle_images_download">5</span><span id="Instalargoogle_images_download">, size=</span><span id="Instalargoogle_images_download">'icon'</span><span id="Instalargoogle_images_download">)</span>

</div>

*   Descargar imágenes de múltiples consultas:

<div class="EnlighterJSWrapper gitEnlighterJSWrapper">

1.  <span id="Instalargoogle_images_download">queries =</span> <span id="Instalargoogle_images_download">[</span><span id="Instalargoogle_images_download">'python'</span><span id="Instalargoogle_images_download">,</span> <span id="Instalargoogle_images_download">'java'</span><span id="Instalargoogle_images_download">,</span> <span id="Instalargoogle_images_download">'cpp'</span><span id="Instalargoogle_images_download">]</span>
2.  <span id="Instalargoogle_images_download">for</span> <span id="Instalargoogle_images_download">query</span> <span id="Instalargoogle_images_download">in</span> <span id="Instalargoogle_images_download">queries:</span>
3.  <span id="Instalargoogle_images_download">download_images</span><span id="Instalargoogle_images_download">(</span><span id="Instalargoogle_images_download">query,</span> <span id="Instalargoogle_images_download">'png'</span><span id="Instalargoogle_images_download">,</span> <span id="Instalargoogle_images_download">5</span><span id="Instalargoogle_images_download">)</span>

</div>

## <span id="Instalargoogle_images_download">Fuentes</span>

*   [https://www.geeksforgeeks.org/how-to-download-google-images-using-python/](https://www.geeksforgeeks.org/how-to-download-google-images-using-python/)
