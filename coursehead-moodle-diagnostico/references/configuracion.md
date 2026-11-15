# Configuración: ajustes y recomendaciones

Nombres tal como se ven en Moodle en español, versión 1.2.0. Explicación ampliada y ejemplos interactivos en el manual: https://claude.ai/artifact/S1C8aFgCzaqxcegdHXqanX

## Ajustes del sitio
Dónde: Administración del sitio › Extensiones › Extensiones locales › Recursos personalizados en el head del curso. Solo administradores. Una sola página.

| Ajuste | Qué hace | Recomendación |
|---|---|---|
| Habilitar el plugin | Interruptor general. Apagado, ningún curso recibe CSS ni JavaScript; no se borra nada. | Encendido. Apagarlo es la medida de emergencia para todo el sitio. |
| Permitir CSS personalizado | Permite editar y aplicar el CSS de los cursos. | Encendido. |
| Permitir JavaScript personalizado | Permite editar y aplicar el JavaScript de los cursos. | Apagado salvo necesidad real. Antes de encenderlo, revisar quién tiene el permiso de editar JavaScript. |
| Inyectar en la página principal del curso | Aplica los recursos en la página principal y en las de sección. | Encendido. |
| Inyectar en páginas de actividades | Aplica los recursos dentro de actividades y recursos. | Encendido, salvo que se quiera limitar la personalización a la portada del curso. |
| Inyectar en páginas de calificaciones | Aplica los recursos en el libro de calificaciones y sus informes. | Apagado: son páginas sensibles. |
| Rutas excluidas | Lista de comienzos de ruta donde nunca se aplica nada. Una por línea, empezando por barra. | Mantener la línea de fábrica. Añadir /mod/quiz/ si hay exámenes que cuentan y, sobre todo, si se permite JavaScript. |
| Longitud máxima del CSS | Tope de caracteres por curso. 0 = sin límite. | Dejar 200000. |
| Longitud máxima del JavaScript | Igual, para JavaScript. | Dejar 200000. |
| Mostrar advertencias de seguridad | Aviso amarillo en la página del curso para quien puede editar JavaScript. | Encendido. |
| Estrategia de carga de JavaScript por defecto | Opción inicial del desplegable en cursos sin configurar. | Diferida. |

## Permisos
Dónde: Administración del sitio › Usuarios › Permisos › Definir roles; buscar «coursehead».

| Permiso | De fábrica | Recomendación |
|---|---|---|
| Gestionar los recursos personalizados del curso | Gestor | Imprescindible para entrar a la página. Quien lo tiene puede eliminar todos los recursos del curso. |
| Editar el CSS personalizado del curso | Gestor | Se puede dar al profesorado con edición si la institución confía en él. Necesita también el anterior. |
| Editar el JavaScript personalizado del curso (solo usuarios de confianza) | Gestor | No darlo a roles que no sean de total confianza: permite ejecutar programas en el navegador de todos los participantes. |

Los tres permisos están marcados en Moodle con riesgo de seguridad; el de JavaScript, además, con riesgo de configuración. Es lo esperado.

## Ajustes del curso
Dónde: dentro del curso, menú «Más» › Recursos personalizados del curso.

| Campo | Qué hace | Recomendación |
|---|---|---|
| Habilitar recursos personalizados para este curso | Interruptor del curso. Desmarcado, no se aplica nada y no se borra nada. | Usarlo para descartar si un problema viene del código del curso. |
| Habilitar CSS personalizado | Aplica o pausa el CSS. | Marcado cuando el CSS esté listo. |
| CSS personalizado | Texto con las reglas CSS, sin etiquetas. | Empezar por pocas reglas y selectores precisos. Comprobar en la página principal y en una actividad. |
| Habilitar JavaScript personalizado | Ejecuta o pausa el JavaScript. | Marcar solo tras probar el programa en un curso de prueba. |
| JavaScript personalizado | Texto con el programa, sin etiquetas. | Programas pequeños, sin datos confidenciales, que no fallen si falta un elemento en la página. |
| Estrategia de carga de JavaScript | Diferida o Bloqueante. | Diferida. |

## Configuraciones tipo
- Solo aspecto, gestionado por gestores: todo de fábrica.
- Aspecto gestionado por el profesorado: de fábrica, más los dos primeros permisos para el rol de profesor con edición.
- Aspecto y comportamiento: encender «Permitir JavaScript personalizado», mantener el permiso de JavaScript solo en gestores de confianza y añadir /mod/quiz/ a «Rutas excluidas».
- Máxima prudencia: apagar «Inyectar en páginas de actividades» para que solo cambie la portada de cada curso.

## Buenas prácticas para el código del cliente
- Guardar una copia del CSS y del JavaScript fuera de Moodle: el plugin no conserva versiones anteriores.
- Probar con una cuenta de alumno y en móvil.
- Ocultar un elemento con CSS no impide usarlo ni protege datos.
- No depender de nombres de elementos que cambian con el tema sin volver a probar tras cada actualización de Moodle o del tema.
