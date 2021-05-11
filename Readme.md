# module::encore.hdf5.binding  [![status](https://github.com/Wandalen/encore.hdf5.binding/workflows/publish/badge.svg)](https://github.com/Wandalen/encore.hdf5.binding/actions?query=workflow%3Apublish) [![stability-experimental](https://img.shields.io/badge/stability-experimental-orange.svg)](https://github.com/emersion/stability-badges#experimental)

This is binding for
[HDF5](https://www.hdfgroup.org/HDF5/).

## About the fork

This is [fork](https://github.com/HDF-NI/hdf5.node), which is created to provide prebuild versions and fix issues of the original implementation.

## How to add to your project

```bash
npm add encore.hdf5.binding
```
If your native hdf5 library is not locate on default path
you can set the path with --hdf5_home_linux switch on this project as well as
dependent projects.

## How to add to your project

```bash
npm add encore.hdf5.binding --hdf5_home_linux=<your native hdf path>
```
For mac and windows the switches are --hdf5_home_mac & --hdf5_home_win

## With yarn

To install with yarn first need to configure so it knows where the libraries are:

```
yarn config set hdf5_home_linux $HDF5_HOME
yarn install
```

## Prerequisites

Note: If node-gyp isn't installed

```bash
npm install -g node-gyp
```

## Try out

Quick start to open and read from an h5 file

```javascript
var hdf5 = require( 'encore.hdf5.binding' ).hdf5;

var Access = require( 'encore.hdf5.binding/lib/globals' ).Access;
var file = new hdf5.File( '/tmp/foo.h5', Access.ACC_RDONLY );
var group = file.openGroup( 'bar' );
```
