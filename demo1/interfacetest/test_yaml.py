import yaml


class YamlUtil:
    def __init__(self, yaml_file):
        self.yaml_file = yaml_file

# 读取yaml文件  Loader:加载的方式
    def read_yaml(self):
        with open(self.yaml_file, encoding='utf-8') as f:
            value = yaml.load(f, Loader=yaml.FullLoader)
            # print(value, type(value))
            return value

if __name__ == '__main__':
    YamlUtil('test_yaml.yaml').read_yaml()

