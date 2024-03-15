from pytube import YouTube
import tkinter as tk
import pyglet

pyglet.font.add_file('Ojuju.ttf')

class MyGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("800x500")
        self.title("YouTube Downloader")

        oj = 'Ojuju ExtraLight'

        self.title_label = tk.Label(self, text='YouTube Downloader', font=(oj, 20))
        self.title_label.pack(pady= 10)

        self.auth_label = tk.Label(self, text='by Coco', font=(oj, 12))
        self.auth_label.pack(pady= 10)

        self.url_frame = tk.Frame(self)
        self.url_frame.columnconfigure(0, weight=1)
        self.url_frame.columnconfigure(1, weight=1)

        self.url_input_label = tk.Label(self.url_frame, text='Youtube Link:', font=(oj, 12))
        self.url_input_label.grid(row= 0, column= 0, pady= 10, padx= 10, sticky='we')

        self.url_input = tk.Text(self.url_frame, font=(oj,12), height=1, width=50)
        self.url_input.grid(row= 0, column= 1, pady= 10, padx= 10, sticky='we')

        self.url_frame.pack(pady=10, padx=10)

        self.btn_frame = tk.Frame(self)
        self.btn_frame.columnconfigure(0, weight=1)
        self.btn_frame.columnconfigure(1, weight=1)

        self.btn360 = tk.Button(self.btn_frame, text="360p", font=(oj, 12), width=20, command=self.pressed360)
        self.btn360.grid(row=0, column=0, padx=10, pady=10, sticky=tk.EW)

        self.btn720 = tk.Button(self.btn_frame, text="720p", font=(oj, 12), width=20, command=self.pressed720)
        self.btn720.grid(row=0, column=1, padx=10, pady=10, sticky=tk.EW)

        self.btn_frame.pack(padx=10, pady=10)

        self.btnDownload = tk.Button(self, text='Download', font=(oj, 12), width=15, command=self.download)
        self.btnDownload.pack(padx=10, pady=10)

        self.mainloop()

    def pressed360(self):
        self.btn360.config(state=tk.DISABLED, relief=tk.SUNKEN)
        self.btn720.config(state=tk.ACTIVE, relief=tk.RAISED)
        global rez
        rez = '360'

    def pressed720(self):
        self.btn720.config(state=tk.DISABLED, relief=tk.SUNKEN)
        self.btn360.config(state=tk.ACTIVE, relief=tk.RAISED)
        global rez
        rez = '720'

    def download(self):
        yt = YouTube(self.url_input.get('1.0', tk.END).strip()
                     # on_progress_callback = progress_func,
                     # on_complete_callback = complete_func,
                     )

        rez_360p_stream = yt.streams.get_by_itag(18)
        rez_720p_stream = yt.streams.get_by_itag(22)

        if rez == '360':
            rez_360p_stream.download(r'C:\Users\Valentin\Desktop\music download')
        elif rez == '720':
            rez_720p_stream.download(r'C:\Users\Valentin\Desktop\music download')
            print('success')

gui = MyGUI()