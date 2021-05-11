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

function runMochaTests( test )
{
  let context = this;
  let ready = __.Consequence();

  let Mocha = require('mocha');
  var mocha = new Mocha();

  let testDir = __.path.join( __dirname, 'mocha', '**.js' );
  let testFiles = __.fileProvider.filesFind
  ({
    filePath : testDir,
    outputFormat : 'absolute',
    filter :
    {
      recursive : 2
    }
  })

  testFiles.forEach( ( file ) => mocha.addFile( __.path.nativize( file ) ) );

  mocha.run( ( fails ) =>
  {
    test.case = 'testing finished without fails';
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
    runMochaTests
  },

}

//

const Self = wTestSuite( Proto );
if( typeof module !== 'undefined' && !module.parent )
_global_.wTester.test( Self.name );

})();
