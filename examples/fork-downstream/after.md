# libbase58 0.1.4 — archived fork

> **README Skills showcase rewrite.** This is not an upstream README or a Bitcoin project release. It documents [`bitcoin/libbase58@b1dd03f`](https://github.com/bitcoin/libbase58/tree/b1dd03fa8d1be4be076bb6152325c6b5cf64f678).

C routines for raw Base58 and Base58Check encoding, decoding, and validation.

## Fork and lifecycle status

GitHub records this archived repository as a fork of [`luke-jr/libbase58`](https://github.com/luke-jr/libbase58). The inspected snapshot does not explain why the fork exists, its divergence, or its synchronization policy. Use the parent repository to investigate a maintained source; do not assume compatibility between the two.

[`configure.ac`](https://github.com/bitcoin/libbase58/blob/b1dd03fa8d1be4be076bb6152325c6b5cf64f678/configure.ac) identifies the snapshot as version `0.1.4`.

## Historical build

The fixed [`INSTALL`](https://github.com/bitcoin/libbase58/blob/b1dd03fa8d1be4be076bb6152325c6b5cf64f678/INSTALL) documents:

```bash
./autogen.sh
./configure
make
```

The optional command-line tool depends on libgcrypt. Tests also use `xxd`. This build was not run for the showcase, and current operating-system or compiler compatibility is unknown.

## C API overview

Include [`libbase58.h`](https://github.com/bitcoin/libbase58/blob/b1dd03fa8d1be4be076bb6152325c6b5cf64f678/libbase58.h) and use:

- `b58tobin` to decode Base58;
- `b58enc` to encode Base58;
- `b58check` to validate Base58Check data;
- `b58check_enc` to encode Base58Check data.

Base58Check operations require the caller to provide a SHA-256 implementation through `b58_sha256_impl`. Raw Base58 operations do not.

## Support and license

This archive exposes no verified support or security-fix policy. The fixed snapshot is distributed under the [MIT license](https://github.com/bitcoin/libbase58/blob/b1dd03fa8d1be4be076bb6152325c6b5cf64f678/COPYING); preserve upstream copyright and notices.
