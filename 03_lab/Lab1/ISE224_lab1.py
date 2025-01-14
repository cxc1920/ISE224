import tkinter as tk
from tkinter.colorchooser import askcolor


class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Paint App")
        self.root.geometry("800x600")

        # Default settings
        self.brush_color = "black"
        self.brush_size = 5

        # Create the canvas
        self.canvas = tk.Canvas(self.root, bg="white", width=800, height=500)
        self.canvas.pack(pady=20)

        # Add buttons for controls
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Choose Color", command=self.choose_color).pack(side="left", padx=10)
        tk.Button(button_frame, text="Clear", command=self.clear_canvas).pack(side="left", padx=10)

        size_label = tk.Label(button_frame, text="Brush Size:")
        size_label.pack(side="left", padx=5)

        self.size_slider = tk.Scale(button_frame, from_=1, to=20, orient="horizontal")
        self.size_slider.set(self.brush_size)
        self.size_slider.pack(side="left", padx=5)

        # Bind mouse events for drawing
        self.canvas.bind("<B1-Motion>", self.paint)

    def choose_color(self):
        """Open a color chooser dialog and update the brush color."""
        color = askcolor(color=self.brush_color)[1]
        if color:
            self.brush_color = color

    def clear_canvas(self):
        """Clear the entire canvas."""
        self.canvas.delete("all")

    def paint(self, event):
        """Draw on the canvas based on mouse movement."""
        x, y = event.x, event.y
        brush_size = self.size_slider.get()
        self.canvas.create_oval(
            x - brush_size, y - brush_size, x + brush_size, y + brush_size,
            fill=self.brush_color, outline=self.brush_color
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()
