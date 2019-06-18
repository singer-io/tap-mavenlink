
### Installing the tap:

```
git clone git@github.com:fishtown-analytics/tap-mavenlink.git
cd tap-mavenlink
python3 -m venv env
source env/bin/activate
pip install -e .
```

Be sure to run the `source` command whenever you want to work on this tap.
You'll see `(env)` in your $PROMPT if your virtual environment is activated.


### Running the tap

Use the helper script (`get_catalog.py`) to generate a catalog with all fields selected:

```
./get_catalog.py > catalog.json
```

Re-run this script whenever the JSON Schemas for the Streams have changed (or when new Streams
are added).

```
tap-mavenlink -c config.json --catalog catalog.json > out.json
```

Inspect the results in `out.json`

### Adding Streams

To add a stream, copy an existing stream (like `workspaces.py`), substituting in configuration
values where necessary/appropriate.

Create a corresponding JSON file (with the same name as the stream) in the schemas/ directory.
Aftering adding (or modifying) a JSON Schema, be sure to run the `./get_catalog.py > catalog.json`
script to make your changes take effect!
