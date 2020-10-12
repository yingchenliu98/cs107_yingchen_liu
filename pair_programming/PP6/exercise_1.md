Pair programming 6

coder: Ruizhe Kang
listener: Will Wang
sharer: Yingchen Liu

1. computational graph for the function
![image](comp_graph.png)

2. evaluation trace for this function

|Trace|Elementary operation |Numerical value| 
|--|--|--|
|$x_1$|$\pi/2$|1.57|
|$v_1$|$\sin(x_1)$|1.00|
|$y_1$|$\pi/3$|1.05|
|$u_1$|$\cos(y_1)$|0.50|
|$u_2$|$-u_1$|-0.50|
|$v_2$|$u_2+v_1$|0.50|
|$v_3$|$v_2^2$|0.25|
|$v_4$|$-v_3$|-0.25|
|$f$|$e^{v_4}$|0.78|
 

3. $f(\pi/2,\pi/3)=0.78$

4. We'll extend the table to calculate the derivatives

|Trace|Elementary operation | numerical value of the function  |derivative of the elementary function|numerical value of the derivative respect to x| numerical value of the derivative respect to y|
|--|--|--|--|--|--|
|$x_1$|$\pi/2$|1.57|1|1|0|
|$v_1$|$\sin(x_1)$|1.00|$cos(x_1)\dot{x_1}$|0.804|0|
|$y_1$|$\pi/3$|1.05|1|0|1|
|$u_1$|$\cos(y_1)$|0.50|$-sin(y_1)\dot{y_1}$|0|-0.804|
|$u_2$|$-u_1$|-0.50|$-\dot{u_1}$|0|0.804|
|$v_2$|$u_2+v_1$|0.50|$\dot{u_2}+\dot{v_1}$|0.804|0.804|
|$v_3$|$v_2^2$|0.25|$2v_2\dot{v_2}$|0.804|0.804|
|$v_4$|$-v_3$|-0.25|$-\dot{v_3}$|-0.804|-0.804|
|$f$|$e^(v_4)$|0.78|$e^(v_4)\dot{v_4}$|-0.627|-0.627|