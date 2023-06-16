import webview

window = None
def on_loaded():
    print('loaded')
    window.show()

window = webview.create_window('Hello world', 'https://pywebview.flowrl.com/hello', hidden=True)
window.events.loaded += on_loaded
webview.start()