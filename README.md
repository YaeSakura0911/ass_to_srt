# ass_to_srt

* English
* [简体中文](https://github.com/Rayark-VOEZ/ass_to_srt/blob/main/README.chs.md)

## Introduction
Ass_to_srt is a tool which can convert Advanced SubStation Alpha (ASS) subtitle files to SubRip (SRT) subtitle files.

## Features
- Remove effects from ASS subtitle files
- Filter the given text in the ASS subtitle file
- Sorts the start time of out-of-order subtitle in ASS subtitle files in ascending order

## Usage
1. Go to [GitHub Release](https://github.com/Rayark-VOEZ/ass_to_srt/releases) to download the executable
2. Run the executable once and let the program automatically generate the `input`, `output` directory, and `config.json` file
3. Place the ASS subtitle file to be converted in the `input` directory
4. Add the text you want to filter in `config.json`
    ```json
    {
        "filter_text": ["text1", "text2", "text3"]
    }
    ```
5. Run the executable
6. Get the converted SRT subtitle file in the `output` directory