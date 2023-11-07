from first_part.src import exercise_1
from first_part.src import exercise_2
from first_part.src import exercise_3
from first_part.src import exercise_4
import pytest



def test_exercise_one(capsys):
    exercise_1()
    captured = capsys.readouterr()
    captured_output = captured.out.strip().split('\n')

    assert captured_output[2] == "Three"
    assert captured_output[4] == "Five"
    assert captured_output[14] == "ThreeFive"
    assert captured_output[6] == "Three"
    assert captured_output[9] == "Five"
    assert captured_output[0] == "1"

def test_first_exercise(capsys):
    exercise_1()
    captured = capsys.readouterr()
    assert captured.out == test_output
    
    
    
def test_colorful_number():
    assert exercise_2(263) == True
    assert exercise_2(236) == False
    assert exercise_2(1234) == True
    assert exercise_2(987) == True
    assert exercise_2(24) == True

    assert exercise_2(0) == True  
    assert exercise_2(9) == True 

    assert exercise_2(11) == False
    assert exercise_2(999) == False
    
def test_exercise_3():
    assert exercise_3(['4', '3', '-2']) == 7
    assert exercise_3([453]) == 453

    assert exercise_3(['nothing', 3, '8', 2, '1']) == 14

    assert exercise_3(['abc', 'xyz', 'def']) == False

    assert exercise_3([]) == False
    
def test_exercise_4():
    assert exercise_4('abba', ['aabb', 'abcd', 'bbaa', 'dada']) == ['aabb', 'bbaa']
    assert exercise_4('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) == ['carer', 'racer']
    assert exercise_4('laser', ['lazing', 'lazy', 'lacer']) == []
    assert exercise_4('Tea', ['ate', 'eat', 'Tea']) == ['ate', 'eat']
    assert exercise_4('conversation', ['voices rant on', 'silent', 'convers ation']) == ['convers ation']