"""
Commands and operators used by Neopro Borrego+ and other devices.

CMDS[domain][function]
"""
CMDS = {
    'switch': #
        {
            'X': #AV
                {'cmd': 'Switch.AV',
                 'supported_inputs': [0,1,2,3,4,5,6,7,8],
                 'supported_outputs': [0,1,2,3,4,5,6,7,8]
                 },
            'V':
                {'cmd': 'Switch.HDV',
                 'supported_inputs': [0,1,2,3,4,5,6,7,8],
                 'supported_outputs': [0,1,2,3,4,5,6,7,8]
                 },
            'D':
                {'cmd': 'Switch.Digital_Audio',
                 'supported_inputs': [0,1,2,3,4,5,6,7,8],
                 'supported_outputs': [0,1,2,3,4,5,6,7,8]
                 },
            'A':
                {'cmd': 'Switch.Analog_Audio',
                 'supported_inputs': [0,1,2,3,4,5,6,7,8],
                 'supported_outputs': [0,1,2,3,4,5,6,7,8]
                 },
            'C':
                {'cmd': 'Switch.Composite_Video',
                 'supported_inputs': [0,1,2,3,4,5,6,7,8],
                 'supported_outputs': [0,1,2,3,4,5,6,7,8]
                 },

            # 'B':
            #     {'cmd': 'Switch.Bass_Level',
            #      'supported_operators': ['+', '-']
            #      },
            # 'T':
            #     {'cmd': 'Switch.Treble_Level',
            #      'supported_operators': ['+', '-', '=', '?']
            #      },

        },
    'Volume': #
        {
            'MO': #AV
                {'cmd': 'Volume.Mute',
                 'supported_outputs': [0,1,2,3,4,5,6,7,8]
                 },
            'MP': #AV
                {'cmd': 'Volume.Partial_Mute',
                 'supported_outputs': [0,1,2,3,4,5,6,7,8]
                 },
            'U': #AV
                {'cmd': 'Volume.Up',
                 'supported_outputs': [0,1,2,3,4,5,6,7,8]
                 },
            'D': #AV
                {'cmd': 'Volume.Down',
                 'supported_outputs': [0,1,2,3,4,5,6,7,8]
                 },


        }
}