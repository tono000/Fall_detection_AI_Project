import streamlit as st
import time
from utils_logo import show_logo
from utils_background import show_background
import os
from ultralytics import YOLO
import beepy


if not st.session_state:
    st.session_state.count = 0
    dict_device= {}
    dict_device["0"] = {"DeviceId": "Device 1", "ToiletId": "id 1", "status": 0, "prev_status": 0,
                        "time_start": 0, "time_len": 0}
    dict_device["1"] = {"DeviceId": "Device 2", "ToiletId": "id 2", "status": 0, "prev_status": 0,
                        "time_start": 0, "time_len": 0}
    dict_device["2"] = {"DeviceId": "Device 3", "ToiletId": "id 3", "status": 0, "prev_status": 0,
                        "time_start": 0, "time_len": 0}
    st.session_state["dict_device"] = dict_device.copy()
    st.session_state.model = YOLO("/home/tuvu/Course/app_project/best.pt")


st.set_page_config(
    page_title="Device tracking list", page_icon="🖼️", initial_sidebar_state="collapsed"
)
st.markdown("# Device tracking list")
st.divider()




frame_dir = "/home/tuvu/Course/app_project/frame_depth_res/"
frame_id = str(st.session_state.count).zfill(4) + ".jpg"
img_path = os.path.join(frame_dir, frame_id)
print(img_path)
results = st.session_state.model(img_path)
if results[0].boxes.xyxy.shape[0] > 0:
    convert_status = 1
    # beepy.beep(sound='coin')
    if st.session_state.count%3==0:
        duration = 0.1  # seconds
        freq = 440  # Hz
        os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))

else:
    convert_status = 0
st.session_state["dict_device"]["0"]["status"] = convert_status

# if st.session_state.count == 30 or st.session_state.count == 60:
#     if st.session_state["dict_device"]["0"]["status"] == 0:
#         convert_status = 1
#     else:
#         convert_status = 0
#     st.session_state["dict_device"]["0"]["status"] = convert_status



if (st.session_state["dict_device"]["0"]["prev_status"] == 1 and
        st.session_state["dict_device"]["0"]["status"] == 1):
    st.session_state["dict_device"]["0"]["time_len"] = time.time() -\
                                                       st.session_state["dict_device"]["0"]["time_start"]
else:
    st.session_state["dict_device"]["0"]["time_start"] = time.time()
    st.session_state["dict_device"]["0"]["time_len"] = 0

index_selected = show_logo(st.session_state["dict_device"])
show_background(st.session_state["dict_device"], index_selected)


st.session_state["dict_device"]["0"]["prev_status"] = st.session_state["dict_device"]["0"]["status"]
st.session_state.count += 1
time.sleep(0.1)
st.rerun()
