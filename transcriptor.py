
transcription_dict = {'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E',
            'Ж': 'ZH', 'З': 'Z','И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М':'M', 
            'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С':'S', 'Т': 'T', 'У':'U', 
            'Ф': 'F', 'Х': 'KH', 'Ц': 'TS', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SCH', 
            'Ы': 'Y','Ъ': 'IE','Ь':'', 'Э': 'E', 'Ю': 'IU', 'Я': 'IA', ' ': ' '}

def transcript(name: str, my_dict = transcription_dict) ->str:
    
    if all(i in my_dict for i in name.upper()):
        return ''.join([my_dict.get(c, c) for c in name.upper()])
    else:
        return 'invalid input'

print(transcript('вася пупкин'))