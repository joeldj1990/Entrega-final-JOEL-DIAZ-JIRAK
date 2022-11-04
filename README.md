# Entrega-intermedia


Web básica de Óptica


Página de inicio, en la ruta ".app1/", que sirve más que nada como carátula.

Tres tipos diferentes de "productos" (anteojos, anteojos de sol y lentes) correspondientes a las clases de models.py, que contienen un listado de diferentes modelos de anteojos y lentes (con características como marca, color, tamaño, precio, etc), los cuales pueden ser agregados a través de la función presente al final de cada listado utilizando diferentes formularios o a través de "admin/".

Pestañas de "horarios" y "preguntas frecuentes", cuyo único propósito es el de experimentar con html y css.

Opción de búsqueda a través del código único de producto (número de 5 dígitos) las características de los distintos productos. Sólo busca en "anteojos", ignora las clases "anteojos de sol" y "lentes"
(Para testear, utilizar cualquier número entre 10000 y 10007, cualquier otro devuelve el mensaje predefinido "No hay datos")

Header y footer siempre presentes sin importar el template, gracias a la herencia de éstos, lo cual permite un rápido desplazamiento entre templates.
EL header se mantiene visible incluso si se scrollea hacia abajo.
