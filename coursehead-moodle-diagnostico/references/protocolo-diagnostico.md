# Protocolo de casos

## Ficha mínima
Pedir según la consulta, no todo siempre:
- Versión de Moodle y del plugin; tema del sitio.
- Rol de quien configura y de quien no ve el efecto.
- Los once ajustes del sitio (captura o lista), en especial los tres interruptores y «Rutas excluidas».
- Del curso: qué muestra el panel «Estado actual» (estado, direcciones que aparecen, revisión) y qué casillas están marcadas.
- La página exacta donde falla: su dirección sin el nombre del sitio, y qué tipo de página es.
- El CSS o el JavaScript afectado, sin datos confidenciales.
- Mensaje literal, si hay alguno.
- Para restauraciones: quién restauró, con qué rol, y si el curso de destino tenía ya recursos.
No pedir claves, acceso administrativo ni el ZIP del plugin.

## Síntoma: no se aplica nada en ningún sitio del curso
1. ¿El panel dice «Todavía no hay recursos…»? No se guardó: revisar el mensaje al guardar.
2. ¿Dice «Desactivado»? Marcar «Habilitar recursos personalizados para este curso».
3. ¿Dice «Activado» pero no muestra la dirección del CSS (o del JavaScript)? Falta una de tres: el permiso del sitio para ese tipo, la casilla del curso o el contenido.
4. ¿Muestra la dirección y aun así no se ve nada? Comprobar «Habilitar el plugin» (el panel no lo refleja) y después pasar a «llega pero no se nota».
5. ¿Se está mirando la propia página del plugin o una pantalla de administración del curso? Ahí nunca se aplica.

## Síntoma: se aplica en unas páginas y en otras no
1. Clasificar la página: principal o sección, actividad, calificaciones, otra del curso, administración, fuera del curso.
2. Contrastar con las tres casillas del sitio y con cada línea de «Rutas excluidas» (comienzo de ruta, con barra inicial).
3. Recordar los casos normales: intento de cuestionario excluido de fábrica; calificaciones apagado de fábrica; portada del sitio y área personal, nunca.
4. Si la página debería recibirlo, pedir que se mire el código fuente de la página y se busque el comentario que el plugin escribe al principio y al final de sus referencias.

## Síntoma: llega pero no se nota (CSS)
Causas probables, por orden: selector que no existe en ese tema o en esa página; regla del tema con más prioridad; errata que invalida la regla o el bloque; propiedad que ese elemento no admite; el elemento se dibuja después.
Comprobación: inspeccionar el elemento en el navegador y ver si la regla aparece, y si aparece tachada. Probar con un selector más preciso antes de recurrir a forzar la prioridad.
No verificado: el orden exacto respecto al CSS del tema. No afirmar que «va después».

## Síntoma: llega pero no se nota (JavaScript)
1. Sitio: «Permitir JavaScript personalizado». Curso: casilla marcada (viene sin marcar).
2. Consola del navegador: un error de sintaxis impide ejecutar todo el programa.
3. Momento de ejecución: con carga diferida la página ya está leída; un programa que espera a un aviso de «página lista» que ya ocurrió puede no hacer nada. Con bloqueante, los elementos aún no existen.
4. Elementos que Moodle crea más tarde por su cuenta pueden no estar cuando el programa corre.
5. La página puede estar excluida (ver síntoma anterior).

## Síntoma: el formulario no guarda
- «El código no debe contener…»: localizar el fragmento literal. Si no hay etiquetas, buscar el falso positivo descrito en límites y separar los signos con un espacio.
- «El código supera la longitud máxima…»: reducir el código o pedir al administrador que suba el límite.
- «El código enviado no superó la validación y no se ha guardado»: el fallo está en un contenido guardado que quien edita no ve (sin permiso o tipo no permitido en el sitio), normalmente porque se bajó un límite después. Lo resuelve quien sí puede ver ese campo, o el administrador subiendo el límite.

## Síntoma: falta el enlace o faltan campos
- Sin enlace en el menú «Más»: falta el permiso de gestionar en ese curso.
- «La edición de … no está disponible»: el sitio no permite ese tipo o falta el permiso de edición. Son dos causas distintas; comprobar las dos.
- Sin botón de eliminar: el curso no tiene registro guardado.

## Síntoma: se perdió al restaurar, duplicar o importar
1. ¿Quién restauró y con qué permisos en el curso de destino? Sin el permiso de edición de cada tipo, ese tipo se descarta.
2. ¿El destino tenía ya recursos (aunque estuvieran vacíos o desactivados)? Se conserva lo del destino.
3. ¿El sitio de destino tiene límites más bajos? Se descarta lo que no cabe.
4. Evidencia: los avisos del registro de la restauración.
Solución de configuración: que un gestor vuelva a pegar el código, o repetir la restauración con un usuario con permisos sobre un curso sin recursos.

## Síntoma: el curso quedó inservible
Orden de actuación: entrar directamente a la página del plugin del curso (allí no se aplica nada) y desmarcar la casilla del tipo sospechoso; si no es posible, el administrador apaga «Permitir JavaScript personalizado» o «Habilitar el plugin». Nada de esto borra el código.

## Consultas de seguridad
Explicar siempre: el JavaScript se ejecuta con la sesión de cada participante; el filtro de etiquetas no es una barrera de seguridad; los cambios quedan en los registros de Moodle sin el contenido; el código es legible por cualquier participante; la entrega exige poder entrar al curso.

## Grado de certeza
Confirmado: evidencia directa del caso y regla documentada aplicable.
Probable: mecanismo compatible con el síntoma, pendiente de una comprobación concreta.
No comprobable: falta la evidencia decisiva; decir cuál.

## Escalamiento al mantenedor
Ficha breve: versiones, tema, síntoma, comportamiento esperado, ajustes relevantes, pasos de reproducción en un curso de prueba, ajustes ya probados con su resultado y evidencia que falta. No incluir código del plugin ni datos personales. No afirmar que se ha enviado.
