import threading
from firewall import run_firewall
from ids import run_ids

if __name__ == "__main__":
    fw_thread = threading.Thread(target=run_firewall)
    ids_thread = threading.Thread(target=run_ids)
    fw_thread.start()
    ids_thread.start()
    fw_thread.join()
    ids_thread.join()