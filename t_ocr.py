#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

import os
import sys
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(
                os.path.abspath(__file__)),
            '../../')))

from deepdoc.vision.seeit import draw_box
from deepdoc.vision import OCR, preprocess_inputs
import numpy as np


def main(inputs):
    ocr = OCR()
    images = preprocess_inputs(inputs)

    for i, img in enumerate(images):
        bxs = ocr(np.array(img))
        bxs = [(line[0], line[1][0]) for line in bxs]
        bxs = [{
            "text": t,
            "bbox": [b[0][0], b[0][1], b[1][0], b[-1][1]],
            "type": "ocr",
            "score": 1} for b, t in bxs if b[0][0] <= b[1][0] and b[0][1] <= b[-1][1]]
        print("\n".join([o["text"] for o in bxs]))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.stderr.write(f"USAGE: {sys.argv[0]} <filename1> [filename2 [filename3 ...]]\n")
        sys.exit(1)
    main(sys.argv[1:])
