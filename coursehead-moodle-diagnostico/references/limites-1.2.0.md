# Límites y valores por defecto: versión 1.2.0

Verificados leyendo el código de 1.2.0 el 15-11-2026. Un límite documentado es un hecho; que haya causado un incidente concreto es una conclusión aparte.

## Valores de fábrica del sitio
| Ajuste | Valor de fábrica |
|---|---|
| Habilitar el plugin | Sí |
| Permitir CSS personalizado | Sí |
| Permitir JavaScript personalizado | No |
| Inyectar en la página principal del curso | Sí |
| Inyectar en páginas de actividades | Sí |
| Inyectar en páginas de calificaciones | No |
| Rutas excluidas | Una línea: /mod/quiz/attempt.php |
| Longitud máxima del CSS | 200000 caracteres |
| Longitud máxima del JavaScript | 200000 caracteres |
| Mostrar advertencias de seguridad | Sí |
| Estrategia de carga de JavaScript por defecto | Diferida (recomendada) |

## Valores de fábrica del curso
| Campo | Valor de fábrica |
|---|---|
| Habilitar recursos personalizados para este curso | Marcado |
| Habilitar CSS personalizado | Marcado |
| CSS personalizado | Vacío |
| Habilitar JavaScript personalizado | Sin marcar |
| JavaScript personalizado | Vacío |
| Estrategia de carga de JavaScript | La que fije el sitio en ese momento (Diferida) |

## Tamaños
- La longitud se cuenta en caracteres, no en bytes; cuentan espacios y saltos de línea.
- 0 (o un número negativo) en una longitud máxima significa sin límite del plugin. Siguen existiendo los límites del servidor para el envío de formularios, que el plugin no controla.
- Los límites se aplican al guardar y al restaurar, no al servir. Bajar un límite no desactiva el código ya guardado, pero impide volver a guardar ese curso hasta que el código quepa.
- Un único CSS y un único JavaScript por curso. No hay varios archivos, ni versiones anteriores, ni historial: al guardar se sustituye lo anterior.
- No se pueden subir imágenes, tipografías ni otros archivos.

## Validación: qué se rechaza
- Seis fragmentos literales, sin distinguir mayúsculas: apertura y cierre de etiqueta style, apertura y cierre de etiqueta script, apertura de PHP y cierre de PHP (interrogación seguida de «mayor que»).
- Falsos positivos conocidos: un JavaScript correcto que compare sin espacios una variable con otra cuyo nombre empiece por «script» o «style» (por ejemplo, un contador «menor que» scripts) contiene el fragmento y se rechaza. También una interrogación seguida inmediatamente de «mayor que» dentro de una cadena o de un selector. Solución: añadir un espacio entre los dos signos o partir la cadena.
- No se detectan errores de sintaxis, selectores inexistentes, reglas inútiles ni programas dañinos.

## Páginas
- Nunca: portada del sitio, área personal y cualquier página fuera de un curso; páginas con diseño de administración, acceso, mantenimiento, redirección o incrustado; rutas de la administración del sitio.
- «Rutas excluidas»: coincidencia por comienzo de ruta, relativa a la raíz de Moodle (sin subcarpeta de instalación), distingue mayúsculas, no admite comodines ni mira lo que sigue al signo de interrogación. Una línea que no empieza por barra no coincide con nada. Las líneas que empiezan por almohadilla son comentarios.
- De fábrica solo queda excluida la pantalla del intento de cuestionario. La entrada, el resumen y la revisión del cuestionario sí reciben recursos mientras «Inyectar en páginas de actividades» esté encendido.
- Las tres casillas de tipo de página valen para todo el sitio; no hay ajuste por curso.
- Las páginas del curso que no son principal, actividad ni calificaciones reciben recursos siempre, salvo exclusión por ruta.
- Las pantallas de calificaciones que usan diseño de administración (por ejemplo, la configuración del libro) no reciben recursos aunque la casilla esté encendida.

## Ámbito
- Por curso completo. No por sección, actividad concreta, grupo, rol ni usuario.
- El mismo contenido para todos los participantes.

## Caché y tiempos
- Revisión: 16 caracteres; cambia en cada guardado y en cada restauración.
- Con la revisión vigente, el navegador puede conservar el archivo 7 días sin volver a pedirlo; la caché es privada (no compartida entre usuarios).
- Tras guardar, el cambio se ve al abrir o recargar una página del curso. Una página que ya estaba abierta no cambia hasta recargarla.
- Los cambios en los ajustes del sitio valen desde la siguiente página que se abra.
- No hay tiempos de espera, reintentos, cuotas ni tareas programadas.

## Estrategias de carga
- Diferida: el programa se ejecuta después de que el navegador haya leído la página.
- Bloqueante: el programa se descarga y se ejecuta antes de seguir dibujando la página.
- La del sitio solo fija la opción inicial del desplegable en un curso sin configurar; no cambia cursos ya guardados.

## Restauración
- Requiere el permiso de edición correspondiente de quien restaura, en el curso de destino.
- No sobrescribe un curso de destino que ya tenga registro de recursos, ni siquiera si está vacío o desactivado.
- Si tras los descartes no queda CSS ni JavaScript, no se crea registro.

## Compatibilidad declarada
Moodle 4.5 LTS a 5.3. Idiomas incluidos: inglés y español.
