from tkinter import Tk, Label, Button, filedialog
from PIL import Image, ImageDraw, ImageFont


def open_image():
    filepath = filedialog.askopenfilename()
    return filepath


def add_watermark(filepath, watermark_text):
    base_image = Image.open(filepath)
    watermark = Image.new("RGBA", base_image.size)
    watermark_draw = ImageDraw.Draw(watermark)

    width, height = base_image.size
    font_size = int(height * 0.05)
    font = ImageFont.truetype("arial.ttf", font_size)

    left, top, right, bottom = watermark_draw.textbbox((0, 0), watermark_text, font=font)
    textwidth = right - left
    textheight = bottom - top

    x = width - textwidth
    y = height - textheight

    watermark_draw.text((x, y), watermark_text, font=font)

    watermarked = Image.alpha_composite(base_image.convert("RGBA"), watermark)

    watermarked.save("watermarked.png", "PNG")


def main():
    root = Tk()
    label = Label(root, text="Select an image to watermark:")
    label.pack()

    open_button = Button(root, text="Open", command=lambda: add_watermark(open_image(), "PanosZermpinos"))
    open_button.pack()

    root.mainloop()


if __name__ == "__main__":
    print('Process Complete!')
    main()
