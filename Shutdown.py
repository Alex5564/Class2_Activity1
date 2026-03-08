import os


def shutdown_computer():
    if os.name == 'nt':
        print("Shutting down Windows computer...")
        os.system("shutdown /s /t 1")
    elif os.name == 'posix':
        print("Shutting down Unix/Linux/Mac computer...")
        os.system("sudo shutdown -h now")
    else:
        print("Unsupported operating system. Cannot shutdown.")


if __name__ == "__main__":
    shutdown_computer()
      
