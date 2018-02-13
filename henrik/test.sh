#gst-launch-1.0 tcamsrc serial=4810628 ! video/x-bayer,format=bggr,width=1024,height=768 ! capssetter join=false caps="video/x-bayer,format=gbrg" ! bayer2rgb ! tee name=t t. ! queue ! videoscale ! video/x-raw,framerate=30/1 ! videoconvert ! ximagesink t. ! queue ! videorate ! video/x-raw,framerate=1/1 ! videoconvert ! jpegenc ! multifilesink location=bilder/frame_%04d.jpg


gst-launch-1.0 tcamsrc serial=4810628 ! video/x-bayer,format=bggr,width=1024,height=768 ! capssetter join=false caps="video/x-bayer,format=gbrg" ! bayer2rgb ! tee name=t t. ! queue ! video/x-raw,framerate=30/1 ! videoconvert ! x264enc ! mp4mux ! filesink location=bilder/a.mp4 t. ! queue ! videorate ! video/x-raw,framerate=1/1 ! videoconvert ! jpegenc ! multifilesink location=bilder/frame_%04d.jpg
