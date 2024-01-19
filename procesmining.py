#process_mining.py

import pandas as pd
import pm4py
from script import creating_manufacturing_flow

process_flow_df = creating_manufacturing_flow("process_flow.txt", 565, 10, 150)

event_log = pm4py.format_dataframe(
    process_flow_df,
    case_id="case",
    activity_key="process",
    timestamp_key="timestamp",
    timest_format="%Y-%m-%d",
)

net = pm4py.discover_heuristics_net(event_log)
pm4py.view_heuristics_net(net)