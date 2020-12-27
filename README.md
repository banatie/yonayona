# yonayona

## 1. Introduction
yonayona is a web app that people can anonymously talk to someone.
It is opened from 12am to 4am.

## 2. Description
### World
One day, you go to stargazing to a forest.
While stargazing, you start hearing someone, and you can communicate with him/her.
Conversation is under typewriting.

### Author
Banatie

### Target User
People who have PC and are awake for nothing at midnight

### Target User Count
1000+

### Interviewed People
4 people

## 3. Features
### Base Features
- Signup
- Login/Logout
- Anonymous
- Display total user count at home page
- Start conversation
- Get someone assigned
- Talk to each other
- Show history by date
- Show duration of conversation at history
- Read history
- Delete history
- Disable conversion except certain time(12am-4am)
- Report Inappropriate message

### Design Features
- tutorial at login
- Display day theme
- Display night theme
- Show BYE... when time is up

### Terms
交信/Communicate

### Restrictions
- Anonymous
- Private conversation
- Only available during mid night(12am - 4am)
- Can talk to one person per day

## 4. Schedule
Task  | Start Date | End Date | Expected Hours | Actual Hours
------- |-------|------------|----------|--------------
Design  | 12/26 | 12/28 | 3h | 
Collect Materials  | 12/26 | 12/28 | 3h | 
css Framework tutorial  | 12/26 | 12/28 | 3h | 
Front End Development  | 12/26 | 12/28 | 3h | 
URI Architecture  | 12/28 | 12/31 | 3h | 
DB Architecture  | 12/28 | 12/31 | 3h | 
Create Django Project  | 12/28 | 12/31 | 3h | 
Backend Development  | 12/28 | 12/31 | 3h | 
Create Flow Chart  | 12/28 | 12/31 | 3h | 
Local Test for All Flow  | 12/28 | 12/31 | 3h | 
Deployment  | 1/1 | 1/2 | 3h | 
Online Test with All Flow  | 1/1 | 1/2 | 3h | 
Improve User Usage/Experience  | 1/1 | 1/2 | 3h | 
SEO Basics | 1/1 | 1/2 | 3h | 
Marketing  | 1/1 | 1/2 | 3h | 
Continuous Improvement  | 1/3 | 1/31 |  | 

## 5. Design
### Inspiring website
- [PaperRock](https://www.paperockcreative.com/)
- [index.studio](https://index.studio/)
- [loris](https://www.loris-stavrinides.com/about)

### Method
- [Atomic Design](https://qiita.com/teradonburi/items/412f65147525ff34dbbd)

### Layout
グリッドレイアウト

### Color
Color Type | Color | Percentage
------- |-------|------- 
Base Color | Black | 70%
Main Color | Gold | 25%
Accent Color | Purple? | 5%

### Key Visual
- [Night Forest](https://www.pexels.com/photo/person-sky-silhouette-night-32237/)

### Materials
#### Icon
- [Flat Icon](http://flat-icon-design.com/)
- [material.io](https://material.io/resources/icons/?style=baseline)

#### Favicon
Parameter | Value
------- |-------
Text | yonayona
Background Color | #000
Text Color | #FFF
Font | Audiowide
Font Size | 20

- [favicon.io](https://favicon.io/favicon-generator/)
- [Google Font](https://fonts.google.com/?preview.text=yonayona&preview.text_type=custom)

#### Pictures
- [pexel](https://www.pexels.com/?onboarding=skipped)

#### Music
- [fesliyanstudios](https://www.fesliyanstudios.com/royalty-free-music/downloads-c/peaceful-and-relaxing-music/22)

#### Font
- [ロンドB](https://moji-waku.com/ronde/index.html)
- [廻想体](https://moji-waku.com/kaiso/index.html)
- [マキナス4](https://moji-waku.com/makinas/index.html)

## 6. Development
### OS
Ubuntu 18.04

### Browser
Mozilla Firefox 83.0

### Frameworks
Django@3.1.4
Materialize@1.0.0

### Database
Postresql

### Server
Heroku Hobby plan($7/month)

### Naming Convention
pep8

### URI Design
/signup
/login
/logout
/communicate
...
TBA

### New Learning
- materializecss
- Ansible
- docstring

## 7. SEO
### titleタグ
検索結果のページの見出しとして使われます。50文字以内が目安
### meta descriptionタグ
検索結果のページの説明として使われます。50〜120文字以内が目安(meta descriptionとは)
### meta keywords
検索結果に反映されないので不要（参考：SEOとキーワード数（メタタグ・タイトル・1ページ内）の正しい設計）
### h1タグ
1〜２個程度で適切なキーワードを含めたほうが良い（参考：SEO１位のための「h1」タグ設定ガイド）
### パンくずリスト
カテゴリ別のページにはつけたほうが良い、後述のOGPにもパンくずリスト表示させることもできます。（例：ECサイトやポータルサイトのカテゴリページ）
### ページ内のキーワード出現頻度は適切か？
５％前後が良いとされていて、１０％を超えると多すぎる。
### 重要な画像（存在しないと意味が伝わらないもの）
表示されないことも考慮してalt属性で説明をつける
### Test
- [funmaker](https://funmaker.jp/seo/funkeyrating/)


## 8. History
Catch Phrase: あなたもYonaYonaしてみませんか？素敵な出会いを
Eliminated features
12/20
- id-to-long message
- One round-trip conversation(一期一会/Once in a lifetime meet)
- Up to 3 people to get replied
- Up to 1 letter/day to write reply