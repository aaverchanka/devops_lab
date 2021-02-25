#!/usr/bin/env python
import psutil
import json
import argparse
from datetime import datetime
import time


class Monitoring:
    # Overall CPU load
    def get_monitor_cpu(self):
        return psutil.cpu_percent(1)

    # Overall memory usage
    def get_monitor_memory(self):
        return psutil.virtual_memory()[2]

    # Overall virtual memory usage
    def get_monitor_swap(self):
        return psutil.swap_memory()[3]

    # IO information
    def get_monitor_io(self):
        io = psutil.disk_io_counters()
        return {
            'io.disks_read': round(io.read_bytes / (1024 * 1024), 2),
            'io.disks_write': round(io.write_bytes / (1024 * 1024), 2)
        }

    # Network information
    def get_monitor_network(self):
        network = psutil.net_io_counters()
        return {
            'network.mb_sent': '%.2fMB' % (network.bytes_sent / 1024 / 1024),
            'network.mb_rec': '%.2fMB' % (network.bytes_recv / 1024 / 1024)
        }

    # Argument parser
    def argument_parser(self):
        parser = argparse.ArgumentParser(description='App which \
                            would monitor the your system/server')
        parser.add_argument('inputs', type=str, help='Input \
        file(.txt or .json)')
        parser.add_argument('minutes', nargs='?', const=5, type=int, default=5, help='Snapshot \
        interval(default 5 minutes)')
        return parser.parse_args()

    # Write info to file
    def write_to_file(self, count_snapshot):
        cpu = self.get_monitor_cpu()
        ram = self.get_monitor_memory()
        swap = self.get_monitor_swap()
        io = self.get_monitor_io()
        network = self.get_monitor_network()
        args = self.argument_parser()
        first_string = '\nSNAPSHOT {0}: \
                TIMESTAMP \
                {1}: '.format(str(count_snapshot), str(datetime.now()))
        second_string = '\nCPU load: {0} '.format(str(cpu))
        third_string = '\nMemory usage: {0} '.format(str(ram))
        fourth_string = '\nVirtual memory usage: {0} '.format(str(swap))
        fifth_string = '\nIO information: {0} '.format(str(io))
        sixth_string = '\nNetwork information: {0} \n'.format(str(network))

        if 'json' in args.inputs:
            with open(args.inputs, 'a') as f:
                json.dump(first_string, f)
                json.dump(second_string, f)
                json.dump(third_string, f)
                json.dump(fourth_string, f)
                json.dump(fifth_string, f)
                json.dump(sixth_string, f)
            f.close()

        elif 'txt' in args.inputs:
            with open(args.inputs, 'a') as t:
                t.write(first_string)
                t.write(second_string)
                t.write(third_string)
                t.write(fourth_string)
                t.write(fifth_string)
                t.write(sixth_string)
            t.close()
        else:
            print("Enter the correct file name. It should be .txt or .json.")

    def start_monitoring(self):
        count_snapshot = 0
        args = self.argument_parser()
        while True:
            count_snapshot += 1
            self.write_to_file(count_snapshot)
            time.sleep(args.minutes * 60)
