# 누구의 소리

## 기본 설정 

### Play 생성

#### 이름
`누구의 소리`

### 기본 응답 

#### 사용자가 Play에 진입시 안내 응답

#### Play를 종료할 때의 응답	

#### 사용자가 Play에서 처리할 수 없는 발화를 한 경우	

## Task List

- **학교 식단 제공:** 어제/오늘/내일/모레
    - 언제? 어떤 학교? -> 검색
    - ~~알레르기 정보~~
- **학교 학사일정 제공:** 이번주/이번달/n달

- **명언 제공**

## API


### health
`/health` returns status code `200` with `OK`

### getSchool

```json
{
    "version": "2.0",
    "action": {
        "actionName": "getSchool",
        "parameters": {
            "scname": {
                "type": "SCHOOL_NAME",
                "value": "은여울중학교"
            }
        }
    },
}
```

| 이름         | 타입      | 설명        |
| :---------- | :------- | :--------- |
| `scname`     | `SCHOOL_NAME` | 검색할 학교 이름 및 키워드 |

```json
{
    "version": "2.0",
    "resultCode": "OK",
    "output": {
        "scmeal": "2018년 11월 23일의 점심은 귤, 기장밥, 근대된장국(중), 안동찜닭(중), 도라지진미채볶음(중), 깍두기입니다.",
        "scschedule": "오늘의 학사일정이 없습니다."
    }
}
```

### getMeal

```json
{
    "version": "2.0",
    "action": {
        "actionName": "getMeal",
        "parameters": {
            "query": {
                "type": "SCHOOL_NAME",
                "value": "은여울중학교"
            },
            "meal_type": {
                "type": "BID_TI_DURATION",
                "value": "점심"
            },
            "days": {
                "type": "BIT_DT_DAY",
                "value": "TODAY"
            }
        }
    },
}
```

| 이름         | 타입      | 설명        |
| :---------- | :------- | :--------- |
| `query`     | `SCHOOL_NAME` | 검색할 학교 이름 및 키워드 |
| `meal_type` | `BID_TI_DURATION`    | 급식 종류(아침, 점심, 저녁) |
| `days`      | `BID_DT_DAY`    | 조회할 상대적 날짜(그끄제, 그제, 어제, 오늘, 내일, 모레, 글피) |

```json
{
    "version": "2.0",
    "resultCode": "OK",
    "output": {
        "meal": "기장밥\n근대된장국(중)\n안동찜닭(중)\n도라지진미채볶음(중)\n메론(중)\n깍두기"
    }
}
```

### getSchedule

```json
{
    "version": "2.0",
    "action": {
        "actionName": "getSchedule",
        "parameters": {
            "name": {
                "type": "SCHOOL_NAME",
                "value": "은여울중학교"
            },
            "month": {
                "type": "BID_DT_YMONTH",
                "value": "11월"
            }
        }
    },
}
```

| 이름     | 타입             | 설명        |
| :------ | :-------------- | :--------- |
| `name`  | `SCHOOL_NAME`   | 검색할 학교 이름 및 키워드 |
| `month` | `BID_DT_YMONTH` | 학사일정을 조회할 달 |

### getKorQuote

```json
{
    "version": "2.0",
    "action": {
        "actionName": "getKorQuote",
        "parameters": {}
    },
}
```

```json
{
    "version": "2.0",
    "resultCode": "OK",
    "output": {
        "quote": "나는 내 인생의 나머지 부분을 위해 내 경력을 연기 할 수 있다면 좋겠다.",
        "author": "클로이 모렐츠"
    }
}
```

### getEngQuote

```json
{
    "version": "2.0",
    "action": {
        "actionName": "getEngQuote",
        "parameters": {}
    },
}
```

```json
{
    "version": "2.0",
    "resultCode": "OK",
    "output": {
        "en-quote": "The words that a father speaks to his children in the privacy of home are not heard by the world, but, as in whispering galleries, they are clearly heard at the end, and by posterity.",
        "en-author": "Jean Paul"
    }
}
```

## Functions

### hischool.meal

#### searchSchool
```py
searchSchool('은여울중학교')
```

| 이름        | 타입      | 설명        |
| :--------- | :------- | :--------- |
| `query`    | `string` | 검색할 학교 이름 및 키워드 |

```py
{'name': '은여울중학교', 'sccode': 'J100006779', 'address': '경기도 김포시 김포한강8로 173-48 (마산동)', 'type': '03', 'office': 'stu.goe.go.kr'}
```

| 타입      | 설명        |
| :------- | :--------- |
| `dict`   | 학교 정보가 반환됨 |

> **참고:** 새로운 데이터는 DB에 `query:school_info`로 저장되고, 함수는 파싱 전 먼저 DB를 서칭한다.

#### getMealTableURL
```py
result = searchSchool('은여울중학교')
getMealTableURL(result, 2, datetime.date.today())
```

| 이름           | 타입      | 설명        |
| :------------ | :------- | :--------- |
| `school_info` | `dict` | 검색할 학교 이름 및 키워드 |
| `meal_type`   | `int`  | 급식 종류(아침/조식: `1`, 점심/중식: `2`, 저녁/석식: `3`) |
| `query_date`  | `datetime.date` 또는 `yyyy.mm.dd` 형식의 `string` | 검색할 날짜 |

```text
http://stu.goe.go.kr/sts_sci_md01_001.do?schulCode=J100006779&schulCrseScCode=3&schulKndScCode=03&schMmealScCode=2&schYmd=2018.11.23
```

| 타입      | 설명        |
| :------- | :--------- |
| `string` | 식단을 파싱할 NEIS URL |

#### parseMeal
급식을 가져온다.

```py
parseMeal('은여울중학교', 2, 0) # 은여울중학교, 점심(2), 오늘로부터 0일 데이터
```

| 이름         | 타입      | 설명        |
| :---------- | :------- | :--------- |
| `query`     | `string` | 검색할 학교 이름 및 키워드 |
| `meal_type` | `int`    | 급식 종류(아침/조식: `1`, 점심/중식: `2`, 저녁/석식: `3`) |
| `days`      | `int`    | 오늘로부터 조회할 날짜까지의 날 수 |

```py
['기장밥', '근대된장국(중)', '안동찜닭(중)', '도라지진미채볶음(중)', '메론(중)', '깍두기']
```

| 타입    | 설명         |
| :----- | :---------- |
| `list` | 식단의 각 메뉴 |

## 코드 인용 및 참고
> 인용 및 참고한 위치에 주석으로 라이선스를 표기했습니다.

- https://github.com/junhoyeo/eunyeoul-chatbot-flask/
- https://github.com/w3bn00b/tanbang-cafeteria/
