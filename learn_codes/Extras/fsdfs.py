import pyaudio
soundObj = pyaudio.PyAudio()

# Learn what your OS+Hardware can do
defaultCapability = soundObj.get_default_host_api_info()
print(defaultCapability)

# See if you can make it do what you want
isSupported = soundObj.is_format_supported(input_format=pyaudio.paInt8, input_channels=1, rate=22050, input_device=0)
print(isSupported)