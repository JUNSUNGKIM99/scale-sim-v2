import argparse
import numpy as np 
import matplotlib.pyplot as plt 

from scalesim.utilities.scalesim_report import ScalesimReport as reporter
from scale_sim import scalesim


def plot_stacked_bar(x, y_series_np, legends, title, y_axis_label=''):
    num_plots = y_series_np.shape[0]
    plt.bar(x, y_series_np[0], label=legends[0])
    bottom = y_series_np[0]
    for plt_id in range(1, num_plots):
        plt.bar(x, y_series_np[plt_id], bottom=bottom,label=legends[plt_id])
        bottom += y_series_np[plt_id]

    plt.ylabel(y_axis_label)
    plt.title(title)
    plt.xticks(rotation=80)
    plt.legend()

    plt.show()

def compare_dataflow():
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', metavar='Topology file', type=str,
                        default="../topologies/conv_nets/test.csv",
                        help="Path to the topology file"
                        )
    parser.add_argument('-c', metavar='Config file', type=str,
                        default="../configs/scale.cfg",
                        help="Path to the config file"
                        )
    parser.add_argument('-p', metavar='log dir', type=str,
                        default="../test_runs",
                        help="Path to log dir"
                        )
    parser.add_argument('-i', metavar='input type', type=str,
                        default="conv",
                        help="Type of input topology, gemm: MNK, conv: conv"
                        )
    parser.add_argument('--save_trace', metavar='Save trace per layer', type=str,
                        default="True",
                        help="Save disk space for trace files per layer"
                        )

    args = parser.parse_args()
    topology = args.t
    config = args.c
    logpath = args.p
    inp_type = args.i
    trace_flag = args.save_trace
    
    if trace_flag == 'True':
        trace_flag = True
    else:
        trace_flag = False

    gemm_input = False
    if inp_type == 'gemm':
        gemm_input = True

    s = scalesim(save_disk_space=trace_flag, verbose=True,
                 config=config,
                 topology=topology,
                 input_type_gemm=gemm_input
                 )
    s.run_scale(top_path=logpath)
