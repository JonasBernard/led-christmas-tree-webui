def get_adapter():
    adapter = None

    try:
        from gpiozero import SPIDevice
        from adapters.pi import PiAdapter

        adapter = PiAdapter()
    except:
        print("The package gpiozero was not found. Assuming the server is not running on a pi.")
        print("If this is running on a Raspberry pi, install by:")
        print("")
        print("sudo apt install python3-gpiozero")

        from adapters.dummy import DummyAdapter

        adapter = DummyAdapter()

    return adapter