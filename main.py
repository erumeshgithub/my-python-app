#!/usr/bin/env python3
"""
Linux-optimized Python app for Android
"""
import os
import sys
import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class LinuxApp(App):
    def build(self):
        # Linux-style logging
        print(f"App starting from: {os.getcwd()}")
        print(f"Python executable: {sys.executable}")
        
        layout = BoxLayout(orientation='vertical')
        label = Label(
            text='Built on Linux GitHub Runner',
            font_size='24sp'
        )
        layout.add_widget(label)
        return layout

if __name__ == '__main__':
    # Linux entry point
    LinuxApp().run()
