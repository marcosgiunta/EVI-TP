para iniciar la API, mysql y adminer lo primero que se deberia hacer es en la terminal, apuntando en la direccion de la carpeta donde 
esta el proyecto de docker, escribir docker-compose up. ejemplo: C:\Users\marco\Desktop\tp_evi> docker-compose up


luego de eso deberia instalarse y levantar las aplicaciones que estan dentro del docker-compose.yml

una vez instalado las aplicaciones. si todo levanta correctamente se puede ingresar al adminer y a la API desde el navegador

ejemplo:

para el adminer:
http://localhost:8080/


para la API: 
http://localhost:5000/tareas


luego se pueden hacer diferentes pruebas de get,delete,post y put con la api desde postman,thunder client,etc. para verficiar el correcto
funcionamiento de la API.

a continuacion en el siguiente link se encuentra un documento donde se muestra la evidencia de que el docker-compose funciona
y que tanto adminer como la API responden correctamente. ademas en la documentacion se justifica las tecnologias elegidas y 
se fundamenta las elecciones tomadas.

LINK: 


ACLARACION: el archivo .env no es recomendable subirlo al github junto al proyecto de docker-compose por temas de seguridad,
ya que el .env contiene informacion sensible. pero para mostrar como esta configurado el .env, se lo comparto para entregar el TP completo


