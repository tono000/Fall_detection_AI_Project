import cv2
import copy
import streamlit as st
from streamlit_image_select import image_select
import time


def load_background_img():
    img_background_normal = cv2.imread("/home/tuvu/Course/app_project/assets/background_normal.png", 1)
    img_background_normal = cv2.cvtColor(img_background_normal, cv2.COLOR_BGR2RGB)
    img_background_abnormal = cv2.imread("/home/tuvu/Course/app_project/assets/background.png", 1)
    img_background_abnormal = cv2.cvtColor(img_background_abnormal, cv2.COLOR_BGR2RGB)
    return [img_background_normal, img_background_abnormal]


def draw_background_normal(img_background_normal):
    img_background_normal = cv2.putText(img_background_normal, "Normal", (325, 300), cv2.FONT_HERSHEY_DUPLEX,
                                        2, (13, 125, 31), 2, cv2.LINE_AA)
    img_background_normal = cv2.putText(img_background_normal, "It is normal here. Dont worry.",
                                        (200, 350), cv2.FONT_HERSHEY_SIMPLEX, 1, (13, 125, 31), 1, cv2.LINE_AA)

    return img_background_normal


def draw_background_abnormal(img_original_abnormal, device_time):
    img_original_abnormal = cv2.putText(img_original_abnormal, "Alert", (380, 300), cv2.FONT_HERSHEY_DUPLEX,
                                        2, (255, 0, 0), 2, cv2.LINE_AA)
    img_original_abnormal = cv2.putText(img_original_abnormal, "Fall event detected " + str(device_time), (300, 350),
                      cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1, cv2.LINE_AA)

    return img_original_abnormal


def initial_font():
    font_dict = {}
    font_dict['font'] = cv2.FONT_HERSHEY_SIMPLEX
    font_dict['font_size'] = 1
    font_dict['font_color'] = (255, 255, 255)  # White color in BGR
    font_dict['font_thickness'] = 2
    font_dict['font_position'] = (50, 50)  # (x, y) coordinates where the text will be placed
    return font_dict

def show_background(dict_device, index_selected):
    background_list = load_background_img()
    font_dict = initial_font()
    status_ = dict_device[str(index_selected)]['status']

    img_cv2 = background_list[status_].copy()

    cv2.putText(img_cv2, dict_device[str(index_selected)]["DeviceId"], (300, 100), cv2.FONT_HERSHEY_DUPLEX,
                    2, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(img_cv2, "Toilet " + dict_device[str(index_selected)]["ToiletId"],
                (275, 200), cv2.FONT_HERSHEY_DUPLEX, 2, (0, 0, 0), 2, cv2.LINE_AA)

    if status_ == 0:
        img_cv2 = draw_background_normal(img_cv2)
    else:
        img_cv2 = draw_background_abnormal(img_cv2, int(dict_device[str(index_selected)]['time_len']))
    st.image(img_cv2)
    return index_selected