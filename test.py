# my_module.py

def my_function():
    from google.colab import drive
    drive.mount('/content/gdrive')
    print("Hello from my_function in my_module!")