# ass_to_srt

* [English]()
* 简体中文

## 介绍
Ass_to_srt 是一个能把 Advanced SubStation Alpha (ASS) 字幕文件转换成 SubRip (SRT) 字幕文件的工具

## 功能
- 移除 ASS 字幕文件中的特效
- 过滤 ASS 字幕文件中给定的文本
- 对 ASS 字幕文件中乱序字幕开始时间进行升序排序

## 使用方法
将待转换的 ASS 字幕文件放在 `input` 目录下

在 `config.json` 中添加要过滤的文本
```json
{
    "filter_text": ["text1", "text2", "text3"]
}
```
运行 `main.py`

在 `output` 目录下得到转换后的 SRT 字幕文件

## 下载