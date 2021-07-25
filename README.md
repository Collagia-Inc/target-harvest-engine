# target-harvest-engine

`target-harvest-engine` is a Singer target for [HarvestEngine](https://gitlab.com/collagia/collagia-info/-/wikis/Collagia/Data-Processing-Services/Harvest-Engine) built with the [Meltano Target SDK](https://sdk.meltano.com).

## Configuration

```
{
  "api_url": "http://localhost/image_objects",
  "connection_id": "abc123"
}
```

### Accepted Config Options

A full list of supported settings and capabilities for this
target are available by running:

```bash
target-harvest-engine --about
```

### Source Authentication and Authorization

Currently there is no authentication and authorization required by the HarvestEngine.

## Usage

You can easily run `target-harvest-engine` by itself or in a pipeline using [Meltano](www.meltano.com).

### Executing the Target Directly

```bash
target-harvest-engine --version
target-harvest-engine --help
# Test using the "Carbon Intensity" sample:
tap-carbon-intensity | target-harvest-engine --config /path/to/target-harvest-engine-config.json
```

### Initialize your Development Environment

```bash
pipx install poetry
poetry install
```

### Create and Run Tests

Create tests within the `target_harvest_engine/tests` subfolder and
then run:

```bash
poetry run pytest
```

You can also test the `target-harvest-engine` CLI interface directly using `poetry run`:

```bash
poetry run target-harvest-engine --help
```

### Testing with [Meltano](meltano.com)

_**Note:** This target will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

Your project comes with a custom `meltano.yml` project file already created. Open the `meltano.yml` and follow any _"TODO"_ items listed in
the file.

Next, install Meltano (if you haven't already) and any needed plugins:

```bash
# Install meltano
pipx install meltano
# Initialize meltano within this directory
cd target-harvest-engine
meltano install
```

Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke target-harvest-engine --version
# OR run a test `elt` pipeline with the Carbon Intensity sample tap:
meltano elt tap-carbon-intensity target-harvest-engine
```

### SDK Dev Guide

See the [dev guide](../../docs/dev_guide.md) for more instructions on how to use the Meltano SDK to
develop your own Singer taps and targets.
