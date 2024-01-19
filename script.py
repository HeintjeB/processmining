#script.py

#import packages
import pandas as pd
from random import randint
from faker import Faker
from datetime import timedelta, date
from WatsonExplorer import Explorer

fake = Faker()

# function for creating a dataset
def creating_manufacturing_flow(
    filepath,
    happy_flow_qty,
    min_deviation_qty,
    max_deviation_qty,
    process_flow_df=pd.DataFrame(),
    case_number=0,
):
    with open(filepath, "r") as file:
        for idx, line in enumerate(file):
            raw_process_flow_list = line.split(",")
            process_flow_list = [
                word.replace("\n", "") for word in raw_process_flow_list
            ]
            key = ["case", "process", "timestamp"]
            items = [[] for _ in range(len(process_flow_list) + 1)]
            process_dictionary = dict(zip(key, items))
            if idx == 0:
                last_number = happy_flow_qty
            else:
                last_number = randint(min_deviation_qty, max_deviation_qty)
            for i in range(0, last_number):
                for index, process in enumerate(process_flow_list):
                    process_dictionary["case"].append(case_number)
                    process_dictionary["process"].append(process)
                    if index == 0:
                        fake_date = fake.date_between(
                            start_date=date(2024, 1, 17), end_date=date(2024, 3, 10)
                        )
                        process_dictionary["timestamp"].append(fake_date)
                    else:
                        fake_date = fake_date + timedelta(randint(1, 10))
                        process_dictionary["timestamp"].append(fake_date)
                case_number += 1
            temp_df = pd.DataFrame(process_dictionary)
            process_flow_df = pd.concat([process_flow_df, temp_df])
    process_flow_df = process_flow_df.fillna("").reset_index(drop=True)
    return process_flow_df