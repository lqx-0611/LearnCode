
import os
import yaml

#获取calc_data的所有数据
def get_datas():
    parent_path = os.path.dirname(os.path.abspath(__file__))
    datas_path =parent_path +'/datas/calc_data'
    with open(datas_path,encoding='UTF-8') as f:
        datas = yaml.safe_load(f)
    return  datas

#获取某个key对应的value值

def get_value(self,a):
    value = self[a]
    return value


if __name__ == '__main__':
    a = get_datas()
    print(a)


