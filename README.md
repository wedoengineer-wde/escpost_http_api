#  ESCPOS HTTP API

A simple wrapper for the library [python-escpos ]( https://github.com/python-escpos/python-escpos )

## Usage

### Installation 

1. Get printer `idVendor` and `idProduct` with `lsusb`
    ```
    Bus 003 Device 008: ID 0483:5743 STMicroelectronics USB Printer P
    ```
    in this case the `idVendor` is `0x0483` and `idProduct` is `0x5743`

2. Modify `install.sh` script setting the respective parameters

    ```
    echo 'SUBSYSTEMS=="usb", ATTRS{idVendor}=="0483" , GROUP="plugdev" , MODE="0666"' > /etc/udev/rules.d/50-myusb.rules
    ```

3. Execute the script as sudo. This will give the necessary permissions to use the printer 
    ```
    sudo ./install.sh
    ```  

4. Modify the file named `settings.json` with the idVendor and idProduct. You can edit another parameters as the port and host of the flask application

5. Install python requeriments 

    ```
    pip install flask pytest python-escpos 
    ```

### Deploy

For the instance you can deploy it as a debug mode. 

``` 
python3 main.py
```

### Endpoints

We have developped two basic apis

1. Print

``` HTTP
POST http://{{host}}/print HTTP/1.1
content-type: {{contentType}}

{
    "text": "this is the text \n to print!!"
}
```

2. Cut

``` HTTP
POST http://{{host}}/cut HTTP/1.1
content-type: {{contentType}}

{
}

```

## License

MIT