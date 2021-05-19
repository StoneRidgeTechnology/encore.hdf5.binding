( function _Binding_s_()
{

'use strict';

if( typeof module !== 'undefined' )
{
  let globals = require( '../globals' );
  let binding = require( '../index' );

  let Self =
  {
    ... binding,
    globals
  }

  module[ 'exports' ] = Self;
}

})();
