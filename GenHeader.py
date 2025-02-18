from Unicode import *

name = 'GB18030-2000'
fr = open(f'{name}.txt', mode='r', encoding='utf-8')

with open(f'{name}-h.txt', mode='w', encoding='utf-8') as fw:
    c = 0
    for line in fr.readlines():
        c += 1
        line_list = line.strip('\n').split('    ')
        # print(c, line_list)
        local_hex, ori, utf32, utf8, utf16 = line_list[0], line_list[1], line_list[2], line_list[3], line_list[4]
        s = '\t{' + local_hex + ', {' + utf8 + ', ' + utf8_to_utf16(utf8) + '}}, // ' + ori + '\n'
        fw.write(s)
        
print(f'{name} 的字符数量：{c}')
