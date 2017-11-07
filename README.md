
# optimaltwodegrees

### Controladores de 2 Grados de Libertad mediante enfoque Optimo.

###### En el presente repositorio se encontraran archivos y funciones programadas en Matlab, para la síntesis y simulación de Controladores de Dos Grados de Libertad haciendo uso de la metodología propuesta en el siguiente trabajo de Grado.

[Consideraciones Optimas en el Diseño de Controladores de Dos Grados de Libertad mediante Enfoque Polinomico](https://www.researchgate.net)

## Documentación

Algunas de las funciones se describen a continuacion

##### two_degrees_system

```matlab
[A, B, C] = two_degrees_system(system)
```
Esta rutina retorna las matrices A, B, C del sistema equivalente en variables de estados de la topologia de dos grados de libertad.

Ejemplo

```matlab

num = 8556.2;
den = [1 32.15 828.13 6838.20 0];
tanks = tf(num,den);
order = length(den) - 1;

[A, B, C] = two_degrees_system('system')
A

   1.0e+03 *

         0    0.0010         0         0         0         0         0         0
         0         0    0.0010         0         0         0         0         0
         0         0         0    0.0010         0         0         0         0
         0   -6.8382   -0.8281   -0.0321    8.5562         0         0         0
         0         0         0         0         0    0.0010         0         0
         0         0         0         0         0         0    0.0010         0
         0         0         0         0         0         0         0    0.0010
         0         0         0         0         0         0         0         0


B

     0
     0
     0
     0
     0
     0
     0
     1


C

     1     0     0     0     0     0     0     0

```


##### auxiliar_system

```matlab
auxiliar_system(A, B, C, input)
```
Esta función retorna las matrices A, B del sistema auxiliar dada la metodología de dos grados de libertad.

Ejemplo

```matlab
[A_bar_step, B_bar_step] = auxiliar_system(A, B, C, 'step')

A_bar_step

   1.0e+03 *

         0    0.0010         0         0         0         0         0         0         0
         0         0    0.0010         0         0         0         0         0         0
         0         0         0    0.0010         0         0         0         0         0
         0         0         0         0    0.0010         0         0         0         0
         0         0   -6.8382   -0.8281   -0.0321    8.5562         0         0         0
         0         0         0         0         0         0    0.0010         0         0
         0         0         0         0         0         0         0    0.0010         0
         0         0         0         0         0         0         0         0    0.0010
         0         0         0         0         0         0         0         0         0


B_bar_step

     0
     0
     0
     0
     0
     0
     0
     0
     1

```


##### get_controllers


```matlab
[C_1, C_2] = get_controllers(K, order, input)
```

Esta función retorna los controladores de dos grados de libertad dado el vector de ganancias del sistema auxiliar, el orden del sistema y el tipo de entrada asociada al estudio.

Ejemplo:


```matlab
[K_step,S,E] = lqr(A_bar_step, B_bar_step,eye(length(A_bar_step)),1);
[C_1, C_2] = get_controllers(K_step, order, 'step')
C_1_step  

            1
  ----------------------
  s^3 + 135 s^2 + 9113 s

Continuous-time transfer function.


C_2_step

   31.97 s^2 + 1982 s + 1
  -------------------# optimaltwodegrees

### Controladores de 2 Grados de Libertad mediante enfoque Optimo.

###### En el presente repositorio se encontraran archivos y funciones programadas en Matlab, para la síntesis y simulación de Controladores de Dos Grados de Libertad haciendo uso de la metodología propuesta en el siguiente trabajo de Grado.

[Consideraciones Optimas en el Diseño de Controladores de Dos Grados de Libertad mediante Enfoque Polinomico](https://www.researchgate.net)

## DocumentaciÃ³n

Algunas de las funciones se describen a continuacion

##### two_degrees_system

```matlab
[A, B, C] = two_degrees_system(system)
```
Esta rutina retorna las matrices A, B, C del sistema equivalente en variables de estados de la topologia de dos grados de libertad.

Ejemplo

```matlab

num = 8556.2;
den = [1 32.15 828.13 6838.20 0];
tanks = tf(num,den);
order = length(den) - 1;

[A, B, C] = two_degrees_system('system')
A

   1.0e+03 *

         0    0.0010         0         0         0         0         0         0
         0         0    0.0010         0         0         0         0         0
         0         0         0    0.0010         0         0         0         0
         0   -6.8382   -0.8281   -0.0321    8.5562         0         0         0
         0         0         0         0         0    0.0010         0         0
         0         0         0         0         0         0    0.0010         0
         0         0         0         0         0         0         0    0.0010
         0         0         0         0         0         0         0         0


B

     0
     0
     0
     0
     0
     0
     0
     1


C

     1     0     0     0     0     0     0     0

```


##### auxiliar_system

```matlab
auxiliar_system(A, B, C, input)
```
Esta función retorna las matrices A, B del sistema auxiliar dada la metodología de dos grados de libertad.

Ejemplo

```matlab
[A_bar_step, B_bar_step] = auxiliar_system(A, B, C, 'step')

A_bar_step

   1.0e+03 *

         0    0.0010         0         0         0         0         0         0         0
         0         0    0.0010         0         0         0         0         0         0
         0         0         0    0.0010         0         0         0         0         0
         0         0         0         0    0.0010         0         0         0         0
         0         0   -6.8382   -0.8281   -0.0321    8.5562         0         0         0
         0         0         0         0         0         0    0.0010         0         0
         0         0         0         0         0         0         0    0.0010         0
         0         0         0         0         0         0         0         0    0.0010
         0         0         0         0         0         0         0         0         0


B_bar_step

     0
     0
     0
     0
     0
     0
     0
     0
     1

```


##### get_controllers


```matlab
[C_1, C_2] = get_controllers(K, order, input)
```

Esta función retorna los controladores de dos grados de libertad dado el vector de ganancias del sistema auxiliar, el orden del sistema y el tipo de entrada asociada al estudio.

Ejemplo:


```matlab
[K_step,S,E] = lqr(A_bar_step, B_bar_step,eye(length(A_bar_step)),1);
[C_1, C_2] = get_controllers(K_step, order, 'step')
C_1_step  

            1
  ----------------------
  s^3 + 135 s^2 + 9113 s

Continuous-time transfer function.


C_2_step

   31.97 s^2 + 1982 s + 1
  ------------------------
  s^4 + 135 s^3 + 9113 s^2

Continuous-time transfer function.
```

##### synthesys_step


```matlab
[C1, C2] = synthesys_step(A,B,C)
```

Esta función retorna los controladores de dos grados de libertad dado las matrices de estado, control y salida del modelo equivalente en espacio de estados de la topologia de 2 Grados de Libertad dada una referencia tipo constante.

Ejemplo:


```matlab
[C1,C2] = synthesys_step(A,B,C)

C1 =

              1
  -------------------------
  s^3 + 2.322 s^2 + 2.196 s

Continuous-time transfer function.


C2 =

  0.006278 s^2 + 0.653 s + 1
  --------------------------
  s^3 + 2.322 s^2 + 2.196 s

Continuous-time transfer function.
```

##### synthesys_ramp


```matlab
[C1, C2] = synthesys_ramp(A,B,C)
```

Esta función retorna los controladores de dos grados de libertad dado las matrices de estado, control y salida del modelo equivalente en espacio de estados de la topologia de 2 Grados de Libertad dada una referencia tipo rampa.

Ejemplo:


```matlab
[C1,C2] = synthesys_ramp(A,B,C)

C1 =

         4.021 s + 1
  --------------------------
  s^4 + 2.912 s^3 + 3.74 s^2

Continuous-time transfer function.


C2 =

  0.0224 s^3 + 2.346 s^2 + 4.021 s + 1
  ------------------------------------
       s^4 + 2.912 s^3 + 3.74 s^2

Continuous-time transfer function.
```

En la carpeta ```/plants``` se encontrara algunos scripts utilizados en la realización del trabajo investigativo, asociados particularmente a los sistemas que permitieron validar la metodología propuesta. Asi mismo, en la carpeta ```/simulations``` se encontraran las simulaciones realizadas haciendo uso de Simulink.-----
  s^4 + 135 s^3 + 9113 s^2

Continuous-time transfer function.
```

##### synthesys_step


```matlab
[C1, C2] = synthesys_step(A,B,C)
```

Esta función retorna los controladores de dos grados de libertad dado las matrices de estado, control y salida del modelo equivalente en espacio de estados de la topologia de 2 Grados de Libertad dada una referencia tipo constante.

Ejemplo:


```matlab
[C1,C2] = synthesys_step(A,B,C)

C1 =

              1
  -------------------------
  s^3 + 2.322 s^2 + 2.196 s

Continuous-time transfer function.


C2 =

  0.006278 s^2 + 0.653 s + 1
  --------------------------
  s^3 + 2.322 s^2 + 2.196 s

Continuous-time transfer function.
```

##### synthesys_ramp


```matlab
[C1, C2] = synthesys_ramp(A,B,C)
```

Esta función retorna los controladores de dos grados de libertad dado las matrices de estado, control y salida del modelo equivalente en espacio de estados de la topologia de 2 Grados de Libertad dada una referencia tipo rampa.

Ejemplo:


```matlab
[C1,C2] = synthesys_ramp(A,B,C)

C1 =

         4.021 s + 1
  --------------------------
  s^4 + 2.912 s^3 + 3.74 s^2

Continuous-time transfer function.


C2 =

  0.0224 s^3 + 2.346 s^2 + 4.021 s + 1
  ------------------------------------
       s^4 + 2.912 s^3 + 3.74 s^2

Continuous-time transfer function.
```

En la carpeta ```/plants``` se encontrara algunos scripts utilizados en la realización del trabajo investigativo, asociados particularmente a los sistemas que permitieron validar la metodología propuesta. Asi mismo, en la carpeta ```/simulations``` se encontraran las simulaciones realizadas haciendo uso de Simulink.


### Optimal Approach for 2 Degree of Freedom Controllers

###### In this repository will be found files and functions programmed in Matlab, for the synthesis and simulation of Drivers of Two Degrees of Freedom making use of the methodology proposed in the following work of Degree.

[Optimum Considerations in the Design of Drivers of Two Degrees of Freedom through a Polynomial Approach](https://www.researchgate.net)

## Documentation

Some of the functions are described as follow

##### two_degrees_system

```matlab
[A, B, C] = two_degrees_system(system)
```
This routine returns the matrices A, B, C of the equivalent system in state variables of the topology of two degrees of freedom.

Example

```matlab

num = 8556.2;
den = [1 32.15 828.13 6838.20 0];
tanks = tf(num,den);
order = length(den) - 1;

[A, B, C] = two_degrees_system('system')
A

   1.0e+03 *

         0    0.0010         0         0         0         0         0         0
         0         0    0.0010         0         0         0         0         0
         0         0         0    0.0010         0         0         0         0
         0   -6.8382   -0.8281   -0.0321    8.5562         0         0         0
         0         0         0         0         0    0.0010         0         0
         0         0         0         0         0         0    0.0010         0
         0         0         0         0         0         0         0    0.0010
         0         0         0         0         0         0         0         0


B

     0
     0
     0
     0
     0
     0
     0
     1


C

     1     0     0     0     0     0     0     0

```


##### auxiliar_system

```matlab
auxiliar_system(A, B, C, input)
```

This function returns the matrices A, B of the auxiliary system given the methodology of two degrees of freedom

Example

```matlab
[A_bar_step, B_bar_step] = auxiliar_system(A, B, C, 'step')

A_bar_step

   1.0e+03 *

         0    0.0010         0         0         0         0         0         0         0
         0         0    0.0010         0         0         0         0         0         0
         0         0         0    0.0010         0         0         0         0         0
         0         0         0         0    0.0010         0         0         0         0
         0         0   -6.8382   -0.8281   -0.0321    8.5562         0         0         0
         0         0         0         0         0         0    0.0010         0         0
         0         0         0         0         0         0         0    0.0010         0
         0         0         0         0         0         0         0         0    0.0010
         0         0         0         0         0         0         0         0         0


B_bar_step

     0
     0
     0
     0
     0
     0
     0
     0
     1

```


##### get_controllers


```matlab
[C_1, C_2] = get_controllers(K, order, input)
```

This function returns the two degrees of freedom controllers given the auxiliary system gain vector, the system order and the type of input associated with the study.

Example:


```matlab
[K_step,S,E] = lqr(A_bar_step, B_bar_step,eye(length(A_bar_step)),1);
[C_1, C_2] = get_controllers(K_step, order, 'step')
C_1_step  

            1
  ----------------------
  s^3 + 135 s^2 + 9113 s

Continuous-time transfer function.


C_2_step

   31.97 s^2 + 1982 s + 1
  ------------------------
  s^4 + 135 s^3 + 9113 s^2

Continuous-time transfer function.
```

##### synthesys_step


```matlab
[C1, C2] = synthesys_step(A,B,C)
```

This function returns the two degrees of freedom controllers given the system matrix, the actuators matrix and the output matrix using the analog model in space state from the two degrees of freedom topology. Give a constant reference.

Example:


```matlab
[C1,C2] = synthesys_step(A,B,C)

C1 =

              1
  -------------------------
  s^3 + 2.322 s^2 + 2.196 s

Continuous-time transfer function.


C2 =

  0.006278 s^2 + 0.653 s + 1
  --------------------------
  s^3 + 2.322 s^2 + 2.196 s

Continuous-time transfer function.
```

##### synthesys_ramp


```matlab
[C1, C2] = synthesys_ramp(A,B,C)
```

This function returns the two degrees of freedom controllers given the system matrix, the actuators matrix and the output matrix using the analog model in space state from the two degrees of freedom topology. Give a ramp reference.

Example:


```matlab
[C1,C2] = synthesys_ramp(A,B,C)

C1 =

         4.021 s + 1
  --------------------------
  s^4 + 2.912 s^3 + 3.74 s^2

Continuous-time transfer function.


C2 =

  0.0224 s^3 + 2.346 s^2 + 4.021 s + 1
  ------------------------------------
       s^4 + 2.912 s^3 + 3.74 s^2

Continuous-time transfer function.
```

In the folder ```/plants``` will find some scripts used in the investigation, particularly associated to the systems that allowed to validate the proposed methodology. Likewise, in the folder ```/simulations``` will find the simulations made using Simulink.
