Integrantes: 

Juan Serrano / Juan Barrera

En el siguiente documento se encuentran los 3 puntos del parcial de lenguajes de programacion


Para ejecutar el punto 1:
Vaya a la ubicacion donde descargo todos los archivos y escriba python calculator.py y podra hacer las operaciones basicas incluyendo operaciones con imaginarios
Tenga en cuenta que las operaciones se hacen gracias a un archivo txt que se coloca en el codigo, en el caso de querer realizar otras operaciones cambie el archivo con nombre **input.txt**


Para Ejecutar el punto 2:

* PARTE 1:
  
  1)Ejecuta el siguiente comando para generar los archivos léxicos y sintácticos para Python:
  
  java -jar /home/juanbarrera/Documentos/Lenguajes/Corte02/Parcial02/antlr-4.13.1-complete.jar -Dlanguage=Python3 -no-listener -visitor IterableFunc.g4
  
  2) Ejecutar .py
  
  python3 iterablefunc.py

*PARTE 2:

  1)Ejecuta el siguiente comando para generar los archivos léxicos y sintácticos para Python:
  
  java -jar /home/juanbarrera/Documentos/Lenguajes/Corte02/Parcial02/antlr-4.13.1-complete.jar -Dlanguage=Python3 -no-listener -visitor filterFunc.g4
  
  
  2) Ejecutar .py
  
  python3 filterfunc.py
  


*Soluciones:
  1) Acualizacion antlr4

pip3 install --upgrade antlr4-python3-runtime
