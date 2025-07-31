import sys, os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

# Optional: Fix Windows Chromium sandbox issue
os.environ["QTWEBENGINE_CHROMIUM_FLAGS"] = "--no-sandbox"

class DiscordWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Discord")
        self.setGeometry(100, 100, 1200, 800)

        browser = QWebEngineView()
        browser.load(QUrl("https://discord.com/app"))  # Loads Discord Web
        self.setCentralWidget(browser)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DiscordWindow()
    window.show()
    sys.exit(app.exec_())
