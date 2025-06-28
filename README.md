# 网上商城管理系统 (Online Shopping Mall Management System)

## 1. 项目简介 (Introduction)

本项目是一个基于 Python 和 PyQt5 的C/S架构网上商城管理系统。系统分为三个主要部分：
- **服务器端 (Server):** 负责处理业务逻辑和数据库交互。
- **商家客户端 (Shop Client):** 供商家管理店铺信息、商品和查看交易。
- **顾客客户端 (Customer Client):** 供顾客浏览商品、购买商品、管理个人信息和查看订单。

系统使用 MySQL 作为后台数据库，实现了用户注册、登录、商品管理、交易处理等核心电商功能。

## 2. 项目结构 (Project Structure)

项目经过重构，遵循 PEP 8 命名规范，目录结构清晰，便于维护。

```
/
├── customer/             # 顾客客户端 UI 和业务逻辑
├── shop/                 # 商家客户端 UI 和业务逻辑
├── customer_ui/          # 顾客客户端 .ui 文件 (由 Qt Designer 设计)
├── shop_ui/              # 商家客户端 .ui 文件 (由 Qt Designer 设计)
├── pic/                  # 项目使用的图片资源
├── env/                  # 环境配置文件 (requirements.txt)
├── customer_main.py      # 顾客客户端主程序入口
├── shop_main.py          # 商家客户端主程序入口
├── server.py             # 服务器主程序
├── mysql_op.py           # MySQL 数据库操作封装模块
├── send_data.py          # 客户端数据发送模块
├── mall.sql              # 数据库定义 SQL 文件
└── README.md             # 项目说明文档
```

## 3. 功能特性 (Features)

### 顾客端
- 用户注册与登录
- 按商品名称、类型、店铺等条件浏览和搜索商品
- 查看商品详细信息
- 购买商品并生成订单
- 查看自己的历史交易记录
- 取消尚未处理的交易
- 查看和修改个人信息（收货人、联系方式、地址等）

### 商家端
- 商家注册与登录
- 添加新商品，包括名称、类型、价格和库存
- 查看店铺的所有商品
- 修改商品信息或下架商品
- 查看店铺的交易记录
- 查看和修改店铺信息

## 4. 数据库设计 (Database Design)

系统采用 MySQL 关系型数据库。包含四张核心表：`customer` (顾客), `shop` (商家), `goods` (商品), 和 `trade` (交易)。

### 4.1. 实体关系图 (ER Diagram)

