from contextlib import contextmanager


# ensure we switch the device off if the program exits unexpectedly

@contextmanager
def manage(pump):

 pump.off()
 yield pump
 pump.off()