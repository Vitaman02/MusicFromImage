import time
import math
import winsound
import numpy as np
from PIL import Image
from graphics import GraphWin, Rectangle, Entry, Text, Point, color_rgb
from datetime import datetime


def get_note_freq(numbered_note: int):
    if numbered_note == -1:
        return 37
    note = 440*(math.pow(2, 1/12)**(numbered_note))
    return int(note)


def play_note(index: int): 
    freq = get_note_freq(index-1)
    winsound.Beep(freq, 250)


def get_image_path():
    width, height = 300, 150
    win = GraphWin("Image Path", width, height)
    win.setBackground(color_rgb(0, 0, 0))

    path_entry = Entry(Point(width // 2, height // 2 - 50), 30)
    path_entry.draw(win)

    ok_button = Rectangle(Point(width-50, height-50), Point(width-5, height-5))
    ok_button.setFill(color_rgb(255, 255, 255))
    ok_button.draw(win)
    ok_button_text = Text(ok_button.getCenter(), "OK")
    ok_button_text.setSize(15)
    ok_button_text.draw(win)

    while True:
        click = win.getMouse()
        clickx = click.getX()
        clicky = click.getY()

        if ok_button.getP1().getX() <= clickx <= ok_button.getP2().getX() and ok_button.getP1().getY() <= clicky <= ok_button.getP2().getY():
            win.close()
            return str(path_entry.getText())


def main():
    width, height = 500, 500
    
    img_path = get_image_path()
    print(img_path)
    win = GraphWin("Hear your image", width, height)
    win.setBackground(color_rgb(0, 0, 0))

    main_text = Text(Point(width // 2, height // 2), "")
    main_text.setSize(20)
    main_text.setTextColor(color_rgb(255, 255, 255))
    main_text.draw(win)

    img = Image.open(img_path)
    img_width, img_height = img.size

    data = np.asarray(img)

    note_labels = ["Pause", "A4", "A4#", "B4",
                "C5", "C5#", "D5", "D5#",
                "E5", "F5", "F5#", "G5",
                "G5#", "A5", "A5#", "B5",
                "C6", "C6#", "D6", "D6#",
                "E6", "F6", "G6", "G6#"]
    note_freqs = [get_note_freq(freq) for freq in range(-1, len(note_labels)-1)]


    rows_per_note = img_height // 5
    remaining_notes = img_height % 5


    start_time = time.time()
    print("Start time:", start_time)

    count = 0
    total = 0
    for row in data:
        if count == 5:
            new_total = int(total)
            diff = -1
            diffs = []
            for i in range(len(note_freqs)):
                diff = abs(note_freqs[i] - new_total)
                diffs.append(diff)
            minimun = min(diffs)
            index = diffs.index(minimun)
            main_text.setText(note_labels[index])
            play_note(index)
            count = 0
            total = 0
        row_sum = 0
        for pixel in row:
            total = 0
            pixel_sum = 0
            for channel in pixel:
                pixel_sum += channel
            row_sum += pixel_sum
        average_row = row_sum / img_width
        total += round(average_row)
        count += 1


    end_time = time.time() - start_time
    print(f"End time: {datetime.now()}")
    print(f"Elapsed time: {end_time}")


if __name__ == "__main__":
    main()