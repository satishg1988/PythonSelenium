class ScreenShots:
    def captureScreenShots(self):
        filename_screenshot = str("--testscreenshot.png")
        directory_screenshot = "E:/PycharmProjects/PythonSelenium/allscreenshots"
        destinationfile_screenshot = directory_screenshot + filename_screenshot
        self.driver.save_screenshot(destinationfile_screenshot)
        print("Screenshot saved successfully in:" + str(destinationfile_screenshot))