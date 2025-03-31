import math
from kivy import config
import json
import os
import time

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.widget import Widget
from kivy.uix.slider import Slider
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.resources import resource_find
from kivy.loader import Loader
from kivy.clock import Clock 
from kivy.graphics.texture import Texture
from kivy.graphics import Color, rectangle
from kivy.properties import ListProperty, NumericProperty

from subprocess import Popen, PIPE
import subprocess
import sys
from threading import Thread

import cv2
from pyscrcpy import Client
from itertools import cycle
import requests
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from appium import webdriver
from appium.webdriver.appium_service import AppiumService
import pytesseract
import re

import tkinter as tk
from tkinter import filedialog
import json
import imageai
from imageai.Detection import VideoObjectDetection, ObjectDetection

import unittest
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import ApppiumBy
from tqdm import tqdm
import glob
import csv


#json code




