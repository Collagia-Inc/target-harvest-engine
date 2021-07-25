import os
import sys
import json

import pytest
from jsonschema import ValidationError
from target_harvest_engine.target import TargetHarvestEngine


def load_stream(filename: str):
    stream = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "data_files", f'{filename}.stream')
    with open(stream) as f:
        return f.readlines()


def test_target_harvest_engine_missing_required_property(sample_config):
    test_stream = "missing_property_example"

    sys.stdin = load_stream(test_stream)
    with pytest.raises(ValidationError) as e:
        TargetHarvestEngine(sample_config).listen()
    assert "'uri' is a required property" in str(e.value)


def test_target_harvest_engine_type_mismatch(sample_config):
    test_stream = "type_mismatch_example"

    sys.stdin = load_stream(test_stream)
    with pytest.raises(ValidationError) as e:
        TargetHarvestEngine(sample_config).listen()
    assert "Failed validating 'type' in schema" in str(e.value)


def test_target_harvest_engine(sample_config, mock_response):
    test_stream = "example"
    test_payload = {
        "uri": "s3://test-bucket/test_path/test_image.png",
        "source_id": "1",
        "ordinal": 1,
        "connection_id": "abc123"
    }

    sys.stdin = load_stream(test_stream)
    TargetHarvestEngine(sample_config).listen()
    assert mock_response.assert_call_count(
        "http://localhost/image_objects", 3) is True
    assert json.loads(mock_response.calls[0].request.body.decode(
        'utf-8')) == test_payload
