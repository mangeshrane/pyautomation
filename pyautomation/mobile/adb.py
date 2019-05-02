import subprocess
import os
from pyautomation.logger.logger import LOG
import re

class Adb(object):
    
    adb = None
    
    def __init__(self, deviceid):
        self.adb = self.command("adb start-server")
        self.deviceid = deviceid
    
    @staticmethod
    def command(command):
        if command.startswith("adb"):
            command = command.replace("adb", os.path.join(os.environ['ANDROID_HOME'],"platform-tools", "adb"))
            LOG.info("Executing command : " + command)
        else:
            LOG.error('This method is designed to run ADB commands only!')
            raise RuntimeError("This method is designed to run ADB commands only!")
        output = subprocess.check_output(command)
        if output is None:
            return ""
        else:
            return output.decode('utf-8').strip();
    
    @staticmethod
    def get_connected_devices():
        devices = [];
        output = Adb.command("adb devices")
        for line in str(output).split("\n"):
            line = line.strip()
            if line.endswith("device"):
                devices.append(line.replace("device", "").strip())
        return devices;
    
    def get_foreground_activity(self, package=False):
        raw = self.command("adb -s "+ self.deviceid +" shell dumpsys window windows | grep mCurrentFocus")
        grp = re.findall('[\w+\.]+', raw)
        if package:
            return '{}/{}'.format(grp[-2], grp[-1])
        else:
            return grp[-1]
    
    def get_android_version(self):
        output = self.command("adb -s "+ self.deviceid +" shell getprop ro.build.version.release")
        if(output.length() == 3):
            output+=".0"
        return output
    
    def _get_installed_packages(self, deviceid):
        packages = []
        output = self.command("adb -s "+ deviceid +" shell pm list packages").split("\n")
        for packageID in output:
            packages.append(packageID.replace("package:","").strip())
        return packages
    
    def get_installed_packages(self):
        return self._get_installed_packages(self.deviceid)

    def open_apps_activity(self, packageid, activityid):
        self.command("adb -s "+ self.deviceid +" shell am start -c api.android.intent.category.LAUNCHER -a api.android.intent.action.MAIN -n " + packageid + "/" +activityid)

    def clear_apps_data(self, package_id):
        self.command("adb -s " + self.deviceid + " shell pm clear " + package_id)

    def force_stop_app(self, packageid):
        self.command("adb -s " + self.deviceid +" shell am force-stop " + packageid)

    def install_app(self, apkpath):
        self.command("adb -s "+ self.deviceid +" install " + apkpath);

    def uninstall_app(self, packageid):
        self.command("adb -s "+ self.deviceid +" uninstall " + packageid);

    def clear_log_buffer(self):
        self.command("adb -s "+ self.deviceid +" shell -c")

    def push_file(self, source, target):
        self.command("adb -s "+ self.deviceid +" push "+source+" "+target);

    def pull_file(self, source, target):
        self.command("adb -s " + self.deviceid + " pull "+source+" "+target);

    def delete_file(self, target):
        self.command("adb -s " + self.deviceid + " shell rm "+ target)

    def move_file(self, source, target):
        self.command("adb -s " + self.deviceid + " shell mv "+source+" "+target)

    def take_screenshot(self, target):
        self.command("adb -s " + self.deviceid + " shell screencap " + target)

    def reboot_device(self):
        self.command("adb -s " + self.deviceid + " reboot")

    def get_device_model(self):
        return self.command("adb -s " + self.deviceid + " shell getprop ro.product.model")

    def get_device_serial_number(self):
        return self.command("adb -s " + self.deviceid + " shell getprop ro.serialno")

    def get_device_carrier(self):
        return self.command("adb -s " + self.deviceid + " shell getprop gsm.operator.alpha")
    
    def get_available_devices(self):
        LOG.info("Checking for available devices")
        devices = []
        connected_devices = self.get_connected_devices()
        for connected_device in connected_devices:
            apps = self._get_installed_packages(connected_device)
            if "io.appium.unlock" not in apps:
                devices.append(connected_device)
        return devices
    
    def __del__(self):
        try:
            self.command("adb kill-server")
        except:
            pass
