import argparse

from scale_sim import scalesim

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
    fusion_flag = False
    
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
                 input_type_gemm=gemm_input,
                 layer_fusion=False)
    s.run_scale(top_path=logpath)
