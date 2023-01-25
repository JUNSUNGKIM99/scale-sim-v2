import os
import inspect
from scale_config import scale_config as cfg
from topology_utils import topologies as topo
from simulator import simulator as sim
from single_layer_sim import single_layer_sim as layer_sim
from fusion_layer_sim import fusion_layer_sim as fusion_sim


topo_obj = topo()
topo_file = '/home/junsung/work23/develop/scale-sim-v2/topologies/conv_nets/one_layer.csv'

topo_obj.load_arrays(topofile=topo_file, mnk_inputs=False)

