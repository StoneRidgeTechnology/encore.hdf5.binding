# module::encore.hdf5.binding  [![status](https://github.com/Wandalen/encore.hdf5.binding/workflows/publish/badge.svg)](https://github.com/Wandalen/encore.hdf5.binding/actions?query=workflow%3Apublish) [![stability-experimental](https://img.shields.io/badge/stability-experimental-orange.svg)](https://github.com/emersion/stability-badges#experimental)

This is binding for [HDF5](https://www.hdfgroup.org/HDF5/).

## About the fork

This is [fork](https://github.com/HDF-NI/hdf5.node), which is created to provide prebuild versions and fix issues of the original implementation.

## Support

Node versions:
* v13
* v14

HDF5 versions:
* v1.10.x
* v1.8.x

## How to add to your project

```bash
npm add encore.hdf5.binding@delta
```

This installation method assumes that you have hdf5 library installed at default path.

## Default path to HDF5 library

The module expects that hdf5 library is installed at:

| Platform |       Path       |
| :------  | :--------------  |
|  Linux   |    /usr/local    |
| Windows  | C:/Software/hdf5 |
|   Mac    |    /usr/local    |

## How to provide custom path to HDF5 library

If your native hdf5 library is not located on default path you can set the path with a switch on this project as well as
dependent projects:

On Linux:

```bash
npm add encore.hdf5.binding@delta --hdf5_home_linux=<your native hdf path>
```

On Mac:

```bash
npm add encore.hdf5.binding --hdf5_home_mac=<your native hdf path>
```

On Windows:

```bash
npm add encore.hdf5.binding --hdf5_home_win=<your native hdf path>
```

## How to install native hdf5 library

Installation instructions can be found [here](https://github.com/Wandalen/encore.hdf5.install)

## Prerequisites

Note: If node-gyp isn't installed

```bash
npm install -g node-gyp
```

## Example

Quick start to open and read from an h5 file

```javascript
var hdf5 = require( 'encore.hdf5.binding' ).hdf5;

var Access = require( 'encore.hdf5.binding/lib/globals' ).Access;
var file = new hdf5.File( '/tmp/foo.h5', Access.ACC_RDONLY );
var group = file.openGroup( 'bar' );
```
