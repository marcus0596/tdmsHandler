import numpy as np
from nptdms import TdmsWriter, RootObject, GroupObject, ChannelObject

root_object = RootObject(properties={
    "Direction": "E",
    "Lane": 'R',
    "Location": 'LA',
    'Sample rate': '0',
    'name': 'test'
})
group_object1 = GroupObject("aux_data", properties={
    "name": 'aux_data',
})

group_object2 = GroupObject('mic_data', properties={
    'name': 'mic_data',
})

timedata = np.array([1.0, 2.0, 3.0, 4.0, 5.0])

with TdmsWriter("my_file.tdms") as tdms_writer:
    # Write first segment
    tdms_writer.write_segment([
        root_object,
        group_object1,
        ChannelObject("aux_data", "time", timedata, properties={})])

    tdms_writer.write_segment([
        root_object,
        group_object1,
        ChannelObject('aux_data', 'distance', [0,0,0,1,2])
    ])
    tdms_writer.write_segment([
        root_object,
        group_object1,
        ChannelObject('aux_data', 'gps', ['$GNGGA','$GNGGA','$GNGGA','$GNGGA','$GNGGA'])
    ])
    # Write another segment with more data for the same channel
    tdms_writer.write_segment([
        root_object,
        group_object2,
        ChannelObject("mic_data", "time", timedata, properties={})
    ])
    tdms_writer.write_segment([
        root_object,
        group_object2,
        ChannelObject("mic_data", "mic1", [0.001,0.001,0.002,.003,.002], properties={})
    ])
    tdms_writer.write_segment([
        root_object,
        group_object2,
        ChannelObject("mic_data", "mic2", [0.001,0.001,0.002,.003,.002], properties={})
    ])
    tdms_writer.write_segment([
        root_object,
        group_object2,
        ChannelObject("mic_data", "mic3", [0.001,0.001,0.002,.003,.002], properties={})
    ])
    tdms_writer.write_segment([
        root_object,
        group_object2,
        ChannelObject("mic_data", "mic4", [0.001,0.001,0.002,.003,.002], properties={})
    ])