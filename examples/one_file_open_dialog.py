import webview

window = None
def on_loaded():
    window.show()
    window.create_file_dialog(dialog_type=webview.OPEN_DIALOG, file_types="Python files (*.py)")

window = webview.create_window('Hello world', 'https://pywebview.flowrl.com/hello', hidden=True)
window.events.loaded += on_loaded
webview.start()