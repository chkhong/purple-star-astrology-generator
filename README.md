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
|  紫微  |   main    |  m0  |
|  天機  |   main    |  m1  |
|  太陽  |   main    |  m2  |
|  武曲  |   main    |  m3  |
|  天同  |   main    |  m4  |
|  廉貞  |   main    |  m5  |
|  天府  |   main    |  m6  |
|  太陰  |   main    |  m7  |
|  貪狼  |   main    |  m8  |
|  巨門  |   main    |  m9  |
|  天相  |   main    | m10  |
|  天梁  |   main    | m11  |
|  七殺  |   main    | m12  |
|  破軍  |   main    | m13  |
|  文昌  |   good    |  g0  |
|  文曲  |   good    |  g1  |
|  左輔  |   good    |  g2  |
|  右弼  |   good    |  g3  |
|  天魁  |   good    |  g4  |
|  天鉞  |   good    |  g5  |
|  祿存  |   good    |  g6  |
|  天馬  |   good    |  g7  |
|  擎羊  |    bad    |  b0  |
|  陀羅  |    bad    |  b1  |
|  火星  |    bad    |  b2  |
|  鈴星  |    bad    |  b3  |
|  地空  |    bad    |  b4  |
|  地劫  |    bad    |  b5  |
|  化祿  |  effect   |  e0  |
|  化權  |  effect   |  e1  |
|  化科  |  effect   |  e2  |
|  化忌  |  effect   |  e3  |
|   廟   | intensity |  i0  |
|   旺   | intensity |  i1  |
|   得   | intensity |  i2  |
|   利   | intensity |  i3  |
|  平闲  | intensity |  i4  |
|   不   | intensity |  i5  |
|   陷   | intensity |  i6  |
|  命宮  |  palace   |  p0  |
| 兄弟宮 |  palace   |  p1  |
| 夫妻宮 |  palace   |  p2  |
| 子女宮 |  palace   |  p3  |
| 財帛宮 |  palace   |  p4  |
| 疾厄宮 |  palace   |  p5  |
| 遷移宮 |  palace   |  p6  |
| 奴僕宮 |  palace   |  p7  |
| 官祿宮 |  palace   |  p8  |
| 田宅宮 |  palace   |  p9  |
| 福德宮 |  palace   | p10  |
| 父母宮 |  palace   | p11  |
|  身宮  |  palace   | p12  |
|   甲   |  tiangan  | tg0  |
|   乙   |  tiangan  | tg1  |
|   丙   |  tiangan  | tg2  |
|   丁   |  tiangan  | tg3  |
|   戊   |  tiangan  | tg4  |
|   己   |  tiangan  | tg5  |
|   庚   |  tiangan  | tg6  |
|   辛   |  tiangan  | tg7  |
|   壬   |  tiangan  | tg8  |
|   癸   |  tiangan  | tg9  |
|   子   |   dizhi   | dz0  |
|   丑   |   dizhi   | dz1  |
|   寅   |   dizhi   | dz2  |
|   卯   |   dizhi   | dz3  |
|   辰   |   dizhi   | dz4  |
|   巳   |   dizhi   | dz5  |
|   午   |   dizhi   | dz6  |
|   未   |   dizhi   | dz7  |
|   申   |   dizhi   | dz8  |
|   酉   |   dizhi   | dz9  |
|   戌   |   dizhi   | dz10 |
|   亥   |   dizhi   | dz11 |

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
http://m.dajiazhao.com/paipan/zwdsjc/9540.html
https://wantubizhi.com/image.aspx
