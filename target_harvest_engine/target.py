from singer_sdk.target_base import Target
from singer_sdk import typing as th

from target_harvest_engine.sinks import (
    HarvestEngineSink,
)


class TargetHarvestEngine(Target):
    name = "target-harvest-engine"
    config_jsonschema = th.PropertiesList(
        th.Property("api_url", th.StringType, required=True),
        th.Property("connection_id", th.StringType, required=True),
    ).to_dict()
    default_sink_class = HarvestEngineSink
