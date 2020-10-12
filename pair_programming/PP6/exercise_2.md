Pair programming 6

coder: Ruizhe Kang
listener: Will Wang
sharer: Yingchen Liu

|Trace|Elementary operation | numerical value of the function  |derivative of the elementary function|numerical value of the derivative respect to x| numerical value of the derivative respect to y|
|--|--|--|--|--|--|
|$(x_1, y_1)$|(1, 1)|(1, 1)|(1, 1)|(1, 0)|(0, 1)|
|$(u_1, v_1)$|$(x_1^2, x_1)$|(1, 1)|$(2x_1\dot{x_1}, \dot{x_1})$|(2, 1)|(0, 0)|
|$(u_2, v_2)$|$(y_1^2, y_1)$|(1, 1)|$(2y_1\dot{y_1}, \dot{y_1})$|(0, 0)|(2, 1)|
|$(u_3, v_3)$|$(u_1+u_2, v_1+v_2)$|(2, 2)|$(\dot{u_1}+\dot{u_2},\dot{v_1}+\dot{v_2})$|(2,1)|(2,1)|
|$(u_4, v_4)$|$(u_3, e^{v_3})$|(2, 7.38)|$(\dot{u_3}, e^{v_3}\dot{v_3})$|(2, 7.38)|(2, 7.38)|

