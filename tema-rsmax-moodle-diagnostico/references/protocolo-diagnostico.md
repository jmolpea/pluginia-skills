# Protocolo de diagnóstico

## Ficha mínima
Pedir según la consulta, no todo siempre:
- Versión del tema (Administración del sitio > Extensiones > Vista general) y de Moodle.
- Si el tema está solo o con el paquete premium (bloques Pluginia, asistente de IA).
- Dónde ocurre: todo el sitio, una página concreta o un curso; dirección de la página sin datos personales.
- Con qué rol se ve (administrador, docente, alumno, visitante) y si la edición está activada.
- Captura de la página y de la pestaña de ajustes implicada.
- Qué se cambió justo antes (paleta, color, logotipo, actualización del tema o de Moodle).
- Para cursos: formato del curso, si tiene finalización activada y si el Aula RSMAX está encendida.
- Modo claro u oscuro; escritorio o móvil; navegador.
No pedir contraseñas, acceso de administrador ni datos de alumnos.

## Árbol síntoma > causas > comprobación

### Los colores no cambian tras guardar
1. Caché: recargar; purgar cachés de Moodle. Comprobación: abrir en ventana privada.
2. Se guardó otra pestaña: Moodle solo guarda la pestaña abierta.
3. El color no está en hexadecimal: se descarta. Comprobación: revisar el campo.
4. Una paleta elegida en el mismo guardado pisó el color: dejar «Personalizada» y volver a escribirlo.
5. SCSS propio en Avanzado impone otro color: vaciarlo temporalmente.

### Elegí la misma paleta y no pasa nada
La paleta actúa cuando el desplegable cambia. Guardar «Personalizada» y volver a elegirla.

### Perdí mis colores al elegir una paleta
Comportamiento previsto. No hay deshacer: reescribir los colores; consultar el registro de cambios de configuración de Moodle para recuperar los valores anteriores.

### Logotipo invisible, blanco macizo o sin colores en el menú
1. Menú oscuro o de marca con logotipo para fondo blanco y la opción de logotipo en blanco apagada.
2. Logotipo con fondo no transparente y la opción encendida: sale un rectángulo blanco.
3. Se subió el logotipo normal, pero el menú usa el compacto.
4. En modo oscuro el tema pone una placa clara detrás del logotipo: es intencionado.

### No aparece el botón del menú
Falta texto o enlace; el enlace no empieza por / ni es una dirección completa; o quien mira ha iniciado sesión y el botón es solo para visitantes. Comprobación: ventana privada.

### Faltan enlaces o columnas del pie
Líneas sin barra vertical, sin texto o con dirección no válida se ignoran. Una columna sin enlaces válidos no se muestra. Redes: dirección completa.

### No aparece el progreso
1. El curso no tiene finalización activada o ninguna actividad la tiene.
2. El ajuste de progreso del curso está apagado (también apaga el de sección).
3. Edición activada, invitado, o rol no seguido por la finalización (un docente).
4. Todas las actividades con finalización llevan la etiqueta de exclusión.
Comprobación: entrar como un alumno de prueba, sin edición.

### Un módulo nunca se completa o el porcentaje parece bajo
Actividades opcionales con finalización, o secciones bloqueadas visibles que cuentan en el total. Ajuste: etiqueta progreso:no en las opcionales.

### No aparece la cabecera con imagen, el mapa o «tu siguiente paso»
Cabecera apagada; edición activada; Aula apagada (sin mapa ni siguiente paso); sin progreso no hay mapa; sitio actualizado desde una versión sin Aula (queda apagada hasta que el administrador la encienda).

### No aparece «Añadir presentación del módulo» o «Añadir área»
Presentación: Aula encendida, edición activada, página principal del curso y permiso para editar los ajustes del curso; en la primera sección solo si ya existe. Área: edición activada y permiso para gestionar actividades.

### No veo «Aspecto de las páginas del curso»
Solo existe con el Aula apagada.

### El banner no se ve
1. Banner de curso con «solo en la página principal» y se mira una actividad.
2. La sección tiene banner propio.
3. En la página de matriculación, a personas que no pueden entrar en el curso puede no cargarles el banner subido (los archivos se sirven a quien puede entrar): probable; verificar con una persona no matriculada. Alternativa: usar la imagen del curso.
4. Caché del curso: purgar cachés.

### Falta la barra anterior/siguiente
Ajuste apagado; edición activada; página con otra barra fija (cuestionario); formato que admite la barra pero la tiene apagada en sus ajustes; actividad oculta.

### La apertura de la página de inicio no sale
Ajuste apagado, o hay un bloque Pluginia visible con contenido. Los visitantes no ven el buscador si el sitio obliga a iniciar sesión.

### El alumno ha «perdido» pestañas del curso
Con el Aula, quien no puede editar ve solo «Curso» y «Mis entregas». Previsto. Si se necesitan otras pestañas, apagar el Aula (afecta a todo el sitio) o consultar al mantenedor.

### El asistente no aparece o aparece donde no debe
Sin el bloque instalado o sin clave de IA no hay chat. El del sitio nunca entra en cursos; el del curso no aparece durante un intento de cuestionario; uno oculto en la página del curso sigue oculto. Los cursos anteriores a la instalación no reciben asistente solos: añadir el bloque.

### Los bloques por defecto no llegan a los cursos nuevos
El sitio fijó sus bloques por otra vía (archivo de configuración o valor ajeno al tema): el tema no lo pisa. Los cursos existentes nunca cambian.

### Sitio sin estilos o roto tras tocar Avanzado
Error en el SCSS propio. Vaciar ambos campos, guardar y purgar cachés.

### Error al guardar la presentación de un módulo
Probable: un campo de una línea supera 255 caracteres. Acortarlo.

### Tras restaurar un curso faltan banners o presentaciones
Se restauran con la copia si esta incluía los archivos del curso. Verificar que el tema está instalado en el sitio de destino. Los ajustes del tema (colores, logotipo) no viajan con el curso.

## Cuándo escalar al mantenedor
Tras probar los ajustes pertinentes sin éxito, o ante un error de Moodle con el tema activo que desaparece al cambiar a Boost. Aportar: versiones, pasos exactos, rol, capturas, resultado esperado y obtenido, y qué ajustes se probaron.
