# Ajustes y pruebas antes de escalar

## Regla de intervención
Buscar primero la solución en los ajustes del tema, de Moodle o del curso. Cambiar un solo elemento cada vez y anotar el valor anterior para poder volver.
No proponer SCSS propio si un ajuste lo cubre. No proponer cambios de código del tema.
Un cambio de tema afecta a todos los usuarios al momento: en sitios con actividad, probar en un sitio de pruebas o en horas de poco uso.

## Qué puede cambiar cada rol
| Rol | Puede cambiar | Dónde |
|---|---|---|
| Administrador | Todos los ajustes del tema, logotipos, modo oscuro (en Boost), bloques de la página de inicio | Apariencia > Temas > RSMAX |
| Docente con edición | Banners, presentación del módulo, áreas, etiquetas de actividad, bloques del curso y de su página de matriculación | En el curso |
| Docente o gestor | Finalización del curso y de las actividades, formato del curso, nombres de sección | Ajustes del curso (Moodle) |

## Lista de revisión rápida
| Síntoma | Primer ajuste a revisar | Prueba |
|---|---|---|
| Color que no cambia | Pestaña correcta guardada, formato hexadecimal, paleta en «Personalizada» | Ventana privada tras recargar |
| Botones ilegibles | Texto de los botones en automático | Mirar un botón principal |
| Logotipo ilegible | Logotipo compacto en PNG transparente; opción de logotipo en blanco | Cambiar solo esa opción |
| Sin progreso | Finalización del curso y de una actividad | Entrar como alumno de prueba |
| Módulo sin completar | Etiqueta progreso:no en opcionales | Completar el resto como alumno de prueba |
| Sin barra entre actividades | Ajuste de barra en todos los formatos | Abrir una actividad sin edición |
| Temario visible desde fuera | Contenido que se muestra antes de matricularse | Abrir el curso como persona no matriculada |

## Pruebas controladas
1. Línea base: captura de la página con el fallo, anotando rol, modo de edición, claro u oscuro y dispositivo.
2. Un cambio: aplicar un solo ajuste y guardar la pestaña.
3. Caché: recargar; si no cambia, purgar cachés.
4. Verificación: misma página, mismo rol, en ventana privada o con «Cambiar rol a» o un usuario de prueba. Un administrador ve siempre todos los bloques y nunca es «visitante».
5. Registro: valor anterior, valor nuevo, resultado. Si no mejora, volver al valor anterior antes de probar otra cosa.

## Pruebas útiles
- Aislar el tema: cambiar temporalmente a Boost. Si el problema sigue, no es del tema.
- Aislar el SCSS propio: vaciar los dos campos de Avanzado (guardando copia) y recargar.
- Aislar un plugin de terceros: comprobar si el fallo solo ocurre en sus páginas.
- Progreso: curso de prueba con tres actividades con finalización; completar una como alumno y comprobar «1 de 3» en la sección y el porcentaje en la cabecera.
- Paleta: anotar los cuatro colores, elegir una paleta, guardar, recargar; después volver a «Personalizada» y reescribirlos.
- Banner: subir una imagen de 1600 × 320, abrir la página principal, una sección y una actividad con cada valor de «Dónde se muestra».
- Página de matriculación: abrir la dirección del curso con un usuario no matriculado y revisar qué contenido se anuncia.
- Etiquetas: poner duracion:30min y tipo:hito en una actividad y comprobar la lista del curso con el Aula encendida.
- Modo oscuro: activarlo en Boost en un sitio de pruebas y revisar logotipo, banners y bloques de terceros.

## SCSS propio: condiciones
Solo si ningún ajuste lo cubre. Advertir: lo mantiene el cliente; puede dejar de funcionar al actualizar el tema o Moodle; un error de sintaxis puede dejar el sitio sin estilos. Pedir que se pruebe primero en un sitio de pruebas y que se guarde copia. No inventar nombres internos del tema: usar selectores que el cliente vea con el inspector del navegador, o pedirlos al mantenedor.

## Solicitud al mantenedor
Solo tras documentar los ajustes probados. Incluir: versión del tema y de Moodle, pasos, rol, capturas, resultado esperado, resultado obtenido, ajustes probados y su efecto. Enviar a julio@rsmax.es. No enviar datos personales de alumnos.