![ER Diagram](https://mermaid.ink/img/pako:eNqNVMtqwzAQ_Jd8ymkPbeIeCgdBg4ccuskhhC6WJWslVqJkpy7C-9clO0lbh-whu9-d2dlljWmM8YnpgBv4QAt2I563vSgUjQ48W9Yd6r3v0C_z8L67h8zJk7S2F040JtFoh-q9H17gN6gP8E9Tz8o0QzV_D1K5WpT2Lp15N3CjI4wIe6M1B8lWbQ37397Bw2Qx8D3E5qV870lT-2HCKT4k_C4-5Kk6h_Rz9H5KzX9k1N4XJd84C5N-MhJ4hM8z7g9U6mC6Q2yqC81fE_E2n8pYkHk33-b_j0X-e7L7-pXlYJd7X9b9B8bX-e1XwRj1lHhH2hQW64b3mH_U4415C2c7qQ4I5B4s9-Vf3J8_t874d1i68p6SgYQjUuC2fU2y40G4W7d6x-HlJq4g4h4K81wX36iQ324b17P6T4_32GvA83DYYeP67FkM0FhJm5jUuJzLzUe7tT02Xz-mO-k_37_8AVhJq5g?type=png)

### 4.2. 表结构描述 (Table Schema)

#### `customer` - 顾客表
存储顾客账户信息。
| 列名 | 数据类型 | 约束 | 描述 |
| :--- | :--- | :--- | :--- |
| `cus_acc` | varchar(30) | PRIMARY KEY | 顾客账户 (主键) |
| `cus_pass` | varchar(30) | | 密码 |
| `cus_name` | varchar(30) | | 收货人姓名 |
| `cus_phone` | varchar(15) | | 联系电话 |
| `cus_addr` | varchar(30) | | 收货地址 |

#### `shop` - 商家表
存储商家店铺信息。
| 列名 | 数据类型 | 约束 | 描述 |
| :--- | :--- | :--- | :--- |
| `shop_acc` | varchar(30) | PRIMARY KEY | 商家账户 (主键) |
| `shop_pass`| varchar(30) | | 密码 |
| `shop_name`| varchar(30) | UNIQUE | 店铺名称 (唯一) |
| `shop_phone`| varchar(15) | | 服务电话 |
| `shop_addr` | varchar(15) | | 店铺所在地 |
| `shop_time`| varchar(20) | | 开店时间 |

#### `goods` - 商品表
存储商品信息，与商家表关联。
| 列名 | 数据类型 | 约束 | 描述 |
| :--- | :--- | :--- | :--- |
| `shop_acc` | varchar(30) | PRIMARY KEY, FOREIGN KEY | 所属商家账户 |
| `goods_name`| varchar(30) | PRIMARY KEY | 商品名称 |
| `goods_type`| varchar(30) | | 商品类型 |
| `goods_prices`| double | CHECK >= 0 | 价格 |
| `goods_rest`| int | CHECK >= 0 | 库存数量 |
| `goods_selled`| int | CHECK >= 0 | 已售数量 |

#### `trade` - 交易表
存储交易订单信息，与顾客、商家、商品表关联。
| 列名 | 数据类型 | 约束 | 描述 |
| :--- | :--- | :--- | :--- |
| `trade_id` | int | PRIMARY KEY, AUTO_INCREMENT | 交易ID (主键) |
| `cus_acc` | varchar(30) | FOREIGN KEY | 顾客账户 |
| `shop_acc` | varchar(30) | FOREIGN KEY | 商家账户 |
| `goods_name`| varchar(30) | FOREIGN KEY | 商品名称 |
| `trade_num` | int | CHECK > 0 | 交易数量 |
| `trade_money`| double | CHECK >= 0.0 | 交易总金额 |
| `trade_time`| varchar(20) | | 交易时间 |

### 4.3. 存储过程 (Stored Procedures)

#### `buy_goods`
- **功能:** 处理购买商品的事务，包括向`trade`表插入一条新纪录，并更新`goods`表中对应商品的库存和销量。
- **参数:** `cus_acc1`, `shop_acc1`, `goods_name1`, `trade_num1`, `trade_money1`, `trade_time1`

## 5. 环境配置与运行 (Setup and Usage)

### 5.1. 环境依赖 (Prerequisites)
- Python 3.x
- PyQt5
- PyMySQL
- MySQL Server

所有 Python 依赖已在 `env/requirements.txt` 中列出，可通过以下命令安装：
```bash
pip install -r env/requirements.txt
```

### 5.2. 数据库配置 (Database Setup)
1. 确保你的 MySQL 服务器正在运行。
2. 使用 MySQL 客户端（如命令行、Navicat 等）连接到数据库。
3. 执行 `mall.sql` 文件中的 SQL 命令来创建数据库 `mall` 和所有表。
4. 根据你的 MySQL 配置，修改 `mysql_op.py` 文件中的数据库连接信息（主机、用户名、密码）。

### 5.3. 运行项目 (Running the Project)
1. **启动服务器:**
   ```bash
   python server.py
   ```
2. **启动客户端:**
   - 启动顾客端: `python customer_main.py`
   - 启动商家端: `python shop_main.py`

## 6. 项目命名 (Project Name)

根据您的要求，项目根目录名称不应为 `Shopping-mall-management-system-master`。建议修改为一个更简洁的名称，例如 `online-shopping-system`。
