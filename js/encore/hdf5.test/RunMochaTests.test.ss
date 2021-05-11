( function _RunMochaTests_test_ss_()
{

'use strict';

//

if( typeof module !== 'undefined' )
{
  const _ = require( 'wTools' );
  _.include( 'wTesting' );
}

//

const _ = _global_.wTools;
const __ = _globals_.testing.wTools;
const fileProvider = __.fileProvider;
const path = fileProvider.path;

// --
// context
// --

function onSuiteBegin( test )
{
  // let context = this;
  // context.provider = fileProvider;
  // let path = context.provider.path;
  // context.suiteTempPath = context.provider.path.tempOpen( path.join( __dirname, '../..' ), 'integration' );
}

//

function onSuiteEnd( test )
{
  // let context = this;
  // let path = context.provider.path;
  // __.assert( __.strHas( context.suiteTempPath, 'integration' ), context.suiteTempPath );
  // path.tempClose( context.suiteTempPath );
}

//

function attributes( test )
{
  let context = this;
  let ready = __.Consequence();

  let Mocha = require( 'mocha' );
  var mocha = new Mocha();

  let testFilePath = __.path.join( __dirname, 'mocha', 'test_attributes.js' );

  mocha.addFile( __.path.nativize( testFilePath ) )

  mocha.run( ( fails ) =>
  {
    test.case = 'test finished without fails';
    test.identical( fails, 0 );
    ready.take( fails )
  });

  return ready;
}

//

function filters( test )
{
  let context = this;
  let ready = __.Consequence();

  let Mocha = require( 'mocha' );
  var mocha = new Mocha();

  let testFilePath = __.path.join( __dirname, 'mocha', 'test_filters.js' );

  mocha.addFile( __.path.nativize( testFilePath ) )

  mocha.run( ( fails ) =>
  {
    test.case = 'test finished without fails';
    test.identical( fails, 0 );
    ready.take( fails )
  });

  return ready;
}

//

function h5ds( test )
{
  let context = this;
  let ready = __.Consequence();

  let Mocha = require( 'mocha' );
  var mocha = new Mocha();

  let testFilePath = __.path.join( __dirname, 'mocha', 'test_h5ds.js' );

  mocha.addFile( __.path.nativize( testFilePath ) )

  mocha.run( ( fails ) =>
  {
    test.case = 'test finished without fails';
    test.identical( fails, 0 );
    ready.take( fails )
  });

  return ready;
}

//

function h5im( test )
{
  let context = this;
  let ready = __.Consequence();

  let Mocha = require( 'mocha' );
  var mocha = new Mocha();

  let testFilePath = __.path.join( __dirname, 'mocha', 'test_h5im.js' );

  mocha.addFile( __.path.nativize( testFilePath ) )

  mocha.run( ( fails ) =>
  {
    test.case = 'test finished without fails';
    test.identical( fails, 0 );
    ready.take( fails )
  });

  return ready;
}

//

function h5lt( test )
{
  let context = this;
  let ready = __.Consequence();

  let Mocha = require( 'mocha' );
  var mocha = new Mocha();

  let testFilePath = __.path.join( __dirname, 'mocha', 'test_h5lt.js' );

  mocha.addFile( __.path.nativize( testFilePath ) )

  mocha.run( ( fails ) =>
  {
    test.case = 'test finished without fails';
    test.identical( fails, 0 );
    ready.take( fails )
  });

  return ready;
}

//

function h5pt( test )
{
  let context = this;
  let ready = __.Consequence();

  let Mocha = require( 'mocha' );
  var mocha = new Mocha();

  let testFilePath = __.path.join( __dirname, 'mocha', 'test_h5pt.js' );

  mocha.addFile( __.path.nativize( testFilePath ) )

  mocha.run( ( fails ) =>
  {
    test.case = 'test finished without fails';
    test.identical( fails, 0 );
    ready.take( fails )
  });

  return ready;
}

//

function h5tb( test )
{
  let context = this;
  let ready = __.Consequence();

  let Mocha = require( 'mocha' );
  var mocha = new Mocha();

  let testFilePath = __.path.join( __dirname, 'mocha', 'test_h5tb.js' );

  mocha.addFile( __.path.nativize( testFilePath ) )

  mocha.run( ( fails ) =>
  {
    test.case = 'test finished without fails';
    test.identical( fails, 0 );
    ready.take( fails )
  });

  return ready;
}

//

function hdf5( test )
{
  let context = this;
  let ready = __.Consequence();

  let Mocha = require( 'mocha' );
  var mocha = new Mocha();

  let testFilePath = __.path.join( __dirname, 'mocha', 'test_hdf5.js' );

  mocha.addFile( __.path.nativize( testFilePath ) )

  mocha.run( ( fails ) =>
  {
    test.case = 'test finished without fails';
    test.identical( fails, 0 );
    ready.take( fails )
  });

  return ready;
}

//

function swmr( test )
{
  let context = this;
  let ready = __.Consequence();

  let Mocha = require( 'mocha' );
  var mocha = new Mocha();

  let testFilePath = __.path.join( __dirname, 'mocha', 'test_swmr.js' );

  mocha.addFile( __.path.nativize( testFilePath ) )

  mocha.run( ( fails ) =>
  {
    test.case = 'test finished without fails';
    test.identical( fails, 0 );
    ready.take( fails )
  });

  return ready;
}

// --
// declare
// --

const Proto =
{

  name : 'RunMochaTests',
  routineTimeOut : 1500000,
  silencing : 0,

  onSuiteBegin,
  onSuiteEnd,
  context :
  {
    provider : null,
    suiteTempPath : null,
    appJsPath : null
  },

  tests :
  {
    attributes,
    filters,
    h5ds,
    h5im,
    h5lt,
    h5pt,
    h5tb,
    hdf5,
    swmr
  },

}

//

const Self = wTestSuite( Proto );
if( typeof module !== 'undefined' && !module.parent )
_global_.wTester.test( Self.name );

})();
