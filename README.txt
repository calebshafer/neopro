
Purpose is to control a neopro borrego+ 8x8 matrix switch
If it works should work with other neopro devices
orignal software that was modified by joobert
https://github.com/joopert/nad_receiver

UNTESTED. As of know

NeoproSwitch.FUNCTION()

FUNCTIONS
switch_av(input, output, time):
switch_hdv(input, output, time):
switch_digital_audio(input, output, time):
switch_analog_audio(input, output, time):
switch_composite_video(input, output, time):

volume_mute(output):
volume_partial_mute(output):
volume_up(output):
volume_down(output):
pwr_on():
def pwr_off():
def audio_switch_state(self):
def audio_volume_state(self):
