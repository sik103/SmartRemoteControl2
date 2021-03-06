## Hardware
### 使用するもの
- 個数はスマートリモコン1つあたりに必要なものである．
- ~~お金~~ 諸事情により，抵抗は家にあるものを合成して使用する．

#### Raspberry PI
|部品|型番|個数|備考|
|---|---|---|---|
|Raspberry PI|Raspberry PI 3 model B|1|||

- その他，micro SDカードや電源ケーブルなども含む．
- `Raspberry PI 2 Model B` でもテストする予定である．

#### 受信部回路

|部品|型番|個数|備考|
|---|---|---|---|
|赤外線受信モジュール|[IR受信モジュール(2.7-5.5V) [DS-1838T]](http://www.aitendo.com/product/3748)|1||
|電解コンデンサ|電解コンデンサ 100µF 25V|1|受信精度を上げるためのもの|
|抵抗|抵抗 100Ω|1|受信精度を上げるためのもの|
|抵抗|抵抗 1kΩ|2|受信精度を上げるためのもの，<br>直列接続で22kΩを作る|
|抵抗|抵抗 10kΩ|2|受信精度を上げるためのもの，<br>直列接続で22kΩを作る|

#### 送信部回路
|部品|型番|個数|備考|
|---|---|---|---|
|ユニバーサル基板|[ユニバーサル基板（Pi-ZERO） [UPi-ZERO-J0]](http://www.aitendo.com/product/17064)|1|今回はRaspberry PI zero用のものを使用した|
|ピンソケット|[254mmピッチピンソケット（2列） [PS254DV]](http://www.aitendo.com/product/6856)|1|aitendoのサイトでは，254mmと表記されているが，2.54mmの間違いと見られる|
|MOSFET|[NチャネルMOSFET(8個入) [2N7000]](http://www.aitendo.com/product/6925)|1||
|MOSFET|[PチャネルパワーMOSFET [IRF9Z34N]](http://www.aitendo.com/product/15267)|1||
|赤外線LED|[赤外線LED（φ5mm/10個入） [YSL-R531FR1C-F1]](http://www.aitendo.com/product/6710)|4||
|抵抗|抵抗 10kΩ|2|並列接続で5kΩ（4.7kΩ）を作る|
|抵抗|抵抗 10Ω|3 * 4|直接接続で30Ω（27Ω）を4つ作る|

#### Google Home
|部品|型番|個数|備考|
|---|---|---|---|
|Google Home|Google Home mini|1|色：アクア|
