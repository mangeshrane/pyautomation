import subprocess
import os
from pyautomation.configuration import CONFIG
from pyautomation.logger.logger import LOG

class Adb(object):
    
    adb = None
    
    def __init__(self):
        self.adb = self.command("adb start-server")
    
    def command(self, command):
        if command.startsWith("adb"):
            command = command.replace("adb ", os.path.join(CONFIG.get("android.home") + "/platform-tools/adb"))
        else:
            raise RuntimeError("This method is designed to run ADB commands only!")
        output = subprocess.Popen(command);
        if output is None:
            return "";
        else:
            return output.strip();
    
    def get_connected_devices(self):
        devices = [];
        output = self.command("adb devices");
        for line in str(output).split("\n"):
            line = line.strip();
            if line.endsWith("device"):
                devices.append(line.replace("device", "").strip());
        return devices;
    
    def get_foreground_activity(self, deviceid):
        return self.command("adb -s "+ deviceid +" shell dumpsys window windows | grep mCurrentFocus")
    
    def get_android_version(self, deviceid):
        output = self.command("adb -s "+ deviceid +" shell getprop ro.build.version.release")
        if(output.length() == 3):
            output+=".0"
        return output
    
    def get_installed_packages(self, deviceid):
        packages = []
        output = self.command("adb -s "+ deviceid +" shell pm list packages").split("\n")
        for packageID in output:
            packages.append(packageID.replace("package:","").trim())
        return packages

    def open_apps_activity(self, deviceid, packageid, activityid):
        self.command("adb -s "+ deviceid +" shell am start -c api.android.intent.category.LAUNCHER -a api.android.intent.action.MAIN -n " + packageid + "/" +activityid)

    def clear_apps_data(self, device_id, package_id):
        self.command("adb -s " + device_id + " shell pm clear " + package_id)

    def force_stop_app(self, deviceid, packageid):
        self.command("adb -s " + deviceid +" shell am force-stop "+packageid)

    def install_app(self, deviceid, apkpath):
        self.command("adb -s "+ deviceid +" install " + apkpath);

    def uninstall_app(self, deviceid, packageid):
        self.command("adb -s "+ deviceid +" uninstall " + packageid);

    def clear_log_buffer(self, deviceid):
        self.command("adb -s "+ deviceid +" shell -c")

    def push_file(self, deviceid, source, target):
        self.command("adb -s "+ deviceid +" push "+source+" "+target);

    def pull_file(self, deviceid, source, target):
        self.command("adb -s " + deviceid + " pull "+source+" "+target);

    def delete_file(self, deviceid, target):
        self.command("adb -s " + deviceid + " shell rm "+ target)

    def move_file(self, deviceid, source, target):
        self.command("adb -s " + deviceid + " shell mv "+source+" "+target)

    def take_screenshot(self, deviceid, target):
        self.command("adb -s " + deviceid + " shell screencap "+target)

    def reboot_device(self, deviceid):
        self.command("adb -s " + deviceid + " reboot")

    def get_device_model(self, deviceid):
        return self.command("adb -s " + deviceid + " shell getprop ro.product.model")

    def get_device_serial_number(self, deviceid):
        return self.command("adb -s " + deviceid + " shell getprop ro.serialno")

    def get_device_carrier(self, deviceid):
        return self.command("adb -s " + deviceid + " shell getprop gsm.operator.alpha")
    
    def get_available_devices(self):
        LOG.info("Checking for available devices")
        devices = []
        connected_devices = self.get_connected_devices()
        for connected_device in connected_devices:
            apps = self.get_installed_packages(connected_device)
            if "io.appium.unlock" not in apps:
                devices.append(connected_device)
        return devices
    
    def __del__(self):
        self.command("adb kill-server")