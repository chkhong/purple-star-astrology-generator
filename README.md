# Purple Star Astrology Docs

This project outputs purple star astrology given birth date and time

---

_TOC_

---

## Implementations

### Definition

**Star-Code Mapping**

|  Star  | Category  | Code |
| :----: | :-------: | :--: |
|  紫微  |   main    |  m1  |
|  天機  |   main    |  m2  |
|  太陽  |   main    |  m3  |
|  武曲  |   main    |  m4  |
|  天同  |   main    |  m5  |
|  廉貞  |   main    |  m6  |
|  天府  |   main    |  m7  |
|  太陰  |   main    |  m8  |
|  貪狼  |   main    |  m9  |
|  巨門  |   main    | m10  |
|  天相  |   main    | m11  |
|  天梁  |   main    | m12  |
|  七殺  |   main    | m13  |
|  破軍  |   main    | m14  |
|  文昌  |   good    |  g1  |
|  文曲  |   good    |  g2  |
|  左輔  |   good    |  g3  |
|  右弼  |   good    |  g4  |
|  天魁  |   good    |  g5  |
|  天鉞  |   good    |  g6  |
|  祿存  |   good    |  g7  |
|  天馬  |   good    |  g8  |
|  擎羊  |    bad    |  b1  |
|  陀羅  |    bad    |  b2  |
|  火星  |    bad    |  b3  |
|  鈴星  |    bad    |  b4  |
|  地劫  |    bad    |  b5  |
|  地空  |    bad    |  b6  |
|  化祿  |  effect   |  e1  |
|  化權  |  effect   |  e2  |
|  化科  |  effect   |  e3  |
|  化忌  |  effect   |  e4  |
|   廟   | intensity |  i1  |
|   旺   | intensity |  i2  |
|   得   | intensity |  i3  |
|   利   | intensity |  i4  |
|  平闲  | intensity |  i5  |
|   不   | intensity |  i6  |
|   陷   | intensity |  i7  |
|  命宮  |  palace   |  p1  |
| 兄弟宮 |  palace   |  p2  |
| 夫妻宮 |  palace   |  p3  |
| 子女宮 |  palace   |  p4  |
| 財帛宮 |  palace   |  p5  |
| 疾厄宮 |  palace   |  p6  |
| 遷移宮 |  palace   |  p7  |
| 奴僕宮 |  palace   |  p8  |
| 官祿宮 |  palace   |  p9  |
| 田宅宮 |  palace   | p10  |
| 福德宮 |  palace   | p11  |
| 父母宮 |  palace   | p12  |
|  身宮  |  palace   | p13  |
|   甲   |  tiangan  | tg1  |
|   乙   |  tiangan  | tg2  |
|   丙   |  tiangan  | tg3  |
|   丁   |  tiangan  | tg4  |
|   戊   |  tiangan  | tg5  |
|   己   |  tiangan  | tg6  |
|   庚   |  tiangan  | tg7  |
|   辛   |  tiangan  | tg8  |
|   壬   |  tiangan  | tg9  |
|   癸   |  tiangan  | tg10 |
|   子   |   dizhi   | dz1  |
|   丑   |   dizhi   | dz2  |
|   寅   |   dizhi   | dz3  |
|   卯   |   dizhi   | dz4  |
|   辰   |   dizhi   | dz5  |
|   巳   |   dizhi   | dz6  |
|   午   |   dizhi   | dz7  |
|   未   |   dizhi   | dz8  |
|   申   |   dizhi   | dz9  |
|   酉   |   dizhi   | dz10 |
|   戌   |   dizhi   | dz11 |
|   亥   |   dizhi   | dz12 |

---

## API

### Arrange Stars

Arrange purple stars 排盘

#### Request

**URL** : `/arrange`

**Method** : `GET`

**Header Parameters**

| Name        | Required | Description                        |
| ----------- | -------- | ---------------------------------- |
| birth_year  | yes      | year of birth in western calendar  |
| birth_month | yes      | month of birth in western calendar |
| birth_day   | yes      | day of birth in western calendar   |
| birth_hour  | yes      | hour of birth in western calendar  |

#### Response (Success)

**Code** : `200 OK`

**Content** :

```json
{
  "success": true,
  "message": "",
  "data": {
    "身宫": "夫妻宫",
    "五行局": "木三局",
    "1": {
      "地支": "子",
      "天干": "甲",
      "宫位": "兄弟宮",
      "主星": [
        ["ziwei", "miao", "ke"],
        ["tanlang", "miao", "ji"]
      ],
      "吉星": [
        ["wenqu", "xian"],
        ["zuofu", "ping"]
      ],
      "煞星": [
        ["qingyang", "xian"],
        ["dikong", "ping"]
      ],
      "杂曜": [
        ["tianxing", "xian"],
        ["tianxi", "ping"]
      ]
    }
  }
}
```

#### Response (Error)

**Code** : `400 BAD REQUEST`

**Content** :

```json
{
  "success": false,
  "message": "Error message",
  "data": []
}
```

---

# Reference

https://baike.baidu.hk/item/%E5%8D%81%E5%9B%9B%E4%B8%BB%E6%98%9F/991733
