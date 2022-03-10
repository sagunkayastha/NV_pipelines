
import cv2
import time
# cap =  cv2.VideoCapture("filesrc location=new_video.mp4 ! qtdemux ! h264parse ! avdec_h264 !  videoconvert ! video/x-raw,format=BGR ! appsink ",cv2.CAP_GSTREAMER)
# cap =  cv2.VideoCapture("filesrc location=new_video.mp4 ! qtdemux ! h264parse ! video/x-h264, stream-format=(string)byte-stream, alignment=(string)au ! nvdec ! video/x-raw(memory:GLMemory),format=(string)NV12 ! glcolorconvert ! video/x-raw(memory:GLMemory),format=(string)RGBA ! appsink ",cv2.CAP_GSTREAMER)
# cap =  cv2.VideoCapture("filesrc location=new_video.mp4 ! qtdemux ! h264parse ! video/x-h264, stream-format=(string)byte-stream, alignment=(string)au ! nvdec ! \
#                         video/x-raw(memory:GLMemory),format=(string)NV12 ! autoconvert    ! appsink ",cv2.CAP_GSTREAMER)
# cap =  cv2.VideoCapture("filesrc location=new_video.mp4 ! qtdemux ! h264parse ! avdec_h264 ! videoconvert n-threads=0 ! appsink ",cv2.CAP_GSTREAMER)
cap =  cv2.VideoCapture("filesrc location=new_video.mp4 ! qtdemux ! h264parse !  nvv4l2decoder ! nvvideoconvert ! video/x-raw, format=BGRx ! videoconvert ! video/x-raw,format=BGR ! appsink  ",cv2.CAP_GSTREAMER)
#cap = cv2.VideoCapture("rtspsrc location=rtsp://admin:Admin123@103.235.197.246:554/Streaming/channels/101  latency=100  ! queue ! rtph265depay !  h265parse ! nvv4l2decoder ! nvvideoconvert ! video/x-raw, format=BGRx ! videoconvert ! video/x-raw,format=BGR ! appsink  ",cv2.CAP_GSTREAMER)
#cap = cv2.VideoCapture("rtspsrc location=rtsp://admin:Admin123@103.235.197.246:554/Streaming/channels/101  latency=100  ! queue ! rtph265depay !  h265parse ! avdec_h265 ! videoconvert n-threads=0 ! appsink ",cv2.CAP_GSTREAMER)
#cap =  cv2.VideoCapture("rtspsrc location=rtsp://admin:Admin123@103.235.197.246:554/Streaming/channels/101  latency=100  ! queue ! rtph265depay ! h265parse ! nvdec ! videoconvert ! appsink",cv2.CAP_GSTREAMER)
#cap =  cv2.VideoCapture("rtspsrc location=rtsp://admin:Admin123@103.235.197.246:554/Streaming/channels/101 ! rtph264depay ! h264parse ! vaapih264dec ! videoconvert ! appsink sync=false",cv2.CAP_GSTREAMER)
if cap.isOpened():
    while True:
        a=time.time()
        ret, frame = cap.read()
        b=time.time()
        # cv2.imshow('123',frame)
        # print(frame)
        print(b-a)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # gst-launch-1.0 filesrc location=new_video.mp4 ! qtdemux ! h264parse ! avdec_h264 ! fakesink
        # gst-launch-1.0 filesrc location=new_video.mp4  ! qtdemux ! h264parse ! nvv4l2decoder ! fakesink

        # h264parse ! "video/x-h264, stream-format=(string)byte-stream, alignment=(string)au" ! nvdec ! "video/x-raw(memory:GLMemory),format=(string)NV12" ! glcolorconvert ! "video/x-raw(memory:GLMemory),format=(string)RGBA" ! ..

# gst-launch-1.0 rtspsrc location="rtsp://admin:Admin123@103.235.197.246:554/Streaming/channels/101"  latency=100  ! rtph264depay ! h264parse ! decodebin ! videoconvert ! appsink

### RTSP WITH GST
#cap =  cv2.VideoCapture("rtspsrc location=rtsp://192.168.0.103:8080/h264_ulaw.sdp !  rtph264depay ! h264parse ! nvv4l2decoder ! nvvidconv ! video/x-raw,format=BGRx ! videoconvert ! video/x-raw,format=BGR ! appsink  ",cv2.CAP_GSTREAMER)
