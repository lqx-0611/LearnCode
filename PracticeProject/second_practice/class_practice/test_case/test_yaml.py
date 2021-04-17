
import  pytest
import yaml

def test_yaml():
    with open("../data/calc.yml",encoding='UTF-8') as f:
        data = yaml.safe_load(f)
    print(data)
