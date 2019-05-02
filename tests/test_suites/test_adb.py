'''
Created on May 2, 2019

@author: mrane
'''
import time

from pyautomation.mobile.adb import Adb


# print(Adb.get_connected_devices())
adb = Adb(Adb.get_connected_devices()[0])
# print("adb.get_device_carrier() " + adb.get_device_carrier())
# print("adb.get_device_serial_number() " + adb.get_device_serial_number())
# print("adb.get_device_model() " + adb.get_device_model())
# # print("adb.reboot_device() " + str(adb.reboot_device()))
# # adb.take_screenshot("file.png")
# adb.install_app(r"C:\Users\mrane\Downloads\selendroid-test-app-0.17.0.apk")
# print("app installed")
# time.sleep(5)
# adb.uninstall_app("io.selendroid.testapp")
print(adb.get_available_devices())
print(adb.get_installed_packages())
print(adb.get_foreground_activity())
print(adb.get_foreground_activity(True))
print(adb.force_stop_app('com.google.android.gm'))