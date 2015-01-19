TARGET = rltotiff
OBJS   = rltotiff.o tiff_rgba_io.o

include ../../../Makefile.dir
include ../../../Makefile.config

LDFLAGS := $(LDFLAGS) -ltiff

clean:
	rm -rf $(OBJS) $(TARGET)
