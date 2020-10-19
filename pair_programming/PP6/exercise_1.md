# Pair programming 6

coder: Ruizhe Kang
listener: Will Wang
sharer: Yingchen Liu

1. computational graph for the function
![image](comp_graph.png)

2. evaluation trace for this function

|Trace|Elementary operation |Numerical value| 
|--|--|--|
|x<sub>1</sub>|pi/2|1.57|
|v<sub>1</sub>|sin(x<sub>1</sub>)|1.00|
|y<sub>1</sub>|pi/3|1.05|
|u<sub>1</sub>|cos(y<sub>1</sub>)|0.50|
|u<sub>2</sub>|-u<sub>1</sub>|-0.50|
|v<sub>2</sub>|u<sub>2</sub>+v<sub>1</sub>|0.50|
|v<sub>3</sub>|v<sub>2</sub><sup>2</sup>|0.25|
|v<sub>4</sub>|-v<sub>3</sub>|-0.25|
|f|exp(v<sub>4</sub>)|0.78|
 

3. f(pi/2,pi/3)=0.78

4. We'll extend the table to calculate the derivatives

|Trace|Elementary operation | numerical value of the function  |derivative of the elementary function|numerical value of the derivative respect to x| numerical value of the derivative respect to y|
|--|--|--|--|--|--|
|x<sub>1</sub>|pi/2|1.57|1|1|0|
|v<sub>1</sub>|sin(x<sub>1</sub>)|1.00|cos(x<sub>1</sub>) \dot{x<sub>1</sub>}|0.804|0|
|y<sub>1</sub>|pi/3|1.05|1|0|1|
|u<sub>1</sub>|cos(y<sub>1</sub>)|0.50|-sin(y<sub>1</sub>) \dot{y<sub>1</sub>}|0|-0.804|
|u<sub>2</sub>|-u<sub>1</sub>|-0.50|-\dot{u<sub>1</sub>}|0|0.804|
|v<sub>2</sub>|u<sub>2</sub>+v<sub>1</sub>|0.50|\dot{u<sub>2</sub>}+ \dot{v<sub>1</sub>}|0.804|0.804|
|v<sub>3</sub>|v<sub>2</sub><sup>2</sup>|0.25|2v<sub>2</sub> \dot{v<sub>2</sub>}|0.804|0.804|
|v<sub>4</sub>|-v<sub>3</sub>|-0.25|-\dot{v<sub>3</sub>}|-0.804|-0.804|
|f|exp(v<sub>4</sub>)|0.78|exp(v<sub>4</sub>) \dot{v_4}|-0.627|-0.627|
