import multiprocessing as mp
import os
from src.detection.visaocomputacional import detection
from src.repositories.db_interaction import *
import shutil


def run_streamlit_server():
    frame_dir = "temp_frames"

    if os.path.exists(frame_dir):
        shutil.rmtree(frame_dir)
        os.makedirs(frame_dir)

    initialize_db(('detected_items', 'items_to_detect'))

    os.system("streamlit run src/streamlit/🏠_Início.py")


if __name__ == "__main__":

    req_queue = mp.Queue()

    st_process = mp.Process(target=run_streamlit_server)
    cv_process = mp.Process(target=detection)

    st_process.start()
    cv_process.start()

    st_process.join()
    cv_process.join()
