# ass_to_srt

* [English](https://github.com/Rayark-VOEZ/ass_to_srt/tree/main)
* 简体中文

## 介绍
Ass_to_srt 是一个能把 Advanced SubStation Alpha (ASS) 字幕文件转换成 SubRip (SRT) 字幕文件的工具

## 功能
- 移除 ASS 字幕文件中的特效
- 过滤 ASS 字幕文件中给定的文本
- 对 ASS 字幕文件中乱序字幕开始时间进行升序排序

## 使用方法
1. 前往 [GitHub Release](https://github.com/Rayark-VOEZ/ass_to_srt/releases) 下载可执行文件 
2. 运行一次可执行文件，让程序自动生成 `input` 、 `output` 目录和 `config.json` 文件 
3. 将待转换的 ASS 字幕文件放在 `input` 目录下 
4. 在 `config.json` 中添加要过滤的文本
    ```json
    {
        "filter_text": ["text1", "text2", "text3"]
    }
    ```
5. 运行可执行文件 
6. 在 `output` 目录下得到转换后的 SRT 字幕文件