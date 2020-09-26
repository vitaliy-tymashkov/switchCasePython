#Switch-case statement in Python


Python doesn't have a switch/case statement because of Unsatisfactory Proposals . Nobody has been able to suggest an implementation that works well with Python's syntax and established coding style. There have been many proposals, some of which you can see in PEP 3103 -- A Switch/Case Statement .

Most programming languages have switch/case because they don't have proper mapping constructs. You cannot map a value to a function, that's why they have it. But in Python, you can easily have a mapping table(dict) where a certain value maps to a certain function. Python functions are first class values, you can use the functions as the values of the dictionary get(key[, default]) method. Performance-wise, the Python dictionary lookup will almost certainly be more efficient than any solution you can rig yourself.

[Link to net-informations.com]
(http://net-informations.com/python/iq/switch.htm)



#Почему в Python нет оператора switch или case?
[Link to programmera.ru] 
(https://programmera.ru/uroki-po-python/pochemu-v-python-net-operatora-switch-ili-case/#:~:text=%D0%A3%20Python%20%D0%BD%D0%B5%D1%82%20%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%82%D0%BE%D1%80%D0%B0%20switch%20%2F%20case%20%D0%B8%D0%B7%2D%D0%B7%D0%B0%20%D0%BD%D0%B5%D1%83%D0%B4%D0%BE%D0%B2%D0%BB%D0%B5%D1%82%D0%B2%D0%BE%D1%80%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D1%85%20%D0%BF%D1%80%D0%B5%D0%B4%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B9.&text=%D0%A4%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%B8%20Python%20%2D%20%D1%8D%D1%82%D0%BE%20%D0%B7%D0%BD%D0%B0%D1%87%D0%B5%D0%BD%D0%B8%D1%8F%20%D0%BF%D0%B5%D1%80%D0%B2%D0%BE%D0%B3%D0%BE,(key%20%5B%2C%20default%5D)).