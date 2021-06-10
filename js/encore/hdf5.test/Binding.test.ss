( function _Binding_test_ss_()
{

'use strict';

//

if( typeof module !== 'undefined' )
{
  const _ = require( 'wTools' );
  _.include( 'wTesting' );
  var Binding = require( '../hdf5/entry/BindingMain.s' )
  var hdf5 = Binding.hdf5;
  var Access = Binding.globals.Access;
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
  let context = this;
  context.provider = fileProvider;
  let path = context.provider.path;
  context.suiteTempPath = context.provider.path.tempOpen( path.join( __dirname, '../..' ), 'binding' );
}

//

function onSuiteEnd( test )
{
  let context = this;
  let path = context.provider.path;
  __.assert( __.strHas( context.suiteTempPath, 'binding' ), context.suiteTempPath );
  path.tempClose( context.suiteTempPath );
}

//

function stringAttributeLength( test )
{
  let context = this;
  let a = test.assetFor( false );
  a.shell.predefined.sync = 1;
  let filePath = a.fileProvider.path.nativize( a.abs( 'test.h5' ) );

  /* */

  test.case = 'string attribute has expected size'
  a.reflect();
  var file = new hdf5.File( filePath, Access.ACC_TRUNC );
  var group = file.createGroup( 'testGroup' );
  group.attribute = 'abcd'
  group.flush();
  group.close();
  file.close();
  var file = new hdf5.File( filePath, Access.ACC_RDONLY );
  var group, attrs;
  var group = file.openGroup( 'testGroup' );
  var attribute = group.readAttribute( 'attribute' );
  test.identical( attribute, 'abcd' );
  group.close();
  file.close();
  var op = a.shell( `h5dump ${filePath}` );
  var gotSize = /STRSIZE (\d+)/g.exec( op.output )[ 1 ];
  test.identical( _.numberFrom( gotSize ), attribute.length + 1 )

  /* */

}

// --
// declare
// --

const Proto =
{

  name : 'encore.hdf5.binding',
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
    stringAttributeLength,
  },

}

//

const Self = wTestSuite( Proto );
if( typeof module !== 'undefined' && !module.parent )
_global_.wTester.test( Self.name );

})();