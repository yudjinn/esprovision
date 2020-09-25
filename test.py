from jinja2 import Environment, FileSystemLoader, Template
from pathlib import Path

template = Template(open('test.j2').read())
print(template.render(deviceID='testing'))

env = Environment(loader=FileSystemLoader(Path(p)))
# template = env.get_template('template.txt')
# print(template.render(config_data))
