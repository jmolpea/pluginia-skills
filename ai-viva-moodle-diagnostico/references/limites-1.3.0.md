# Límites y valores por defecto de AI Viva 1.3.0

Verificados en una revisión estática de la versión 1.3.0, revisada el 15-11-2026. «Fijo» significa que no hay ajuste para cambiarlo. Que un límite exista no demuestra que haya causado un incidente concreto.

## Licencia
| Concepto | Valor |
|---|---|
| Periodo de evaluación sin clave | 15 días desde el primer uso (fijo) |
| Vinculación de la clave | Dirección web exacta del sitio; cambiar de dominio, de carpeta o de http a https la invalida |
| Comprobación | Sin conexión a internet |

## Ajustes del sitio
| Ajuste (nombre en pantalla) | De fábrica | Mínimo o comportamiento |
|---|---|---|
| Modelos disponibles para el profesorado | Los tres marcados | Si no se marca ninguno, se ofrecen los tres |
| Activar moderación de contenido de OpenAI | Activado | Solo filtra texto; si el filtro no responde, la llamada continúa |
| Máximo de tokens por llamada a la API | 16000 | Valores menores de 256 se tratan como 256 |
| Tamaño máximo global de video (MB) | 500 | Techo para el tamaño de vídeo de cada actividad |
| Conservación de grabaciones por defecto (días) | 15 | Solo propone el valor en actividades nuevas |
| Texto del aviso RGPD | Vacío | Vacío = aviso incluido, traducido al idioma del alumno |
| Tiempo de espera de la API (segundos) | 300 | Valores menores de 30 se tratan como 30 |
| Máximo de llamadas a la API por usuario por minuto | 30 | Valores menores de 1 se tratan como 1; el 0 no significa «sin límite» |

## Ajustes de la actividad
| Ajuste (nombre en pantalla) | De fábrica | Opciones o límites |
|---|---|---|
| Nombre de la actividad | — | Obligatorio, hasta 255 caracteres |
| Número máximo de intentos | 2 | 1, 2, 3 o Ilimitado |
| Apertura · Cierre | Sin fecha | El cierre debe ser posterior a la apertura |
| Tamaño máximo del PDF (MB) | 20 | Mínimo 1; el formulario no impone máximo |
| Duración máxima de la presentación | 10 min | 5, 10, 15 o 30 minutos |
| Tamaño máximo del archivo de video (MB) | El máximo global (500) | Entre 1 y el máximo global |
| Duración de la sesión del tribunal (minutos) | 10 | Mínimo 1; el formulario no impone máximo |
| Modelo IA (documento, tribunal, evaluación) | GPT-6.1 Sol | GPT-6.1 Sol, GPT-6 Astra, GPT-6 Luna (los permitidos) |
| Nombres de los miembros | Dr. Smith, Prof. Johnson, Dr. Williams | Vacío = «Examinador N» |
| Rol / Cargo | Chair, Reviewer, Subject Expert | Texto libre |
| Voz TTS | Onyx, Nova, Echo | 13 voces: Alloy, Ash, Ballad, Cedar, Coral, Echo, Fable, Marin, Nova, Onyx, Sage, Shimmer, Verse |
| Avatar | 3 (masculino), 2 (femenino), 1 (neutro) | Tres incluidos o una imagen propia (un archivo de imagen) |
| Calificación máxima | 100 | Entero, mínimo 1 |
| Pesos documento · presentación · tribunal | 33 · 33 · 34 | Enteros de 0 a 100 que sumen exactamente 100 |
| Retener las calificaciones para revisión del profesor | Activado | — |
| Notificar al estudiante cuando se publique la nota | Activado | — |
| Conservar las grabaciones (días) | Valor del sitio (15) | 0 = no borrar nunca; no admite negativos |
| Excepción: número máximo de intentos | Por defecto | 1 a 20 o Ilimitado |

