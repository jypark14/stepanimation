import stepAnimation

def staticSquareAnimation(canvas, width, height, step):
    left = 0
    canvas.create_rectangle(left, 0, left+20, 20, fill="blue")

stepAnimation.run(staticSquareAnimation)
