# Api X-MEN 

_Este proyecto es un ejercicio para que magneto pueda reclutar mas mutantes pedida por mercado libre_

## Comentarios Adicionales 

_Sobre el punto de fluctuaciones agresivas  lo probe con jmeter y la verdad se la banca bastante bien._

_Lo subi a un servidor mio en linode (flask, mysql)_ para no tener que pagar en aws  o crear una cuenta de más.

Contemplando la realidad de las fluctuaciones agresivas  mi opinion seria, montar la base en un rds, hacer todo el desarrollo en docker para la escalabilidad, reservando slots de amazon, con anticipacion (suponiendo que sabemos el momento de la demanda con anticipacion como un black friday por ejemplo.) , para tener el menor costo posible. 

_Todo el detalle de el ejercicio esta en el pdf adjunto al proyecto_



## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

Mira **Deployment** para conocer como desplegar el proyecto.


### Pre-requisitos 📋

_Que cosas necesitas para instalar el software y como instalarlas_

```
Necesitas Python Mysql 
```

### Instalación 🔧

_Una serie de ejemplos paso a paso que te dice lo que debes ejecutar para tener un entorno de desarrollo ejecutandose_


```
 importar squema.sql
 pip install -r requirements.txt
```

_Y ejecutá_

```
python3 app.py
```
_Para un virtual enviroment_

```
source /mutant/bin/ACTIVATE
python3 app.py
```

## Ejecutando las pruebas ⚙️

_Para ejecutar los test nos paramos en la carpeta test dentro del proyecto_

```
pytest <nombre del test>
```
### EndPoints🔩

_Tenemos dos endpoints_

```
/mutant/ method="post" 
```
_se le envia este json_

```
{
“dna”:["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]
}
```

_Y este endpoint que devuelve las estadisticas_

```
/stats/ method="post" 
```

### Y las pruebas de estilo de codificación ⌨️

_La aplicacion se encuentra publicada en :_

```
http://kamecameja.com
```



## Autores ✒️

* **Maprigo** - *Trabajo Inicial* - [maprigo](https://github.com/maprigo)



---
⌨️ con ❤️ por [maprigo](https://github.com/maprigo) 😊
