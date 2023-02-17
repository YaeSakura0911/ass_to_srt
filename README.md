# ass_to_srt

* English
* [简体中文]()

## Introduction
Ass_to_srt is a tool which can convert Advanced SubStation Alpha (ASS) subtitle files to SubRip (SRT) subtitle files.

## Features
- Remove effects from ASS subtitle files
- Filter the given text in the ASS subtitle file
- Sorts the start time of out-of-order subtitle in ASS subtitle files in ascending order

## Usage
Place the ASS subtitle file to be converted in the `input` directory

Add the text you want to filter in `config.json`
```json
{
    "filter_text": ["text1", "text2", "text3"]
}
```
Run `main.py`

Get the converted SRT subtitle file in the `output` directory

## Download
