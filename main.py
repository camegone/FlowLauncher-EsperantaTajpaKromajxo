import sys
from pathlib import Path

plugindir = Path.absolute(Path(__file__).parent)
paths = (".", "lib")
sys.path = [str(plugindir / p) for p in paths] + sys.path

from flowlauncher import FlowLauncher
import pyperclip

class EsperantaTajpo(FlowLauncher):
    # TODO: Should load plugin settings
    is_convert_x = True
    is_convert_h = True
    is_convert_cap = True
    is_convert_w = True
    
    def __init__(self):
        super().__init__()
        """
        self.is_convert_x = self.settings.get("is_convert_x", True)
        self.is_convert_h = self.settings.get("is_convert_h", True)
        self.is_convert_cap = self.settings.get("is_convert_cap", True)
        self.is_convert_w = self.settings.get("is_convert_w", True)
        """

    def query(self, query):
        return [
            {
                "Title": "Convert2Esperanto: {}".format(('Your query is: ' + query , query)[query == '']),
                "SubTitle": "Copy Esperanto sentence to clipboard.",
                "IcoPath": "Images/icon.png",
                # "ContextData": ["foo", "bar"]
                "JsonRPCAction": {
                    "method": "convert_epo",
                    "parameters": [query]
                }
            }
        ]
        
    """
    def context_menu(self, data):
        return [
            {
                "title": "Hello World Python's Context menu",
                "subTitle": "Press enter to open Flow the plugin's repo in GitHub",
                "icoPath": "Images/icon.png", # related path to the image
                "jsonRPCAction": {
                    "method": "open_url",
                    "parameters": ["https://github.com/Flow-Launcher/Flow.Launcher.Plugin.HelloWorldPython"]
                },
                "score" : 0
            }
        ]
    """
    
    def convert_epo(self, query):
        str = query
        if (self.is_convert_x):
            # convert x post fixes
            str = str.replace("cx", "ĉ")
            str = str.replace("gx", "ĝ")
            str = str.replace("hx", "ĥ")
            str = str.replace("jx", "ĵ")
            str = str.replace("sx", "ŝ")
            str = str.replace("ux", "ŭ")
            
            str = str.replace("Cx", "Ĉ")
            str = str.replace("Gx", "Ĝ")
            str = str.replace("Hx", "Ĥ")
            str = str.replace("Jx", "Ĵ")
            str = str.replace("Sx", "Ŝ")
            str = str.replace("Ux", "Ŭ")
            
            str = str.replace("CX", "Ĉ")
            str = str.replace("GX", "Ĝ")
            str = str.replace("HX", "Ĥ")
            str = str.replace("JX", "Ĵ")
            str = str.replace("SX", "Ŝ")
            str = str.replace("UX", "Ŭ")
        
        if (self.is_convert_h):
            # convert h post fixes
            str = str.replace("ch", "ĉ")
            str = str.replace("gh", "ĝ")
            str = str.replace("hh", "ĥ")
            str = str.replace("jh", "ĵ")
            str = str.replace("sh", "ŝ")
            # str = str.replace("uh", "ŭ")

            str = str.replace("Ch", "Ĉ")
            str = str.replace("Gh", "Ĝ")
            str = str.replace("Hh", "Ĥ")
            str = str.replace("Jh", "Ĵ")
            str = str.replace("Sh", "Ŝ")
            # str = str.replace("Uh", "Ŭ")

            str = str.replace("CH", "Ĉ")
            str = str.replace("GH", "Ĝ")
            str = str.replace("HH", "Ĥ")
            str = str.replace("JH", "Ĵ")
            str = str.replace("SH", "Ŝ")
            # str = str.replace("UH", "Ŭ")
        
        if (self.is_convert_cap):
            # convert ^ post fixes
            str = str.replace("c^", "ĉ")
            str = str.replace("g^", "ĝ")
            str = str.replace("h^", "ĥ")
            str = str.replace("j^", "ĵ")
            str = str.replace("s^", "ŝ")
            str = str.replace("u^", "ŭ")

            str = str.replace("C^", "Ĉ")
            str = str.replace("G^", "Ĝ")
            str = str.replace("H^", "Ĥ")
            str = str.replace("J^", "Ĵ")
            str = str.replace("S^", "Ŝ")
            str = str.replace("U^", "Ŭ")

        if (self.is_convert_w):
            # convert w
            str = str.replace("w", "ǔ")
            str = str.replace("W", "Ǔ")
        
        pyperclip.copy(str)
        return

# load plugin class
if __name__ == "__main__":
    EsperantaTajpo()
