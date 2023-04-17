#!/Users/frankhansen/.pyenv/shims/python

name: netif_rx
ID: 1183
format:
	field:unsigned short common_type;         offset:0; size:2; signed:0;
	field:unsigned char common_flags;         offset:2; size:1; signed:0;
	field:unsigned char common_preempt_count; offset:3; size:1; signed:0;
	field:int common_pid;                     offset:4; size:4; signed:1;

	field:void * skbaddr;         offset:8;  size:8; signed:0;
	field:unsigned int len;       offset:16; size:4; signed:0;
	field:__data_loc char[] name; offset:20; size:4; signed:1;

print fmt: "dev=%s skbaddr=%p len=%u", __get_str(name), REC->skbaddr, REC->len

# coding: utf-8

from socket import inet_ntop
from bcc import BPF
import ctypes as ct

bpf_text = '''<SEE CODE SNIPPET ABOVE>'''

TASK_COMM_LEN = 16 # linux/sched.h

class RouteEvt(ct.Structure):
    _fields_ = [
        ("comm",    ct.c_char * TASK_COMM_LEN),
    ]

def event_printer(cpu, data, size):
    # Decode event
    event = ct.cast(data, ct.POINTER(RouteEvt)).contents

    # Print event
    print "Just got a packet from %s" % (event.comm)

if __name__ == "__main__":
    b = BPF(text=bpf_text)
    b["route_evt"].open_perf_buffer(event_printer)

    while True:
        b.kprobe_poll()
