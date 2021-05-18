
let cp = require( 'child_process' );
let exec = cp.execSync;

let output = null;
try
{
  output = exec( 'h5cc -showconfig', { stdio : 'pipe' } );
}
catch( err )
{
  throw Error( `Failed to find hdf5 library installation. Reason:\n` + err.message );
}

output = output.toString();

// console.log( output )

let version = /HDF5 Version:(.*)/.exec( output )
let installation = /Installation point:(.*)/.exec( output );

console.log( installation[ 1 ].trim() )