# gmusicapi-scripts — deprecated

> **README Skills showcase rewrite.** This is not an upstream README. It documents [`thebigmunch/gmusicapi-scripts@5492593`](https://github.com/thebigmunch/gmusicapi-scripts/tree/5492593db20efb0ea5ad5dcf1b2e1a0e4d0349e8).

This archived Python package exposed five command-line workflows built on `gmusicapi-wrapper` and `gmusicapi`.

## Use the successor

The project is deprecated in favor of [`thebigmunch/google-music-scripts`](https://github.com/thebigmunch/google-music-scripts). Start there rather than installing this historical snapshot.

No current service availability, authentication flow, dependency compatibility, or safe migration path was verified for this showcase.

## Historical command surface

The fixed [`setup.py`](https://github.com/thebigmunch/gmusicapi-scripts/blob/5492593db20efb0ea5ad5dcf1b2e1a0e4d0349e8/setup.py) registered:

| Command | Source module |
| --- | --- |
| `gmdelete` | `gmusicapi_scripts.gmdelete` |
| `gmdownload` | `gmusicapi_scripts.gmdownload` |
| `gmsearch` | `gmusicapi_scripts.gmsearch` |
| `gmsync` | `gmusicapi_scripts.gmsync` |
| `gmupload` | `gmusicapi_scripts.gmupload` |

The package rejected Python versions earlier than 3.4 and listed Python 3.4/3.5 classifiers. That is historical metadata, not a modern compatibility claim.

## Safety boundary

These commands interacted with an external music service and authentication layer. Some operations could download, upload, synchronize, or delete library data. Review the source and use dry-run behavior where available; do not provide credentials to this archived code based on this example.

See the fixed [`CHANGELOG.md`](https://github.com/thebigmunch/gmusicapi-scripts/blob/5492593db20efb0ea5ad5dcf1b2e1a0e4d0349e8/CHANGELOG.md) for historical behavior changes.

## License

The fixed snapshot includes an [MIT license](https://github.com/thebigmunch/gmusicapi-scripts/blob/5492593db20efb0ea5ad5dcf1b2e1a0e4d0349e8/LICENSE).
