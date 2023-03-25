# caesar-example

시저 암호화, 복호화 프로젝트입니다.

## How to start

```shell
$ git clone https://github.com/ulgoon/caesar-example.git
$ cd caesar-example
$ python caesar.py
```

## Requirements

- 사용자로부터 문장을 입력받아 암호화, 복호화를 실시해야 한다.
- 0~25사이의 정수 값을 키로 활용하여야한다.
- 복호화 유무는 암호화를 기본값(decode=False)으로 사용하며, 사용자가 복호화를 원할경우 True를 세번째 전달인자로 사용되어야 한다.
- 각각 입력받은 문장, 키, 암호화유무를 활용하여 암호화(복호화)를 수행한 결과물을 문자열로 출력하여야 한다.
- (Optional) 텍스트 파일(.txt, .md) 파일에 대해 전체 암호화를 수행

## Features

- Encode(Sentence, key, decode=False)
  - 지정한 키(0~25)를 활용하여 Sentence의 암호화를 진행합니다.
- Decode(Sentence, key, decode=True)
  - 지정한 키(0~25)를 활용하여 Sentence의 복호화를 진행합니다.
