import pyautogui
# Take a screenshot of the screen
screenshot = pyautogui.screenshot()
# Get the color of a pixel at a specific location
pixel_color = screenshot.getpixel((x, y))
# Iterate over the pixels on the screenshot
for x in range(screenshot.width):
    for y in range(screenshot.height):
        # Get the color of the current pixel
        pixel_color = screenshot.getpixel((x, y))

        # Check if the pixel matches the color of the image
        if pixel_color == (255, 0, 0):
            # Move the mouse to the location of the pixel
            pyautogui.moveTo(x, y)
# Search for the image on the screen
image_loc = pyautogui.locateOnScreen('demonShield.png')

# Check if the image was found on the screen
if image_loc is not None:
    # Move the mouse to the location of the image
    pyautogui.moveTo(image_loc[0], image_loc[1])
