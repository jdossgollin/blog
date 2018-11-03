---
layout: post
title: Nuevas Inundaciones en Paraguay
date: 2018-10-31
category: water-climate-risk
author: James
comments: true
mathjax: true
thumbnail: /img/posts/2018-10-31-paraguay-floods/rainfall-time-series.png
---

Según los periodistas de [Floodlist](http://floodlist.com/america/paraguay-asuncion-river-floods-october-2018){:target="_blank"}, más de 10000 personas en Asunción y otras partes de Paraguay han sido obligados a abandonar sus hogares debido a graves inundaciones del Río Paraguay.
Desde que yo, junto con tres coautores extraordinarios, acabo de publicar un artículo en Journal of Climate sobre los impulsores de lluvias fuertes y inundaciones en esta región {% cite DossGollin:2018bn %}, preparé una breve exploración de si los mismos mecanísmos físicos que identificamos provocaron el evento actual.

<!--more-->

> *El hombre, mis hijos —nos decía—, es como un río. Tiene barraca y orilla. Nace y desemboca en otros ríos. Alguna utilidad debe prestar. Mal río es el que muere en un estero...*  
Hijo de Hombre, Augusto Roa Bastos

He pasado momentos hermosos en Paraguay, un país cuya vida está estrechamente relacionada con sus ríos.
Históricamente proporcionaron comida, agua, y navegación; hoy proveen casi toda la electricidad del país gracias a proyectos hidroeléctricos (a veces controvertidos) en Yguazu y Yacyreta.
Sin embargo, el hecho de que la mayoría de los paraguayos se encuentran a lo largo de los ríos Paraguay y Paraná  significa que los paraguaos están altamente expuestos a las inundaciones.

Before we dive into analyzing what has caused the most recent floods, a few notes:

- If you are looking for a **version in English** of this post, please click [here!]({{ site.baseurl }}{% post_url 2018-10-31-paraguay-floods %})
- Hago referencia a nuestro trabajo varias veces y también cito otros trabajos académicos. **Si está interesado pero no puede acceder a un documento, contácteme y con gusto compartiré un pdf con usted**! Liberemos al conocimiento!
- Mi castellano anda muy mal debido a que durante los últimos años escribo casí solo inglés! Disculpas por los errores de ortografía. Si alguna cosa no haya conseguido explicar, por favor de dejarme saber.

## Cuenca del Río Paraguay

Vale la pena refrescarnos de la geografía de la región.
La figura 1(b) de nuestro artículo muestra la cuenca del río Paraguay.
Para analizar, sirve dividir entre la parte superior (en el Chaco) y la parte inferior (donde viven la mayoría de los Paraguayos).
Las letras ASU indican Asunción, capital paraguaya.

Una característica relevante de esta región es que es extremadamente plana.
Esto se muestra mediante los contornos de elevación en el mapa.
Como consecuencia, las precipitaciones que caen aquí tienden a tardar mucho tiempo en drenarse.
Esto implica que precipitaciones durante un período prolongado pueden causar inundaciones, incluso si ninguna de las tormentas individuales es particularmente intensa.
<p align="center">
  <img src="/img/posts/2018-10-31-paraguay-floods/study_area.jpg" alt="Map of study area" align="center" height="350">
</p>

## Lluvias Observadas

Ahora estamos listos para explorar las lluvias que provocaron este evento.

Empecemos examinando la lluvia observada en los últimos meses.
Esta figura muestra la precipitación sobre la región definida por el cuadro rojo del mapa de arriba.
Podemos ver que entre el 14 de septiembre y el 30 de octubre de 2018, la región observó una série persistente de lluvias.
Por contexto, la precipitación promedio en esta región es de poco menos de 4 mm por día.
<p align="center">
  <img src="/img/posts/2018-10-31-paraguay-floods/rainfall-time-series.png" alt="Observed rainfall time series" align="center" height="350">
</p>

Ahora examinemos como se ven las lluvias en el mapa.
Dado que las lluvias más fuertes ocurrieron entre el 14 de septiembre y el presente, he sumado las lluvias durante ese período.
Esta imagen muestra **anomalías** de lluvia, que significa la diferencia entre lo que se observó y el promedio esperado dado el ciclo estacional.[^anomalies]
Podemos ver que la región que alimenta la región fue particularmente afectada por lluvias fuertes.[^data-quality]
<p align="center">
  <img src="/img/posts/2018-10-31-paraguay-floods/rainfall.png" alt="Observed rainfall map" align="center" height="350">
</p>

## Mecanismos Directos

Vale la pena pensar un poco sobre este patrón de lluvia.
En nuestro artículo {% cite DossGollin:2018bn %}, encontramos  que las precipitaciones intensas en Paraguay suelen ser provocadas por el Corriente de Vientos de Bajo Nivel de Sudamérica, o en inglés "South American Low-Level Jet", que trae la humedad y la energía (ambas son necesarias para la lluvia) desde la Amazonia hasta el sureste de Sudamérica.
Este <<corriente>> de humedad e energía puede a veces pasa los 25 grados Sur, en cuyo caso favorecerá la occurencia de lluvias en el norte de Argentina y Uruguay (el llamado "corriente tipo Chaco" {% cite Salio:2002ev %}), o puede girar hacia el Este, en cuyo caso favorecerá la lluvia sobre Paraguay y SW Brasil (llamado"corriento tipo No-Chaco {% cite Vera:2006ib %}).
Si nos fijamos en la figura 6 de nuestro estudio, disponible [en mi página de GitHub](https://github.com/jdossgollin/2018-paraguay-floods/raw/master/figs/wt_composite.pdf){:target="_blank"}, se puede ver que la lluvia observada durante las últimas seis semanas se parece mucho al tipo de tiempo (lo llamamos el número 4) que identificamos como un factor clave de las inundaciónes de 2015-16.

Para tener una mejor idea de cómo se comportó el Corriente de Vientos de Bajo nivel de Sudamérica durante este período, podemos observar las anomalías climáticas que persistieron durante este período.
La variable más interpretable para investigar es el viento.
Esta gráfica muestra el viento a 850 hPa, que es la parte inferior de la atmósfera donde se transporta la mayor parte de la humedad y la energía en el corriente de bajo nivel, por lo que estos datos nos dicen mucho sobre el transporte de humedad a gran escala por la atmósfera.
<p align="center">
  <img src="/img/posts/2018-10-31-paraguay-floods/vector-wind.png" alt="Mapa de vientos" align="center" height="350">
</p>

La característica más obvia aquí es que la región alrededor (60W, 17.5S) muestra fuertes anomalías de viento, lo que significa que el corriente de bajo nivel fue mucho más fuerte durante este período.
Esto tiene sentido lo que vimos en el gráfico de series de tiempo de lluvia: es razonable suponer que durante la mayoría o todos los picos de la serie de tiempo de lluvia, el corriente de bajo nivel estuvo activo ese día y / o el día anterior.

También es interesante observar algunas otras características en esta trama.
Primero, si miramos un poco hacia el sureste de Paraguay, digamos en torno a (52.5W, 27.5S), vemos que la anomalía del viento, aunque de semana, apunta hacia Paraguay.
Esto significa que (en promedio) la circulación no permitió que el corriente de bajo nivel empujara a Uruguay (este sería el evento del chaco "Chaco" definido anteriormente).
Además, el aire que se mueve en esta dirección hacia la cuenca del río Paraguay inferior apoya la convergencia.
En pocas palabras, cuando dos paquetes de aire cerca del fondo de la atmósfera chocan entre sí, tenderán a subir (ya que el suelo está debajo de ellos, no pueden bajar) y el movimiento ascendente favorece la lluvia.
También parece que hay algunas cosas interesantes que suceden en las latitudes medias; Parece que hay un fuerte bajo persistente centrado alrededor (82.5W, 42.5S) que podría ser relevante aquí.

## Mecanismos Indirectos

Ya hemosvisto un análisis no exhaustivo (es un blog en mi tiempo libre0!).

Aún así, ya vimos que las tormentas de lluvia que provocaron las inundaciones actuales consistente con las observaciones[^reanalysis] del corriente de bajo nivel.
En nuestro artíuclo en Journal of Climate, encontramos algunos enlaces interesantes entre algunos índices climáticos regionales y las precipitaciones en esta región.

Aquí exploraremos un posible mecanismo, que es el océano.
Dado que el calor específico (cantidad de energía requerida para elevar la temperatura) del agua es mucho más grande que el calor específico del aire, las anomalías del calentamiento en el océano pueden provocar una circulación atmosférica persistente en estas escalas de tiempo relativamente cortas.[^ocean-atmosphere]

<p align="center">
  <img src="/img/posts/2018-10-31-paraguay-floods/sea-surf-temp.png" alt="Temperatura de la superficie del mar" align="center" height="350">
</p>

Hay mucho que se podría desempacar aquí, pero me centraré en una observación particular.
En nuestro artículo, planteamos la hipótesis de que un <<dipolo>> en el Atlántico centro-sur, lo definimos como que va de 30W a 10W y de 15S a 40S, puede favorecer los eventos tipo "No-Chaco" sobre los eventos tipo "Chaco" y por lo tanto aumentar el probabilidad de fuertes lluvias en Paraguay.

<p align="center">
  <img src="/ img/posts/2018-10-31-paraguay-floods/ChacoNoChacojet.png" alt="Temperatura de la superficie del mar" align="center" height="350">
</p>

Aunque la hípotese especifíca fue que esto podría suceder durante los años de El Niño en el verano (diciembre-febrero), un dipolo como el que identificamos estuvo activo durante las últimas semanas.
El dipolo durante las inundaciones actuales parece desplazarse un poco hacia el sur y el este de la region que identificamos (aproximadamente cinco grados).
No obstante, **puede** haber contribuido a la lluvia que observamos.

## Terminando

¡Gracias por leer hasta aquí!
Unos cuantos puntos más en caso de que os interese.

### Más investigación

¡No sería justo para mí escribir una publicación completa sin dejar espacio para futuras lecturas y futuros trabajos!

- Para obtener más información sobre la relación entre el Jet de bajo nivel de América del Sur y la lluvia, consulte la literatura académica {% cite Marengo:2004kr Boers:2013jh Salio:2007gd %} o [esta página excelente](http://www.eumetrain.org/satmanu/CMs/Sallj/index.htm){:target="blank}.
- He hablado sobre el corriente de vientos bajo nivel, pero es parte de un sistema complejo que se ha examinado a través de una variedad de otras perspectivas. Algunas personas han considerado esta región como parte de un sistema <<Monsoon>> {% cite Marengo:2012cm %}. Otros han escrito sobre la <<Zona de convergencia del Océano Atlántico del Sur>> {% cite Nielsen:2018ep Carvalho:2004ix Carvalho2002 %}. Todas las perspectivas parecen útiles y aún estamos aprendiendo mucho.
- La relación identificada entre el dipolo en el Atlántico y el corriente de bajo nivel sigue siendo una hipótesis. Aún no tenemos datos suficientes para determinar absolutamente qué tan fuerte es la conección.

### Gracias y renuncias

- Esta es una publicación de blog, no un artículo académico, por lo que es probable que haya cometido algunos errores en el análisis. Si encuentra alguno, por favor [contácteme](mailto:james.doss-gollin@columbia.edu)!
- ¡Gracias a [NOAA ESRL](https://www.esrl.noaa.gov/psd/data/composites/day/){:target="_blank"} por proveer los datos y mapas
- Esta es una publicación viva y tengo la intención de actualizarla en las próximas semanas, ya que recibo comentarios de algunos colegas. Podrá encontrar todas las versiones de esta publicación [en mi GitHub](https://github.com/jdossgollin/jdossgollin.github.io).

### Bibliografía

_Para una copia de cualquier artículo en formato PDF, por favor contácteme_.

{% bibliography --cited %}

### Notas al pie

Algunas advertencias adicionales y comentarios para el lector concienzudo:

[^anomalies]: por supuesto, si está interesado la calculación del ciclo estacional para que podamos eliminarlo para identificar anomalías, querrá entrar en los detalles de cómo se hace. Creo que la herramienta web que estoy utilizando estima el ciclo estacional (también conocido como "Climatología") toma promedios mensuales (es decir, promedio de todos los septembres, promedio de todos los octobers, etc.). Es una metodología bastante aproximado, pero tiende a dar resultados similares a los métodos más sofisticados.
[^data-quality]: este no es el mejor conjunto de datos de lluvia. Ya que estamos promediando durante un tiempo relativamente largo, deberíamos estar más o menos cubiertos. Para estar seguro, observé algunos otros conjuntos de datos de lluvia y descubrí que parecía razonable.
[^reanalysis]: los datos que estoy utilizando provienen de un llamado re-análisis, lo que significa que no es una observación directa.
[^ocean-atmosphere]: sugerir que el océano solo impulsa la atmósfera es una simplificación excesiva: la atmósfera también impulsa el océano ya que son sistemas acoplados.
