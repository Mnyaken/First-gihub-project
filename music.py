from tkinter import *



window = Tk()
window.title('Music Player')
window.geometry('600x300')

window.config(bg="white")


def add_songs():
    song = filedialog.askopenfilename(initialdir =r"C:/audios/",title = "choose a songs",filetypes =(("mp3files","*.mp3"),))
    

 
song_listbox = Listbox(window,bg='blue', fg='gray' ,width='60')
song_listbox.pack(pady=20)


btn_backward_img=PhotoImage(file=r"C:/images/backward.png")

btn_forward_img=PhotoImage(file=r"C:/images/forward.png")

btn_play_img=PhotoImage(file=r"C:/images/play.png")

btn_pause_img=PhotoImage(file=r"C:/images/pause.png")

btn_stop_img=PhotoImage(file=r"C:/images/stop.png")


controls_frame=Frame(window)
controls_frame.pack()


#Button

btn_backward=Button(controls_frame,image=btn_backward_img,borderwidth=0)
btn_backward.grid(column = 0 ,row=0,padx=10)

btn_forward=Button(controls_frame,image=btn_forward_img,borderwidth=0)
btn_forward.grid(column = 1,row=0,padx=10)
         
btn_play=Button(controls_frame,image=btn_play_img,borderwidth=0)
btn_play.grid(column = 2,row=0,padx=10)
         
btn_pause=Button(controls_frame,image=btn_pause_img,borderwidth=0)
btn_pause.grid(column = 3, row =0,padx=10)
         
btn_stop=Button(controls_frame,image=btn_stop_img,borderwidth=0)
btn_stop.grid(column = 4, row = 0,padx=10)                                                    

my_menu = Menu(window)
window.config(menu = my_menu)
add_songs_menu = Menu(my_menu)

my_menu.add_cascade(label = "addsongs" ,menu = add_songs_menu)
add_songs_menu.add_command(label = "add 1 song to playlist",command = add_songs)

window.mainloop()
                
