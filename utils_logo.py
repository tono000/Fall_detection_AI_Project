import cv2
import copy
import streamlit as st
from streamlit_image_select import image_select
import time


def get_logo_caption_lst(dict_device):
    logo_device = {"normal": "/home/tuvu/Course/app_project/assets/dow123421341234nload.png",
                   "alert": "/home/tuvu/Course/app_project/assets/asdaf231412341234.png"}
    captions_lst = []
    logo_list = []
    for device_id in dict_device.keys():
        captions_lst.append(dict_device[device_id]["DeviceId"])
        if dict_device[device_id]["status"] == 0:
            logo_list.append(logo_device["normal"])
        else:
            logo_list.append(logo_device["alert"])

    return captions_lst, logo_list

def show_logo(dict_device):
    captions_lst, logo_list = get_logo_caption_lst(dict_device)
    index_selected = image_select(
        "",
            images=logo_list,
            captions=captions_lst,
            index=0,
            use_container_width=False,
            return_value="index",
    )
    return index_selected