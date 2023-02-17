import json
import os.path
import re


def get_start(item: list) -> str:
    return item[1]


def filter_se(sub: str) -> str:
    """
    过滤字幕中的特效
    :param sub: 待过滤的字幕
    :return: 过滤后的字幕
    """
    return re.sub(u'\\{.*?}', '', sub)


def check_text(sub: str, texts: set) -> bool:
    """
    检测字幕中是否含有所给文本
    :param sub: 待检测的字幕
    :param texts: 文本集合
    :return:
        True - 包含所给文本;
        False - 不包含所给文本
    """
    filter_flag = False  # 过滤标志位, 包含为True, 不包含为False
    for text in texts:
        if text in sub:
            filter_flag = True
            break
    return filter_flag


def load_ass_file() -> list:
    """
    获取input目录下所有ass文件
    :return: 返回一个包含所有文件路径的列表
        例: ['D:/ass_to_srt/input/subtitle1.ass', 'D:/ass_to_srt/input/subtitle2.ass']
    """
    ass_path_list = []
    for root, dirs, files in os.walk('./input'):
        for file in files:
            if file.endswith('.ass'):
                ass_path_list.append(f'{root}/{file}')
        break
    return ass_path_list


def subtitle_handler(filepath: str):
    """
    处理ass文件
    :param filepath: 文件路径
    :return:
    """
    # 读取ass文件
    ass_file = open(file=f'{filepath}', mode='r', encoding='utf-8')
    # 将ass文件拆成列表
    ass_list = ass_file.read().splitlines()
    dialogue_list = []
    # 遍历ass列表
    for ass in ass_list:
        if ass.find('Dialogue') == 0:
            # 过滤特效
            new_ass = filter_se(ass)
            # 过滤字符
            if not check_text(new_ass, FILTER_TEXT):
                dialogue_list.append(new_ass.split(','))
    # 对字幕开始时间进行升序排序
    dialogue_list.sort(key=get_start)
    # print(dialogue_list)
    write_srt_file(filepath, dialogue_list)


def write_srt_file(filepath: str, subs: list):
    filepath = filepath.replace('input', 'output').replace('ass', 'srt')
    srt_file = open(file=f'{filepath}', mode='w', encoding='utf-8')
    index = 1  # 字幕行号
    # 将字幕写入文件
    for sub in subs:
        start_time = sub[1]
        end_time = sub[2]
        subtitle = sub[9]
        # TODO: 检测并过滤空行字幕
        if not subtitle.isspace():
            print(index)
            print(f'{start_time} --> {end_time}')
            print(f'{subtitle}\n')
            srt_file.write(f'{index}\n')
            srt_file.write(f'{start_time} --> {end_time}\n')
            # 最后一行不用写入换行
            if index == len(subs):
                srt_file.write(f'{subtitle}')
            else:
                srt_file.write(f'{subtitle}\n\n')
            index += 1


if __name__ == '__main__':
    # 判断有无input目录
    if not os.path.isdir('./input'):
        os.makedirs('input')
    # 判断有无output目录
    if not os.path.isdir('./output'):
        os.makedirs('output')
    # 读取配置文件
    config = json.load(open(file='./config.json', mode='r', encoding='utf-8'))
    FILTER_TEXT = config['filter_text']  # 过滤字符集
    # 读取input目录下所有ass文件
    ass_list = load_ass_file()
    # 处理字幕
    for ass in ass_list:
        subtitle_handler(ass)
