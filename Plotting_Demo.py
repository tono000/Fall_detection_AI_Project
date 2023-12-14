import streamlit as st
import time
import numpy as np
import os
import cv2

st.set_page_config(page_title="Plotting Demo", page_icon="")

st.markdown("# Plotting Demo (for demo only)")
#st.sidebar.header("Plotting Demo")

#cap = cv2.VideoCapture(0)
frame_placeholder = st.empty()
#stop_button_pressed = st.button("Stop")
frame_dir = '/home/tuvu/Course/app_project/frame_depth_res/'
for frame_id in sorted(os.listdir(frame_dir)):
    frame = cv2.imread(os.path.join(frame_dir, frame_id))
    print(frame_id)
    #img_input = st.session_state["img_frame"]

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #st.session_state["img_frame"] = img_input
    frame_placeholder.image(frame,channels="RGB")
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    time.sleep(0.2)
cv2.destroyAllWindows()
#progress_bar = st.sidebar.progress(0)
#status_text = st.sidebar.empty()
#last_rows = np.random.randn(1, 1)
#chart = st.line_chart(last_rows)

#for i in range(1, 101):
    #new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    #status_text.text("%i%% Complete" % i)
    #chart.add_rows(new_rows)
    #progress_bar.progress(i)
    #last_rows = new_rows
    #time.sleep(0.05)

#progress_bar.empty()

## Streamlit widgets automatically run the script from top to bottom. Since
## this button is not connected to any other logic, it just causes a plain
## rerun.
#st.button("Re-run")
