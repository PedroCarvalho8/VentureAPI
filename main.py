import multiprocessing as mp
import os
from src.detection.visaocomputacional import detection
from src.repositories.db_interaction import *


def run_streamlit_server():

    initialize_db(('detected_items',))

    os.system("streamlit run src/streamlit/server.py")


if __name__ == "__main__":

    req_queue = mp.Queue()

    st_process = mp.Process(target=run_streamlit_server)
    cv_process = mp.Process(target=detection)

    st_process.start()
    cv_process.start()

    st_process.join()
    cv_process.join()
