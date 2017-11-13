import json
import java.io
from org.apache.commons.io import IOUtils
from java.nio.charset import StandardCharsets
from org.apache.nifi.processor.io import StreamCallback
from org.apache.nifi.processor.exception import ProcessException

class PPutfile(StreamCallback):
    def __init__(self):
        pass
    def process(self,inputStream,outputStream):
        text = IOUtils.toString(inputStream,StandardCharsets.UTF_8)
        f.write(text)

flowfile = session.get()

try:
    if (flowfile != None):
        # 從flowfile取得檔案名稱
        filename = flowfile.getAttribute("filename")
        f = open("d:/tmp/" + filename,"a+")

        flowfile = session.write(flowfile,PPutfile())
        f.close()

    session.transfer(flowfile, REL_SUCCESS)
except:
    ProcessException