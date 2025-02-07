import pandas as pd

def merge_fraud_ip_address_data(fraud_data,ip_address_country):
    fraud_data = fraud_data.sort_values('ip_address')
    ip_address_country = ip_address_country.sort_values('lower_bound_ip_address')
    merged_fraud_data = pd.merge_asof(
        fraud_data, 
        ip_address_country, 
        left_on='ip_address', 
        right_on='lower_bound_ip_address', 
        direction='backward'
    )
    merged_fraud_data = merged_fraud_data[
        (merged_fraud_data['ip_address'] >= merged_fraud_data['lower_bound_ip_address']) & 
        (merged_fraud_data['ip_address'] <= merged_fraud_data['upper_bound_ip_address'])
    ]
    return merged_fraud_data