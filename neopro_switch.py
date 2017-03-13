"""
Neopro Borrego+ has an RS232 interface to control the receiver.

Functions can be found on the Neopro website: http://www.neoprointegrator.com/documents/CURRENT_CAT5_Int_Guide.pdf

former name
"__init__.py"
"""

from neopro_commands import CMDS
import serial  # pylint: disable=import-error

DEFAULT_TIMEOUT = 1
DEFAULT_WRITE_TIMEOUT = 1
DEVICE_ID = 'B' #b for borrego

class NeoproSwitch(object):
    """Neopro Switch."""
    def __init__(self, serial_port, timeout=DEFAULT_TIMEOUT,
                 write_timeout=DEFAULT_WRITE_TIMEOUT):
        """Create RS232 connection."""
        self.ser = serial.Serial(serial_port, baudrate=115200, timeout=timeout,
                                 write_timeout=write_timeout)

    def ex_com(self, cmd):

        if not self.ser.is_open:
            self.ser.open()

        self.ser.write(cmd)
        self.ser.read(1)

    def switch_command(self, domain, function, input, output, time):

        if input in CMDS[domain][function]['supported_inputs']:
            if input >= 9 or input < 0:
                raise ValueError('Invalid Input')

        if output in CMDS[domain][function]['supported_outputs']:
            if output >= 9 or output < 0:
                raise ValueError('Invalid Output')

        cmd = '[' + DEVICE_ID + function + ',' +  str(input) + ',' + str(output) + ',' + str(time) + ']'

        return self.ex_com(cmd)

    def switch_av(self, input, output, time):
        """Execute Main.Dimmer."""
        return self.switch_command('switch', 'X', input, output, time)

    def switch_hdv(self, input, output, time):
        """Execute Main.Mute."""
        return self.switch_command('switch', 'V', input, output, time)

    def switch_digital_audio(self, input, output, time):
        """Execute Main.Mute."""
        return self.switch_command('switch', 'D', input, output, time)

    def switch_analog_audio(self, input, output, time):
        """Execute Main.Mute."""
        return self.switch_command('switch', 'A', input, output, time)

    def switch_composite_video(self, input, output, time):
        """Execute Main.Mute."""
        return self.switch_command('switch', 'L', input, output, time)

    # def switch_volume(self, input, output, time):
    #     """Execute Main.Mute."""
    #     return self.exec_command('switch', 'C', input, output, time)

    # def switch_bass_level(self, operator, time):
    #     """Execute Main.Mute."""
    #     return self.exec_command('switch', 'B', input, output, time)

    # def switch_treble(self, operator, time):
    #     """Execute Main.Mute."""
    #     return self.exec_command('switch', 'T',input, output, time)

    def volume_command(self, domain, function, output):
        if output in CMDS[domain][function]['supported_outputs']:
            if output >= 9 or output < 0:
                raise ValueError('Invalid Output')

        cmd = '[' + DEVICE_ID + 'L' + ','  + function + ',' + str(output) + ']'

        return self.ex_com(cmd)

    def volume_mute(self, output):
        return self.volume_command('Volume', "M0", output)

    def volume_partial_mute(self, output):
        return self.volume_command('Volume', "MP", output)

    def volume_up(self, output):
        return self.volume_command('Volume', "U", output)

    def volume_down(self, output):
        return self.volume_command('Volume', "D", output)

    def pwr_on(self):
        cmd = '[P,1]'
        return self.ex_com(cmd)

    def pwr_off(self):
        cmd = '[P,0]'
        return self.ex_com(cmd)

    def audio_switch_state(self):
        cmd = '[?xA]'
        return self.ex_com(cmd)

    def audio_volume_state(self):
        cmd = '[?xL]'
        return self.ex_com(cmd)





