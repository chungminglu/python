import json
from org.apache.commons.io import IOUtils
from java.nio.charset import StandardCharsets
from org.apache.nifi.processor.io import StreamCallback

class PyStreamCallback(StreamCallback):
  def __init__(self):
    pass

  def process(self, instream, outstream):
    # To read content as a byte array:
    # data = IOUtils.toByteArray(instream)

    # To read content as a string:
    data = IOUtils.toString(instream, StandardCharsets.UTF_8)

    # Do wordcount
    words = {}
    for word in data.strip().split():
      if word not in words:
        words[word] = 1
      else:
        words[word] += 1

    # Write modified content
    outstream.write(bytearray(json.dumps(words)))
    
flowfile = session.get()
if (flowfile != None):
  # If you need to do something with attributes:
  # myVar = flowfile.getAttribute('filename')

  # To operate on content, setup a callback:
  flowfile = session.write(flowfile, PyStreamCallback())

  # Finish
  session.transfer(flowfile, REL_SUCCESS)