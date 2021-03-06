# SecureImage Solver

Uses convolutional neural networks to solve CAPTCHA images generated by
[SecureImage](https://www.phpcaptcha.org/) library in php with an accuracy of 90%.
Bits and pieces taken from [Patrick Li's project.](https://github.com/PatrickLib/captcha_recognize)

## Requirements

- Python 3.5-3.7 (64-bit)
- pip 19.0 or later
- Ubuntu 16.04 or later (64-bit)
- macOS 10.12.6 (Sierra) or later (64-bit) (no GPU support)
- Windows 7 or later (64-bit) (Python 3 only)
- Raspbian 9.0 or later

## Usage

Clone/Download the repository & install by running `python setup.py install`

* Get solution for an image.
  ```python
  import captcha_api
  captcha_api.predict('/path/to/image.png')
  ```

* Generate random images for testing.

  ```
  $> php securimage_solver/secureimage_show.php
  ```

#### Examples of CAPTCHAs that have been successfully solved:

[![Image1](images/7NwHCn_141c1458-b5e4-439f-be01-8a8b30c6cbd8.png)]()
[![Image2](images/kLSF7y_dc083c8e-d116-4448-a938-6e3516205d01.png)]()


[![Image3](images/z6brnd_4166a5cd-d98a-4099-9b86-4d13dbd100c5.png)]()
[![Image4](images/A8MZBV_472d2d51-84e0-442a-a278-83df5fa8e238.png)]()

# License

The mighty MIT license. Check [License](LICENSE) file for more info.
