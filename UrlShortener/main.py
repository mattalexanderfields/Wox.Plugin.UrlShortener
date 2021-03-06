# encoding=utf8

from wox import Wox, WoxAPI
from UrlShortener import ClsShortener
import pyperclip

class UShort(Wox):

    def query(self, key):
        mShortener = ClsShortener()
        res_url = mShortener.update_url(key)
        #os.system("echo '%s' | pbcopy" % res_url)
        results = []
        results.append({
            "Title": "Context menu entry",
            "SubTitle": "Data: {}".format(res_url),
            "IcoPath":"Images/app.ico",
			"JsonRPCAction": {
                        "method": "copy_to",
                        "parameters": [res_url],
                        "dontHideAfterAction": True}
        })
        return results

    def copy_to(self,data):
        pyperclip.copy(data)
        WoxAPI.change_query(data)


if __name__ == "__main__":
    UShort()