import os

import yaml


def get_datas():
    parent_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = parent_path + '/data/calc.yml'
    print(f'文件地址：{data_path}')
    with open(data_path,encoding='UTF-8') as f:
          data = yaml.safe_load(f)
    return data


if __name__ == '__main__':
    print(get_datas())