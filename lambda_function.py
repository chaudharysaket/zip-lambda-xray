from aws_xray_sdk.core import xray_recorder

def lambda_handler(event, context):
    # ... some code

    subsegment = xray_recorder.begin_subsegment('subsegment_name')
    # Code to record
    # Add metadata or annotation here, if necessary
    subsegment.put_metadata('key', dict, 'namespace')
    subsegment.put_annotation('key', 'value')

    xray_recorder.end_subsegment()

    # ... some other code
    return True