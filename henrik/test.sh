#gst-launch-1.0 tcamsrc serial=4810628 ! video/x-bayer,format=bggr,width=1024,height=768 ! capssetter join=false caps="video/x-bayer,format=gbrg" ! bayer2rgb ! tee name=t t. ! queue ! videoscale ! video/x-raw,framerate=30/1 ! videoconvert ! ximagesink t. ! queue ! videorate ! video/x-raw,framerate=1/1 ! videoconvert ! jpegenc ! multifilesink location=bilder/frame_%04d.jpg


#gst-launch-1.0 tcamsrc num-buffers=40 serial=4810628 ! video/x-bayer,format=bggr,width=1024,height=768 ! capssetter join=false caps="video/x-bayer,format=gbrg" ! bayer2rgb ! tee name=t t. ! queue ! videoscale ! video/x-raw,framerate=30/1 ! videoconvert ! x264enc ! mp4mux ! filesink location=bilder/faen.mp4 t. ! queue ! videorate ! video/x-raw,framerate=1/1 ! videoconvert ! jpegenc ! multifilesink location=bilder/frame_%04d.jpg


#gst-launch-1.0 -e tcamsrc num-buffers=120 serial=4810628 ! tee name=t t. ! queue ! videoscale ! video/x-raw,width=1024,height=768,framerate=30/1 ! videoconvert ! x264enc ! mp4mux ! filesink location=bilder/test.mp4 t. ! queue ! videorate ! video/x-raw,width=1024,height=768,framerate=1/1 ! videoconvert ! jpegenc ! multifilesink location=bilder/frame_%04d.jpg


#gst-launch-1.0 tcamsrc num-buffers=120 ! tee name=t t. ! video/x-raw,framerate=30/1 ! videoconvert ! x264enc ! mp4mux ! filesink location=bilder/faen.mp4 t. ! videorate ! video/x-raw,framerate=1/1 ! videoconvert ! jpegenc ! multifilesink location=bilder/frame_%04d.jpg


#gst-launch-1.0 tcamsrc name=src ! queue max_size_buffers=2 ! videoconvert ! capsfilter caps="video/x-raw,format=BGRx" ! videoconvert ! gtksink name=sink

gst-launch-1.0 tcamsrc num-buffers=30 name=src ! tee name=t t. ! videoconvert ! jpegenc ! multifilesink location=bilder/frame_%04d.jpg t. ! videoconvert ! x264enc ! mp4mux ! filesink location=bilder/test.mp4
