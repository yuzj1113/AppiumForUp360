# coding=utf-8
from util.dos_cmd import DosCmd
from util.port import Port
import threading
import time
import os
from util.write_user_command import WriteUserCommand
import multiprocessing


class Server:
    def __init__(self):
        self.dos = DosCmd()
        self.device_list = self.get_devices()
        self.write_file = WriteUserCommand()

    def get_devices(self):
        '''
        获取设备信息
        '''

        devices_list = []
        result_list = self.dos.excute_cmd_result('adb devices')
        if len(result_list) >= 2:
            for i in result_list:
                if 'List' in i:
                    continue
                devices_info = i.split('\t')
                if devices_info[1] == 'device':
                    devices_list.append(devices_info[0])
            return devices_list
        else:
            return ''

    def create_port_list(self, start_port):
        '''
        创建可用端口
        '''
        port = Port()
        port_list = []
        port_list = port.create_port_list(start_port, self.device_list)
        return port_list

    def create_command_list(self, i, dir):
        '''
        生成命令
        '''
        # appium -p 4700 -bp 4701 -U 127.0.0.1:21503

        command_list = []
        appium_port_list = self.create_port_list(4724)
        bootstrap_port_list = self.create_port_list(4901)
        device_list = self.device_list
        # --no-reset
        now = time.strftime("%Y-%m-%d_%H_%M_%S")
        day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        file_name = os.getcwd() + "\\report\\log\\" + day + "\\" + dir
        print(file_name)
        if os.path.exists(file_name):
            file_name = file_name + "\\" + now + "_" + str(i) + ".log"
        else:
            os.makedirs(file_name)
            file_name = file_name + "\\" + now + "_" + str(i) + ".log"

        command = "appium -p " + str(appium_port_list[i]) + " -bp " + str(bootstrap_port_list[i]) + " -U " + \
                  device_list[i] + "  --session-override --log "+file_name
        # appium -p 4723 -bp 4726 -U 127.0.0.1:62001 --no-reset --session-override --log E:/Teacher/Imooc/AppiumPython/report/log/test01.log
        command_list.append(command)
        self.write_file.write_data(i, device_list[i], str(bootstrap_port_list[i]), str(appium_port_list[i]))

        return command_list

    def start_server(self, i, dir):
        '''
        启动服务
        '''
        self.start_list = self.create_command_list(i, dir)
        print(self.start_list)

        self.dos.excute_cmd(self.start_list[0])

    def kill_server(self):
        server_list = self.dos.excute_cmd_result('tasklist | find "node.exe"')
        if len(server_list) > 0:
            self.dos.excute_cmd('taskkill -F -PID node.exe')

    def main(self, dir):
        thread_list = []
        self.kill_server()
        self.write_file.clear_data()
        for i in range(len(self.device_list)):
            #appium_start = threading.Thread(target=self.start_server, args=(i,))
            appium_start = multiprocessing.Process(target=self.start_server, args=(i, dir))
            thread_list.append(appium_start)

        for j in thread_list:
            j.start()

        time.sleep(15)


if __name__ == '__main__':
    server = Server()

