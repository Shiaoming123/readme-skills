# libbase58 0.1.4 — archived fork

[![Version: 0.1.4](https://img.shields.io/badge/version-0.1.4-0969da.svg)](https://github.com/bitcoin/libbase58/blob/b1dd03fa8d1be4be076bb6152325c6b5cf64f678/configure.ac) [![Status: archived](https://img.shields.io/badge/status-archived-6e7781.svg)](https://github.com/bitcoin/libbase58) [![License: MIT](https://img.shields.io/badge/license-MIT-2da44e.svg)](https://github.com/bitcoin/libbase58/blob/b1dd03fa8d1be4be076bb6152325c6b5cf64f678/COPYING)

> **README Skills optimization demo.** This is not an upstream README or a Bitcoin project release. It preserves the complete original API guidance and adds identity, build, lifecycle, and support context for [`bitcoin/libbase58@b1dd03f`](https://github.com/bitcoin/libbase58/tree/b1dd03fa8d1be4be076bb6152325c6b5cf64f678).

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

## Initialisation

Before using libbase58 for Base58Check, provide a SHA-256 function with this signature:

```c
bool my_sha256(void *digest, const void *data, size_t datasz);
```

Assign it to `b58_sha256_impl`:

```c
b58_sha256_impl = my_sha256;
```

This is required only for Base58Check. Raw Base58 does not need SHA-256.

## Decoding Base58

Allocate a buffer for the binary data, initialize a variable with the buffer size, and call:

```c
bool b58tobin(void *bin, size_t *binsz, const char *b58, size_t b58sz);
```

The canonical Base58 byte length is assigned to `binsz` on success and can be larger than the actual buffer when the input has many leading zeroes. The full binary buffer is used regardless of that canonical length. If `b58sz` is zero, it is initialized with `strlen(b58)`; a true zero-length Base58 string is not supported.

## Validating Base58Check

After calling `b58tobin`, validate Base58Check data with:

```c
int b58check(const void *bin, size_t binsz, const char *b58, size_t b58sz);
```

Use the same buffers passed to `b58tobin`. A negative return value means an error occurred; otherwise the value is the Base58Check version byte from the decoded data.

## Encoding Base58

Allocate a string for the Base58 content, initialize a `size_t` with the allocation size, and call:

```c
bool b58enc(char *b58, size_t *b58sz, const void *data, size_t binsz);
```

Pass a pointer to the string-size variable, not the size itself. On return, that variable contains the bytes used, including the null terminator. The function returns `false` on failure or when the output buffer is too small, and `true` on success.

## Encoding Base58Check

Base58Check encoding also requires a version byte:

```c
bool b58check_enc(
    char *b58c,
    size_t *b58c_sz,
    uint8_t ver,
    const void *data,
    size_t datasz
);
```

## Support and license

This archive exposes no verified support or security-fix policy. The fixed snapshot is distributed under the [MIT license](https://github.com/bitcoin/libbase58/blob/b1dd03fa8d1be4be076bb6152325c6b5cf64f678/COPYING); preserve upstream copyright and notices.
