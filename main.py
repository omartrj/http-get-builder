import tkinter as tk
from app import HttpRequestBuilder

def main():
    root = tk.Tk()
    root.title("HTTP Request Builder")
    HttpRequestBuilder(root)
    root.mainloop()

if __name__ == "__main__":
    main()
