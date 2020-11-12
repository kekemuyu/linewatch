# linewatch
LineWatch是一款主打wifi、蓝牙连接和集成众多传感器的可编程手表。以micropython语言为基础构建手表的软件系统。当前已实现时钟、闹钟、罗盘、天气、应用和设置等主要功能。其中应用部分依托于iotbbs平台，可以实现自制应用的创建、发布，手表端可以浏览应用市场的应用、下载、安装、运行等功能，实现了类似智能手机的功能。

## 硬件

[原理图链连接地址](https://iotbbs.vip/download)

- esp32-d4-pico集成4MB的flash，wifi，蓝牙
- 实时时钟bm8530
- 温湿度sht30(BMP280可选)
- 三轴地磁HMC5883
- 三轴加速度LIS3DH
- 微型震动马达
- SMD蜂鸣器
- 200mah电池
- cp2104实现电脑usb和手表通讯

## 软件

- micropython开源编程语言，专为小型硬件设计

