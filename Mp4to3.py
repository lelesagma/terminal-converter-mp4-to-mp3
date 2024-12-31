import os
from tkinter import Tk, filedialog
from moviepy.editor import VideoFileClip

def select_mp4_files():
    Tk().withdraw()  
    mp4_files = filedialog.askopenfilenames(title="Sélectionnez des fichiers MP4", filetypes=[("Fichiers MP4", "*.mp4")])
    return mp4_files

def select_output_directory():
    Tk().withdraw()  
    output_directory = filedialog.askdirectory(title="Sélectionnez le dossier de sortie pour les fichiers MP3")
    return output_directory

def convert_mp4_to_mp3(mp4_files, output_directory):
    for mp4_file in mp4_files:
        
        file_name = os.path.splitext(os.path.basename(mp4_file))[0]
        
        mp3_file = os.path.join(output_directory, f"{file_name}.mp3")
        
        
        video = VideoFileClip(mp4_file)
        video.audio.write_audiofile(mp3_file)
        video.close()
        print(f"Converti : {mp4_file} -> {mp3_file}")

if __name__ == "__main__":
    mp4_files = select_mp4_files()
    if mp4_files:
        output_directory = select_output_directory()
        if output_directory:
            convert_mp4_to_mp3(mp4_files, output_directory)
        else:
            print("Aucun dossier de sortie sélectionné.")
    else:
        print("Aucun fichier MP4 sélectionné.")
