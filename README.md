<p><strong></strong><strong><span id="Instalargoogle_images_download" data-mce-mark="1">&nbsp;</span><em style="font-size: 1.5em;">google_images_download</em></strong></p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>Como se puede observar, es simplemente una funci&oacute;n que recibe una serie de par&aacute;metros.</p>
<p>Los par&aacute;metros que obligatoriamente debemos pasarle a la funci&oacute;n son los siguientes:</p>
<ul>
<li><span id="Instalargoogle_images_download"><em>query:</em>&nbsp;</span>consulta que queremos realizar para buscar las im&aacute;genes. Es de tipo cadena y solo se puede pasar una &uacute;nica cadena.</li>
<li><em><span id="Instalargoogle_images_download">image_format:&nbsp;</span></em>formato en el cual queremos descargar las im&aacute;genes, por ejemplo png, jpg.</li>
<li><span id="Instalargoogle_images_download"><em>limit:&nbsp;</em></span>n&uacute;mero m&aacute;ximo de im&aacute;genes que queremos descargar.</li>
</ul>
<p>Adem&aacute;s de los par&aacute;metros obligatorios, tambi&eacute;n se pueden especificar otros dos par&aacute;metros, aunque &eacute;stos no son obligatorios porque tienen un valor por defecto:</p>
<ul>
<li><span id="Instalargoogle_images_download"><em>size:</em>&nbsp;</span>especifica el tama&ntilde;o de la imagen. Los valores que se pueden introducir son&nbsp;<em>large, medium, icon.</em></li>
<li><span id="Instalargoogle_images_download"><em>ratio:</em></span><em>&nbsp;</em>relaci&oacute;n de aspecto de la imagen, que puede tomar los valores&nbsp;<em>tall, square, wide, panoramic.</em></li>
</ul>
<p>En la funci&oacute;n simplemente realizaremos una petici&oacute;n de descarga con los par&aacute;metros que hayamos introducido especificados en un diccionario.</p>
<p>Si no se ha producido ninguna&nbsp;<a href="https://mapecode.com/excepciones-en-python/" rel="noopener noreferrer" target="_blank">excepci&oacute;n</a>&nbsp;durante la descarga las im&aacute;genes se habr&aacute;n guardado en una carpeta llamada&nbsp;<em>downloads,&nbsp;</em>localizada en el mismo directorio donde hayamos ejecutado el script.</p>
<h3><span id="Instalargoogle_images_download">Ejemplos de uso</span></h3>
<p>Ahora os voy a mostrar dos ejemplos de uso del script para descargar im&aacute;genes de google con Python:</p>
<ul>
<li>Descargar im&aacute;genes de python en formato icono:</li>
</ul>
<div class="EnlighterJSWrapper gitEnlighterJSWrapper"><ol class="hoverEnabled gitEnlighterJS EnlighterJS">
<li class=" odd"><span id="Instalargoogle_images_download">download_images</span><span id="Instalargoogle_images_download">(</span><span id="Instalargoogle_images_download">'python'</span><span id="Instalargoogle_images_download">, </span><span id="Instalargoogle_images_download">'jpg'</span><span id="Instalargoogle_images_download">, </span><span id="Instalargoogle_images_download">5</span><span id="Instalargoogle_images_download">, size=</span><span id="Instalargoogle_images_download">'icon'</span><span id="Instalargoogle_images_download">)</span></li>
</ol></div>
<ul>
<li>Descargar im&aacute;genes de m&uacute;ltiples consultas:</li>
</ul>
<div class="EnlighterJSWrapper gitEnlighterJSWrapper"><ol class="hoverEnabled gitEnlighterJS EnlighterJS">
<li class=" odd"><span id="Instalargoogle_images_download">queries = </span><span id="Instalargoogle_images_download">[</span><span id="Instalargoogle_images_download">'python'</span><span id="Instalargoogle_images_download">, </span><span id="Instalargoogle_images_download">'java'</span><span id="Instalargoogle_images_download">, </span><span id="Instalargoogle_images_download">'cpp'</span><span id="Instalargoogle_images_download">]</span></li>
<li class=" even"><span id="Instalargoogle_images_download">for</span><span id="Instalargoogle_images_download"> query </span><span id="Instalargoogle_images_download">in</span><span id="Instalargoogle_images_download"> queries:</span></li>
<li class=" odd"><span id="Instalargoogle_images_download"> download_images</span><span id="Instalargoogle_images_download">(</span><span id="Instalargoogle_images_download">query, </span><span id="Instalargoogle_images_download">'png'</span><span id="Instalargoogle_images_download">, </span><span id="Instalargoogle_images_download">5</span><span id="Instalargoogle_images_download">)</span></li>
</ol></div>
<h2><span id="Instalargoogle_images_download">Fuentes</span></h2>
<ul>
<li><a href="https://www.geeksforgeeks.org/how-to-download-google-images-using-python/" rel="nofollow noopener noreferrer" target="_blank">https://www.geeksforgeeks.org/how-to-download-google-images-using-python/</a></li>
</ul>
