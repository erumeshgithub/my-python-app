[app]
# App identification
title = LinuxBuiltApp
package.name = linuxapp
package.domain = org.linux

# Linux-specific source handling
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,txt,ttf

# Linux-style version management
version = 1.0

# Requirements for Linux build environment
requirements = python3,kivy

[buildozer]
# Linux build optimization
log_level = 2
warn_on_root = 0

[android]
# Android targets
api = 33
minapi = 21
ndk = 25b

# Auto-accept licenses for Linux CI
android.accept_sdk_license = True

# Permissions
android.permissions = INTERNET

# Linux build optimization
p4a.branch = develop
android.arch = arm64-v8a

# Linux-specific anti-lock for CI environments
android.skip_anti_locking = True
