import threading
import time
import queue
import socket
import json
from mysql_op import *


class Shop:
    def __init__(self, conn):
        self.conn = conn

    def register(self, recv):
        op1 = Shop_op()
        if op1.register(recv['user'], recv['passwd'], recv['shop_name'], recv['phone'], recv['addr']):
            data = {'result': 'success'}
        else:
            data = {'result': 'fail'}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def login(self, recv):
        op1 = Shop_op()
        if op1.login(recv['user'], recv['passwd']):
            data = {'result': 'success'}
        else:
            data = {'result': 'fail'}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def addgoods(self, recv):
        op1 = Shop_op()
        if op1.add_goods(recv['user'], recv['goods_name'], recv['goods_type'], recv['goods_prices'], recv['goods_rest']):
            data = {'result': 'success'}
        else:
            data = {'result': 'fail'}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def viewgoods(self, recv):
        op1 = Shop_op()
        data = {'result': op1.view_goods(
            recv['user'], recv['goods_name'], recv['goods_type'])}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def viewtrade(self, recv):
        op1 = Shop_op()
        data = {'result': op1.view_trade(
            recv['user'], recv['goods_name'], recv['goods_type'])}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def selectgoods(self, recv):
        op1 = Shop_op()
        data = {'result': op1.select_goods(recv['user'])}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def deletegoods(self, recv):
        op1 = Shop_op()
        if op1.delete_goods(recv['user'], recv['goods_name']):
            data = {'result': 'success'}
        else:
            data = {'result': 'fail'}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def selectgoodsinfo(self, recv):
        op1 = Shop_op()
        # data={'result':'success'}
        data = {'result': op1.select_goodsinfo(
            recv['user'], recv['goods_name'])}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def updategoods(self, recv):
        op1 = Shop_op()
        if op1.update_goods(recv['user'], recv['old_goods_name'], recv['goods_name'], recv['goods_type'], recv['goods_prices'], recv['goods_rest']):
            data = {'result': 'success'}
        else:
            data = {'result': 'fail'}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def shopinfo(self, recv):
        op1 = Shop_op()
        data = {'result': op1.shop_info(recv['user'])}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def updateshop(self, recv):
        op1 = Shop_op()
        if op1.update_shop(recv['user'], recv['passwd'], recv['shop_name'], recv['phone'], recv['addr']):
            data = {'result': 'success'}
        else:
            data = {'result': 'fail'}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()


class Customer:
    def __init__(self, conn):
        self.conn = conn

    def register(self, recv):
        op1 = Customer_op()
        if op1.register(recv['user'], recv['passwd'], recv['cus_name'], recv['phone'], recv['addr']):
            data = {'result': 'success'}
        else:
            data = {'result': 'fail'}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def login(self, recv):
        op1 = Customer_op()
        if op1.login(recv['user'], recv['passwd']):
            data = {'result': 'success'}
        else:
            data = {'result': 'fail'}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def viewgoods(self, recv):
        op1 = Customer_op()
        data = {'result': op1.view_goods(
            recv['goods_name'], recv['goods_type'], recv['shop_name'])}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def allgoods(self, recv):
        op1 = Customer_op()
        data = {'result': op1.all_goods()}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def buygoods(self, recv):
        op1 = Customer_op()
        if op1.buy_goods(recv['user'], recv['goods_name'], recv['shop_acc'], recv['trade_num'], recv['trade_money']):
            data = {'result': 'success'}
        else:
            data = {'result': 'fail'}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def viewtrade(self, recv):
        op1 = Customer_op()
        data = {'result': op1.view_trade(
            recv['user'], recv['goods_name'], recv['goods_type'])}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def alltrade(self, recv):
        op1 = Customer_op()
        data = {'result': op1.all_trade(recv['user'])}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def offtrade(self, recv):
        op1 = Customer_op()
        if op1.off_trade(recv['trade_id']):
            data = {'result': 'success'}
        else:
            data = {'result': 'fail'}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def cusinfo(self, recv):
        op1 = Customer_op()
        data = {'result': op1.cus_info(recv['user'])}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def updatecus(self, recv):
        op1 = Customer_op()
        if op1.update_cus(recv['user'], recv['passwd'], recv['cus_name'], recv['phone'], recv['addr']):
            data = {'result': 'success'}
        else:
            data = {'result': 'fail'}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()


if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 5000))
    s.listen(20)
    while True:
        conn, addr = s.accept()
        try:
            recv_data = conn.recv(1024)
            if not recv_data:
                continue
            
            recv = json.loads(recv_data.decode())
            print(f"Received from {addr}: {json.dumps(recv)}")

            if recv['id'] == 'shop':
                shop_handler = Shop(conn)
                shop_routes = {
                    'register': shop_handler.register,
                    'login': shop_handler.login,
                    'add_goods': shop_handler.addgoods,
                    'view_goods': shop_handler.viewgoods,
                    'view_trade': shop_handler.viewtrade,
                    'select_goods': shop_handler.selectgoods,
                    'delete_goods': shop_handler.deletegoods,
                    'select_goodsinfo': shop_handler.selectgoodsinfo,
                    'update_goods': shop_handler.updategoods,
                    'shop_info': shop_handler.shopinfo,
                    'update_shop': shop_handler.updateshop,
                }
                handler = shop_routes.get(recv['type'])
                if handler:
                    handler(recv)
                else:
                    print(f"Unknown shop request type: {recv['type']}")
                    conn.close()

            elif recv['id'] == 'customer':
                customer_handler = Customer(conn)
                customer_routes = {
                    'register': customer_handler.register,
                    'login': customer_handler.login,
                    'view_goods': customer_handler.viewgoods,
                    'all_goods': customer_handler.allgoods,
                    'buy_goods': customer_handler.buygoods,
                    'view_trade': customer_handler.viewtrade,
                    'all_trade': customer_handler.alltrade,
                    'off_trade': customer_handler.offtrade,
                    'cus_info': customer_handler.cusinfo,
                    'update_cus': customer_handler.updatecus,
                }
                handler = customer_routes.get(recv['type'])
                if handler:
                    handler(recv)
                else:
                    print(f"Unknown customer request type: {recv['type']}")
                    conn.close()
            else:
                print(f"Unknown client id: {recv['id']}")
                conn.close()

        except json.JSONDecodeError:
            print(f"Error decoding JSON from {addr}")
            conn.close()
        except socket.error as e:
            print(f"Socket error with {addr}: {e}")
            conn.close()
        except Exception as e:
            print(f"An unexpected error occurred with {addr}: {e}")
            conn.close()
