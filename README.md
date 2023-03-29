# pdl-cts-server

A CTS server for the Persian Digital Library (PDL) project.

## Setup

```sh
# create virtual environment
python3 -m venv venv
source venv/bin/activate # in fish: source venv/bin/activate.fish

# install `capitains-nautilus` from submodule in `./Nautilus`
python -m pip install -e Nautilus/ # this also installs all needed dependencies from `requirements.txt`
```

Currently, we are using a submodule in `./Nautilus` for a local version of `capitains-nautilus`, see https://github.com/Capitains/Nautilus/issues/95.

I created the file `working_requirements.txt` using `python -m pip freeze > working_requirements.txt` to show which exact version combination is working.

## Run server

```sh
source venv/bin/activate # in fish: source venv/bin/activate.fish
python app.py
```

Now we can run queries against the CTS server to explore the corpus.

## Examples queries

**Query all capabilities: GetCapabilities**

```sh
curl "http://localhost:8000/cts?request=GetCapabilities"
```

**Query a passage from a certain URN: GetPassage**

```sh
curl "http://localhost:8000/cts?request=GetPassage&urn=urn:cts:perslit:forooghi.divan"
curl "http://localhost:8000/cts?request=GetPassage&urn=urn:cts:perslit:attar.mokhtarname"
```

**Query Valid Reff**

```sh
curl "http://localhost:8000/cts?request=GetValidReff&urn=urn:cts:perslit:forooghi.divan"
curl "http://localhost:8000/cts?request=GetValidReff&urn=urn:cts:perslit:attar.mokhtarname"
```

\*\*Query First URN that belongs to given URN

**Other Queries**

- `GetFirstUrn`: `curl "http://localhost:8000/cts?request=GetFirstUrn&urn=urn:cts:perslit:attar.mokhtarname"`
- `GetLabel`: `curl "http://localhost:8000/cts?request=GetLabel&urn=urn:cts:perslit:attar.mokhtarname"`
- `GetPrevNextUrn` and `GetPassagePlus` are currently not supported, see #1.

## Further Reading

- [CTS](http://cts.informatik.uni-leipzig.de/Canonical_Text_Service.html)
- [CTS URN Specification](https://github.com/cite-architecture/ctsurn_spec)
- [Persian Digital Library (PDL)](https://persdigumd.github.io/PDL/)
- This project was inspired by [CDLI Text Services](https://github.com/cdli-gh/cdli-cts-server) for the [Cuneiform Digital Library Collective](https://cdli.mpiwg-berlin.mpg.de/).

## Development / Next steps

- [ ] Set up a Nemo UI, see [docs](https://flask-capitains-nemo.readthedocs.io/en/latest/).
- [ ] Expand PDL dataset with all data from Ganjoor, see https://github.com/PersDigUMD/PDL/issues/1 and https://github.com/PersDigUMD/PDL/issues/2.
