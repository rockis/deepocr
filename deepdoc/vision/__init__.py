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
import io
import os.path
import sys

import pdfplumber

from .ocr import OCR


def preprocess_inputs(inputs):
    from PIL import Image
    import traceback
    images = []

    def pdf_pages(fnm, zoomin=3):
        nonlocal images
        pdf = pdfplumber.open(fnm)
        images = [p.to_image(resolution=72 * zoomin).annotated for i, p in
                  enumerate(pdf.pages)]

    def images_and_outputs(fnm):
        nonlocal images
        if fnm.split(".")[-1].lower() == "pdf":
            pdf_pages(fnm)
            return
        try:
            fp = open(fnm, 'rb')
            binary = fp.read()
            fp.close()
            images.append(Image.open(io.BytesIO(binary)).convert('RGB'))
        except Exception:
            traceback.print_exc()

    for input in inputs:
        if not os.path.exists(input):
            sys.stderr.write(f"ERROR: No such file or directory: '{input}'")
            sys.exit(1)
        images_and_outputs(input)
    return images

def init_in_out(args):
    from PIL import Image
    import traceback
    images = []

    def pdf_pages(fnm, zoomin=3):
        nonlocal images
        pdf = pdfplumber.open(fnm)
        images = [p.to_image(resolution=72 * zoomin).annotated for i, p in
                            enumerate(pdf.pages)]

    def images_and_outputs(fnm):
        nonlocal images
        if fnm.split(".")[-1].lower() == "pdf":
            pdf_pages(fnm)
            return
        try:
            fp = open(fnm, 'rb')
            binary = fp.read()
            fp.close()
            images.append(Image.open(io.BytesIO(binary)).convert('RGB'))
        except Exception:
            traceback.print_exc()

    images_and_outputs(args.inputs)

    return images, args.inputs


__all__ = [
    "OCR",
    "init_in_out",
]
