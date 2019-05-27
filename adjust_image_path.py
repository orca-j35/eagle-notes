'''
最初使用「马克飞象」在EverNote使用markdown撰写笔记，
在添加图片时「马克飞象」会自动插入，并指定路径，比如:
![Alt text](./1458361937611.png)
目前我使用Typora来撰写笔记，并希望将图片放置到./${filename}.assets目录中，比如:
![Alt text](0x00_使用规则.assets/.1458361937611.png)

此脚本用于完成上述工作
'''
import re
import os
r = re.compile(r'(?P<prefix>!\[.+?\]\()(?P<target>\./)(?P<suffix>.+?\))')
print('退出 qq')
while True:
    file_path = input('欲调整格式的文件:')
    if file_path == 'qq':
        break
    relative_dir = f"{os.path.split(file_path)[-1].split('.')[0]}.assets/"
    with open(file_path, 'r', encoding='utf-8') as fin:
        text = fin.read()

    target = r.sub(rf'![Alt text]({relative_dir}.\g<suffix>', text)

    with open(file_path, 'w', encoding='utf-8') as fin:
        fin.write(target)
