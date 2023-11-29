import re

def transcript(name: str) ->str:
    my_dict = {'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E',
                'Ж': 'ZH', 'З': 'Z','И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М':'M', 
                'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С':'S', 'Т': 'T', 'У':'U', 
                'Ф': 'F', 'Х': 'KH', 'Ц': 'TS', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SCH', 
                'Ы': 'Y','Ъ': 'IE','Ь':'', 'Э': 'E', 'Ю': 'IU', 'Я': 'IA', ' ': ' '}
    
    if all(i in my_dict for i in name):
        return ''.join([my_dict.get(c, c) for c in name.upper()])
    else:
        return 'invalid input'

