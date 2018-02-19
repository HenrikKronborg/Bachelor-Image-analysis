#gst-launch-1.0 tcamsrc serial=4810628 ! video/x-bayer,format=bggr,width=1024,height=768 ! capssetter join=false caps="video/x-bayer,format=gbrg" ! bayer2rgb ! tee name=t t. ! queue ! videoscale ! video/x-raw,framerate=30/1 ! videoconvert ! ximagesink t. ! queue ! videorate ! video/x-raw,framerate=1/1 ! videoconvert ! jpegenc ! multifilesink location=bilder/frame_%04d.jpg


#gst-launch-1.0 tcamsrc num-buffers=40 serial=4810628 ! video/x-bayer,format=bggr,width=1024,height=768 ! capssetter join=false caps="video/x-bayer,format=gbrg" ! bayer2rgb ! tee name=t t. ! queue ! videoscale ! video/x-raw,framerate=30/1 ! videoconvert ! x264enc ! mp4mux ! filesink location=bilder/faen.mp4 t. ! queue ! videorate ! video/x-raw,framerate=1/1 ! videoconvert ! jpegenc ! multifilesink location=bilder/frame_%04d.jpg

#gst-launch-1.0 tcamsrc num-buffers=60 ! video/x-bayer,format=bggr,width=1024,height=768,framerate=30/1 ! capssetter join=false caps="video/x-bayer,format=gbrg" ! bayer2rgb ! tee name=t t. ! queue max-size-buffers=1000 max-size-bytes=20000000 ! videoscale ! video/x-raw,framerate=30/1 ! videoconvert ! x264enc rc-lookahead=10 tune=4 ! mp4mux ! filesink location=bilder/test.mp4 t. ! queue max-size-buffers=1000 max-size-bytes=20000000 ! videorate ! video/x-raw,framerate=1/1 ! videoconvert ! jpegenc ! multifilesink location=bilder/frame_%04d.jpg


###################3

#gst-launch-1.0 v4l2src device=/dev/video1 ! 'video/x-raw, width=1024, height=768, format=bggr, framerate=30/1' ! nvvidconv ! 'video/x-raw(memory:NVMM), width=1024, height=768, format=NV12' ! nvtee ! nvivafilter cuda-process=true pre-process=true post-process=true customer-lib-name="libnvsample_cudaprocess.so" ! 'video/x-raw(memory:NVMM), format=(string)NV12' ! nvoverlaysink display-id=0 -e

#gst-launch-1.0 nvcamerasrc fpsRange="30 30" ! 'video/x-raw(memory:NVMM), width=(int)3840, height=(int)2160, format=(string)I420, framerate=(fraction)30/1' ! nvtee ! nvivafilter cuda-process=true customer-lib-name="libsample_process.so" ! 'video/x-raw(memory:NVMM), format=(string)NV12' ! nvoverlaysink -e

#gst-launch-1.0 nvcamerasrc fpsRange="30 30" ! 'video/x-raw(memory:NVMM), width=(int)3840, height=(int)2160, format=(string)I420, framerate=(fraction)30/1' ! nvtee ! nvivafilter cuda-process=true customer-lib-name="libsample_process.so" ! 'video/x-raw(memory:NVMM), format=(string)NV12' ! nvoverlaysink -e


gst-launch-1.0 tcamsrc serial=4810628 ! video/x-bayer,format=bggr,width=1024,height=768,framerate=30/1 ! capssetter join=false caps="video/x-bayer,format=gbrg" ! bayer2rgb ! videoconvert ! nvoverlaysink