## Archivos y formatos
| Concepto | Valor |
|---|---|
| Documento | Solo PDF; se comprueba el contenido real del archivo, no la extensión |
| Vídeo de la presentación | WebM o MP4 generado por el navegador (también se acepta Ogg) |
| Audio de la presentación | Partes consecutivas de 4 minutos; hasta 20 partes; cada una de 25 MB como máximo |
| Capturas de pantalla | Hasta 40 por presentación, JPEG, lado mayor 1280 px, 1 MB como máximo cada una; una cada 15 segundos o más según la duración |
| Respuesta al tribunal | Hasta 5 minutos y 25 MB por respuesta; menos de 0,8 segundos se descarta como demasiado corta |
| Recorte del trabajo del alumno | Ninguno: documento y transcripciones se envían completos |
| Límites del servicio de IA para PDF | OpenAI limita páginas y tamaño por documento (cifras en su documentación); si se superan, se usa solo el texto extraído |
| Límites del servidor | Los límites de subida de PHP y del servidor web deben ser iguales o mayores que el tamaño de vídeo configurado; el plugin no los modifica |

## Tiempos
| Concepto | Valor |
|---|---|
| Cuenta atrás antes de grabar | 5 segundos |
| Avisos durante la grabación | A falta de 2 minutos y de 1 minuto |
| Consulta del estado mientras se espera un análisis | Cada 4 segundos; a los 3 minutos aparece el aviso de que tarda más de lo habitual |
| Margen para la última respuesta tras acabar el tribunal | 2 minutos |
| Cierre automático de un tribunal abandonado | 15 minutos después del final, por una tarea que corre cada 10 minutos |
| Espera del audio de un examinador | Reintento a los 8 segundos; si se atasca 10 segundos, se muestra el texto |
| Preparación previa del tribunal | La primera intervención se guarda preparada hasta 2 horas |
| Espera entre regeneraciones del mismo intento por el mismo docente | 60 segundos por opción; 120 segundos para «Re-analizar todo» |
| Duración indicada de una regeneración | 1 a 3 minutos |
| Borrado nocturno de grabaciones | 02:30 |

## Llamadas a la IA
| Concepto | Valor |
|---|---|
| Reintentos ante saturación o error del servicio | Hasta 3 intentos con esperas crecientes; los errores de clave, saldo o petición no se reintentan |
| Respuesta cortada por longitud | Se repite una vez con el doble de espacio; si sigue cortada, error visible y no se guarda |
| Longitud de las intervenciones del tribunal | Tope corto y fijo (1 a 3 frases), independiente del ajuste de tokens |
| Llamadas por respuesta del alumno en el tribunal | Unas 3 (transcribir, generar la pregunta, ponerle voz) |
| Qué cuenta para el límite por minuto | Las llamadas hechas en nombre de ese alumno: tribunal, análisis del documento y evaluación |
| Modelo de transcripción y de voz | Fijos; no se eligen en los ajustes |
| Clave secundaria | Si existe, se usa para transcripción y voz |

## Reglas de borrado de grabaciones
Se borran vídeo, audios de la presentación, capturas y audios de las respuestas cuando se cumplen todas las condiciones:
- la actividad tiene un plazo mayor que 0;
- el intento tiene grabación;
- han pasado esos días desde que el alumno terminó el tribunal (o desde su última actividad, si no lo terminó);
- y, si lo terminó, la nota está publicada.
Consecuencia verificada: si la nota se publica cuando el plazo ya ha pasado, el borrado ocurre la noche siguiente a la publicación. Los textos de ayuda en pantalla dicen «días después de calificarse y publicarse»; el cálculo real cuenta desde el final del tribunal.
Tras el borrado ya no se puede re-analizar la presentación; sí recalcular la evaluación con la transcripción guardada.

## Reglas de excepciones
Una excepción por usuario o por grupo. La de usuario prevalece sobre las de grupo.
Con varios grupos: apertura más temprana, cierre más tardío y el número de intentos más alto. Atención: «Ilimitado» en un grupo no gana frente a un número en otro grupo (se toma el número); para garantizar intentos ilimitados use una excepción de usuario.

## Precios orientativos que muestra el plugin
Por millón de tokens de entrada / salida: GPT-6.1 Sol 2 $ / 10 $; GPT-6 Astra 10 $ / 50 $; GPT-6 Luna 0,10 $ / 0,50 $. Transcripción: unos 0,0045 $ por minuto. Las voces se facturan aparte.
Son los precios de lista que conocía la versión 1.3.0; los vigentes son los de OpenAI. El plugin no calcula ni muestra el gasto real.
