#!/usr/bin/env python
# -*- coding: utf-8 -*-

from main.config.soft_import_module import soft_import
# browsers
from main.softwares.browsers.firefox_browsers import firefox_browsers
from main.softwares.browsers.chromium_browsers import chromium_browsers

try:
    from main.softwares.memory.memorydump import MemoryDump
except ImportError:
    pass


def get_categories():
    category = {
        'chats': {'help': 'Chat clients supported'},
        'sysadmin': {'help': 'SCP/SSH/FTP/FTPS clients supported'},
        'databases': {'help': 'SQL clients supported'},
        'mails': {'help': 'Email clients supported'},
        'memory': {'help': 'Retrieve passwords from memory'},
        'wifi': {'help': 'Wifi'},
        'browsers': {'help': 'Web browsers supported'},
        'wallet': {'help': 'Windows credentials (credential manager, etc.)'},
        'git': {'help': 'GIT clients supported'},
        'unused': {'help': 'This modules could not be used because of broken dependence'}
    }
    return category


def get_modules_names():
    return [
        ("main.softwares.mails.clawsmail", "ClawsMail"),
        ("main.softwares.mails.thunderbird", "Thunderbird"),
        ("main.softwares.databases.dbvis", "DbVisualizer"),
        ("main.softwares.sysadmin.env_variable", "Env_variable"),
        ("main.softwares.sysadmin.apachedirectorystudio", "ApacheDirectoryStudio"),
        ("main.softwares.sysadmin.filezilla", "Filezilla"),
        ("main.softwares.sysadmin.fstab", "Fstab"),
        ("main.softwares.browsers.opera", "Opera"),
        ("main.softwares.chats.pidgin", "Pidgin"),
        ("main.softwares.chats.psi", "PSI"),
        ("main.softwares.sysadmin.shadow", "Shadow"),
        ("main.softwares.sysadmin.aws", "Aws"),
        ("main.softwares.sysadmin.docker", "Docker"),
        ("main.softwares.sysadmin.rclone", "Rclone"),
        ("main.softwares.sysadmin.ssh", "Ssh"),
        ("main.softwares.sysadmin.cli", "Cli"),
        ("main.softwares.sysadmin.gftp", "gFTP"),
        ("main.softwares.sysadmin.keepassconfig", "KeePassConfig"),
        ("main.softwares.sysadmin.grub", "Grub"),
        ("main.softwares.databases.sqldeveloper", "SQLDeveloper"),
        ("main.softwares.databases.squirrel", "Squirrel"),
        ("main.softwares.wifi.wifi", "Wifi"),
        ("main.softwares.wifi.wpa_supplicant", "Wpa_supplicant"),
        ("main.softwares.wallet.kde", "Kde"),
        ("main.softwares.wallet.libsecret", "Libsecret"),
        ("main.softwares.memory.mimipy", "Mimipy"),
        ("main.softwares.git.gitforlinux", "GitForLinux")
    ]

    # very long to execute
    # try:
    # 	module_names.append(MemoryDump())
    # except:
    # 	pass


def get_modules():
    modules = [soft_import(package_name, module_name)() for package_name, module_name in get_modules_names()]
    return modules + chromium_browsers + firefox_browsers
