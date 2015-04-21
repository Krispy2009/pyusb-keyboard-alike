from keyboard_alike import reader


class BarCodeReader(reader.Reader):
    """
    This class supports Newland 2D Barcode Scanner (NLS-HR32)
    """
    pass


if __name__ == "__main__":
    reader = BarCodeReader(0x1eab, 0x0003, 84, 8, should_reset=True)
    reader.initialize()
    print(reader.read().strip())
    reader.disconnect()
