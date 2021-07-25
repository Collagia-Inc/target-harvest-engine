from singer_sdk.sinks import RecordSink
from target_harvest_engine.client import HarvestEngineAPI


class HarvestEngineSink(RecordSink):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._he_client = None

    @property
    def he_client(self) -> HarvestEngineAPI:
        if not self._he_client:
            self._he_client = HarvestEngineAPI(self.config)
        return self._he_client

    def _create_payload(self, record):
        record["connection_id"] = self.config["connection_id"]
        return record

    def process_record(self, record: dict, context: dict) -> None:
        payload = self._create_payload(record)
        self.he_client.post(payload)
